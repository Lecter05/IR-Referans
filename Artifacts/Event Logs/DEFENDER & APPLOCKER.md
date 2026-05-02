
```
1. Windows Defender Operational
Öncelik: Yüksek
Konum → Microsoft-Windows-Windows Defender%4Operational.evtx
Gözlem Notu: Tehdit algılama (1116, 1117), karantina (1009), gerçek zamanlı koruma devre dışı (5001, 5010, 5012), tanım güncelleme (2000, 2001), tarama başlatma/bitirme (1001, 1002), dışlama ekleme (5007) olayları incelenir; 5001 savunma devre dışı bırakılmasına (T1562.001) işaret eder.
```

```
2. Windows Defender — Exclusion Events
Öncelik: Yüksek
Konum → Microsoft-Windows-Windows Defender%4Operational.evtx
Gözlem Notu: Event ID 5007 (ayar değişikliği) içinde "Exclusions" string'i aranır; saldırganlar malware dizinini dışlama listesine ekleyerek taramadan kaçar.
```

```
3. Exploit Guard — ASR Rules
Öncelik: Yüksek
Konum → Microsoft-Windows-Windows Defender%4Operational.evtx
Gözlem Notu: Attack Surface Reduction kuralı engelleme (1121), denetim (1122) olayları; Office macro, script injection ve credential stealing girişimlerini tespit eder.
```

```
4. AppLocker — EXE and DLL
Öncelik: Yüksek
Konum → Microsoft-Windows-AppLocker%4EXE and DLL.evtx
Gözlem Notu: İzin verilen yürütme (8002), engellenen yürütme (8003), denetim modu uyarısı (8004); 8003/8004 olayları yetkisiz uygulama yürütme girişimlerini (T1059) gösterir.
```

```
5. AppLocker — MSI and Script
Öncelik: Yüksek
Konum → Microsoft-Windows-AppLocker%4MSI and Script.evtx
Gözlem Notu: Script yürütme izin/engelleme (8005, 8006, 8007) olayları PowerShell, VBScript, JScript, MSI yürütme denetimini kapsar.
```

```
6. WDAC / Code Integrity
Öncelik: Yüksek
Konum → Microsoft-Windows-CodeIntegrity%4Operational.evtx
Gözlem Notu: Kod bütünlüğü ihlali (3033 — denetim), engelleme (3077), imzasız sürücü yükleme (3034), politika yükleme (3099); Win11'de Smart App Control olayları da bu kanaldadır.
```

```
7. Security-Mitigations (Exploit Protection)
Öncelik: Orta
Konum → Microsoft-Windows-Security-Mitigations%4KernelMode.evtx ve UserMode.evtx
Gözlem Notu: Exploit Protection (Windows Defender Exploit Guard) olayları; CFG, DEP, ASLR ihlalleri (1-24 arası Event ID'ler) exploit girişimlerini gösterir (Win10 1709+).
```

```
8. Exploit Guard — Controlled Folder Access
Öncelik: Orta
Konum → Microsoft-Windows-Windows Defender%4Operational.evtx
Gözlem Notu: Kontrollü klasör erişimi engelleme (1123), denetim (1124) olayları ransomware korumasının devrede olduğunu ve engellenen yazma girişimlerini gösterir.
```

```
9. Exploit Guard — Network Protection
Öncelik: Orta
Konum → Microsoft-Windows-Windows Defender%4Operational.evtx
Gözlem Notu: Zararlı/şüpheli URL erişimi engelleme (1125), denetim (1126) olayları C2 bağlantı girişimlerini gösterir.
```

```
10. AppLocker — Packaged App
Öncelik: Düşük
Konum → Microsoft-Windows-AppLocker%4Packaged app-Execution.evtx
Gözlem Notu: UWP/Modern uygulama yürütme denetimi (8020, 8021, 8022, 8023, 8024); nadir kullanılır ancak sideloading senaryolarında önemli olabilir.
```

