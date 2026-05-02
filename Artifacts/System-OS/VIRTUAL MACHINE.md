
```
1. VM Göstergesi (Registry)
Öncelik: Yüksek
Konum → HKLM\HARDWARE\DESCRIPTION\System\BIOS → SystemManufacturer / SystemProductName
Gözlem Notu: "VMware", "QEMU", "VirtualBox", "Microsoft Corporation" (Hyper-V) gibi değerler sanal ortam göstergesidir.
```

```
2. VM Sürücü ve Servisler
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\ → VMTools, VBoxGuest, vmci vb.
Gözlem Notu: VM araçlarına ait servis kayıtları (VMware Tools, VirtualBox Guest Additions) sanal ortam varlığını doğrular.
```

```
3. VM MAC Adresi Kalıpları
Öncelik: Orta
Erişim: Live System
Konum → Ağ adaptörü MAC adresi (ipconfig /all veya registry)
Gözlem Notu: 00:0C:29, 00:50:56 (VMware), 08:00:27 (VirtualBox), 00:15:5D (Hyper-V) gibi OUI değerleri VM göstergesidir.
```

```
4. VM Cihaz Adları
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Enum\PCI\ ve \IDE\
Gözlem Notu: PCI/IDE cihaz tanımlayıcılarında VMware, VBox, Red Hat gibi sanal donanım isimleri yer alır.
```

```
5. Hyper-V Entegrasyon Servisleri
Öncelik: Orta
Konum → HKLM\SOFTWARE\Microsoft\Virtual Machine\Guest\Parameters
Gözlem Notu: Hyper-V misafir makine parametreleri ve host bilgisi bu anahtarda saklanır.
```

```
6. VM Tools Dosya Yolları
Öncelik: Orta
Konum → C:\Program Files\VMware\VMware Tools\, C:\Program Files\Oracle\VirtualBox Guest Additions\
Gözlem Notu: VM araçlarının dosya sistemi üzerindeki varlığı sanal ortam kullanımını doğrular.
```

```
7. WSL (Windows Subsystem for Linux) İzleri
Öncelik: Orta
Konum → C:\Users\<Kullanıcı>\AppData\Local\Packages\*CanonicalGroup*\ ve HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Lxss\
Gözlem Notu: WSL dağıtım bilgileri, konfigürasyonu ve Linux dosya sistemi konumu; saldırganlar tespitten kaçınmak için WSL kullanabilir.
```

```
8. ACPI Tabloları
Öncelik: Düşük
Konum → HKLM\HARDWARE\ACPI\DSDT\ ve FADT\
Gözlem Notu: ACPI tablo isimleri (VBOX, VMWARE, PRLS, BOCHS) sanallaştırma platformunu açığa çıkarır.
```

```
9. SMBIOS/DMI Verileri
Öncelik: Düşük
Erişim: Live System
Konum → wmic baseboard / wmic bios çıktısı veya registry BIOS anahtarı
Gözlem Notu: Anakart üretici, BIOS sürüm ve seri numarası bilgileri sanal makine tespitinde yardımcı olur.
```

```
10. Windows Sandbox İzleri
Öncelik: Düşük
Konum → C:\ProgramData\Microsoft\Windows\Containers\
Gözlem Notu: Windows Sandbox konteyner yapılandırma ve çalışma dosyaları; sandbox kullanım izlerini gösterir (Win10 Pro+ / Win11).
```

