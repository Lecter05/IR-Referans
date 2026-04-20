## SERVICES ARTIFACT'LARI

```
1. Windows Servis Kaydı (CurrentControlSet)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\<ServiceName> → ImagePath, Start, Type, ObjectName
Gözlem Notu: ImagePath'te tırnak içermeyen boşluklu yollar veya olağandışı binary konumlarına bakılır.
```

```
2. Servis DLL (svchost.exe servisleri)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\<svc>\Parameters → ServiceDll
Gözlem Notu: svchost.exe ile çalışan servislerin ServiceDll değerindeki DLL yoluna bakılır.
```

```
3. Servis Failure Recovery (FailureActions / FailureCommand)
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\<ServiceName> → FailureActions, FailureCommand
Gözlem Notu: Servis fail ettiğinde çalıştırılan FailureCommand'da zararlı komut olup olmadığına bakılır.
```

```
4. Driver Servisleri (Kernel / File System Drivers)
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\<DriverName> → Type = 1 veya 2, Start = 0/1/2
Gözlem Notu: Type değeri 1 (kernel) veya 2 (fs) olan servislerde imzasız driver'lara bakılır.
```

```
5. Unquoted Service Path Hijacking
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\* → ImagePath
Gözlem Notu: Boşluk içeren ve tırnak ile sarılmamış ImagePath değerlerinde yol sömürüsüne bakılır.
```

```
6. Service Control Manager ACL Abuse
Öncelik: Düşük
Erişim: Live System
Konum → HKLM\SYSTEM\CurrentControlSet\Services\<svc> → Servis DACL (sc sdshow ile görüntülenir)
Gözlem Notu: Düşük yetkili kullanıcıların servis yapılandırmasını değiştirip değiştiremediğine bakılır.
```
