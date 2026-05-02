
```
1. wevtutil.exe Çalışma İzleri
Öncelik: Yüksek
Konum → Prefetch → wevtutil.pf; Amcache; $UsnJrnl; BAM/DAM
MITRE: T1070.001
Gözlem Notu: wevtutil.exe'nin Prefetch kaydının varlığına ve çalıştırılma zamanına bakılır.
```

```
2. PowerShell Clear-EventLog / wevtutil Komutları
Öncelik: Yüksek
Konum → PowerShell Operational Log → EID 4104; ConsoleHost_history.txt
MITRE: T1070.001
Gözlem Notu: Clear-EventLog veya wevtutil cl komutlarının PowerShell script block loglarında kaydına bakılır.
```

```
3. IIS / Web Sunucu Log Temizleme
Öncelik: Orta
Konum → C:\inetpub\logs\LogFiles\W3SVC*\*.log
MITRE: T1070.001
Gözlem Notu: IIS log dosyalarının silinip silinmediğine veya belirli satırların düzenlenip düzenlenmediğine bakılır.
```

```
4. RDP Bağlantı Log Temizleme
Öncelik: Orta
Konum → Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx ve Microsoft-Windows-TerminalServices-RDPClient%4Operational.evtx
MITRE: T1070.001
Gözlem Notu: RDP oturum loglarının temizlenip temizlenmediğine veya zaman boşluklarına bakılır.
```

```
5. Scheduled Task Log Aracılığıyla Otomatik Temizleme
Öncelik: Orta
Konum → C:\Windows\System32\Tasks\ içinde log temizleme görevi; TaskScheduler Operational → EID 106
MITRE: T1070.001
Gözlem Notu: Periyodik log temizleme için oluşturulmuş zamanlanmış görevlere bakılır.
```

```
6. Phantom Log Deletion (Thread Killing)
Öncelik: Düşük
Erişim: Live System
Konum → Sysmon → EID 1, 10 (lsass.exe erişimi); ETW session kayıtları
MITRE: T1070.001
Gözlem Notu: Event Log servisinin thread'lerinin durdurularak log yazımının engellenip engellenmediğine bakılır.
```
