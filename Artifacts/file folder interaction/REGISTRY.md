
## MRU Listeleri

```
1. RecentDocs MRU
Öncelik: Yüksek
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs
Gözlem Notu: Kullanıcının açtığı son dosyaların binary MRU listesini tutar; dosya adı ve uzantısı çözümlenebilir.
```

```
2. RecentDocs (uzantıya göre)
Öncelik: Yüksek
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.<ext>
Gözlem Notu: Her dosya uzantısı için ayrı alt anahtar tutar; belirli bir dosya tipinin ne zaman açıldığını gösterir.
```

```
3. OpenSavePidlMRU
Öncelik: Yüksek
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU
Gözlem Notu: Aç/Kaydet diyaloğunda seçilen dosyaların tam yolunu uzantı bazında tutar; hangi uygulamanın hangi dosyayı açtığını gösterir.
```

```
4. LastVisitedPidlMRU
Öncelik: Yüksek
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU
Gözlem Notu: Aç/Kaydet diyaloğunda son ziyaret edilen klasörü ve bunu tetikleyen uygulamayı birlikte tutar.
```

```
5. RunMRU
Öncelik: Orta
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
Gözlem Notu: Win+R diyaloguna yazılan komutların ve dosya yollarının listesini MRU sırasıyla tutar.
```

```
6. TypedPaths
Öncelik: Orta
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths
Gözlem Notu: Explorer adres çubuğuna elle yazılan yolları (UNC dahil) tutar; erişilen ağ paylaşımlarını ortaya çıkarır.
```

```
7. WordWheelQuery (Arama MRU)
Öncelik: Orta
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery
Gözlem Notu: Explorer arama kutusuna yazılan arama terimlerini sıralı şekilde tutar; kullanıcının ne aradığını gösterir.
```

```
8. Map Network Drive MRU
Öncelik: Orta
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Map Network Drive MRU
Gözlem Notu: Ağ sürücüsü eşleme sihirbazında girilen UNC yollarını MRU sırasıyla tutar.
```

```
9. OpenSaveMRU (eski)
Öncelik: Düşük
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU
Gözlem Notu: OpenSavePidlMRU'nun eski sürümüdür; Win7 ve öncesi sistemlerden taşınan profillerde bulunabilir.
```

```
10. LastVisitedMRU (eski)
Öncelik: Düşük
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedMRU
Gözlem Notu: LastVisitedPidlMRU'nun eski sürümüdür; eski profillerden kalan verileri içerebilir.
```

```
11. PushPinFolder MRU
Öncelik: Düşük
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\PushPinFolder
Gözlem Notu: Kullanıcının Quick Access veya Explorer'a sabitlediği klasörlerin yolunu tutar.
```

```
12. MyDocs MRU (Doc Find Spec MRU)
Öncelik: Düşük
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Doc Find Spec MRU
Gözlem Notu: Eski dosya arama spesifikasyonlarını tutar; nadir ama ek bağlam sağlayabilir.
```

---

## Shell Bags

```
1. ShellBags (Desktop — BagMRU)
Öncelik: Yüksek
Konum → HKCU\Software\Microsoft\Windows\Shell\BagMRU
Gözlem Notu: Explorer'da gezilen klasörlerin hiyerarşik ağaç yapısını tutar; silinmiş klasörlerin bile varlığını kanıtlar.
```

```
2. ShellBags (Desktop — Bags)
Öncelik: Yüksek
Konum → HKCU\Software\Microsoft\Windows\Shell\Bags
Gözlem Notu: Her klasör için görünüm ayarlarını (simge boyutu, sıralama, konum) tutar; klasöre erişim zamanını dolaylı gösterir.
```

```
3. ShellBags (UsrClass — BagMRU)
Öncelik: Yüksek
Konum → HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\BagMRU
Gözlem Notu: Masaüstü dışı pencereler için klasör gezinti geçmişini tutar; ZIP, ağ paylaşımı ve kontrol paneli yollarını içerir.
```

```
4. ShellBags (UsrClass — Bags)
Öncelik: Yüksek
Konum → HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\Bags
Gözlem Notu: UsrClass hive'ındaki klasör görünüm detaylarını tutar; NTUSER.DAT'takilerle birlikte analiz edilmelidir.
```

---

## UserAssist

```
1. UserAssist
Öncelik: Yüksek
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{CEBFF5CD-...}\Count
Gözlem Notu: GUI üzerinden çalıştırılan programların ROT13 kodlu adını, çalıştırma sayısını ve son çalışma zamanını tutar.
```

```
2. UserAssist (Win11)
Öncelik: Yüksek
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{F4E57C4B-...}\Count
Gözlem Notu: Windows 11'e özgü GUID altında aynı yapıdaki verileri tutar; Win10 GUID'i ile birlikte kontrol edilmelidir.
```

---

## Jump Lists (Registry)

```
1. ApplicationDestinations
Öncelik: Orta
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU
Gözlem Notu: Uygulamaların dosya açma diyaloğunda son eriştiği hedefleri tutar; Jump List dosyalarıyla çapraz doğrulanır.
```

---

## Harici Cihaz / USB

```
1. USB Depolama Aygıtları (USBSTOR)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR
Gözlem Notu: Bağlanan USB depolama cihazlarının marka, model, seri numarası ve ilk/son bağlantı zamanını tutar.
```

```
2. USB Geçmişi
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Enum\USB
Gözlem Notu: Tüm USB cihazlarının (depolama dahil) VID/PID ve cihaz tanımlayıcı bilgisini tutar.
```

```
3. MountedDevices
Öncelik: Yüksek
Konum → HKLM\SYSTEM\MountedDevices
Gözlem Notu: Sisteme bağlanmış tüm birimlerin sürücü harfi veya mount noktası ile disk imzasını eşleştirir.
```

```
4. MountPoints2
Öncelik: Yüksek
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2
Gözlem Notu: Kullanıcı bazında bağlanan birimlerin (USB, ağ paylaşımı) GUID'ini ve son erişim zamanını tutar.
```

```
5. DeviceClasses (Disk)
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\DeviceClasses
Gözlem Notu: Disk ve birim cihaz sınıfı GUID'leri altında bağlanan cihazların arayüz bilgisini tutar.
```

```
6. PortableDevices
Öncelik: Orta
Konum → HKLM\SOFTWARE\Microsoft\Windows Portable Devices\Devices
Gözlem Notu: MTP/PTP ile bağlanan taşınabilir cihazların (telefon, kamera) friendly name bilgisini tutar.
```

```
7. StorageDevicePolicies
Öncelik: Düşük
Konum → HKLM\SYSTEM\CurrentControlSet\Control\StorageDevicePolicies
Gözlem Notu: USB yazma koruması politikasının etkin olup olmadığını gösterir; veri sızdırma bağlamında kontrol edilir.
```

```
8. RemovableMedia (EMDMgmt)
Öncelik: Düşük
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\EMDMgmt
Gözlem Notu: ReadyBoost için değerlendirilen çıkarılabilir medyanın seri numarasını ve son bağlantı zamanını tutar.
```

---

## Program Execution / Dosya Açma

```
1. AppCompatCache (ShimCache)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache
Gözlem Notu: Çalıştırılan veya var olduğu bilinen EXE'lerin dosya yolunu ve son değişiklik zamanını tutar.
```

```
2. Amcache.hve
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Amcache
Gözlem Notu: SHA1 hash, dosya yolu, boyut, yayıncı ve ilk çalıştırma zamanını içerir; dosya varlığının kanıtıdır.
```

```
3. BAM (Background Activity Moderator)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\<SID>
Gözlem Notu: Kullanıcı bazında son çalıştırılan EXE'nin tam yolunu ve UTC zaman damgasını tutar (Win10 1709+).
```

```
4. DAM (Desktop Activity Moderator)
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\dam\State\UserSettings\<SID>
Gözlem Notu: BAM ile aynı yapıdadır; masaüstü oturumlarına özgü çalıştırma bilgisini ayrıca kaydeder.
```

---

## Network Paylaşım / Mapped Drive

```
1. Network Drives
Öncelik: Yüksek
Konum → HKCU\Network
Gözlem Notu: Kalıcı olarak eşlenmiş ağ sürücülerinin UNC yolunu, sürücü harfini ve kullanıcı adını tutar.
```

```
2. Net Share (LanmanServer)
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Shares
Gözlem Notu: Bu sistemde oluşturulmuş ağ paylaşımlarının adını, yolunu ve izin ayarlarını tutar.
```

---

## Office MRU

```
1. Office File MRU (Word)
Öncelik: Yüksek
Konum → HKCU\Software\Microsoft\Office\<ver>\Word\File MRU
Gözlem Notu: Word ile açılan son dosyaların tam yolunu ve erişim zamanını tutar; ağ yolları dahildir.
```

```
2. Office File MRU (Excel)
Öncelik: Yüksek
Konum → HKCU\Software\Microsoft\Office\<ver>\Excel\File MRU
Gözlem Notu: Excel ile açılan son dosyaların tam yolunu ve erişim zamanını tutar.
```

```
3. Office File MRU (PowerPoint)
Öncelik: Yüksek
Konum → HKCU\Software\Microsoft\Office\<ver>\PowerPoint\File MRU
Gözlem Notu: PowerPoint ile açılan son dosyaların tam yolunu ve erişim zamanını tutar.
```

```
4. Office Place MRU
Öncelik: Orta
Konum → HKCU\Software\Microsoft\Office\<ver>\Word\Place MRU
Gözlem Notu: Office uygulamalarında son kullanılan kaydetme konumlarını (yerel dizin, OneDrive, SharePoint) tutar.
```

---

## Diğer Registry

```
1. Search History (File Explorer)
Öncelik: Orta
Konum → HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery
Gözlem Notu: Explorer arama kutusuna girilen terimleri tutar; kullanıcının hangi dosyayı aradığını gösterir.
```

```
2. Internet Explorer / Edge Download MRU
Öncelik: Orta
Konum → HKCU\Software\Microsoft\Internet Explorer\Download Directory
Gözlem Notu: IE/Edge Legacy ile indirme yapılan son dizin yolunu tutar.
```

```
3. Recycle Bin Info (BitBucket)
Öncelik: Düşük
Konum → HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\BitBucket
Gözlem Notu: Her sürücü için Geri Dönüşüm Kutusu boyut sınırını ve yapılandırma ayarlarını tutar.
```
