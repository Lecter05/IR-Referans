# Lateral Movement — Hızlı Triyaj (10-15 dk)

> **Breakout time:** 29 dakika (eCrime ortalaması, CrowdStrike 2026). En hızlı gözlenen vaka 27 saniye. Initial access → operator devir süresi 22 saniyeye düştü (Mandiant M-Trends 2026).


## Triyaj Akışı

> Amaç: alarmı hızla "gerçek lateral movement mı, değil mi?" sorusuna cevaplamak. her adım bir sonrakini odaklıyor.

### Dakika 0-2 — Scope & Pivot Point Tespiti

Alarm aldığın host **kaynak mı, hedef mi?** Çoğu SIEM ikisini karıştırır.

İlk IOC'yi sabitle: hostname, kullanıcı hesabı (service account'sa kritik), zaman damgası.

**Üç pivot sorusu:**

1. Bu account bu hosta normalde erişir mi?
2. Bu host bu hosta normalde erişir mi?
3. Bu zaman dilimi normal mi?

Üçünden herhangi biri "hayır" → devam et.

---

### Dakika 2-5 — Kimlik Doğrulama İzi

Lateral movement **her zaman** authentication event üretir. Önce buraya bak.

**Security.evtx — Kritik Event ID'ler:**

- **4624 Type 3 (Network)** — SMB, PsExec, WMI, WinRM, admin share. Workstation → workstation Type 3/10 = güçlü lateral movement göstergesi. Çoğu ortamda legitimate use-case'i yok.
- **4624 Type 10 (RemoteInteractive)** — RDP. Tuhaf IP'den gece yarısı Type 10 = kırmızı bayrak.
- **4648** — Explicit credential logon (runas, çalıntı parolayla PsExec).
- **4672** — Special privileges atandı. Bilinmeyen hesaba SeDebugPrivilege / SeBackupPrivilege = hemen soruştur.
- **4625** — Failed logon patternleri. Aynı kaynaktan 10 dk'da 50+ = brute force / password spray.

**Altın anahtar:** `Logon ID` alanını takip et → aynı Logon ID ile 4624 → 4648 → 4688 → 4634/4647 zinciri saldırganın tam oturumunu ortaya çıkarır.

**Domain Controller'da:**

- **4768 (TGT)** / **4769 (TGS)** — OverPass-the-Hash → RC4/AES hash doğrudan gönderilir. **4769'da Ticket Encryption Type 0x17 (RC4) = Kerberoasting sinyali.**
- **4776** — NTLM doğrulama. Pass-the-Hash durumunda 4776 + 4624 Type 9/3 + 4648 + 4672 birlikte görünür.

---

### Dakika 5-8 — Süreç ve Komut İcrası

Authentication teyit edildiyse → host üzerinde ne çalıştı?

**4688 / Sysmon EID 1** — Process creation (command-line auditing AÇIK olmalı)

**Parent → Child anomalileri:**

- `services.exe` → `psexesvc.exe` → Klasik PsExec
- `wmiprvse.exe` → `powershell.exe` / `cmd.exe` → WMI remote exec (fileless LM)
- `wsmprovhost.exe` → herhangi bir child → WinRM / PSRemoting
- `svchost.exe` → `cmd.exe` (tuhaf argüman) → schtasks/at remote execution

**PowerShell Operational (EID 4104 — Script Block Logging)** — Saldırganın tam niyetini ortaya çıkarır. Tara: `-enc`, `-nop`, `-w hidden`, `IEX`, `DownloadString`, `Invoke-Expression`

**WinRM Operational log** — Kaynak IP + hedef host korelasyonu.

**Süreç isim kamuflajı:** `C:\Users\Public\svchost.exe` gibi System32 dışında "sistem" isimli binary'ler.

---

### Dakika 8-11 — Ağ ve Share İzleri

**Sysmon EID 3 (Network Connection)** — Process → remote host eşlemesi (altın değerinde).

**Kritik portlar:**

- **445** → SMB → PsExec, admin share, PtH
- **135 + dinamik yüksek** → RPC/WMI → WMI remote exec
- **3389** → RDP → Remote desktop
- **5985/5986** → WinRM → PSRemoting
- **88** → Kerberos → Non-DC hosttan 88'e bağlantı = şüpheli

**5140 / 5145** — Ağ share erişimi. `5145` + `ADMIN$` altında `.exe`/`.ps1`/`.bat` oluşturulması = tool transfer.

**5156** — WFP connection allowed (process + hedef IP/port).

---

### Dakika 11-15 — Persistence & Yayılma Sinyali

Lateral movement başarılıysa saldırgan foothold bırakır.

- **7045 (System log)** — Yeni servis kurulumu. PsExec imzası: `PSEXESVC` servisi + `\PIPE\psexesvc` named pipe.
- **4697 (Security log)** — Privileged servis yüklenmesi.
- **Sysmon 17/18** — Named pipe oluşturma/bağlanma (PsExec, Cobalt Strike SMB beacon).
- **4698/4699** — Scheduled task oluşturma/silme. Remote schtasks + 4624 Type 3 kombinasyonu = güçlü LM göstergesi.
- **Sysmon 19/20** — WMI Event Filter/Consumer (persistence veya LM).
- **TerminalServices-LocalSessionManager/Operational 21, 22, 25** — RDP oturum başlangıç/reconnect (4778/4779 ile eşleştir).

**15 dakika yetmezse:** Host'u izole et (EDR containment — 15 dk altında çalıştığını doğrula) veya Tier-2/IR'a devret. "Biraz daha bakayım" genellikle yanlış seçimdir; breakout time 29 dk ve %50'sini zaten yedin.

---

## Tamamlayıcı Araçlar

### Artefact Toplama

- **KAPE** — 60-120 sn'de canlı hosttan kritik artefact (evtx, Prefetch, Amcache, ShimCache, RDP bitmap cache, SRUM). Targets: `!BasicCollection`, `SANS_Triage`.
- **CyLR / DFIR-ORC** — Alternatifler.

### Log Parsing

- **Hayabusa** — Sigma tabanlı hızlı evtx tarayıcı, severity/MITRE işaretli timeline. 15 dk'dan kısa sürede tam klasör tarar.
- **Chainsaw** — Sigma + kendi kuralları ile hızlı triaj.
- **EvtxECmd** — CSV/JSON normalize, Timeline Explorer'da filtrele.
- **DeepBlueCLI** — 4648/4624/Password Spray/Mimikatz pattern tespiti.

### Bellek Analizi

- **Volatility 3 / MemProcFS**

### Ağ Tarafı  
- **Zeek/Suricata** — `kerberos.log` içinde `etype=23 (RC4)` = Kerberoast sinyali. `smb_files.log` içinde admin share'e `.exe` yazımı.

### Görselleştirme
- LogonTracer
