
```
1. WMI-Activity Operational
Öncelik: Yüksek
Konum → Microsoft-Windows-WMI-Activity%4Operational.evtx
Gözlem Notu: WMI kalıcı olay aboneliği oluşturma (5857, 5858, 5859, 5860, 5861) persistence ve lateral movement'a (T1546.003) işaret eder; 5861 EventConsumer adını ve yürütülecek komutu içerir.
```

```
2. WMI — Uzak WMI Yürütme Korelasyonu
Öncelik: Yüksek
Konum → Security.evtx + WMI-Activity%4Operational.evtx
Gözlem Notu: Security 4624 (Type 3) + 4688 (wmiprvse.exe child process) + WMI-Activity 5857 korelasyonu uzak WMI yürütmeyi doğrular.
```
