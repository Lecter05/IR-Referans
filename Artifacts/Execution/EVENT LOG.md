## EVENT LOG ARTIFACT'leri

```
1. Security.evtx — Event ID 4688 (Process Creation)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Oluşturulan sürecin adı, PID, üst süreç PID'i ve kullanıcı bilgisini tutar; komut satırı kaydı için ek GPO gerekir (Varsayılan: Kapalı — komut satırı kısmı).
```

```
2. Sysmon Event ID 1 (Process Create) (Varsayılan: Kapalı — Sysmon kurulu değilse)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: Komut satırı, hash (MD5/SHA256/IMPHASH), üst süreç ilişkisi, oturum ve kullanıcı bilgisini tutar.
```

```
3. PowerShell Script Block Logging — Event ID 4104
Öncelik: Yüksek
Konum → Microsoft-Windows-PowerShell%4Operational.evtx
Gözlem Notu: Çalıştırılan PowerShell script bloğunun tam metnini kaydeder; obfuscation sonrası de-obfuscated halini de içerebilir (Win10+, kısmen varsayılan açık). (T1059.001)
```

```
4. PowerShell Module Logging — Event ID 4103 (Varsayılan: Kapalı)
Öncelik: Yüksek
Konum → Microsoft-Windows-PowerShell%4Operational.evtx
Gözlem Notu: Çağrılan PowerShell modül ve cmdlet'lerin parametre detaylarını kaydeder. (T1059.001)
```

```
5. System.evtx — Event ID 7045 (Yeni Servis Kurulumu)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\System.evtx
Gözlem Notu: Yeni kurulan servisin adı, ImagePath'i, başlatma tipi ve hesap bilgisini kaydeder. (T1569.002)
```

```
6. Security.evtx — Event ID 4697 (Servis Kurulumu — Audit) (Varsayılan: Kapalı)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: 7045'e ek olarak kurulumu yapan kullanıcının SID'ini de içerir; audit policy ile etkinleştirilir. (T1569.002)
```

```
7. Task Scheduler Event Log — Event ID 106, 140, 200, 201 (Varsayılan: Kapalı — Win10'da)
Öncelik: Yüksek
Konum → Microsoft-Windows-TaskScheduler%4Operational.evtx
Gözlem Notu: Zamanlanmış görevin kaydedilme, güncelleme, başlatma ve tamamlanma olaylarını kaydeder. (T1053.005)
```

```
8. WMI-Activity Operational Log — Event ID 5857, 5858, 5860, 5861
Öncelik: Yüksek
Konum → Microsoft-Windows-WMI-Activity%4Operational.evtx
Gözlem Notu: WMI provider yüklemesi, hata ve kalıcı event subscription oluşturma/tetiklenme olaylarını kaydeder. (T1047)
```

```
9. AppLocker Event Logs (Varsayılan: Kapalı — AppLocker etkin değilse)
Öncelik: Yüksek
Konum → Microsoft-Windows-AppLocker%4EXE and DLL.evtx (ve diğer alt kanallar)
Gözlem Notu: İzin verilen veya engellenen EXE/DLL/script çalıştırmalarını dosya yolu, hash ve yayıncı ile kaydeder. (T1059)
```

```
10. PowerShell Classic Log — Event ID 400, 403, 600
Öncelik: Orta
Konum → Windows PowerShell.evtx
Gözlem Notu: PowerShell engine başlatma/durdurma olaylarını ve HostApplication alanında çalıştırma komutunu tutar.
```

```
11. Windows Defender Operational
Öncelik: Orta
Konum → Microsoft-Windows-Windows Defender%4Operational.evtx
Gözlem Notu: Event ID 1116/1117 ile tespit edilen zararlı dosyanın yolu, hash'i ve alınan aksiyonu kaydeder; dolaylı execution kanıtı.
```

```
12. System.evtx — Event ID 7034, 7035, 7036, 7040
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\System.evtx
Gözlem Notu: Servislerin başlatma, durdurma, çökme ve start tipinin değiştirilme olaylarını tutar.
```

```
13. Security.evtx — Event ID 4648 (Explicit Logon)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Farklı kimlik bilgileriyle (runas vb.) çalıştırılan sürecin hedef sunucu ve kullanıcı bilgisini tutar.
```

```
14. BITS Client Operational — Event ID 3, 59, 60
Öncelik: Orta
Konum → Microsoft-Windows-Bits-Client%4Operational.evtx
Gözlem Notu: BITS iş oluşturma, tamamlama ve notify komut çalıştırma olaylarını kaydeder.
```

```
15. WDAC / Code Integrity Log — Event ID 3076, 3077 (Varsayılan: Kapalı — WDAC politikası yoksa)
Öncelik: Orta
Konum → Microsoft-Windows-CodeIntegrity%4Operational.evtx
Gözlem Notu: Windows Defender Application Control tarafından engellenen veya denetlenen binary/script'lerin kaydını tutar.
```

```
16. Microsoft Office Alerts Log
Öncelik: Orta
Konum → Microsoft Office Alerts.evtx (OAlerts.evtx)
Gözlem Notu: Makro çalıştırma veya güvenlik uyarı olaylarını kaydeder; Office tabanlı execution kanıtı sağlar. (T1204.002)
```

```
17. Application.evtx — Event ID 1000, 1001, 1002
Öncelik: Düşük
Konum → C:\Windows\System32\winevt\Logs\Application.evtx
Gözlem Notu: Uygulama çökmesi veya hatasında sürecin adını, modülünü ve hata zamanını tutar.
```

```
18. Windows Script Host (WSH) Logs
Öncelik: Düşük
Konum → Application.evtx (WSH hataları)
Gözlem Notu: wscript.exe / cscript.exe ile çalıştırılan VBS/JS script'lerinin hata kayıtlarını tutar. (T1059.005 / T1059.007)
```

```
19. PrintService Operational — Event ID 316
Öncelik: Düşük
Konum → Microsoft-Windows-PrintService%4Operational.evtx
Gözlem Notu: Spool dizinine yazılan ve çalıştırılan DLL'leri tespit etmek için kullanılır (PrintNightmare gibi exploitation senaryoları).
```

```
20. DriverFrameworks-UserMode — Event ID 2004
Öncelik: Düşük
Konum → Microsoft-Windows-DriverFrameworks-UserMode%4Operational.evtx
Gözlem Notu: USB bağlantı olaylarıyla ilişkilendirerek harici medyadan çalıştırma zamanlamasını doğrulamada kullanılır.
```

```
21. DNS Client Event Log (Varsayılan: Kapalı — Analytic kanal)
Öncelik: Düşük
Konum → Microsoft-Windows-DNS-Client%4Operational.evtx
Gözlem Notu: Çalıştırılan programın yaptığı DNS sorgularını süreç bazında kaydeder; C2 iletişimini süreçle eşleştirir.
```

----

> Varsayılan: Kapalı ibaresi taşıyan artifact'lar, olay öncesinde etkinleştirilmemişse mevcut olmayabilir.
>
> "Erişim: Live System" yalnızca canlı sistem veya RAM dump gerektiren artifact'larda belirtilmiştir.  
>
> Öncelik değerleri, execution kanıtı sağlama güvenilirliği ifade eder.
