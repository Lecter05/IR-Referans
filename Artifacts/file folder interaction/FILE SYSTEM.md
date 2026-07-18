
## LNK (Shortcut) Dosyaları

```
1. Recent Items LNK
Öncelik: Yüksek
Konum → %APPDATA%\Microsoft\Windows\Recent\
Gözlem Notu: Açılan her dosya için otomatik oluşturulan LNK dosyası hedef yolunu, MAC zamanlarını ve volume bilgisini tutar.
```

```
2. AutomaticDestinations (Jump Lists)
Öncelik: Yüksek
Konum → %APPDATA%\Microsoft\Windows\Recent\AutomaticDestinations\
Gözlem Notu: Her uygulamanın AppID'sine göre son erişilen dosyaların OLE compound yapısında listesini tutar.
```

```
3. CustomDestinations (Jump Lists)
Öncelik: Yüksek
Konum → %APPDATA%\Microsoft\Windows\Recent\CustomDestinations\
Gözlem Notu: Kullanıcının veya uygulamanın elle sabitlediği dosya/görev kayıtlarını tutar.
```

```
4. Office Recent LNK
Öncelik: Orta
Konum → %APPDATA%\Microsoft\Office\Recent\
Gözlem Notu: Office uygulamalarının kendi oluşturduğu LNK dosyalarını tutar; Office MRU ile çapraz doğrulanır.
```

```
5. Desktop LNK
Öncelik: Orta
Konum → %USERPROFILE%\Desktop\
Gözlem Notu: Masaüstündeki kısayolların hedef yolunu ve oluşturulma zamanını tutar; kullanıcı tarafından bilinçli yerleştirilmiş dosyalara işaret eder.
```

```
6. Startup LNK
Öncelik: Orta
Konum → %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\
Gözlem Notu: Oturum açılışında otomatik çalıştırılan dosyalara ait kısayolları tutar.
```

---

## Prefetch

```
1. Prefetch Dosyaları
Öncelik: Yüksek
Konum → C:\Windows\Prefetch\*.pf
Gözlem Notu: Çalıştırılan her EXE için yüklenen dosya/dizin listesini tutar; hangi dosyalara erişildiğini gösterir.
```

```
2. Prefetch (svchost dahil)
Öncelik: Yüksek
Konum → C:\Windows\Prefetch\ (svchost.exe-*.pf dahil tüm .pf dosyaları)
Gözlem Notu: svchost.exe hash farklılıkları ile servis bazında erişilen dosyaları ayırt etmeye yardımcı olur.
```

---

## Thumbnail Cache

```
1. Thumbcache (Genel)
Öncelik: Orta
Konum → %LOCALAPPDATA%\Microsoft\Windows\Explorer\thumbcache_*.db
Gözlem Notu: Görüntülenen resim ve belgelerin küçük resim önbelleğini tutar; silinmiş dosyaların görsel kanıtını içerebilir.
```

```
2. Thumbcache_32.db
Öncelik: Orta
Konum → %LOCALAPPDATA%\Microsoft\Windows\Explorer\thumbcache_32.db
Gözlem Notu: 32px boyutundaki küçük resimleri tutar; en küçük çözünürlüklü önbellek dosyasıdır.
```

```
3. Thumbcache_96.db
Öncelik: Orta
Konum → %LOCALAPPDATA%\Microsoft\Windows\Explorer\thumbcache_96.db
Gözlem Notu: 96px boyutundaki küçük resimleri tutar; Explorer detay görünümünde kullanılır.
```

```
4. Thumbcache_256.db
Öncelik: Orta
Konum → %LOCALAPPDATA%\Microsoft\Windows\Explorer\thumbcache_256.db
Gözlem Notu: 256px boyutundaki küçük resimleri tutar; orta simge görünümü için oluşturulur.
```

```
5. Thumbcache_1024.db
Öncelik: Orta
Konum → %LOCALAPPDATA%\Microsoft\Windows\Explorer\thumbcache_1024.db
Gözlem Notu: 1024px boyutundaki küçük resimleri tutar; büyük simge veya önizleme görünümünde oluşturulur.
```

```
6. Thumbcache_sr.db
Öncelik: Düşük
Konum → %LOCALAPPDATA%\Microsoft\Windows\Explorer\thumbcache_sr.db
Gözlem Notu: Özel çözünürlüklü küçük resimleri tutar; set-resolution thumbnail'ler için kullanılır.
```

```
7. Thumbcache_idx.db
Öncelik: Orta
Konum → %LOCALAPPDATA%\Microsoft\Windows\Explorer\thumbcache_idx.db
Gözlem Notu: Tüm thumbcache dosyalarının indeks tablosunu tutar; hangi dosyanın hangi cache'te olduğunu eşleştirir.
```

```
8. iconcache.db
Öncelik: Düşük
Konum → %LOCALAPPDATA%\Microsoft\Windows\Explorer\iconcache_*.db
Gözlem Notu: Uygulama ve dosya simgelerini cacheler; silinmiş bir programın simge verisinin hâlâ mevcut olup olmadığını gösterir.
```

---

## NTFS Metadata

```
1. $MFT (Master File Table)
Öncelik: Yüksek
Konum → C:\$MFT
Gözlem Notu: Birimdeki her dosya ve klasörün adını, boyutunu, zaman damgalarını ($SI ve $FN) ve veri konumunu tutar.
```

```
2. $UsnJrnl:$J (USN Journal)
Öncelik: Yüksek
Konum → C:\$Extend\$UsnJrnl
Gözlem Notu: Dosya oluşturma, silme, yeniden adlandırma ve değiştirme olaylarını kronolojik sırayla kaydeder.
```

```
3. $LogFile (NTFS Journal)
Öncelik: Yüksek
Konum → C:\$LogFile
Gözlem Notu: NTFS transaksiyonel işlem günlüğüdür; dosya sistemi değişikliklerinin geri alınabilir kaydını tutar.
```

```
4. $I30 (Directory Index)
Öncelik: Yüksek
Konum → <klasör>\$I30
Gözlem Notu: Klasör içindeki dosya girişlerinin indeks kaydını tutar; silinen dosyaların adı ve zaman damgası slack alanda kalabilir.
```

```
5. Zone.Identifier (ADS — MOTW)
Öncelik: Yüksek
Konum → <dosya>:Zone.Identifier (ZoneId=3/4)
Gözlem Notu: İnternetten veya güvenilmeyen kaynaktan indirilen dosyanın kaynak URL'sini ve ZoneId değerini tutar.
```

```
6. Alternate Data Streams (ADS)
Öncelik: Orta
Konum → <dosya>:<stream_adı>
Gözlem Notu: Dosyaya eklenen gizli veri akışlarını tutar; veri gizleme veya payload saklama amacıyla kullanılabilir.
```

```
7. $UsnJrnl:$MAX
Öncelik: Orta
Konum → C:\$Extend\$UsnJrnl:$MAX
Gözlem Notu: USN Journal'ın maksimum boyut ve tahsis bilgisini tutar; journal wrap-around tespiti için kontrol edilir.
```

```
8. $Secure:$SDS
Öncelik: Düşük
Konum → C:\$Secure
Gözlem Notu: Dosya ve klasör güvenlik tanımlayıcılarını (ACL) merkezi olarak tutar; izin değişikliklerini analiz eder.
```

```
9. $Bitmap
Öncelik: Düşük
Konum → C:\$Bitmap
Gözlem Notu: Birimin cluster tahsis haritasını tutar; boş alan ve kullanılan alanın dağılımını gösterir.
```

```
10. $Boot
Öncelik: Düşük
Konum → C:\$Boot
Gözlem Notu: NTFS biriminin boot sektörünü ve BPB (BIOS Parameter Block) bilgisini tutar; birim bütünlüğü doğrulaması için kullanılır.
```

---

## Recycle Bin

```
1. Recycle Bin Meta ($I dosyaları)
Öncelik: Yüksek
Konum → C:\$Recycle.Bin\<SID>\$I<filename>
Gözlem Notu: Silinen dosyanın orijinal tam yolunu, boyutunu ve silinme tarih/saatini tutar.
```

```
2. Recycle Bin İçerik ($R dosyaları)
Öncelik: Yüksek
Konum → C:\$Recycle.Bin\<SID>\$R<filename>
Gözlem Notu: Silinen dosyanın gerçek içeriğini tutar; dosya kurtarma ve içerik analizi için kullanılır.
```

---

## Downloads & Tarayıcı Dosya İzleri

```
1. Chrome Downloads
Öncelik: Yüksek
Konum → %LOCALAPPDATA%\Google\Chrome\User Data\Default\History
Gözlem Notu: İndirilen dosyaların URL, hedef yol, başlangıç/bitiş zamanı ve dosya boyutu bilgisini SQLite veritabanında tutar.
```

```
2. Edge Downloads
Öncelik: Yüksek
Konum → %LOCALAPPDATA%\Microsoft\Edge\User Data\Default\History
Gözlem Notu: Edge Chromium ile indirilen dosyaların URL, hedef yol ve zaman bilgisini SQLite veritabanında tutar.
```

```
3. Firefox Downloads
Öncelik: Yüksek
Konum → %APPDATA%\Mozilla\Firefox\Profiles\<profile>\places.sqlite
Gözlem Notu: Firefox ile indirilen dosyaların URL ve hedef yol bilgisini moz_annos tablosunda tutar.
```

```
4. IE/Edge Legacy Downloads
Öncelik: Orta
Konum → %LOCALAPPDATA%\Microsoft\Windows\INetCache\
Gözlem Notu: IE ve eski Edge tarafından önbelleğe alınan web içeriğini ve indirme kalıntılarını tutar.
```

```
5. IE Cache
Öncelik: Düşük
Konum → %LOCALAPPDATA%\Microsoft\Windows\INetCache\IE\
Gözlem Notu: IE'nin HTTP cache dosyalarını tutar; indirilen veya görüntülenen web dosyalarının kopyalarını içerir.
```

---

## Shadow Copies / VSS

```
1. Volume Shadow Copies
Öncelik: Yüksek
Konum → \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy<N>\
Gözlem Notu: Dosyaların önceki sürümlerini tutar; silinen veya değiştirilen dosyaların orijinal halini kurtarmak için kritik öneme sahiptir.
```

---

## Temp & Staging Alanları

```
1. Windows Temp
Öncelik: Orta
Konum → C:\Windows\Temp\
Gözlem Notu: Sistem ve servis süreçlerinin geçici dosyalarını tutar; exploit payload'ları ve staging dosyaları burada bırakılabilir.
```

```
2. User Temp
Öncelik: Orta
Konum → %TEMP% / %TMP%
Gözlem Notu: Kullanıcı oturumuna ait geçici dosyaları tutar; makro çıktıları, arşiv açma kalıntıları ve indirme önbellekleri bulunur.
```

```
3. AppData Temp
Öncelik: Orta
Konum → %LOCALAPPDATA%\Temp\
Gözlem Notu: User Temp ile genellikle aynı dizini gösterir; uygulama bazlı geçici dosyaları tutar.
```

---

## OneDrive / Cloud Sync

```
1. OneDrive Metadata
Öncelik: Orta
Konum → %USERPROFILE%\AppData\Local\Microsoft\OneDrive\logs\
Gözlem Notu: OneDrive senkronizasyon loglarını tutar; hangi dosyaların ne zaman yüklendiğini veya indirildiğini gösterir.
```

```
2. OneDrive SyncDiagnostics
Öncelik: Orta
Konum → %LOCALAPPDATA%\Microsoft\OneDrive\logs\SyncDiagnostics.log
Gözlem Notu: Senkronizasyon hatalarını ve dosya çakışma kayıtlarını tutar; veri sızdırma zaman çizelgesi oluşturur.
```

```
3. OneDrive Settings
Öncelik: Düşük
Konum → %LOCALAPPDATA%\Microsoft\OneDrive\settings\
Gözlem Notu: Senkronize edilen klasör listesini ve hesap yapılandırmasını tutar.
```

---

## WER (Windows Error Reporting)

```
1. WER Reports
Öncelik: Düşük
Konum → %LOCALAPPDATA%\Microsoft\Windows\WER\ReportArchive\
Gözlem Notu: Arşivlenen hata raporlarında çöken uygulamanın yolunu, modül listesini ve kilitlenme zamanını tutar.
```

```
2. WER Queue
Öncelik: Düşük
Konum → %LOCALAPPDATA%\Microsoft\Windows\WER\ReportQueue\
Gözlem Notu: Henüz gönderilmemiş hata raporlarını tutar; çökme anındaki dosya erişim bilgisini içerebilir.
```

---

## Compressed / Archive İzler

```
1. 7-Zip MRU
Öncelik: Orta
Konum → %APPDATA%\7-Zip\ (7zFM.ini)
Gözlem Notu: 7-Zip ile açılan veya oluşturulan arşivlerin son dosya yollarını tutar.
```

```
2. WinRAR MRU
Öncelik: Orta
Konum → %APPDATA%\WinRAR\ (winrar.ini, regtmp.tmp)
Gözlem Notu: WinRAR ile açılan veya oluşturulan arşivlerin geçmiş listesini ve çıkartma yollarını tutar.
```
