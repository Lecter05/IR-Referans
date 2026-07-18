# Windows IR — Hive & Artifact Lokasyonları

> Incident Response süreçlerinde incelenmesi gereken kritik dosya ve dizinlerin konumları.
> `<kullanıcı>` ifadesi hedef kullanıcı profil adını, `<SID>` ise kullanıcı güvenlik tanımlayıcısını temsil eder.

---

## A — Sistem Yapılandırması ve Registry

### 1. Registry Hive Dosyaları

- `C:\Windows\System32\config\` → SAM, SYSTEM, SECURITY, SOFTWARE, DEFAULT, COMPONENTS, BBI, *.LOG1, *.LOG2
- `C:\Windows\System32\config\RegBack\` → Yukarıdaki hive dosyalarının yedekleri
- `C:\Windows\Repair\` → SAM
- `C:\Users\<kullanıcı>\` → NTUSER.DAT
- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\Windows\` → UsrClass.dat
- `C:\System Volume Information\` → Syscache.hve
- `C:\Windows\appcompat\Programs\` → Amcache.hve

### 2. Boot ve Sistem Bütünlüğü

- `C:\Boot\` → BCD
- `C:\Windows\System32\CodeIntegrity\` → Kod bütünlüğü politika dosyaları
- `C:\Windows\System32\CatRoot\` → Katalog imza dosyaları
- `C:\Windows\System32\WDI\` → Tanılama verileri
- `C:\Windows\System32\ELAM\` → Early Launch Anti-Malware verileri
- `C:\Windows\Logs\MeasuredBoot\` → Ölçülü önyükleme logları

---

## B — Olay Günlükleri ve Loglar

### 3. Windows Event Logs

- `C:\Windows\System32\winevt\Logs\` → *.evtx

### 4. Kurulum ve Güncelleme Logları

- `C:\Windows\INF\` → setupapi.dev.log, setupapi.setup.log, setupapi.app.log
- `C:\Windows\Logs\CBS\` → CBS.log
- `C:\Windows\Logs\DISM\` → dism.log
- `C:\Windows\Panther\` → Unattend.xml, unattend\
- `C:\Windows\SoftwareDistribution\` → DataStore\DataStore.edb, Download\
- `C:\Users\<kullanıcı>\AppData\Local\Temp\` → MSI*.log

### 5. IIS Web Sunucu Logları

- `C:\inetpub\logs\LogFiles\W3SVC*\` → *.log
- `C:\inetpub\wwwroot\` → Web root dizini (webshell araması için)

### 6. Hata Raporları ve Crash Dump

- `C:\ProgramData\Microsoft\Windows\WER\` → ReportArchive\, ReportQueue\
- `C:\Users\<kullanıcı>\AppData\Local\CrashDumps\` → Uygulama crash dump dosyaları
- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\Windows\WER\` → Kullanıcı düzeyi hata raporları
- `C:\Windows\` → MEMORY.DMP
- `C:\Windows\Minidump\` → *.dmp
- `C:\Windows\LiveKernelReports\` → Kernel hata raporları

### 7. Firewall Logları

- `C:\Windows\System32\LogFiles\Firewall\` → pfirewall.log

---

## C — Dosya Sistemi Artifact'ları

### 8. NTFS Yapıları

- `C:\$MFT` → Master File Table — tüm dosya kayıtları
- `C:\$LogFile` → NTFS işlem günlüğü
- `C:\$Bitmap` → Küme (cluster) tahsis haritası
- `C:\$Boot` → Önyükleme sektörü bilgileri
- `C:\$Secure` → Dosya güvenlik tanımlayıcıları
- `C:\$Extend\$UsnJrnl` → USN Change Journal ($J ve $MAX veri akışları)
- Her NTFS dizininde `$I30` → Dizin indeks kaydı — silinmiş dosya adlarının tespiti için

### 9. Prefetch Dosyaları

- `C:\Windows\Prefetch\` → *.pf, Ag*.db

**Saldırı aracı izleri için özellikle aranacak prefetch dosyaları:** mimikatz.pf, procdump.pf, ntdsutil.pf, vssadmin.pf, rundll32.pf, bcdedit.pf, cmdkey.pf, mstsc.pf, rdpclip.pf

### 10. Geri Dönüşüm Kutusu

- `C:\$Recycle.Bin\<SID>\` → $I* (metadata), $R* (asıl dosya içeriği)

Diğer sürücülerde de aranmalı: D:\$Recycle.Bin\, E:\$Recycle.Bin\ vb.

### 11. Volume Shadow Copy

- `\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy<N>\` → N numaralı gölge kopya; sistemin önceki halini içerir
- `C:\System Volume Information\` → VSS metadata

### 12. Bellek ve Sayfalama Dosyaları

- `C:\hiberfil.sys` → Hazırda bekletme bellek dökümü
- `C:\pagefile.sys` → Sanal bellek sayfa dosyası
- `C:\swapfile.sys` → Modern uygulama takas dosyası

---

## D — Kullanıcı Aktivitesi

### 13. Shell Artifact'ları (LNK, JumpList, Thumbnail)

- `C:\Users\<kullanıcı>\AppData\Roaming\Microsoft\Windows\Recent\` → *.lnk
- `…\Recent\AutomaticDestinations\` → Otomatik JumpList dosyaları
- `…\Recent\CustomDestinations\` → Özel JumpList dosyaları
- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\Windows\Explorer\` → thumbcache_*.db, iconcache_*.db

### 14. Aktivite Geçmişi ve Bildirimler

- `C:\Users\<kullanıcı>\AppData\Local\ConnectedDevicesPlatform\<alt klasör>\` → ActivitiesCache.db
- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\Windows\Notifications\` → wpndatabase.db
- `C:\Users\<kullanıcı>\AppData\Roaming\Microsoft\Office\Recent\` → Son açılan Office dosyaları

### 15. PowerShell ve Komut Satırı Geçmişi

- `C:\Users\<kullanıcı>\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\` → ConsoleHost_history.txt
- `C:\Windows\System32\WindowsPowerShell\v1.0\` → profile.ps1
- `C:\Users\<kullanıcı>\Documents\PowerShell\` → Microsoft.PowerShell_profile.ps1
- `C:\Users\<kullanıcı>\Documents\` → PowerShell_transcript.*.txt

### 16. Windows Arama ve İndeks

- `C:\ProgramData\Microsoft\Search\Data\Applications\Windows\` → Windows.edb
- `C:\Users\<kullanıcı>\AppData\Local\Packages\Microsoft.Windows.Cortana_*\LocalState\DeviceSearchCache\` → AppCache.db

### 17. OneDrive Logları

- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\OneDrive\logs\` → SyncDiagnostics.log
- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\OneDrive\settings\` → Yapılandırma dosyaları

---

## E — Tarayıcı Artifact'ları

### 18. Google Chrome

- `C:\Users\<kullanıcı>\AppData\Local\Google\Chrome\User Data\Default\` → History, Login Data, Cookies, Web Data, Local State
- `…\Default\Cache\` → Tarayıcı önbellek dosyaları
- `…\Default\Extensions\` → Yüklü uzantılar

### 19. Microsoft Edge

- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\Edge\User Data\Default\` → History, Login Data, Local State
- `…\Default\Extensions\` → Yüklü uzantılar

### 20. Mozilla Firefox

- `C:\Users\<kullanıcı>\AppData\Roaming\Mozilla\Firefox\Profiles\<profil>\` → places.sqlite, cookies.sqlite, logins.json, formhistory.sqlite, key4.db

### 21. Internet Explorer / Eski Edge

- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\Windows\WebCache\` → WebCacheV01.dat
- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\Windows\INetCache\` → Geçici internet dosyaları
- `C:\Users\<kullanıcı>\AppData\LocalLow\Microsoft\CryptnetUrlCache\` → Content\, MetaData\

---

## F — Persistence Mekanizmaları

### 22. Startup Klasörleri

- `C:\Users\<kullanıcı>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\` → Kullanıcı başlangıç öğeleri
- `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\` → Tüm kullanıcılar için başlangıç öğeleri

### 23. Görev Zamanlayıcı (Scheduled Tasks)

- `C:\Windows\System32\Tasks\` → *.xml, At*
- `C:\Windows\System32\Tasks\Microsoft\Windows\` → Alt görev tanımları

### 24. Group Policy Betikleri

- `C:\Windows\System32\GroupPolicy\Machine\Scripts\` → Startup\, scripts.ini, psscripts.ini
- `C:\Windows\System32\GroupPolicy\User\Scripts\` → Logon\

**Domain ortamında SYSVOL:**

- `\\<domain>\SYSVOL\<domain>\Policies\<GUID>\` → Machine\Preferences\Groups\Groups.xml, Machine\Preferences\Services\Services.xml

### 25. WMI Repository

- `C:\Windows\System32\wbem\Repository\` → OBJECTS.DATA, INDEX.BTR, MAPPING*.MAP

### 26. BITS (Arka Plan Aktarım Servisi)

- `C:\ProgramData\Microsoft\Network\Downloader\` → qmgr.db, qmgr0.dat, qmgr1.dat

---

## G — Kimlik Bilgileri ve Credential Dump

### 27. Windows Vault ve DPAPI

- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\Vault\<alt klasör>\` → Policy.vpol, *.vcrd
- `C:\Users\<kullanıcı>\AppData\Roaming\Microsoft\Protect\<SID>\` → Şifrelenmiş DPAPI master key dosyaları
- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\Credentials\` → Şifrelenmiş kimlik bilgileri
- `C:\Users\<kullanıcı>\AppData\Roaming\Microsoft\Credentials\` → Şifrelenmiş kimlik bilgileri

### 28. Credential Dump İzleri

- `C:\Windows\NTDS\ntds.dit` → Active Directory veritabanı (yalnızca DC)
- `C:\Windows\Temp\lsass.dmp` → LSASS bellek dökümü
- `C:\Users\<kullanıcı>\AppData\Local\Temp\lsass*.dmp` → Kullanıcı temp dizininde LSASS dump
- `C:\ProgramData\Microsoft\Windows\WER\ReportQueue\` → lsass.exe*.dmp aranır
- `C:\Windows\Temp\`, kullanıcı Temp ve profil kökü → *.kirbi (Kerberos bilet dosyaları)

---

## H — Ağ Bağlantıları ve Uzak Erişim

### 29. SSH ve Ağ Yapılandırması

- `C:\Users\<kullanıcı>\.ssh\` → known_hosts, config, authorized_keys
- `C:\ProgramData\ssh\` → administrators_authorized_keys
- `C:\Windows\System32\drivers\etc\` → hosts, lmhosts.sam
- `C:\ProgramData\Microsoft\Wlansvc\Profiles\Interfaces\<adaptör>\` → *.xml (Wi-Fi profilleri)
- `C:\ProgramData\Microsoft\Network\Connections\Pbk\` → rasphone.pbk
- `C:\Users\<kullanıcı>\AppData\Roaming\Microsoft\Network\Connections\Pbk\` → rasphone.pbk

### 30. RDP (Uzak Masaüstü)

- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\Terminal Server Client\Cache\` → *.bmc, bcache*.bmc
- `C:\Users\<kullanıcı>\Documents\` → Default.rdp

### 31. Üçüncü Parti Uzak Erişim Araçları

- `C:\Users\<kullanıcı>\AppData\Roaming\TeamViewer\` → Connections.txt
- `C:\Program Files\TeamViewer\` → Connections_incoming.txt
- `C:\Users\<kullanıcı>\AppData\Roaming\AnyDesk\` → ad.trace, system.conf
- `C:\ProgramData\AnyDesk\` → ad_svc.trace, system.conf
- `C:\Users\<kullanıcı>\AppData\Roaming\RustDesk\config\` → *.toml
- `C:\Users\<kullanıcı>\.ngrok2\` → ngrok.yml

---

## I — Dosya Transfer Araçları

### 32. FTP / SCP / Arşiv İstemcileri

- `C:\Users\<kullanıcı>\AppData\Roaming\FileZilla\` → recentservers.xml, queue.sqlite3
- `C:\Users\<kullanıcı>\AppData\Roaming\` → WinSCP.ini
- `C:\Users\<kullanıcı>\AppData\Roaming\WinRAR\` → Yapılandırma ve geçmiş
- `C:\Users\<kullanıcı>\AppData\Roaming\7-Zip\` → Yapılandırma ve geçmiş

---

## J — SRUM ve Kaynak Kullanımı

### 33. System Resource Usage Monitor

- `C:\Windows\System32\sru\` → SRUDB.dat

---

## K — Diğer Artifact'lar

### 34. Yazıcı Spool

- `C:\Windows\System32\spool\PRINTERS\` → Yazdırma kuyruğu dosyaları
- `C:\Windows\System32\spool\drivers\` → Yazıcı sürücüleri

### 35. WSL (Windows Subsystem for Linux)

- `\\wsl$\<dağıtım>\home\<kullanıcı>\` → .bashrc, .bash_history vb.
- `C:\Users\<kullanıcı>\AppData\Local\Packages\` → *CanonicalGroup* ile başlayan klasörler (Ubuntu, Debian vb.)

### 36. Uygulama Bazlı Artifact'lar

- `C:\Users\<kullanıcı>\AppData\Local\Steam\htmlcache\` → Steam tarayıcı önbelleği
- `C:\Users\<kullanıcı>\AppData\Local\Packages\Microsoft.WindowsNotepad_*\LocalState\TabState\` → Notepad sekme verileri
- `C:\Users\<kullanıcı>\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_*\LocalState\` → plum.sqlite
- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\Media Player\` → Medya oynatıcı geçmişi
- `C:\Users\<kullanıcı>\AppData\Local\Microsoft\Windows\INetCache\Content.Outlook\` → Outlook ek önbelleği
- `C:\ProgramData\Microsoft\Windows\Containers\` → Konteyner yapılandırması
- `C:\Program Files\VMware\VMware Tools\` → VMware sanallaştırma araçları
- `C:\Program Files\Oracle\VirtualBox Guest Additions\` → VirtualBox misafir eklentileri
