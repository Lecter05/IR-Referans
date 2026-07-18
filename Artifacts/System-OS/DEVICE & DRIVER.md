
```
1. USBSTOR Registry
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR\
Gözlem Notu: Bağlanan USB depolama cihazlarının üretici, model, seri numarası ve ilk/son bağlantı zaman damgalarını içerir.
```

```
2. USB Registry
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Enum\USB\
Gözlem Notu: Tüm USB cihazlarının (depolama dışı dahil) VID/PID ve cihaz tanımlayıcılarını listeler.
```

```
3. MountedDevices
Öncelik: Yüksek
Konum → HKLM\SYSTEM\MountedDevices
Gözlem Notu: Sürücü harfi ve volume GUID eşlemelerini içerir; hangi cihazların hangi harfe atandığını gösterir.
```

```
4. setupapi.dev.log (Cihaz detayı)
Öncelik: Yüksek
Konum → C:\Windows\INF\setupapi.dev.log
Gözlem Notu: Her cihaz kurulumu için zaman damgalı satır satır günlük tutar; USB ilk bağlantı zamanı doğrulaması için kullanılır.
```

```
5. Portable Devices
Öncelik: Orta
Konum → HKLM\SOFTWARE\Microsoft\Windows Portable Devices\Devices\
Gözlem Notu: MTP/PTP protokolüyle bağlanan taşınabilir cihazların (telefon, kamera) friendly name'lerini saklar.
```

```
6. DeviceContainers
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Enum\SWD\WPDBUSENUM\
Gözlem Notu: WPD (Windows Portable Devices) aracılığıyla erişilen cihazların ek tanımlayıcılarını içerir.
```

```
7. Volume GUID Eşleme
Öncelik: Orta
Konum → HKLM\SYSTEM\MountedDevices + HKLM\SOFTWARE\Microsoft\Windows Search\VolumeInfoCache\
Gözlem Notu: Birim GUID'lerini fiziksel cihazlara eşlemek ve USB depolama birimini tanımlamak için kullanılır.
```

```
8. Driver Store (FileRepository)
Öncelik: Orta
Konum → C:\Windows\System32\DriverStore\FileRepository\
Gözlem Notu: Sistemde yüklü tüm sürücü paketlerinin depolandığı dizindir; beklenmeyen sürücüler aranmalıdır.
```

```
9. Bluetooth Cihaz Geçmişi
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Devices\
Gözlem Notu: Eşleştirilmiş Bluetooth cihazlarının MAC adresleri ve cihaz adlarını içerir.
```

```
10. VM Disk Dosya İzleri
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Enum\SCSI altındaki disk model tanımlayıcısı
Gözlem Notu: "Virtual", "VBOX HARDDISK" gibi sanal disk isimleri aranır.
```

```
11. EMDMgmt (ReadyBoost)
Öncelik: Düşük
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\EMDMgmt
Gözlem Notu: USB cihaz seri numarası ve son bağlantı zamanı bilgisini ReadyBoost performans verileriyle birlikte saklar.
```

```
12. Disk Signature
Öncelik: Düşük
Konum → HKLM\SYSTEM\MountedDevices → \DosDevices\ girdileri
Gözlem Notu: Bağlanan disk birimlerinin disk imzası ve partition offset bilgilerini içerir.
```

```
13. Signed Catalog Dosyaları
Öncelik: Düşük
Konum → C:\Windows\System32\CatRoot\{hash}\*.cat
Gözlem Notu: Sürücü ve bileşen imza doğrulama kataloglarıdır; imza zinciri bütünlüğü kontrolü için kullanılır.
```
