
```
1. Prefetch Dosyalarının Silinmesi
Öncelik: Yüksek
Konum → C:\Windows\Prefetch\*.pf
MITRE: T1070.004
Gözlem Notu: Prefetch klasörünün tamamen boşaltılıp boşaltılmadığına veya belirli .pf dosyalarının silinip silinmediğine bakılır.
```

```
2. $MFT (Master File Table) Kayıt Analizi
Öncelik: Yüksek
Konum → C:\$MFT
MITRE: T1070.004
Gözlem Notu: Silinmiş dosya kayıtlarının $MFT içindeki IN_USE flag'inin kaldırılmış olup olmadığına bakılır.
```

```
3. $UsnJrnl (USN Change Journal)
Öncelik: Yüksek
Konum → C:\$Extend\$UsnJrnl:$J
MITRE: T1070.004
Gözlem Notu: Dosya silme, yeniden adlandırma ve oluşturma olaylarının journal'daki kaydına bakılır; journal'ın fsutil ile silinip silinmediği kontrol edilir.
```

```
4. Amcache.hve Temizleme
Öncelik: Yüksek
Konum → C:\Windows\AppCompat\Programs\Amcache.hve
MITRE: T1070.004
Gözlem Notu: Çalıştırılan programların hash ve zaman bilgilerinin silinip silinmediğine veya hive'ın sıfırlanıp sıfırlanmadığına bakılır.
```

```
5. SRUM (System Resource Usage Monitor) Veritabanı
Öncelik: Yüksek
Konum → C:\Windows\System32\sru\SRUDB.dat
MITRE: T1070.004
Gözlem Notu: Uygulama çalışma geçmişi ve ağ kullanım verilerinin silinip silinmediğine bakılır; silme girişimi bile iz bırakır.
```

```
6. Recent Dosyalar ve LNK Dosyaları Silme
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Recent\*.lnk ve %APPDATA%\Microsoft\Office\Recent\
MITRE: T1070.004
Gözlem Notu: Son kullanılan dosya kısayollarının toplu silinip silinmediğine bakılır.
```

```
7. Jump Lists Temizleme
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations\*.automaticDestinations-ms ve CustomDestinations\
MITRE: T1070.004
Gözlem Notu: Görev çubuğu ve başlat menüsü erişim geçmişinin toplu silinip silinmediğine bakılır.
```

```
8. Güvenli Silme Araçları İzleri
Öncelik: Yüksek
Konum → Prefetch (sdelete.pf, cipher.pf, eraser.pf, bleachbit.pf) ve $UsnJrnl kayıtları
MITRE: T1070.004
Gözlem Notu: SDelete, Cipher /w, Eraser, BleachBit gibi araçların Prefetch veya Amcache kaydına bakılır.
```

```
9. PowerShell ConsoleHost_history Silme
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
MITRE: T1070.003
Gözlem Notu: PowerShell komut geçmişi dosyasının silinip silinmediğine veya boşaltılıp boşaltılmadığına bakılır.
```

```
10. $LogFile (NTFS Transaction Log)
Öncelik: Orta
Konum → C:\$LogFile
MITRE: T1070.004
Gözlem Notu: NTFS işlem logundaki silme operasyonlarının izlerine bakılır.
```

```
11. $I30 (Directory Index) Slack Space
Öncelik: Orta
Konum → Her NTFS dizininin $I30 index attribute'u
MITRE: T1070.004
Gözlem Notu: Silinmiş dosya adlarının dizin index slack alanında kalıntı olarak bulunup bulunmadığına bakılır.
```

```
12. Windows.edb (Windows Search Index)
Öncelik: Orta
Konum → C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.edb
MITRE: T1070.004
Gözlem Notu: Arama indeks veritabanının silinip silinmediğine veya boyutunun anormal şekilde küçülüp küçülmediğine bakılır.
```

```
13. Thumbcache / Thumbs.db Silme
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Local\Microsoft\Windows\Explorer\thumbcache_*.db
MITRE: T1070.004
Gözlem Notu: Küçük resim önbellek dosyalarının silinip silinmediğine bakılır; silinmiş görsel dosyaların thumbnail kalıntısı bulunabilir.
```

```
14. ActivitiesCache.db (Timeline) Silme
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Local\ConnectedDevicesPlatform\<account>\ActivitiesCache.db
MITRE: T1070.004
Gözlem Notu: Windows Timeline / Activity History veritabanının silinip silinmediğine bakılır (Win10; Win11'de kaldırıldı).
```

```
15. Disk Üzerinde Üzerine Yazma İzleri (Wiping)
Öncelik: Orta
Konum → Unallocated space ve dosya slack alanları
MITRE: T1485
Gözlem Notu: Boş alanlarda tekrarlayan byte pattern'lerinin (0x00, 0xFF, rastgele) varlığına bakılır.
```

```
16. $Recycle.Bin Dışında Doğrudan Silme
Öncelik: Orta
Konum → $MFT ve $UsnJrnl kayıtları
MITRE: T1070.004
Gözlem Notu: Shift+Delete veya programatik silme ile Recycle Bin'i atlayan dosya silme izlerine bakılır.
```

```
17. Alternate Data Streams (ADS) Silme
Öncelik: Orta
Konum → Dosyalar üzerindeki Zone.Identifier ve diğer ADS stream'leri
MITRE: T1070.004
Gözlem Notu: Zone.Identifier (MOTW) stream'inin dosyadan kaldırılıp kaldırılmadığına bakılır; indirme kaynağı bilgisi gizlenir.
```

```
18. Pagefile / Hiberfil Analizi
Öncelik: Orta
Konum → C:\pagefile.sys ve C:\hiberfil.sys
MITRE: T1070.004
Gözlem Notu: Bellek kalıntılarının pagefile veya hibernate dosyasından elde edilip edilemeyeceğine bakılır; saldırgan bunları sıfırlamış olabilir.
```

```
19. WER (Windows Error Reporting) Raporları Silme
Öncelik: Düşük
Konum → C:\ProgramData\Microsoft\Windows\WER\ ve C:\Users\<user>\AppData\Local\Microsoft\Windows\WER\
MITRE: T1070.004
Gözlem Notu: Crash raporlarının silinip silinmediğine bakılır; zararlı yazılım crash dump'ları forensic veri içerebilir.
```
