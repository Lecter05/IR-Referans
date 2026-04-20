## FILE SYSTEM ARTIFACT'LARI

```
1. Startup Klasörü (Kullanıcı)
Öncelik: Yüksek
Konum → %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
Gözlem Notu: Klasörde beklenmeyen .lnk, .bat, .vbs, .exe dosyalarının varlığına bakılır.
```

```
2. Startup Klasörü (Tüm Kullanıcılar)
Öncelik: Yüksek
Konum → C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
Gözlem Notu: Global startup klasöründeki dosyalara bakılır.
```

```
3. DLL Search Order Hijacking
Öncelik: Yüksek
Konum → Hedef uygulamanın kurulum dizini (örn. C:\Program Files\<app>)
Gözlem Notu: Meşru uygulama dizininde olmaması gereken veya imzasız DLL dosyalarına bakılır.
```

```
4. DLL Side-Loading
Öncelik: Yüksek
Konum → İmzalı ve güvenilen EXE'nin yanında bulunan sahte DLL dosyaları
Gözlem Notu: Signed binary'nin yanında hash'i eşleşmeyen veya imzasız DLL'lere bakılır.
```

```
5. Scheduled Task XML Tanım Dosyaları
Öncelik: Yüksek
Konum → C:\Windows\System32\Tasks\ (alt klasörler dahil)
Gözlem Notu: XML dosyalarındaki <Exec><Command> etiketlerinde beklenmeyen binary yollarına bakılır.
```

```
6. WMI Repository (OBJECTS.DATA)
Öncelik: Yüksek
Konum → C:\Windows\System32\wbem\Repository\OBJECTS.DATA
Gözlem Notu: WMI kalıcı aboneliklerinin binary dump'ında CommandLineEventConsumer aranır.
```

```
7. Group Policy Scripts (Startup/Logon)
Öncelik: Orta
Konum → C:\Windows\System32\GroupPolicy\Machine\Scripts\Startup ve User\Scripts\Logon
Gözlem Notu: GPO ile dağıtılan startup/logon script'lerinde tanınmayan dosyalara bakılır.
```

```
8. Logon Scripts (scripts.ini / psscripts.ini)
Öncelik: Orta
Konum → C:\Windows\System32\GroupPolicy\Machine\Scripts\scripts.ini ve psscripts.ini
Gözlem Notu: ini dosyalarındaki script referanslarının meşru olup olmadığına bakılır.
```

```
9. Phantom DLL Hijacking
Öncelik: Orta
Erişim: Live System
Konum → Procmon ile tespit; hedef dizinde oluşturulan sahte DLL
Gözlem Notu: Sistemde referans edilip bulunamayan (NAME NOT FOUND) DLL yollarına bakılır.
```

```
10. Alternate Data Streams (ADS)
Öncelik: Orta
Konum → Herhangi bir dosya veya dizin üzerinde <dosya>:<stream>
Gözlem Notu: dir /r veya streams.exe ile NTFS ADS içeriği kontrol edilir.
```

```
11. PowerShell Profile Dosyaları
Öncelik: Orta
Konum → %UserProfile%\Documents\PowerShell\Microsoft.PowerShell_profile.ps1 ve %WinDir%\System32\WindowsPowerShell\v1.0\profile.ps1
Gözlem Notu: Her PowerShell oturumunda otomatik çalışan profile dosyalarındaki komutlara bakılır.
```

```
12. Amcache.hve
Öncelik: Orta
Konum → C:\Windows\AppCompat\Programs\Amcache.hve
Gözlem Notu: Çalıştırılan binary'lerin ilk çalışma zamanı ve SHA1 hash bilgisi elde edilir.
```

```
13. Prefetch Dosyaları
Öncelik: Orta
Konum → C:\Windows\Prefetch\*.pf
Gözlem Notu: Persistence mekanizması ile tetiklenen binary'nin Prefetch kaydının varlığına bakılır.
```

```
14. BITS Jobs (qmgr0.dat / qmgr1.dat)
Öncelik: Orta
Konum → C:\ProgramData\Microsoft\Network\Downloader
Gözlem Notu: BITS transfer job'larında kalıcılık veya download payload göstergelerine bakılır.
```

```
15. IIS / Web Shell
Öncelik: Orta
Konum → C:\inetpub\wwwroot\ ve alt dizinleri
Gözlem Notu: Web sunucu kök dizininde son tarihli veya olağandışı web script dosyalarına bakılır.
```

```
16. .bashrc (WSL)
Öncelik: Düşük
Konum → \\wsl$\<distro>\home\<user>\.bashrc
Gözlem Notu: WSL aktifse Linux tarafındaki shell profile dosyalarında eklenen komutlara bakılır.
```
