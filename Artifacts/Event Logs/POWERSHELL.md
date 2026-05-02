
```
1. PowerShell Operational — Script Block Logging
Öncelik: Yüksek
Konum → Microsoft-Windows-PowerShell%4Operational.evtx
Gözlem Notu: Event ID 4104 her PowerShell script bloğunun tam metnini yakalar; AMSI entegrasyonuyla obfuscation çözülmüş versiyonu loglanır; suspicious olarak etiketlenen bloklar otomatik loglanır (Warning seviyesi). (Varsayılan: Kapalı, Win10 1709+ GPO ile etkin)
```

```
2. PowerShell Operational — Genel
Öncelik: Yüksek
Konum → Microsoft-Windows-PowerShell%4Operational.evtx
Gözlem Notu: Script Block Logging (4104), Module Logging (4103), Transcript başlatma (40961, 40962); 4104 obfuscated kodun decode edilmiş halini yakalar (Win10 5.0+ ve PowerShell 7).
```

```
3. Windows PowerShell (Legacy)
Öncelik: Yüksek
Konum → %SystemRoot%\System32\winevt\Logs\Windows PowerShell.evtx
Gözlem Notu: Engine başlatma (400), engine durdurma (403), pipeline yürütme (800) olaylarına bakılır (T1059.001); HostApplication alanı çalıştırılan komut satırını gösterir.
```

```
4. PowerShell — Constrained Language Mode
Öncelik: Orta
Konum → PowerShell%4Operational.evtx
Gözlem Notu: Event ID 4100 (komut doğrulama hatası), 53504 (CLM aktifleşme) Constrained Language Mode bypass girişimlerini gösterir.
```
