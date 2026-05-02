
```
1. SYSTEM Hive
Öncelik: Yüksek
Konum → C:\Windows\System32\config\SYSTEM
Gözlem Notu: Bilgisayar adı, disk yapısı, servisler, ağ arayüzleri ve boot yapılandırması bu hive içinde tutulur.
```

```
2. SOFTWARE Hive
Öncelik: Yüksek
Konum → C:\Windows\System32\config\SOFTWARE
Gözlem Notu: Kurulu yazılımlar, işletim sistemi sürümü, uninstall kayıtları ve run key'ler bu hive'dan elde edilir.
```

```
3. SAM Hive
Öncelik: Yüksek
Konum → C:\Windows\System32\config\SAM
Gözlem Notu: Yerel kullanıcı hesapları, grup üyelikleri ve son oturum açma zaman damgaları bu dosyada saklanır.
```

```
4. SECURITY Hive
Öncelik: Yüksek
Konum → C:\Windows\System32\config\SECURITY
Gözlem Notu: LSA secret'ları, güvenlik politikaları ve önbelleklenmiş domain kimlik bilgileri burada yer alır.
```

```
5. NTUSER.DAT
Öncelik: Yüksek
Konum → C:\Users\<Kullanıcı>\NTUSER.DAT
Gözlem Notu: Kullanıcıya özgü çalıştırma geçmişi, MRU listeleri ve masaüstü yapılandırması bu dosyada saklanır.
```

```
6. AmCache.hve
Öncelik: Yüksek
Konum → C:\Windows\appcompat\Programs\Amcache.hve
Gözlem Notu: Çalıştırılan uygulamaların SHA1 hash'leri, dosya yolları ve ilk çalıştırma zamanları burada kayıtlıdır.
```

```
7. OS Versiyon Bilgisi
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion
Gözlem Notu: ProductName, BuildLab, InstallDate, EditionID ve UBR değerleri ile tam OS sürümü ve kurulum tarihi belirlenir.
```

```
8. Bilgisayar Adı
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName
Gözlem Notu: Aktif bilgisayar adı bu anahtarda tutulur; değiştirilmişse eski ad ActiveComputerName altında kalabilir.
```

```
9. Saat Dilimi Ayarı
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\TimeZoneInformation
Gözlem Notu: Sistemin saat dilimi ve UTC offset değerleri burada yer alır; zaman damgası analizinde ilk bakılacak noktadır.
```

```
10. Son Kapanma Zamanı
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Windows → ShutdownTime
Gözlem Notu: 8 byte'lık FILETIME formatında son düzgün kapanma zamanını gösterir.
```

```
11. Kurulu Yazılım Listesi
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\
Gözlem Notu: Program adı, sürümü, yayıncısı, kurulum tarihi ve kaldırma komutu bilgileri bu anahtar altında listelenir.
```

```
12. Run / RunOnce Keys
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run[Once]
Gözlem Notu: Sistem başlangıcında otomatik çalıştırılan programlar; kalıcılık (persistence) tespitinde kritiktir.
```

```
13. Kullanıcı Run Keys
Öncelik: Yüksek
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run[Once]
Gözlem Notu: Kullanıcı oturumu açılışında tetiklenen otomatik başlatma girdileri burada yer alır.
```

```
14. Services Kayıtları
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\
Gözlem Notu: Tüm Windows servisleri, sürücüleri, başlangıç türleri ve çalıştırılan ikili dosya yolları bu anahtar altındadır.
```

```
15. ProfileList
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\
Gözlem Notu: Sistemde tanımlı tüm kullanıcı profillerinin SID'leri, profil yolları ve son yükleme zamanları listelenir.
```

```
16. Winlogon Ayarları
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
Gözlem Notu: Shell, Userinit ve otomatik oturum açma ayarları burada tutulur; değiştirilmişse kalıcılık göstergesidir.
```

```
17. LSA Yapılandırması
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa
Gözlem Notu: Authentication paketleri, Security Packages ve RunAsPPL durumu bu anahtar altında tanımlıdır.
```

```
18. Image File Execution Options (IFEO)
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\
Gözlem Notu: Debugger değeri atanmış girdiler, bir programın başlatılması yerine başka bir ikilinin çalıştırılmasına olanak tanır.
```

```
19. BAM/DAM (Background Activity Moderator)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\<SID>
Gözlem Notu: Programların son çalıştırılma zaman damgalarını içerir; Win10 1709+ sürümlerde mevcuttur.
```

```
20. AppCompatCache (ShimCache)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache
Gözlem Notu: Çalıştırılan veya var olan dosyaların yolu, boyutu ve son değiştirilme zamanını saklar; program çalıştırma kanıtı sağlar.
```

```
21. Windows Defender Durumu
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows Defender\
Gözlem Notu: Gerçek zamanlı korumanın, imza güncellemelerinin ve tarama geçmişinin durumunu içerir; devre dışı bırakılmışsa T1562 göstergesidir.
```

```
22. Windows Defender Exclusions
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions\
Gözlem Notu: Yol, uzantı ve süreç bazlı tarama istisnaları; saldırganlar tarafından tespitten kaçınmak için eklenir.
```

```
23. UsrClass.dat
Öncelik: Orta
Konum → C:\Users\<Kullanıcı>\AppData\Local\Microsoft\Windows\UsrClass.dat
Gözlem Notu: ShellBags verileri ve COM nesne kayıtları bu dosyada tutulur; klasör erişim geçmişi için kritiktir.
```

```
24. BBI / BCD Hive
Öncelik: Orta
Konum → C:\Boot\BCD / C:\Windows\System32\config\BBI
Gözlem Notu: Boot yapılandırma veritabanı; önyükleme sırasının değiştirilip değiştirilmediğini gösterir.
```

```
25. Registry Transaction Logs (.LOG1 / .LOG2)
Öncelik: Orta
Konum → C:\Windows\System32\config\*.LOG1, *.LOG2
Gözlem Notu: Hive dosyalarına yazılamamış bekleyen değişiklikleri içerir; dirty hive durumlarında veri kurtarma için gereklidir.
```

```
26. RegBack Yedekleri
Öncelik: Orta
Konum → C:\Windows\System32\config\RegBack\
Gözlem Notu: Registry hive'larının otomatik yedekleridir; Win10 1803+ sonrası varsayılan olarak boş olabilir, kontrol edilmelidir.
```

```
27. CurrentControlSet Belirleme
Öncelik: Orta
Konum → HKLM\SYSTEM\Select → Current, Default, LastKnownGood
Gözlem Notu: Hangi ControlSet'in aktif olduğunu belirler; ControlSet001/002 karşılaştırmasında referans noktasıdır.
```

```
28. Kurulu Yazılım (32-bit on 64-bit)
Öncelik: Orta
Konum → HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\
Gözlem Notu: 64-bit sistemde çalışan 32-bit uygulamaların kurulum kayıtları bu alternatif yolda tutulur.
```

```
29. Environment Variables (System)
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
Gözlem Notu: Sistem geneli ortam değişkenleri burada tanımlıdır; PATH manipülasyonu tespiti için incelenmelidir.
```

```
30. Environment Variables (User)
Öncelik: Orta
Konum → HKCU\Environment
Gözlem Notu: Kullanıcıya özgü ortam değişkenleri; kötü amaçlı DLL yükleme yolları eklenip eklenmediği kontrol edilmelidir.
```

```
31. W32Time Yapılandırması
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\W32Time\
Gözlem Notu: NTP sunucu yapılandırması ve zaman senkronizasyon parametreleri burada tutulur; zaman manipülasyonu tespiti için önemlidir.
```

```
32. AppCompatFlags / Shims
Öncelik: Orta
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\
Gözlem Notu: Uygulama uyumluluk shim veritabanları ve özel shim girdileri persistence veya savunma atlatma amacıyla kullanılabilir.
```

```
33. SilentProcessExit
Öncelik: Orta
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\
Gözlem Notu: Süreç sonlanma sonrası tetiklenen izleme yapılandırması; bazı saldırılarda gizli çalıştırma için kullanılabilir.
```

```
34. BootExecute
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Session Manager → BootExecute
Gözlem Notu: Önyükleme sırasında kernel başlatma sonrası çalışan programlar (varsayılan: autocheck autochk *); değiştirilmişse şüphelidir.
```

```
35. Donanım Profili (BIOS)
Öncelik: Orta
Erişim: Live System
Konum → HKLM\HARDWARE\DESCRIPTION\System\BIOS
Gözlem Notu: BIOS sürümü, üretici, sistem modeli ve seri numarası bilgileri burada yer alır; sanal makine tespitinde kullanılır.
```

```
36. NetworkList Profilleri
Öncelik: Orta
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles\
Gözlem Notu: Bağlanılan ağların adları, ilk ve son bağlantı zaman damgaları bu anahtar altında tutulur.
```

```
37. Terminal Server Client
Öncelik: Orta
Konum → HKCU\Software\Microsoft\Terminal Server Client\Servers\
Gözlem Notu: RDP ile bağlanılan uzak sunucuların IP/hostname bilgilerini ve kullanılan kullanıcı adlarını listeler.
```

```
38. Kod Bütünlüğü Politikası
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\CI\
Gözlem Notu: Device Guard / WDAC kod bütünlüğü politika durumunu gösterir.
```

```
39. Secure Boot Durumu
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\SecureBoot\State → UEFISecureBootEnabled
Gözlem Notu: Secure Boot'un aktif olup olmadığını gösterir; devre dışı bırakılmışsa bootkit riski değerlendirilmelidir.
```

```
40. Windows Firewall Profilleri
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\
Gözlem Notu: Domain/Private/Public profil ayarları ve aktif/pasif durumları burada tanımlıdır.
```

```
41. KnownDLLs
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs
Gözlem Notu: Sistem tarafından korunan DLL listesidir; değiştirilmişse DLL hijacking girişimi göstergesidir.
```

```
42. Event Log Kanal Yapılandırması
Öncelik: Orta
Konum → HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Channels\
Gözlem Notu: Tüm olay günlüğü kanallarının etkin/devre dışı durumunu ve maksimum boyut ayarlarını içerir; kritik kanalların devre dışı bırakılması T1562 göstergesidir.
```

```
43. DEFAULT Hive
Öncelik: Düşük
Konum → C:\Windows\System32\config\DEFAULT
Gözlem Notu: Yeni oluşturulan kullanıcı profillerine uygulanan varsayılan registry ayarları bu dosyadadır.
```

```
44. COMPONENTS Hive
Öncelik: Düşük
Konum → C:\Windows\System32\config\COMPONENTS
Gözlem Notu: Windows bileşen deposu (WinSxS) ile ilgili kurulum ve güncelleme verileri bu hive'da bulunur.
```

```
45. MUI Cache
Öncelik: Düşük
Konum → HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache
Gözlem Notu: Çalıştırılan uygulamaların açıklama metinlerini önbelleğe alır; nadiren temizlenir.
```

```
46. İşlemci Bilgisi
Öncelik: Düşük
Erişim: Live System
Konum → HKLM\HARDWARE\DESCRIPTION\System\CentralProcessor\0
Gözlem Notu: İşlemci tanımlayıcısı, hız ve model bilgisini içerir; donanım envanteri ve VM tespiti için referanstır.
```

```
47. Registered Applications
Öncelik: Düşük
Konum → HKLM\SOFTWARE\RegisteredApplications
Gözlem Notu: Varsayılan program ilişkilendirmeleri için kayıtlı uygulamaların listesidir.
```

```
48. SvcHost Grupları
Öncelik: Düşük
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Svchost
Gözlem Notu: Svchost.exe altında gruplanmış servis listesidir; beklenmeyen servis eklenmişse incelenmelidir.
```
