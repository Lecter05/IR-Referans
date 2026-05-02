
```
1. Volume Shadow Copy Silme (vssadmin delete shadows)
Öncelik: Yüksek
Konum → System.evtx → Event ID 7036 (VSS servisi) ve Application.evtx → Event ID 8194 (VSS)
MITRE: T1490
Gözlem Notu: vssadmin delete shadows veya wmic shadowcopy delete komutlarının çalıştırılıp çalıştırılmadığına Prefetch ve event log'lardan bakılır.
```

```
2. Volume Shadow Copy Resize ile Sınırlama
Öncelik: Yüksek
Konum → vssadmin resize shadowstorage komut geçmişi; Prefetch'te vssadmin.pf
MITRE: T1490
Gözlem Notu: Shadow copy alanının çok küçük bir boyuta (örn. 1MB) düşürülerek mevcut kopyaların silinip silinmediğine bakılır.
```

```
3. VSS Servisinin Devre Dışı Bırakılması
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\VSS → Start değeri
MITRE: T1490
Gözlem Notu: VSS servisinin Start değerinin 4 (disabled) yapılıp yapılmadığına bakılır.
```

```
4. bcdedit ile Recovery Seçenekleri Kapatma
Öncelik: Yüksek
Konum → BCD store; Prefetch'te bcdedit.pf; PowerShell/cmd geçmişi
MITRE: T1490
Gözlem Notu: bcdedit /set {default} recoveryenabled No ve bcdedit /set {default} bootstatuspolicy ignoreallfailures komutlarının çalıştırılıp çalıştırılmadığına bakılır.
```

```
5. System Restore Kapatma
Öncelik: Orta
Konum → HKLM\SOFTWARE\Policies\Microsoft\Windows NT\SystemRestore → DisableSR
MITRE: T1490
Gözlem Notu: System Restore'un policy ile kapatılıp kapatılmadığına ve mevcut restore point'lerin silinip silinmediğine bakılır.
```

```
6. WMI ile Shadow Copy Silme
Öncelik: Orta
Konum → Prefetch'te WMIC.pf; $UsnJrnl; PowerShell geçmişi
MITRE: T1490
Gözlem Notu: Get-WmiObject Win32_ShadowCopy veya wmic shadowcopy delete komutlarının çalıştırılıp çalıştırılmadığına bakılır.
```

```
7. PowerShell ile Shadow Copy Silme
Öncelik: Orta
Konum → PowerShell Operational Log → EID 4104; ConsoleHost_history.txt
MITRE: T1490
Gözlem Notu: PowerShell ile WMI veya CIM üzerinden shadow copy silme komutlarının script block loglarında kaydına bakılır.
```
