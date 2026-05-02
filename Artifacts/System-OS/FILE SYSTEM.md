
```
1. $MFT (Master File Table)
Öncelik: Yüksek
Konum → <Volume>\$MFT
Gözlem Notu: NTFS birimdeki tüm dosya ve klasörlerin metadata kaydını (oluşturulma, değiştirilme, erişim zamanları, boyut) içerir.
```

```
2. $LogFile
Öncelik: Yüksek
Konum → <Volume>\$LogFile
Gözlem Notu: NTFS işlem günlüğüdür; son dosya sistemi değişikliklerinin kurtarılması için kullanılır.
```

```
3. $UsnJrnl
Öncelik: Yüksek
Konum → <Volume>\$Extend\$UsnJrnl:$J
Gözlem Notu: Dosya oluşturma, silme, yeniden adlandırma ve içerik değişikliklerinin kronolojik kaydını tutar.
```

```
4. Volume Shadow Copies
Öncelik: Yüksek
Konum → \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy<N>\
Gözlem Notu: Önceki zaman noktalarındaki dosya ve registry durumlarının anlık görüntüleridir; silinen kanıtların kurtarılmasında kritiktir.
```

```
5. Hibernation Dosyası
Öncelik: Yüksek
Konum → C:\hiberfil.sys
Gözlem Notu: Uyku moduna geçişteki RAM'in tam dökümüdür; bellek analizi yapılabilir.
```

```
6. Setupapi Log (Cihaz Kurulumu)
Öncelik: Yüksek
Konum → C:\Windows\INF\setupapi.dev.log
Gözlem Notu: Donanım ve sürücü kurulum olaylarının zaman damgalı günlüğüdür; USB cihaz ilk bağlantı zamanı için kritiktir.
```

```
7. SRU (System Resource Usage)
Öncelik: Yüksek
Konum → C:\Windows\System32\sru\SRUDB.dat
Gözlem Notu: Uygulama bazında ağ kullanımı, CPU süresi, enerji tüketimi ve veri transferi istatistiklerini ESE veritabanında tutar.
```

```
8. Prefetch Dosyaları
Öncelik: Yüksek
Konum → C:\Windows\Prefetch\*.pf
Gözlem Notu: Çalıştırılan uygulamaların dosya yolları, çalışma sayıları ve son 8 çalışma zamanını içerir.
```

```
9. Tasks Klasörü
Öncelik: Yüksek
Konum → C:\Windows\System32\Tasks\
Gözlem Notu: Zamanlanmış görevlerin XML tanım dosyaları; çalıştırılacak komut, tetikleyici ve oluşturan kullanıcı bilgisini içerir.
```

```
10. Startup Klasörleri
Öncelik: Yüksek
Konum → C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\ ve C:\Users\<Kullanıcı>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\
Gözlem Notu: Bu klasörlere yerleştirilen kısayol veya dosyalar oturum açılışında otomatik çalıştırılır.
```

```
11. $I30 Index Kayıtları
Öncelik: Orta
Konum → Her NTFS klasörünün $I30 attribute'u
Gözlem Notu: Silinmiş dosya adları slack alanında kalabilir; klasör içerik geçmişinin kurtarılmasında kullanılır.
```

```
12. Pagefile
Öncelik: Orta
Konum → C:\pagefile.sys
Gözlem Notu: RAM'den diske aktarılmış bellek sayfalarını içerir; şifreler, komutlar ve süreç belleği kalıntıları bulunabilir.
```

```
13. Windows.old
Öncelik: Orta
Konum → C:\Windows.old\
Gözlem Notu: Büyük sürüm yükseltmesi sonrası eski işletim sistemi dosyaları ve kullanıcı verileri bu klasörde saklanır.
```

```
14. Panther Kurulum Logları
Öncelik: Orta
Konum → C:\Windows\Panther\
Gözlem Notu: Windows kurulum ve yükseltme sürecinin detaylı günlüklerini (setupact.log, setuperr.log, unattend.xml) içerir.
```

```
15. Windows Update Log
Öncelik: Orta
Konum → C:\Windows\SoftwareDistribution\DataStore\DataStore.edb
Gözlem Notu: Güncelleme geçmişi ESE veritabanı formatındadır; yüklenen ve bekleyen güncellemelerin kaydını içerir.
```

```
16. WER Raporları
Öncelik: Orta
Konum → C:\ProgramData\Microsoft\Windows\WER\
Gözlem Notu: Uygulama ve sistem çökmelerine ait hata raporları; crash eden sürecin adı, modülleri ve zaman damgası bulunur.
```

```
17. Hosts Dosyası
Öncelik: Orta
Konum → C:\Windows\System32\drivers\etc\hosts
Gözlem Notu: DNS çözümlemesini geçersiz kılan statik girişler; kötü amaçlı yönlendirme veya güvenlik ürünü engelleme tespiti için kontrol edilmelidir.
```

```
18. Drivers Klasörü
Öncelik: Orta
Konum → C:\Windows\System32\drivers\
Gözlem Notu: Kernel-mode sürücü dosyalarının (.sys) bulunduğu dizindir; beklenmeyen veya imzasız sürücüler incelenmelidir.
```

```
19. CatRoot / CatRoot2
Öncelik: Orta
Konum → C:\Windows\System32\catroot\ ve catroot2\
Gözlem Notu: Dijital imza katalog dosyaları ve Windows Update imza doğrulama veritabanıdır; imza manipülasyonu tespiti için önemlidir.
```

```
20. Kod Bütünlüğü Logları
Öncelik: Orta
Konum → C:\Windows\System32\CodeIntegrity\
Gözlem Notu: WDAC ve HVCI politika dosyaları (.p7b, .cip); imza doğrulama ve driver bütünlüğü yapılandırmasını gösterir.
```

```
21. wbem Repository
Öncelik: Orta
Konum → C:\Windows\System32\wbem\Repository\
Gözlem Notu: WMI kalıcı abonelikleri (event subscriptions) bu veritabanında tutulur; WMI tabanlı persistence tespiti için incelenir.
```

```
22. Driver Store (FileRepository)
Öncelik: Orta
Konum → C:\Windows\System32\DriverStore\FileRepository\
Gözlem Notu: Sistemde yüklü tüm sürücü paketlerinin depolandığı dizindir; beklenmeyen sürücüler aranmalıdır.
```

```
23. Swapfile
Öncelik: Düşük
Konum → C:\swapfile.sys
Gözlem Notu: Modern Windows uygulamaları (UWP) için kullanılan takas dosyasıdır; uygulama bellek kalıntıları içerebilir.
```

```
24. Setupapi App Log
Öncelik: Düşük
Konum → C:\Windows\INF\setupapi.app.log
Gözlem Notu: Uygulama düzeyinde kurulum olaylarının kaydıdır.
```

```
25. CBS Log
Öncelik: Düşük
Konum → C:\Windows\Logs\CBS\CBS.log
Gözlem Notu: Windows bileşen deposu (Component Based Servicing) işlemlerinin ve güncelleme kurulumlarının detaylı günlüğüdür.
```

```
26. DISM Log
Öncelik: Düşük
Konum → C:\Windows\Logs\DISM\dism.log
Gözlem Notu: Windows görüntü servis işlemlerinin ve özellik ekleme/kaldırma faaliyetlerinin kaydıdır.
```

```
27. Superfetch/SysMain Veritabanları
Öncelik: Düşük
Konum → C:\Windows\Prefetch\Ag*.db
Gözlem Notu: Uygulama başlatma kalıplarının istatistiksel kaydını tutar.
```

```
28. WinSxS (Side-by-Side Assembly)
Öncelik: Düşük
Konum → C:\Windows\WinSxS\
Gözlem Notu: Windows bileşenlerinin farklı sürümlerinin tutulduğu depodur; supply chain saldırı izleri aranabilir.
```

```
29. TrustedInstaller Log
Öncelik: Düşük
Konum → C:\Windows\Logs\CBS\TrustedInstaller.log (CBS.log içinde)
Gözlem Notu: TrustedInstaller servisi tarafından gerçekleştirilen bileşen yükleme ve güncelleme işlemlerinin kaydıdır.
```

```
30. SoftwareDistribution\Download
Öncelik: Düşük
Konum → C:\Windows\SoftwareDistribution\Download\
Gözlem Notu: İndirilen güncelleme paketlerinin geçici olarak saklandığı klasördür.
```

```
31. ELAM (Early Launch Anti-Malware) Verileri
Öncelik: Düşük
Konum → C:\Windows\ELAM\
Gözlem Notu: Önyükleme sırasında kernel'den önce yüklenen anti-malware sürücü verilerini içerir.
```

```
32. Cryptnet URL Cache
Öncelik: Düşük
Konum → C:\Users\<Kullanıcı>\AppData\LocalLow\Microsoft\CryptnetUrlCache\
Gözlem Notu: Sertifika doğrulama (CRL/OCSP) yanıtlarının önbelleğidir; sertifika tabanlı saldırı izleri içerebilir.
```
