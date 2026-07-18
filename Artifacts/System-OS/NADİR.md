
```
1. Last Access Timestamp Yapılandırması
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\FileSystem → NtfsDisableLastAccessUpdate
Gözlem Notu: Değeri 1 veya 0x80000001 ise son erişim zaman damgaları güncellenmez; dosya erişim analizini doğrudan etkiler.
```

```
2. BITS Jobs
Öncelik: Orta
Konum → HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\BITS\ ve C:\ProgramData\Microsoft\Network\Downloader\qmgr0.dat / qmgr1.dat
Gözlem Notu: BITS transferlerinin veritabanıdır; saldırganlar dosya indirme ve persistence için BITS görevlerini kullanabilir.
```

```
3. Measured Boot / TCG Log
Öncelik: Orta
Konum → C:\Windows\Logs\MeasuredBoot\*.log
Gözlem Notu: TPM tarafından ölçülen boot bileşenlerinin hash günlüğüdür; önyükleme zinciri bütünlüğünü doğrular.
```

```
4. Scheduled Task Atlık Dosyaları
Öncelik: Düşük
Konum → C:\Windows\System32\Tasks\Microsoft\Windows\ alt klasörleri
Gözlem Notu: Varsayılan Windows bakım görevleri arasına gizlenmiş kötü amaçlı görev tanımları aranmalıdır.
```

```
5. Print Nightmare / Spooler İzleri
Öncelik: Düşük
Konum → C:\Windows\System32\spool\drivers\ ve HKLM\SYSTEM\CurrentControlSet\Control\Print\
Gözlem Notu: Yazıcı sürücüsü olarak yüklenen kötü amaçlı DLL dosyaları için spool/drivers dizini kontrol edilmelidir.
```

```
6. Font Cache
Öncelik: Düşük
Konum → C:\Windows\ServiceProfiles\LocalService\AppData\Local\FontCache\
Gözlem Notu: Font dosyası aracılığıyla exploit edilen güvenlik açıklarının izlerini içerebilir.
```

```
7. Windows Notification Database
Öncelik: Düşük
Konum → C:\Users\<Kullanıcı>\AppData\Local\Microsoft\Windows\Notifications\wpndatabase.db
Gözlem Notu: Sistem ve uygulama bildirimlerinin geçmişini SQLite veritabanında saklar; zaman çizelgesi oluşturmada yardımcıdır.
```

```
8. ETL Boot Trace
Öncelik: Düşük
Konum → C:\Windows\System32\WDI\LogFiles\BootCKCL.etl
Gözlem Notu: Önyükleme sırasında kaydedilen ETW izleme dosyasıdır; boot sürecindeki anomaliler incelenebilir.
```

```
9. Delivery Optimization Cache
Öncelik: Düşük
Konum → C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Microsoft\Windows\DeliveryOptimization\
Gözlem Notu: Windows Update ve Store içeriklerinin P2P dağıtım önbelleğidir.
```

```
10. TPM Bilgileri
Öncelik: Düşük
Konum → HKLM\SYSTEM\CurrentControlSet\Services\TPM\ ve tpm.msc
Gözlem Notu: TPM sürümü, durumu ve sahiplik bilgisini içerir; Secure Boot ve BitLocker bütünlüğü doğrulamasında kullanılır.
```

```
11. System Restore Yapılandırması
Öncelik: Düşük
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SystemRestore
Gözlem Notu: Sistem geri yükleme özelliğinin aktif/pasif durumunu ve son geri yükleme noktası bilgisini içerir.
```

```
12. WDI\Perftrack
Öncelik: Düşük
Konum → C:\Windows\System32\WDI\
Gözlem Notu: Windows Diagnostic Infrastructure performans izleme verileri; boot ve resume performans anormalliklerini gösterir.
```

```
13. Token Broker Cache
Öncelik: Düşük
Konum → C:\Users\<Kullanıcı>\AppData\Local\Microsoft\TokenBroker\Cache\
Gözlem Notu: Microsoft hesap kimlik doğrulama token'larının önbelleğidir; oturum token'ları içerebilir.
```

