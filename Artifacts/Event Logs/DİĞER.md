
```
1. Forwarded Events
Öncelik: Yüksek
Konum → ForwardedEvents.evtx
Gözlem Notu: Windows Event Forwarding (WEF) ile merkezi toplanan olaylar; birden fazla endpoint'in loglarını tek kanalda içerebilir; yapılandırmaya bağlı olarak kapsamı değişir.
```

```
2. LSA Operational (Varsayılan: Kapalı — Win10 1809+)
Öncelik: Yüksek
Konum → Microsoft-Windows-LSA%4Operational.evtx
Gözlem Notu: LSA eklentisi/sürücü yükleme denetimi; LSA Protection (RunAsPPL) atlatma girişimleri, credential guard olayları izlenir.
```

```
3. Microsoft Defender for Endpoint (MDE kuruluysa; Varsayılan: Kapalı standalone sistemlerde)
Öncelik: Yüksek
Konum → Microsoft-Windows-SENSE%4Operational.evtx
Gözlem Notu: MDE sensör durumu, bağlantı sorunları, algılama olayları; EDR ajanının devre dışı bırakılma girişimlerini doğrulamada kullanılır.
```

```
4. PrintService — Admin (PrintNightmare)
Öncelik: Orta
Konum → Microsoft-Windows-PrintService%4Admin.evtx
Gözlem Notu: Yazıcı sürücüsü yükleme (316, 808, 811, 842) olayları PrintNightmare (CVE-2021-34527) exploit girişimlerini tespit etmek için kontrol edilir.
```

```
5. CAPI2 (CryptoAPI) (Varsayılan: Kapalı)
Öncelik: Orta
Konum → Microsoft-Windows-CAPI2%4Operational.evtx
Gözlem Notu: Sertifika doğrulama hataları (11, 30, 40, 70, 90), CRL/OCSP kontrolleri; sahte sertifika veya TLS interception tespitinde faydalıdır.
```

```
6. Authentication / CredentialGuard
Öncelik: Orta
Konum → Microsoft-Windows-Authentication%4AuthenticationPolicyFailures-DomainController.evtx
Gözlem Notu: Credential Guard engellemeleri, kimlik doğrulama ilkesi hataları; yalnızca domain controller'larda anlamlıdır.
```

```
7. Security-Audit-Configuration-Client
Öncelik: Orta
Konum → Microsoft-Windows-Security-Audit-Configuration-Client%4Operational.evtx
Gözlem Notu: Denetim ilkesi değişikliklerini detaylı gösterir; T1562.002 (audit policy tampering) tespitinde Security 4719 ile birlikte kullanılır.
```

```
8. Windows Installer (MsiInstaller)
Öncelik: Orta
Konum → Application.evtx (Source: MsiInstaller)
Gözlem Notu: MSI paketi yükle (1033), kaldır (1034), başarılı yükleme (11707), başarısız yükleme (11708) olayları yazılım yükleme zaman çizelgesi oluşturur.
```

```
9. VHD / VHDX Mount
Öncelik: Orta
Konum → Microsoft-Windows-VHDMP%4Operational.evtx
Gözlem Notu: VHD/VHDX/ISO dosyası bağlama (1, 2) olayları; ISO ve VHD tabanlı payload dağıtım tekniklerinde (Win11 MOTW bypass yöntemlerinde) kontrol edilir.
```

```
10. Microsoft Office Alerts
Öncelik: Orta
Konum → OAlerts.evtx (Microsoft Office kuruluysa)
Gözlem Notu: Office uygulaması uyarıları ve hata mesajları; makro etkinleştirme, korumalı görünüm atlatma gibi başlangıç erişimi vektörlerini destekler.
```

```
11. DeviceGuard Operational
Öncelik: Orta
Konum → Microsoft-Windows-DeviceGuard%4Operational.evtx (Win10 Enterprise / Win11)
Gözlem Notu: HVCI (Hypervisor-Protected Code Integrity) durumu, VBS politika yükleme; CI politika değişikliği ve WDAC entegrasyonu kontrol edilir.
```

```
12. Application Experience / Program Compatibility
Öncelik: Düşük
Konum → Microsoft-Windows-Application-Experience%4Program-Compatibility-Assistant.evtx
Gözlem Notu: Program uyumluluk asistanı olayları (17) yürütülen uygulamalar hakkında ek kanıt sağlar; ProgramInventory (800) silinmiş uygulamaların varlığını doğrulayabilir.
```

```
13. PrintService Operational
Öncelik: Düşük
Konum → Microsoft-Windows-PrintService%4Operational.evtx
Gözlem Notu: Yazdırma işi gönderme (307) kullanıcı, belge adı ve yazıcı bilgisini kaydeder; veri sızıntısı araştırmalarında faydalıdır.
```

```
14. Kernel-PnP
Öncelik: Düşük
Konum → Microsoft-Windows-Kernel-PnP%4Device Configuration.evtx
Gözlem Notu: USB cihaz bağlanma (400, 410) ve çıkarma (411) olayları cihaz seri numarası ile çıkarılabilir medya kullanımını doğrular.
```

```
15. DriverFrameworks-UserMode
Öncelik: Düşük
Konum → Microsoft-Windows-DriverFrameworks-UserMode%4Operational.evtx
Gözlem Notu: USB cihaz takma (2003, 2010, 2100, 2101, 2105) olayları; Kernel-PnP ile birlikte USB timeline oluşturmada destekleyicidir.
```

```
16. Partition/Diagnostic (Win10 1903+)
Öncelik: Düşük
Konum → Microsoft-Windows-Partition%4Diagnostic.evtx
Gözlem Notu: Disk bağlama olayları VHD mount, USB disk gibi blok cihaz kullanımını kaydeder; seri numarası ve üretici bilgisi içerir.
```

```
17. COM+ / DCOM
Öncelik: Düşük
Konum → System.evtx (Source: DCOM, Event ID 10016)
Gözlem Notu: DCOM izin hataları (10016) genellikle gürültüdür ancak lateral movement sırasında uzaktan DCOM aktivasyonu denemelerini yakalayabilir.
```

```
18. Shell-Core / ShellStartupTrigger (Varsayılan: Kapalı)
Öncelik: Düşük
Konum → Microsoft-Windows-Shell-Core%4Operational.evtx
Gözlem Notu: Shell başlatma sırasında yüklenen uygulamaların listesi; startup persistence doğrulamasında destek sağlar (T1547).
```

```
19. Kernel-Boot / Kernel-General
Öncelik: Düşük
Konum → Microsoft-Windows-Kernel-General%4Operational.evtx
Gözlem Notu: Sistem başlatma/kapatma zaman damgaları (12, 13), saat değişikliği (1); boot timeline oluşturmada ve anti-forensics tespitinde kullanılır.
```

```
20. User Profile Service
Öncelik: Düşük
Konum → Microsoft-Windows-User Profile Service%4Operational.evtx
Gözlem Notu: Profil yükleme (1, 2) ve kaldırma (3, 4) olayları kullanıcı oturum açma/kapama zaman çizelgesini destekler.
```

```
21. Group Policy Operational
Öncelik: Düşük
Konum → Microsoft-Windows-GroupPolicy%4Operational.evtx
Gözlem Notu: GP işleme (4000-4007, 5000-5340 serisi), GPO uygulanma süresi ve hataları; domain ortamında politika değişikliği doğrulamasında kullanılır.
```

```
22. Diagnosis-Scripted
Öncelik: Düşük
Konum → Microsoft-Windows-Diagnosis-Scripted%4Operational.evtx
Gözlem Notu: Follina (CVE-2022-30190) exploit girişimleri sırasında msdt.exe aktivitesi bu kanalda iz bırakır.
```

```
23. EFS (Encrypting File System) (Varsayılan: Kapalı — denetim ilkesi gerektirir)
Öncelik: Düşük
Konum → Security.evtx (4962-4964, 5765-5770)
Gözlem Notu: EFS ile dosya şifreleme/çözme olayları; dosya bazlı şifreleme kullanan ransomware varyantlarında kontrol edilir.
```

```
24. Hyper-V Worker (Hyper-V etkinse)
Öncelik: Düşük
Konum → Microsoft-Windows-Hyper-V-Worker%4Operational.evtx
Gözlem Notu: VM başlatma/durdurma olayları; saldırganın analiz ortamı oluşturma veya sanal makine kullanarak savunmadan kaçma girişimlerinde kontrol edilir.
```

```
25. PowerShell DSC (Varsayılan: Kapalı)
Öncelik: Düşük
Konum → Microsoft-Windows-DSC%4Operational.evtx
Gözlem Notu: DSC yapılandırma uygulama olayları; saldırgan DSC üzerinden persistence kuruyorsa bu kanalda iz bırakır.
```

```
26. Setup Log
Öncelik: Düşük
Konum → Setup.evtx
Gözlem Notu: Windows özellik güncellemeleri ve bileşen kurulumları; yükseltme sırasında oluşan değişiklikleri ve yama durumunu doğrular.
```
