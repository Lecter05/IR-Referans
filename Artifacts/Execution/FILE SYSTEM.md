## FILE SYSTEM ARTIFACT'leri

```
1. Prefetch
Öncelik: Yüksek
Konum → C:\Windows\Prefetch\<EXENAME>-<HASH>.pf
Gözlem Notu: Son 8 çalıştırma zamanı, çalıştırma sayısı ve yüklenen dosya/dizin listesini tutar (Win11 SSD'de varsayılan açık).
```

```
2. SRUM (System Resource Usage Monitor)
Öncelik: Yüksek
Konum → C:\Windows\System32\sru\SRUDB.dat
Gözlem Notu: Son 30-60 günde çalışan her programın CPU, ağ, enerji kullanım detayını kullanıcı SID'i ile birlikte tutar.
```

```
3. Scheduled Tasks XML
Öncelik: Yüksek
Konum → C:\Windows\System32\Tasks\ ve alt dizinleri
Gözlem Notu: Zamanlanmış görevin XML tanımını (komut, argüman, tetikleyici, oluşturan kullanıcı) içerir. (T1053.005)
```

```
4. WMI Repository
Öncelik: Yüksek
Konum → C:\Windows\System32\wbem\Repository\ (OBJECTS.DATA, INDEX.BTR, MAPPING*.MAP)
Gözlem Notu: WMI event subscription ile çalıştırılan komut/script'lerin kalıcı tanımlarını tutar. (T1047)
```

```
5. PowerShell ConsoleHost History
Öncelik: Yüksek
Konum → %APPDATA%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
Gözlem Notu: Kullanıcının PowerShell konsolunda yazdığı tüm komutları düz metin olarak saklar. (T1059.001)
```

```
6. PowerShell Transcript Logs (Varsayılan: Kapalı)
Öncelik: Yüksek
Konum → Varsayılan çıktı dizini (GPO ile yapılandırılır, genellikle %USERPROFILE%\Documents)
Gözlem Notu: Oturum boyunca girdi/çıktıyı tam metin olarak kaydeder; GPO ile etkinleştirildiğinde her oturum için ayrı dosya oluşturur.
```

```
7. ActivitiesCache.db (Timeline)
Öncelik: Orta
Konum → %LOCALAPPDATA%\ConnectedDevicesPlatform\<ID>\ActivitiesCache.db
Gözlem Notu: Çalıştırılan uygulamaların AppID, başlangıç/bitiş zamanı ve odak süresi kaydını SQLite formatında tutar (Win10; Win11'de kısıtlı).
```

```
8. Recent / LNK Dosyaları (Shortcut Execution)
Öncelik: Orta
Konum → %APPDATA%\Microsoft\Windows\Recent\ ve C:\Users\<user>\Desktop\*.lnk
Gözlem Notu: LNK hedef yolu, MAC zaman damgaları ve hedef dosyanın volume bilgisini tutar; dolaylı çalıştırma kanıtıdır.
```

```
9. Jump Lists
Öncelik: Orta
Konum → %APPDATA%\Microsoft\Windows\Recent\AutomaticDestinations\ ve CustomDestinations\
Gözlem Notu: Uygulamaların son açtığı dosyaların listesini tutar; uygulamanın çalıştırıldığını dolaylı olarak kanıtlar.
```

```
10. $MFT Zaman Damgaları
Öncelik: Orta
Konum → \\.\C: (raw) — $MFT
Gözlem Notu: EXE/DLL/script dosyalarının Created/Modified/Accessed zaman damgalarını ve $SI vs $FN tutarsızlığını inceler (timestomping tespiti).
```

```
11. $UsnJrnl (USN Journal)
Öncelik: Orta
Konum → \\.\C: — $Extend\$UsnJrnl:$J
Gözlem Notu: Dosya oluşturma, silme, yeniden adlandırma kayıtlarını tutar; silinmiş EXE veya script dosyalarının varlığını kanıtlar.
```

```
12. BITS Jobs Veritabanı
Öncelik: Orta
Konum → C:\ProgramData\Microsoft\Network\Downloader\qmgr.db
Gözlem Notu: BITS ile indirilen ve notify komutuyla çalıştırılan dosyaların URL, hedef yol ve zaman bilgisini tutar.
```

```
13. Startup Dizinleri
Öncelik: Orta
Konum → %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\ ve ProgramData karşılığı
Gözlem Notu: Oturum açılışında otomatik çalıştırılan script veya LNK dosyalarının varlığını ve zaman damgasını kontrol eder.
```

```
14. Superfetch / SysMain Veritabanı
Öncelik: Düşük
Konum → C:\Windows\Prefetch\Ag*.db
Gözlem Notu: Uzun süreli çalıştırma geçmişi ve erişim paternlerini tutar; ek bağlam sağlar.
```

```
15. Windows Error Reporting (WER)
Öncelik: Düşük
Konum → C:\ProgramData\Microsoft\Windows\WER\ReportArchive\ ve ReportQueue\
Gözlem Notu: Çöken veya hata veren uygulamanın tam yolu, modül listesi ve kilitlenme zamanını tutar.
```

```
16. Recycle Bin ($I / $R dosyaları)
Öncelik: Düşük
Konum → C:\$Recycle.Bin\{SID}\
Gözlem Notu: Silinen EXE veya script dosyalarının orijinal yolunu, boyutunu ve silinme zamanını tutar.
```

```
17. Thumbcache / IconCache
Öncelik: Düşük
Konum → %LOCALAPPDATA%\Microsoft\Windows\Explorer\iconcache_*.db
Gözlem Notu: Daha önce var olan ancak silinmiş bir EXE'nin simge verisinin hâlâ cachede bulunması dolaylı kanıt oluşturur.
```

---

> Varsayılan: Kapalı ibaresi taşıyan artifact'lar, olay öncesinde etkinleştirilmemişse mevcut olmayabilir.
>
> "Erişim: Live System" yalnızca canlı sistem veya RAM dump gerektiren artifact'larda belirtilmiştir.  
>
> Öncelik değerleri, execution kanıtı sağlama güvenilirliği ifade eder.
