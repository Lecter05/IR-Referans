
```
1. Application Log — Ana Olay Kaydı
Öncelik: Orta
Konum → %SystemRoot%\System32\winevt\Logs\Application.evtx
Gözlem Notu: Uygulama çökmesi (1000 — Windows Error Reporting), uygulama hatası (1001 — WER Bucket), EMET/Exploit Protection olayları (1, 2), MSI yüklemeleri (MsiInstaller 1033, 1034, 11707, 11724) incelenir.
```

```
2. Application — Windows Error Reporting
Öncelik: Orta
Konum → Application.evtx
Gözlem Notu: Event ID 1000 ve 1001 (WER) çöken sürecin adını, modülünü ve hata ofsetini gösterir; exploit sonrası çökme belirtisi olabilir.
```

```
3. Application — ESENT Database Events
Öncelik: Düşük
Konum → Application.evtx
Gözlem Notu: ESENT kaynağından (Event ID 102, 105, 325, 326) gelen olaylar Active Directory veritabanı (ntds.dit) veya Exchange veritabanı erişimini doğrulamak için faydalıdır.
```

