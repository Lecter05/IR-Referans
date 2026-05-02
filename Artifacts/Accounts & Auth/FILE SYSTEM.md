
```
1. SAM Veritabanı
Öncelik: Yüksek
Konum → C:\Windows\System32\config\SAM
MITRE: T1003.002
Gözlem Notu: Yerel hesapların NTLM hash'lerinin saklandığı veritabanının offline kopyasına bakılır.
```

```
2. SYSTEM Hive (SAM Şifreleme Anahtarı)
Öncelik: Yüksek
Konum → C:\Windows\System32\config\SYSTEM
MITRE: T1003.002
Gözlem Notu: SAM veritabanını decrypt etmek için gereken bootkey'in SYSTEM hive'ından elde edilip edilemeyeceğine bakılır.
```

```
3. SECURITY Hive
Öncelik: Yüksek
Konum → C:\Windows\System32\config\SECURITY
MITRE: T1003.004
Gözlem Notu: LSA secrets, cached domain credentials ve policy bilgilerinin saklandığı hive'a bakılır.
```

```
4. Volume Shadow Copy içindeki SAM/SYSTEM
Öncelik: Yüksek
Konum → \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy<N>\Windows\System32\config\SAM
MITRE: T1003.002
Gözlem Notu: Shadow copy'lerden elde edilebilecek SAM/SYSTEM kopyalarına bakılır; saldırgan bu yöntemle hash çıkarabilir.
```

```
5. NTDS.dit (Domain Controller)
Öncelik: Yüksek
Konum → C:\Windows\NTDS\ntds.dit
MITRE: T1003.003
Gözlem Notu: Domain ortamında tüm hesapların hash'lerinin saklandığı Active Directory veritabanının kopyalanıp kopyalanmadığına bakılır.
```

```
6. NTDS.dit Shadow Copy Erişimi
Öncelik: Yüksek
Konum → Prefetch (ntdsutil.pf, vssadmin.pf); $UsnJrnl'de ntds.dit kopyalama izi
MITRE: T1003.003
Gözlem Notu: ntdsutil, vssadmin veya diskshadow ile NTDS.dit'in kopyalanıp kopyalanmadığına bakılır.
```

```
7. DPAPI Master Key Dosyaları
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Roaming\Microsoft\Protect\<SID>\<GUID>
MITRE: T1003.004
Gözlem Notu: DPAPI master key dosyalarının varlığına ve son değiştirme tarihine bakılır; credential decrypt için kullanılır.
```

```
8. Credential Manager Vault Dosyaları
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Local\Microsoft\Credentials\<GUID> ve C:\Users\<user>\AppData\Roaming\Microsoft\Credentials\<GUID>
MITRE: T1555.404
Gözlem Notu: Windows Credential Manager'da saklanan generic ve domain credential blob'larına bakılır.
```

```
9. Kerberos Ticket Dosyaları (kirbi/ccache)
Öncelik: Yüksek
Konum → C:\Users\<user>\*.kirbi, %TEMP%\*.kirbi, C:\Windows\Temp\*.kirbi
MITRE: T1558
Gözlem Notu: Dışa aktarılmış Kerberos ticket dosyalarının disk üzerindeki varlığına bakılır.
```

```
10. LSASS Memory Dump Dosyası
Öncelik: Yüksek
Konum → C:\Windows\Temp\lsass.dmp, C:\Users\<user>\AppData\Local\Temp\lsass*.dmp, herhangi bir dizinde lsass*.dmp
MITRE: T1003.001
Gözlem Notu: LSASS process'inin memory dump dosyasının disk üzerinde bırakılıp bırakılmadığına bakılır.
```

```
11. Comsvcs.dll MiniDump İzleri
Öncelik: Yüksek
Konum → Prefetch (rundll32.pf); $UsnJrnl'de .dmp dosyası oluşturma; PowerShell EID 4104
MITRE: T1003.001
Gözlem Notu: rundll32.exe comsvcs.dll MiniDump komutuyla LSASS dump alınıp alınmadığına bakılır.
```

```
12. Procdump İzleri
Öncelik: Yüksek
Konum → Prefetch (procdump.pf, procdump64.pf); Amcache; $UsnJrnl
MITRE: T1003.001
Gözlem Notu: Procdump aracının LSASS'ı hedef alarak çalıştırılıp çalıştırılmadığına bakılır.
```

```
13. Mimikatz İzleri (Dosya Sistemi)
Öncelik: Yüksek
Konum → Prefetch (mimikatz.pf); Amcache; $MFT (mimikatz.exe, mimilib.dll, mimidrv.sys); $UsnJrnl
MITRE: T1003.001
Gözlem Notu: Mimikatz ve ilişkili dosyaların (mimilib.dll, mimidrv.sys) dosya sistemi kalıntılarına bakılır.
```

```
14. Chrome / Edge Saved Passwords Veritabanı
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\Login Data ve C:\Users\<user>\AppData\Local\Microsoft\Edge\User Data\Default\Login Data
MITRE: T1555.003
Gözlem Notu: Tarayıcıda saklanan credential veritabanına erişilip erişilmediğine (son erişim zamanı) bakılır.
```

```
15. Group Policy Preferences (cpassword)
Öncelik: Yüksek
Konum → \\<domain>\SYSVOL\<domain>\Policies\<GUID>\Machine\Preferences\Groups\Groups.xml ve Services\Services.xml
MITRE: T1552.006
Gözlem Notu: GPP XML dosyalarında cpassword attribute'u ile saklanan şifrelenmiş parolalara bakılır (MS14-025).
```

```
16. SAM / SYSTEM / SECURITY Backup Kopyaları
Öncelik: Orta
Konum → C:\Windows\Repair\SAM, C:\Windows\System32\config\RegBack\SAM (Win10 1803 öncesi)
MITRE: T1003.002
Gözlem Notu: Eski yedek kopyaların var olup olmadığına bakılır (Win10 1803+ RegBack varsayılan kapalı; Win11'de yok).
```

```
17. DPAPI System Master Key
Öncelik: Orta
Konum → C:\Windows\System32\Microsoft\Protect\S-1-5-18\User\
MITRE: T1003.004
Gözlem Notu: SYSTEM hesabının DPAPI master key'lerinin varlığına bakılır.
```

```
18. Credential Manager Vault Policy
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Local\Microsoft\Vault\<GUID>\Policy.vpol ve <GUID>.vcrd
MITRE: T1555.404
Gözlem Notu: Windows Vault'ta saklanan web ve Windows kimlik bilgileri dosyalarına bakılır.
```

```
19. Task Manager / Process Explorer LSASS Dump
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Local\Temp\lsass.DMP (Task Manager varsayılan çıktı yolu)
MITRE: T1003.001
Gözlem Notu: Task Manager'ın "Create dump file" ile oluşturduğu LSASS dump dosyasının varlığına bakılır.
```

```
20. Windows Credential Manager (cmdkey Geçmişi)
Öncelik: Orta
Konum → Prefetch (cmdkey.pf, vaultcmd.pf); PowerShell geçmişi
MITRE: T1555.404
Gözlem Notu: cmdkey.exe ile saklanan veya listelenen credential kayıtlarının Prefetch izlerine bakılır.
```

```
21. Unattend.xml / Sysprep Dosyaları
Öncelik: Orta
Konum → C:\Windows\Panther\Unattend.xml, C:\Windows\Panther\unattend\Unattend.xml, C:\Windows\System32\Sysprep\sysprep.xml
MITRE: T1552.001
Gözlem Notu: Kurulum dosyalarında plaintext veya base64 kodlanmış parola bilgisi olup olmadığına bakılır.
```

```
22. Firefox Saved Passwords
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Roaming\Mozilla\Firefox\Profiles\<profile>\logins.json ve key4.db
MITRE: T1555.003
Gözlem Notu: Firefox'ta saklanan şifreli credential dosyalarının erişim zamanına bakılır.
```

```
23. Chrome / Edge DPAPI State Dosyası
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Local State ve Microsoft\Edge\User Data\Local State
MITRE: T1555.003
Gözlem Notu: Tarayıcı parolalarını decrypt etmek için gereken DPAPI şifreli anahtarın erişim zamanına bakılır.
```

```
24. Kerberos Ticket Cache (Live)
Öncelik: Yüksek
Erişim: Live System
Konum → Bellekte LSASS process'i içinde (volatile); klist çıktısı
MITRE: T1558
Gözlem Notu: Aktif Kerberos TGT ve service ticket'larının listesi ve geçerlilik sürelerine bakılır.
```

```
25. SecureString / PSCredential Export Dosyaları
Öncelik: Düşük
Konum → Disk genelinde *.xml, *.clixml (Export-Clixml ile dışa aktarılmış credential); PowerShell geçmişi
MITRE: T1555
Gözlem Notu: PowerShell ile dışa aktarılan SecureString veya PSCredential nesne dosyalarına bakılır.
```
