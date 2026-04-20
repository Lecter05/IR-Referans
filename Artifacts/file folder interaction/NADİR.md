## DİĞER / NADİR ARTIFACT'LAR

```
1. Windows.edb (Windows Search Index)
Öncelik: Yüksek
Konum → %PROGRAMDATA%\Microsoft\Search\Data\Applications\Windows\Windows.edb
Gözlem Notu: Sistemdeki indekslenmiş tüm dosyaların adı, yolu, boyutu, tarihi ve kısmi içerik metnini ESE veritabanında tutar.
```

```
2. Amcache.hve (Dosya Referansları)
Öncelik: Yüksek
Konum → C:\Windows\AppCompat\Programs\Amcache.hve
Gözlem Notu: Çalıştırılan ve kurulan dosyaların SHA1 hash, yol ve zaman bilgisini tutar; dosya varlığının kanıtıdır.
```

```
3. ActivitiesCache.db (Timeline)
Öncelik: Orta
Konum → %LOCALAPPDATA%\ConnectedDevicesPlatform\<klasör>\ActivitiesCache.db
Gözlem Notu: Açılan dosyaların AppID, URI, başlangıç/bitiş zamanı ve cihaz bilgisini SQLite formatında tutar (Win10; Win11'de kısıtlı).
```

```
4. SRUDB.dat (System Resource Usage Monitor)
Öncelik: Orta
Konum → C:\Windows\System32\sru\SRUDB.dat
Gözlem Notu: Son 30-60 günde çalışan uygulamaların ağ ve disk kullanım istatistiklerini tutar; dosya transferi hacmini gösterir.
```

```
5. Cortana DB
Öncelik: Orta
Konum → %LOCALAPPDATA%\Packages\Microsoft.Windows.Cortana_*\LocalState\DeviceSearchCache\AppCache.db
Gözlem Notu: Cortana arama önbelleğindeki dosya ve uygulama arama geçmişini tutar (Win10).
```

```
6. Windows Search DB (Win11)
Öncelik: Orta
Konum → %PROGRAMDATA%\Microsoft\Search\Data\Applications\Windows\
Gözlem Notu: Win11'deki güncellenmiş arama veritabanı yapısını tutar; Windows.edb ile birlikte incelenir.
```

```
7. Syscache.hve
Öncelik: Düşük
Konum → C:\System Volume Information\Syscache.hve
Gözlem Notu: Sistem birimine yazılan dosyaların referanslarını tutar; eski Windows sürümlerinde daha yaygındır.
```

```
8. Windows Timeline (ActivitiesCache.db)
Öncelik: Orta
Konum → %USERPROFILE%\AppData\Local\ConnectedDevicesPlatform\<L.*>\ActivitiesCache.db
Gözlem Notu: Kullanıcının cihazlar arası etkinlik geçmişini tutar; açılan dosya ve uygulama URI'lerini içerir.
```

```
9. hiberfil.sys
Öncelik: Yüksek
Erişim: Live System
Konum → C:\hiberfil.sys
Gözlem Notu: Uyku modunda RAM içeriğinin sıkıştırılmış kopyasını tutar; bellek analizi gibi süreç ve dosya erişim bilgisi çıkarılabilir.
```

```
10. pagefile.sys
Öncelik: Orta
Erişim: Live System
Konum → C:\pagefile.sys
Gözlem Notu: RAM'den diske swap edilen bellek sayfalarını tutar; dosya yolları, komut satırları ve parola kalıntıları bulunabilir.
```

```
11. swapfile.sys
Öncelik: Düşük
Erişim: Live System
Konum → C:\swapfile.sys
Gözlem Notu: Modern uygulamaların (UWP) suspend edilen bellek verilerini tutar; Win10+ sistemlerde pagefile'ı tamamlar.
```

```
12. setupapi.dev.log (USB Kurulum)
Öncelik: Yüksek
Konum → C:\Windows\INF\setupapi.dev.log
Gözlem Notu: USB ve diğer PnP cihazların ilk kurulum tarih/saatini ve sürücü bilgisini düz metin olarak tutar.
```

```
13. setupapi.setup.log
Öncelik: Düşük
Konum → C:\Windows\INF\setupapi.setup.log
Gözlem Notu: Windows kurulumu ve bileşen güncellemesi sırasındaki cihaz kurulum detaylarını tutar.
```

```
14. FileZilla XML Geçmiş
Öncelik: Orta
Konum → %APPDATA%\FileZilla\recentservers.xml
Gözlem Notu: Son bağlanılan FTP/SFTP sunucularının adres, port, kullanıcı adı ve bazen şifre bilgisini XML formatında tutar.
```

```
15. FileZilla Kuyruk
Öncelik: Orta
Konum → %APPDATA%\FileZilla\queue.sqlite3
Gözlem Notu: Transfer kuyruğundaki dosyaların kaynak ve hedef yollarını SQLite veritabanında tutar.
```

```
16. WinSCP Log
Öncelik: Orta
Konum → %APPDATA%\WinSCP.ini
Gözlem Notu: WinSCP ile bağlanılan sunucu bilgilerini ve oturum ayarlarını tutar.
```

```
17. Outlook Attachment Cache (SecureTemp)
Öncelik: Orta
Konum → %LOCALAPPDATA%\Microsoft\Windows\INetCache\Content.Outlook\
Gözlem Notu: Outlook'ta açılan e-posta eklerinin geçici kopyalarını tutar; silinen eklerin kalıntıları bulunabilir.
```

```
18. Notepad Unsaved Tabs (Win11)
Öncelik: Orta
Konum → %LOCALAPPDATA%\Packages\Microsoft.WindowsNotepad_*\LocalState\TabState\
Gözlem Notu: Win11 Notepad'de kaydedilmemiş sekmelerin içeriğini tutar; hassas veri notu veya komut taslakları bulunabilir.
```

```
19. Sticky Notes DB
Öncelik: Düşük
Konum → %LOCALAPPDATA%\Packages\Microsoft.MicrosoftStickyNotes_*\LocalState\plum.sqlite
Gözlem Notu: Yapışkan not içeriklerini SQLite formatında tutar; parola, IP adresi veya komut notu bırakılmış olabilir.
```

```
20. Spool Dosyaları (Print Spooler)
Öncelik: Düşük
Konum → C:\Windows\System32\spool\PRINTERS\
Gözlem Notu: Yazdırma kuyruğundaki .SPL ve .SHD dosyalarını tutar; yazdırılan belgenin içeriği kurtarılabilir.
```

```
21. PSReadLine Geçmişi
Öncelik: Yüksek
Konum → %APPDATA%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
Gözlem Notu: PowerShell konsolunda yazılan dosya işlem komutlarının (Copy, Move, Remove) tam geçmişini düz metin tutar.
```

```
22. BITS Database
Öncelik: Orta
Konum → %ALLUSERSPROFILE%\Microsoft\Network\Downloader\qmgr*.dat
Gözlem Notu: BITS ile indirilen dosyaların kaynak URL, hedef yol ve iş durumunu tutar.
```

```
23. BITS Database (Win10/11)
Öncelik: Orta
Konum → %ALLUSERSPROFILE%\Microsoft\Network\Downloader\
Gözlem Notu: Win10/11'de ESE veritabanı formatına geçen BITS kayıtlarını tutar.
```

```
24. WordPad RecentFileList
Öncelik: Düşük
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Applets\Wordpad\Recent File List
Gözlem Notu: WordPad ile açılan son dosyaların tam yolunu tutar.
```

```
25. Paint MRU
Öncelik: Düşük
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Applets\Paint\Recent File List
Gözlem Notu: Paint ile açılan son resim dosyalarının tam yolunu tutar.
```

```
26. WMP Database
Öncelik: Düşük
Konum → %LOCALAPPDATA%\Microsoft\Media Player\
Gözlem Notu: Windows Media Player kütüphanesindeki medya dosyalarının yolunu ve metadata bilgisini tutar.
```

```
27. OLE Compound Dosya Metadata
Öncelik: Düşük
Konum → <Office dosyaları içinde gömülü>
Gözlem Notu: Office belgelerinin OLE yapısında gömülü dosya yollarını, yazar adını ve son kaydedilen konumu tutar.
```

```
28. MSI Log (Windows Installer)
Öncelik: Düşük
Konum → %TEMP%\MSI*.log
Gözlem Notu: MSI kurulumu sırasında kopyalanan dosyaların hedef yolunu ve kurulum zamanını tutar.
```

```
29. Steam Shader Cache
Öncelik: Düşük
Konum → %LOCALAPPDATA%\Steam\htmlcache\
Gözlem Notu: Steam istemcisinin HTML önbellek dosyalarını tutar; uygulama etkileşim geçmişi için incelenir.
```

```
30. Reparse Point Metadata (Symlink/Junction)
Öncelik: Düşük
Konum → $MFT içinde (ReparsePoint attribute)
Gözlem Notu: Sembolik bağlantı ve junction noktalarının hedef yolunu $MFT reparse attribute içinde tutar.
```

```
31. VSS Writer Metadata
Öncelik: Düşük
Konum → C:\System Volume Information\
Gözlem Notu: Volume Shadow Copy writer metadata ve snapshot zaman damgalarını tutar.
```

```
32. Microsoft Teams Download Cache
Öncelik: Orta
Konum → %USERPROFILE%\Downloads\ + %APPDATA%\Microsoft\Teams\
Gözlem Notu: Teams üzerinden indirilen dosyaların hedef yolunu ve uygulama önbellek verilerini tutar.
```

```
33. CBS Log
Öncelik: Düşük
Konum → C:\Windows\Logs\CBS\CBS.log
Gözlem Notu: Component-Based Servicing işlemlerini kaydeder; sistem dosyası değişiklik ve güncelleme geçmişini tutar.
```

```
34. DISM Log
Öncelik: Düşük
Konum → C:\Windows\Logs\DISM\dism.log
Gözlem Notu: DISM aracıyla yapılan imaj düzenleme, özellik ekleme/kaldırma ve onarım işlemlerinin kaydını tutar.
```

```
35. Windows Search History
Öncelik: Düşük
Konum → %LOCALAPPDATA%\Microsoft\Windows\Explorer\ (SearchHistory)
Gözlem Notu: Explorer'daki arama geçmişi önbelleğini tutar; WordWheelQuery ile birlikte analiz edilir.
```
