# Volatility 3 — Bellek Analizi Playbook

---

## Faz 1 — Bağlam Oluşturma

### windows.info

Bellek imajının SystemTime değerinden olay zaman çizelgesinin referans noktası oluşturulur.

### windows.sessions

- **Session 0** — Servis oturumu, yalnızca SYSTEM olmalı. Beklenmedik kullanıcı hesabı var mı kontrol et.
- **Session 1+** — Etkileşimli kullanıcı oturumu. Hangi kullanıcılar oturum açmış incele.
- **Console** — Fiziksel konsol erişimi. Odak noktası — doğrudan klavye/ekran etkileşimi.

---

## Faz 2 — Süreç Analizi

### windows.pslist

Hızlı ve güvenilir, ancak rootkit'lerin bağlantısını kopardığı (unlinked) süreçleri **göremez**.

**Kontrol noktaları:**

- System, smss.exe, wininit.exe, services.exe, lsass.exe → her birinden **yalnızca bir tane** olmalı.
- İsim kamuflajı ara → svchostt.exe, Isass.exe (büyük i), scvhost.exe vb.
- svchost.exe süreçlerinin PPID'si **mutlaka** services.exe olmalı.

### windows.psscan

Gizlenmiş ve yakın zamanda sonlanmış süreçleri yakalar. **Her vakada** pslist ile psscan diff'lenmelidir:

```bash
vol.py -f bellek.mem -r csv windows.pslist  > pslist.csv
vol.py -f bellek.mem -r csv windows.psscan > psscan.csv
sort pslist.csv > a; sort psscan.csv > b; diff a b > gizlenmis_surecler.txt
```

### windows.pstree

Ebeveyn-çocuk ilişkilerini ağaç yapısında gösterir. Temp, ProgramData, Downloads gibi şüpheli dizinlerden çalışan süreçleri tespit et.

### windows.cmdline

Her sürecin başlatılma argümanlarını gösterir.

- powershell.exe, cmd.exe, wscript.exe, mshta.exe → argümanları mutlaka incele.
- svchost.exe → -k parametresi ile başlamayan örnekler şüphelidir.

---

## Faz 3 — Ağ Bağlantıları

### windows.netscan & windows.netstat

Yalnızca anlık aktif bağlantıları gösterir. İkisi de diff'lenmelidir:

```bash
vol.py -f bellek.mem -r csv windows.netstat > netstat.csv
vol.py -f bellek.mem -r csv windows.netscan > netscan.csv
sort netstat.csv > c; sort netscan.csv > d; diff c d > gizlenmis_ag.txt
```

**Şüpheli göstergeler:**

- notepad.exe, calc.exe, rundll32.exe, powershell.exe gibi süreçlerin dış IP'ye ESTABLISHED bağlantısı.
- Bilinen saldırı portları: 4444 (Metasploit), 8443 (Empire), 1337, 31337.
- DNS çözümlemesi olmayan ham IP adresleri.
- İş istasyonunda 80/443 üzerinde LISTENING durumunda bekleyen beklenmedik ikili dosyalar (örn. hfs.exe).

---

## Faz 4 — Kod Enjeksiyonu

### windows.malfind

Her sürecin VAD ağacını dolaşarak şu kriterlerin **üçünü birden** sağlayan bölgeleri raporlar:

1. PAGE_EXECUTE_READWRITE koruması
2. Private memory (VadS tag, PrivateMemory=1)
3. Herhangi bir dosyaya map edilmemiş

Eşleşen her VAD'ın ilk 64 baytı hex + disassembly olarak basılır.

**Uyarı:** Bazı yükleyiciler (Coreflood, Cobalt Strike loader vb.) PE başlığını sıfırlar veya önce RW tahsis edip ardından VirtualProtect ile RWX'e çevirir — bu durumda malfind sessiz kalabilir.

**Not:** MsMpEng.exe → Windows Defender süreci; false positive üretebilir.

**Şüpheli bulgu varsa izlenecek adımlar:**

```bash
# 1. Şüpheli bellek bölgesini dump et
vol.py -f bellek.mem windows.malfind --dump --pid <PID>

# 2. String analizi
strings dosya.dmp | grep -i 'http\|https\|cmd\|powershell'

# 3. Sandbox'a gönder (VirusTotal, Any.Run, Hybrid Analysis vb.)
```

### windows.hollowprocesses (ek kontrol)

Process Hollowing tespiti için kullanılır. Malfind sonuçlarını destekler.

### windows.vadinfo --pid PID (ek kontrol)

Belirli bir sürecin tüm VAD bölgelerini listeler. PAGE_EXECUTE_READWRITE korumalı bölgeleri filtrele.

---

## Faz 5 — Handle, DLL ve Dosya Analizi

### windows.handles --pid PID

Sürecin açık tuttuğu dosya, registry key ve mutant handle'larını listeler.

- **File:** Temp, ProgramData, Public gibi dizinlere bırakılan dosyaları ara.
- **Key:** Kalıcılık (persistence) yollarına işaret eden registry anahtarlarını kontrol et (Run, RunOnce, Services vb.).

### windows.dlllist & windows.ldrmodules

%TEMP%, %APPDATA%, C:\ProgramData\, Downloads veya kullanıcı profili altından yüklenen DLL'ler enjeksiyon göstergesidir.

**Şüpheli DLL bulunursa:**

```bash
# 1. Dosyanın bellekteki konumunu bul
vol.py -f bellek.mem windows.filescan | grep -i 'supheli.dll'

# 2. Dosyayı dump et (filescan'den alınan sanal adres ile)
vol.py -f bellek.mem windows.dumpfiles --virtaddr 0x<ADRES>
```

---

## Faz 6 — Kalıcılık ve Registry

### windows.svcscan

Kayıtlı servisleri listeler. Anormal dizinlerden çalışan servisleri filtrele:

```bash
vol.py -f bellek.mem windows.svcscan | \
  egrep -i 'TEMP|APPDATA|ProgramData|Downloads|PerfLogs|Public|Recycle\.Bin|Tasks|Spool|Startup|Wbem|System Volume Information'
```

Şüpheli binary bulunursa → windows.filescan + windows.dumpfiles --virtaddr ile dump et.

### windows.registry.hivelist

Bellekte bulunan registry hive'larını listeler. Offline analiz için dump edilebilir:

```bash
vol.py -f bellek.mem windows.registry.hivelist --dump -o hives/
```

### windows.hashdump

Yerel kullanıcı hesaplarının NTLM hash değerlerini döker.

- **aad3b435...** (LM kısmı) → LM hash devre dışı/yok.
- **31d6cfe0...** (NT kısmı) → Boş (şifresiz) parola.

**Önemli:** Domain hesapları hashdump çıktısında yer almaz. Bunlar için aşağıdaki eklentiler kullanılır (pycryptodome kurulu olmalı):

- **windows.lsadump** → LSA secrets — düz metin parolalar, VPN/servis şifreleri.
- **windows.cachedump** → MSCache v2 — önbelleğe alınmış domain kullanıcı hash'leri.

Elde edilen hash değerleri Hashcat veya John the Ripper ile kırılabilir.
