## EVENT LOG ARTIFACT'LARI

```
1. Security.evtx — Event ID 4698 (Scheduled Task Oluşturma)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Yeni oluşturulan zamanlanmış görevin XML içeriğindeki komut satırına bakılır.
```

```
2. TaskScheduler Operational — Event ID 106, 140, 200, 201
Öncelik: Yüksek
Konum → Microsoft-Windows-TaskScheduler%4Operational.evtx
Gözlem Notu: Task oluşturma (106) ve çalıştırma (200) olaylarında görev adı ve komuta bakılır.
```

```
3. System.evtx — Event ID 7045 (Servis Kurulumu)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\System.evtx
Gözlem Notu: Yeni kurulan servisin adı, binary yolu ve hesap türüne (LocalSystem) bakılır.
```

```
4. PowerShell Script Block Logging — Event ID 4104
Öncelik: Yüksek
Konum → Microsoft-Windows-PowerShell%4Operational.evtx
Gözlem Notu: ScriptBlock loglarında persistence oluşturan komutlara (New-ScheduledTask, Set-ItemProperty vb.) bakılır.
```

```
5. WMI-Activity Operational — Event ID 5857, 5858, 5859, 5860, 5861
Öncelik: Yüksek
Konum → Microsoft-Windows-WMI-Activity%4Operational.evtx
Gözlem Notu: Event ID 5861'de kalıcı WMI filter/consumer binding olaylarına bakılır.
```

```
6. Sysmon — Process Create (Event ID 1)
Öncelik: Yüksek
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: ParentImage ve CommandLine alanlarında persistence binary'sinin çalışma anına bakılır (Sysmon kuruluysa).
```

```
7. Sysmon — Registry Value Set (Event ID 12, 13, 14)
Öncelik: Yüksek
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: Run key ve diğer autostart kayıtlarına yapılan değişikliklerin detayına bakılır (Sysmon kuruluysa).
```

```
8. Sysmon — WMI Event (Event ID 19, 20, 21)
Öncelik: Yüksek
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: WMI EventFilter, EventConsumer ve FilterToConsumerBinding oluşturma olaylarına bakılır.
```

```
9. System.evtx — Event ID 7040, 7034 (Servis Değişikliği)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\System.evtx
Gözlem Notu: Servis başlatma türü değişikliği veya tekrarlanan crash'lere bakılır.
```

```
10. Security.evtx — Event ID 4657 (Registry Değişikliği)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: SACL etkinse Run key gibi kritik kayıt defteri değerlerindeki değişikliklere bakılır.
```

```
11. BITS-Client Operational — Event ID 59, 60
Öncelik: Orta
Konum → Microsoft-Windows-Bits-Client%4Operational.evtx
Gözlem Notu: BITS transfer başlatma olaylarında hedef URL ve indirilen dosya yoluna bakılır.
```

```
12. AppLocker / WDAC Log — Event ID 8003, 8004, 8006, 8007
Öncelik: Düşük
Konum → Microsoft-Windows-AppLocker%4*.evtx
Gözlem Notu: Engellenmiş veya izin verilmiş çalıştırma olaylarında persistence binary path'ine bakılır.
```
