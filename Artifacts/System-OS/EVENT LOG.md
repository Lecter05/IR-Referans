
```
1. System.evtx
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\System.evtx
Gözlem Notu: Servis başlatma/durdurma (7035, 7036, 7045), sürücü yükleme, sistem hataları ve başlangıç/kapanma olayları burada kayıtlıdır.
```

```
2. Security.evtx
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Oturum açma/kapama (4624/4634), hesap yönetimi, denetim politikası değişiklikleri ve ayrıcalık kullanımı olaylarını içerir.
```

```
3. Sysmon Operational
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: Kuruluysa süreç oluşturma, ağ bağlantıları, dosya hash'leri ve registry değişiklikleri gibi ayrıntılı denetim olaylarını içerir.
```

```
4. TaskScheduler Operational
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-TaskScheduler%4Operational.evtx
Gözlem Notu: Zamanlanmış görev oluşturma (106), güncelleme (140), silme (141) ve çalıştırma (200/201) olaylarını kaydeder.
```

```
5. PowerShell Operational
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-PowerShell%4Operational.evtx
Gözlem Notu: PowerShell script bloğu günlüğü (4104), modül yükleme ve pipeline çalıştırma olaylarını içerir.
```

```
6. Kernel-PnP Configuration
Öncelik: Yüksek
Konum → Microsoft-Windows-Kernel-PnP%4Configuration.evtx
Gözlem Notu: Plug and Play cihaz ekleme ve kaldırma olaylarını (400/410) zaman damgalı olarak kaydeder.
```

```
7. CodeIntegrity Operational
Öncelik: Yüksek
Konum → Microsoft-Windows-CodeIntegrity%4Operational.evtx
Gözlem Notu: İmzasız veya geçersiz imzalı sürücü/modül yükleme denemeleri (3001, 3002, 3033) burada raporlanır.
```

```
8. Windows Defender Operational
Öncelik: Yüksek
Konum → Microsoft-Windows-Windows Defender%4Operational.evtx
Gözlem Notu: Tehdit tespitleri (1116/1117), tarama sonuçları, tanım güncellemeleri ve gerçek zamanlı koruma durumu değişiklikleri kaydedilir.
```

```
9. WMI-Activity Operational
Öncelik: Yüksek
Konum → Microsoft-Windows-WMI-Activity%4Operational.evtx
Gözlem Notu: WMI sorguları, kalıcı abonelik oluşturma ve provider yükleme olaylarını kaydeder; WMI persistence tespiti için kritiktir.
```

```
10. Event Log Temizleme İzi — Event ID 1102 / 104
Öncelik: Yüksek
Konum → Security.evtx → Event ID 1102 / System.evtx → Event ID 104
Gözlem Notu: Olay günlüğünün temizlendiğini ve temizleyen hesabı gösterir; anti-forensics göstergesidir.
```

```
11. Değiştirilen Denetim Politikası — Event ID 4719
Öncelik: Yüksek
Konum → Security.evtx → Event ID 4719
Gözlem Notu: Denetim politikasında yapılan değişiklikler log toplama engellemesi göstergesi olabilir.
```

```
12. System BugCheck — Event ID 1001
Öncelik: Yüksek
Konum → System.evtx → Event ID 1001
Gözlem Notu: BSOD hata kodu, parametreleri ve döküm dosyası yolunu olay günlüğünde raporlar.
```

```
13. Application.evtx
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Application.evtx
Gözlem Notu: Uygulama hataları, MSI kurulumları (11707/11724) ve uygulama düzeyinde uyarı olaylarını kaydeder.
```

```
14. Windows PowerShell.evtx
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Windows PowerShell.evtx
Gözlem Notu: PowerShell engine başlatma (400/403) ve provider yükleme olaylarını kaydeder.
```

```
15. DriverFrameworks-UserMode Operational
Öncelik: Orta
Konum → Microsoft-Windows-DriverFrameworks-UserMode%4Operational.evtx
Gözlem Notu: USB ve kullanıcı modu sürücü yükleme/kaldırma olaylarını ve cihaz ekleme zamanlarını içerir.
```

```
16. Kernel-Boot Operational
Öncelik: Orta
Konum → Microsoft-Windows-Kernel-Boot%4Operational.evtx
Gözlem Notu: Önyükleme sürecinin detaylı aşamalarını ve boot type bilgisini içerir.
```

```
17. Windows Firewall Operational
Öncelik: Orta
Konum → Microsoft-Windows-Windows Firewall With Advanced Security%4Firewall.evtx
Gözlem Notu: Güvenlik duvarı kuralı ekleme (2004), değiştirme (2005), silme (2006) ve profil değişikliği olaylarını içerir.
```

```
18. WindowsUpdateClient Operational
Öncelik: Orta
Konum → Microsoft-Windows-WindowsUpdateClient%4Operational.evtx
Gözlem Notu: Güncelleme indirme, kurulum ve hata olaylarını kaydeder; güncellemenin engellenip engellenmediği kontrol edilebilir.
```

```
19. GroupPolicy Operational
Öncelik: Orta
Konum → Microsoft-Windows-GroupPolicy%4Operational.evtx
Gözlem Notu: Grup İlkesi uygulama sonuçları, hataları ve işleme sürelerini detaylı olarak içerir.
```

```
20. NTLM Operational
Öncelik: Orta
Konum → Microsoft-Windows-NTLM%4Operational.evtx
Gözlem Notu: NTLM kimlik doğrulama olaylarını ve engellenen NTLM isteklerini kaydeder.
```

```
21. BitLocker Management
Öncelik: Orta
Konum → Microsoft-Windows-BitLocker%4BitLocker Management.evtx
Gözlem Notu: BitLocker şifreleme durumu değişiklikleri, kilit açma denemeleri ve kurtarma anahtarı kullanım olaylarını içerir.
```

```
22. Audit-CVE
Öncelik: Orta
Konum → Microsoft-Windows-Audit-CVE.evtx
Gözlem Notu: Bilinen CVE açıklarını hedefleyen istismar girişimlerinin tespitini raporlar (Win10 1903+).
```

```
23. DeviceGuard Operational
Öncelik: Orta
Konum → Microsoft-Windows-DeviceGuard%4Operational.evtx
Gözlem Notu: VBS (Virtualization Based Security) ve Credential Guard durumu olaylarını kaydeder.
```

```
24. AppLocker Logları
Öncelik: Orta
Konum → Microsoft-Windows-AppLocker%4*.evtx → EXE and DLL, MSI and Script, Packaged app logları
Gözlem Notu: AppLocker tarafından izin verilen veya engellenen uygulama çalıştırma olaylarını içerir.
```

```
25. Hyper-V Logları
Öncelik: Orta
Konum → Microsoft-Windows-Hyper-V*.evtx → Çeşitli Hyper-V alt logları
Gözlem Notu: Hyper-V etkinleştirilmişse VM oluşturma, başlatma ve yapılandırma değişikliklerini kaydeder.
```

```
26. Kernel-ShimEngine Operational
Öncelik: Düşük
Konum → Microsoft-Windows-Kernel-ShimEngine%4Operational.evtx
Gözlem Notu: Uygulama uyumluluk shim'lerinin uygulanma olaylarını kaydeder; beklenmeyen shim kullanımı tespiti için incelenir.
```

```
27. Setup.evtx
Öncelik: Düşük
Konum → C:\Windows\System32\winevt\Logs\Setup.evtx
Gözlem Notu: Windows kurulum ve servisleme olaylarını (KB kurulumları dahil) kaydeder.
```

```
28. WDAG (Application Guard) Logları
Öncelik: Düşük
Konum → Microsoft-Windows-WDAG logları
Gözlem Notu: Application Guard konteyner oluşturma ve izolasyon olaylarını içerir (Win10 Enterprise / Win11).
```
