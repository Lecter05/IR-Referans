
```
1. SAM Veritabanı Çevrimdışı Analizi
Öncelik: Yüksek
Konum → C:\Windows\System32\config\SAM (offline)
MITRE: T1003.002
Gözlem Notu: SAM hive'ından yerel kullanıcı listesi, RID, son logon zamanı, parola değişim tarihi ve hesap bayrakları elde edilir.
```

```
2. SAM Hive — F ve V Değerleri
Öncelik: Yüksek
Konum → HKLM\SAM\SAM\Domains\Account\Users\<RID> → F (hesap metadata) ve V (kullanıcı bilgisi)
MITRE: T1003.002
Gözlem Notu: F değerindeki son logon, parola değişim, hesap bitiş tarihi ve V değerindeki NTLM hash offset'ine bakılır.
```

```
3. SECURITY Hive — LSA Secrets
Öncelik: Yüksek
Konum → HKLM\SECURITY\Policy\Secrets\<name>\CurrVal ve OldVal
MITRE: T1003.004
Gözlem Notu: Service account parolaları ($MACHINE.ACC, DefaultPassword, DPAPI anahtarları) gibi secret değerlerine bakılır.
```

```
4. SECURITY Hive — Cached Credentials
Öncelik: Yüksek
Konum → HKLM\SECURITY\Cache → NL$1 ... NL$10 (DCC2 hash)
MITRE: T1003.005
Gözlem Notu: Domain Cached Credentials (DCC2) hash'lerinin varlığına ve sayısına bakılır.
```

```
5. LSA Protection (PPL) Durumu
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa → RunAsPPL
MITRE: T1003.001
Gözlem Notu: LSASS'ın Protected Process Light olarak çalışıp çalışmadığına ve bu korumanın devre dışı bırakılıp bırakılmadığına bakılır.
```

```
6. LSASS Dump (WER / Silinmiş Dosya)
Öncelik: Yüksek
Konum → C:\ProgramData\Microsoft\Windows\WER\ReportQueue\*\lsass.exe*.dmp ve $MFT'de lsass*.dmp kalıntıları
MITRE: T1003.001
Gözlem Notu: Windows Error Reporting aracılığıyla LSASS crash dump alınıp alınmadığına veya silinmiş dump kalıntılarına bakılır.
```

```
7. LSASS Dump via Silent Process Exit
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\lsass.exe → MonitorProcess ve HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\lsass.exe → GlobalFlag
MITRE: T1003.001
Gözlem Notu: SilentProcessExit mekanizmasının LSASS dump almak için konfigüre edilip edilmediğine bakılır.
```
