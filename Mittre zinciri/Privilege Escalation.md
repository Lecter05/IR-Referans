

## Process Injection — T1055


**Yaygın yöntemler:**
- DLL Injection
- Process Hollowing
- Thread Hijacking
- APC Injection (QueueUserAPC)

**Nereye bakarsın:**
- Volatility `malfind` — memory'de inject edilmiş kod bölgeleri
- Volatility `dlllist` — process'e ait beklenmedik DLL'ler
- Process Injection çoğunlukla Defense Evasion ile birlikte kullanılır.

**IOC:**
- Meşru process (explorer.exe, svchost.exe) anormal ağ bağlantısı yapıyor
- Beklenmedik parent-child zinciri: notepad.exe → cmd.exe
- Memory'de PE header'ı olan yürütülebilir bölgeler (malfind çıktısı)


---

## Access Token Manipulation — T1134

22 farklı tehdit grubunda belgelenmiş. Saldırgan yüksek yetkili bir
process'in token'ını alarak o kimlikle hareket eder. Credential
gerektirmez, var olan oturumu kullanır.

**Alt teknikler:**

**T1134.001 — Token Impersonation (Potato Attacks)**
SeImpersonatePrivilege olan servis hesapları hedef alınır.
IIS, MSSQL, Windows servis hesapları bu yetkiye sahip olabilir.
Araçlar: PrintSpoofer, JuicyPotato, RoguePotato, GodPotato

**T1134.002 — Create Process with Token**
Çalınan token ile yeni yüksek yetkili process başlatılır.

**T1134.003 — Make and Impersonate Token**
Bilinen credential ile token üretilir ve bürünme yapılır.

**Nereye bakarsın:**
- Security 4672 — özel yetki atandı, beklenmedik hesapta görünüyorsa şüpheli
- Security 4673 — yetkili servis çağrısı
- Security 4688 — PrintSpoofer64.exe, JuicyPotato.exe, GodPotato.exe
- Prefetch — bu araç isimleri var mı?
- Sysmon ID 10 — lsass.exe'ye erişim denemeleri

**IOC:**
- Düşük yetkili servis hesabı (IUSR, mssql-svc, network service)
  aniden SYSTEM işlemi yapıyor
- SeImpersonatePrivilege olan hesaptan beklenmedik process üretimi
- cmd.exe veya powershell.exe'nin parent'ı servis hesabı

**Dikkat:**
4672 tek başına yeterli değil, her admin logonu üretir.
Asıl anomali: daha önce düşük yetkiyle görünen hesabın 4672 üretmesi.

---

## UAC Bypass — T1548.002

Admin yetkisine sahip ama UAC engeline takılan saldırgan için.
Windows'ta bazı process'ler otomatik yükselen (auto-elevate) özelliktedir.
Saldırgan bunların registry okumalarını manipüle eder.

**Yaygın yöntemler:**

| Binary | Yöntem |
|---|---|
| fodhelper.exe | HKCU\...\ms-settings\shell\open\command |
| eventvwr.exe | HKCU\...\mscfile\shell\open\command |
| sdclt.exe | HKCU\...\exefile\shell\open\command |
| cmstp.exe | INF dosyası ile |
| computerdefaults.exe | ms-settings manipulation |

**Nereye bakarsın:**
- Sysmon ID 13 — şu key'lere yazma:
  * `HKCU\Software\Classes\ms-settings\shell\open\command`
  * `HKCU\Software\Classes\mscfile\shell\open\command`
- Security 4688 — yüksek yetkili process'in parent'ı beklenmedik uygulama
- Prefetch — fodhelper.exe, eventvwr.exe, sdclt.exe

**IOC:**
- fodhelper.exe çalışıyor → child process yüksek yetkiyle (High Integrity) başlıyor
- Registry key'de komut satırı veya binary path görünüyor
- Kısa süre içinde yazma → process çalışma → key silme zinciri

**Dikkat:**
Saldırgan genellikle işlem bittikten sonra registry key'i siler.
$UsnJrnl ve Sysmon logları silinse bile zaman damgası kalabilir.

---

## DLL Hijacking / DLL Side-Loading — T1574.001 / T1574.002

Uygulama DLL ararken meşru DLL'den önce zararlı DLL'i yükler.
Side-Loading'de ise meşru imzalı exe yanına zararlı DLL bırakılır,
exe onu yükler. 

**Fark:**
- **T1574.001 DLL Hijacking** — DLL arama sırasını istismar eder
- **T1574.002 DLL Side-Loading** — meşru exe'nin yanına zararlı DLL bırakılır

**Yaygın hedefler:**
MicrosoftEdgeUpdate.exe, OneDriveUpdater.exe, Teams.exe,
Windows Defender bileşenleri, AV yazılım dizinleri

**Nereye bakarsın:**
- Sysmon ID 7 — Image Loaded, imzasız veya beklenmedik dizinden DLL
- Amcache — yeni DLL'in hash ve path bilgisi
- $UsnJrnl — uygulama dizinine yeni dosya kopyalandı mı?
- MFT — DLL'in oluşturulma zamanı, orijinal exe ile ilişkisi

**IOC:**
- Bilinen exe ile aynı dizinde imzasız DLL
- DLL'in hash'i VirusTotal'da eşleşmiyor veya bilinmiyor
- Meşru exe'nin normalde kullanmadığı bir DLL'i yüklemesi

**Dikkat:**
DLL Side-Loading tespit edilmesi zor çünkü imzalı meşru exe çalışıyor.
Amcache hash kontrolü ve Sysmon ID 7 bu noktada kritik.

---

## AlwaysInstallElevated — T1611 (Misconfiguration)

İki registry key birden 1 ayarlıysa herhangi bir kullanıcı
SYSTEM yetkisiyle MSI dosyası kurabilir. Yaygın bir misconfiguration.

**Kontrol edilecek key'ler:**

HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated = 1
HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated = 1
- Application.evtx — MsiInstaller event'leri
- Security 4688 — msiexec.exe SYSTEM token'ıyla çalışmış mı?

**IOC:**
- Her iki key de 1 değerinde
- Kullanıcı msiexec başlatıyor, process SYSTEM token'ıyla devam ediyor
- Beklenmedik .msi dosyası kullanıcı dizininde (AppData, Temp)

**Dikkat:**
Bu misconfiguration kurumsal ortamlarda düşünüldüğünden sık karşılaşılır.
Group Policy ile yayılmış olabilir, tek sistemle sınırlı olmayabilir.

---

## Exploitation for Privilege Escalation — T1068

Kernel veya işletim sistemi bileşenlerindeki güvenlik açıklarını
istismar ederek SYSTEM yetkisi elde etme. CVE bazlı.

**Yaygın örnekler:**
- PrintNightmare (CVE-2021-34527) — Print Spooler
- HiveNightmare / SeriousSAM (CVE-2021-36934) — SAM erişimi
- EternalBlue (MS17-010) — SMB
- Dirty Pipe (Linux — referans için)

**PrintNightmare için özel bakış:**
- PrintService.evtx — hata ve anomali
- Security 4688 — spoolsv.exe'nin beklenmedik child process'i
- Sysmon ID 7 — spoolsv.exe beklenmedik DLL yükledi mi?
- Dizin: `C:\Windows\System32\spool\drivers\` altında yeni DLL var mı?


**IOC:**
- Yama durumu kontrol et: hangi KB'lar eksik?
- spoolsv.exe veya kernel process'lerinden beklenmedik child
- Yüksek yetkiyle çalışan bilinmeyen binary

**Dikkat:**
Exploit başarısız denemeleri crash dump bırakabilir.
`C:\Windows\Minidump\` ve `C:\ProgramData\Microsoft\Windows\WER\` kontrol et.

---

## Unquoted Service Path — T1574.009

Servis binary yolunda boşluk varsa ve tırnak işareti yoksa
Windows yolu parça parça dener. Saldırgan doğru yere binary bırakır.

**Örnek:**

C:\Program Files\My App\service.exe

Windows şunları dener:

C:\Program.exe
C:\Program Files\My.exe
C:\Program Files\My App\service.exe



**Nereye bakarsın:**
- `HKLM\SYSTEM\CurrentControlSet\Services\` altında tırnaksız boşluklu ImagePath değerleri
- Komut (canlı sistem): `wmic service get name,pathname | findstr /i /v "C:\Windows"`
- $UsnJrnl — servis dizinine yeni binary kopyalandı mı?
- System 7045 / Security 4697 — servis değişikliği

**IOC:**
- Tırnaksız path, boşluk içeriyor
- Ara dizinde (Program Files altı) beklenmedik .exe dosyası
- Servis yeniden başlatılmış ve yeni binary çalışmış

**Dikkat:**
- Bu teknik servis restart veya sistem reboot gerektirir.
- $UsnJrnl'de dosya oluşturma + Prefetch'te binary çalışması korelasyonu kritik.

---

## Weak Service Permissions — T1574.010

Servis binary'si veya servisin kendisi zayıf izinlere sahipse
saldırgan binary'yi değiştirir veya servis konfigürasyonunu düzenler.

**İki senaryo:**
1. Servis binary'si üzerine yazılabilir → zararlı binary ile değiştir
2. Servis konfigürasyonu düzenlenebilir → ImagePath değiştir

**Nereye bakarsın:**
- $UsnJrnl — servis binary'si değiştirildi mi?
- MFT — binary'nin $STANDARD_INFORMATION vs $FILE_NAME timestamp farkı
  (timestomping ile gizlenmeye çalışılmış olabilir)
- System 7045 / 7040 — servis kurulumu veya başlangıç tipi değişimi

**IOC:**
- Servis binary'sinin hash'i değişmiş
- Servis SYSTEM veya LocalSystem yetkisiyle çalışıyor ama binary imzasız

---

## Scheduled Task / Job Abuse — T1053.005

Zaten yüksek yetkiyle çalışan bir task'i değiştirme veya
SYSTEM yetkisiyle yeni task oluşturma yoluyla yetki yükseltme.

**Nereye bakarsın:**
- Security 4698 — scheduled task oluşturuldu
- Security 4702 — mevcut task güncellendi (önemli: mevcut task değişimi)
- TaskScheduler/Operational 106 / 140 — kayıt ve güncelleme
- `C:\Windows\System32\Tasks\` — task XML dosyaları, içerik ve kullanıcı
- `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache`

**IOC:**
- SYSTEM yetkisiyle çalışan task'in Action kısmında beklenmedik binary
- Task adı meşru Windows task'lerine benzetilmiş (masquerading)
- Kısa süreli task (bir kez çalış, sil kendini)

**Dikkat:**
Saldırgan task'i oluşturup sildiyse Security 4699 var mı kontrol et.
TaskScheduler log temizlenmiş olabilir — $UsnJrnl'de Tasks dizini değişimine bak.
