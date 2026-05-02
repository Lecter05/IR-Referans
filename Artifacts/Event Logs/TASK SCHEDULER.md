
```
1. Task Scheduler Operational (Varsayılan: Kapalı — Win10; Win11 22H2+ kısmen açık)
Öncelik: Yüksek
Konum → Microsoft-Windows-TaskScheduler%4Operational.evtx
Gözlem Notu: Görev oluşturma (106), güncelleme (140), silme (141), yürütme (100, 200, 201), görev tamamlanma (102, 201) olayları persistence tespitinde (T1053.005) kritiktir; 106 içindeki TaskName ve Command alanları incelenir.
```

```
2. Task Scheduler — At/Schtasks Komut Satırı Korelasyonu
Öncelik: Yüksek
Konum → Security.evtx + TaskScheduler%4Operational.evtx
Gözlem Notu: Security 4698 (görev kaydı XML ile), TaskScheduler 106 (görev oluşturma) ve 4688 (schtasks.exe süreç oluşturma) birlikte korelasyon yapılır.
```
