## SCHEDULED TASKS ARTIFACT'LARI

```
1. Zamanlanmış Görevler (schtasks / Task Scheduler)
Öncelik: Yüksek
Konum → C:\Windows\System32\Tasks\<TaskName>.xml
Gözlem Notu: Tüm görevlerdeki Action etiketinde çalıştırılan komut ve tetikleyici koşula bakılır.
```

```
2. Gizli/Silinmiş Görev Kalıntıları (SD Değeri)
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\<task> → SD
Gözlem Notu: SD değeri silinerek GUI'den gizlenen görevlerin TaskCache Tree kaydına bakılır (Win10/11).
```

```
3. TaskCache — Actions / Triggers / DynamicInfo
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks\{GUID} → Actions, Triggers, DynamicInfo
Gözlem Notu: Actions değerinden çalıştırılan binary, DynamicInfo'dan son çalışma zamanı elde edilir.
```

```
4. AT Komutu ile Oluşturulan Görevler (Eski)
Öncelik: Düşük
Konum → C:\Windows\System32\Tasks\At*
Gözlem Notu: Eski at.exe komutuyla oluşturulan görev kalıntılarına bakılır.
```
