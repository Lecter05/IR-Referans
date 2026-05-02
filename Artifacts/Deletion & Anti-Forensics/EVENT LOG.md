
```
1. Security Log Temizleme — Event ID 1102
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1070.001
Gözlem Notu: Event ID 1102'nin varlığı Security log'unun temizlendiğini doğrudan kanıtlar; temizleyen hesap bilgisi burada yer alır.
```

```
2. System Log Temizleme — Event ID 104
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\System.evtx
MITRE: T1070.001
Gözlem Notu: Event ID 104'ün varlığı herhangi bir event log kanalının temizlendiğini gösterir; hangi log silindiği ve kim tarafından yapıldığı burada yer alır.
```

```
3. Toplu Log Silme (wevtutil cl ile tüm kanallar)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\*.evtx
MITRE: T1070.001
Gözlem Notu: Çok sayıda .evtx dosyasının aynı zaman diliminde sıfırlanıp sıfırlanmadığına veya dosya boyutlarının anormal küçük olup olmadığına bakılır.
```

```
4. Event Log Dosyası Doğrudan Silme
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\ → ilgili .evtx dosyaları
MITRE: T1070.001
Gözlem Notu: .evtx dosyalarının dosya sistemi düzeyinde (Recycle Bin'e gitmeden) silinip silinmediğine $MFT ve $UsnJrnl'den bakılır.
```

```
5. PowerShell Operational Log Temizleme
Öncelik: Yüksek
Konum → Microsoft-Windows-PowerShell%4Operational.evtx → Event ID 4104 serisi
MITRE: T1070.001
Gözlem Notu: PowerShell script block loglarının toplu temizlenip temizlenmediğine veya log dosyası boyutunun anormal küçülüp küçülmediğine bakılır.
```

```
6. Sysmon Operational Log Temizleme
Öncelik: Yüksek
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
MITRE: T1070.001
Gözlem Notu: Sysmon log dosyasının temizlenip temizlenmediğine veya büyük zaman boşlukları olup olmadığına bakılır.
```

```
7. Event Log Servisi Durdurma
Öncelik: Yüksek
Konum → System.evtx → Event ID 7035, 7036 (EventLog servisi için) ve Security.evtx → Event ID 4719
MITRE: T1562.002
Gözlem Notu: EventLog servisinin durdurulma olayına ve audit policy değişikliği (4719) kaydına bakılır.
```

```
8. Sysmon Driver Unload
Öncelik: Yüksek
Konum → Sysmon Operational → EID 255 (driver error) veya servis silme; System.evtx → EID 1 (driver unload)
MITRE: T1562.001
Gözlem Notu: Sysmon driver'ının (SysmonDrv) unload veya kaldırılma olaylarına bakılır.
```

```
9. Windows Defender Log Temizleme
Öncelik: Orta
Konum → Microsoft-Windows-Windows Defender%4Operational.evtx → Event ID 1116, 1117, 5001, 5010
MITRE: T1562.001
Gözlem Notu: Defender tespit ve aksiyon loglarının silinip silinmediğine veya real-time protection kapatma olaylarına bakılır.
```

```
10. Firewall Log Temizleme
Öncelik: Orta
Konum → C:\Windows\System32\LogFiles\Firewall\pfirewall.log
MITRE: T1562.004
Gözlem Notu: Firewall log dosyasının silinip silinmediğine veya boşaltılıp boşaltılmadığına bakılır.
```

```
11. Task Scheduler Log Temizleme
Öncelik: Orta
Konum → Microsoft-Windows-TaskScheduler%4Operational.evtx
MITRE: T1070.001
Gözlem Notu: Zamanlanan görev loglarının temizlenip temizlenmediğine veya zaman boşluklarına bakılır.
```

```
12. WMI-Activity Log Temizleme
Öncelik: Orta
Konum → Microsoft-Windows-WMI-Activity%4Operational.evtx
MITRE: T1070.001
Gözlem Notu: WMI aktivite loglarının temizlenip temizlenmediğine veya dosya boyutunun sıfırlanıp sıfırlanmadığına bakılır.
```

```
13. ETW Trace Session Manipülasyonu
Öncelik: Orta
Erişim: Live System
Konum → Autologger ve trace session kayıtları; logman query ile kontrol
MITRE: T1562.006
Gözlem Notu: Kritik ETW oturumlarının (Microsoft-Windows-Threat-Intelligence vb.) durdurulup durdurulmadığına bakılır.
```
