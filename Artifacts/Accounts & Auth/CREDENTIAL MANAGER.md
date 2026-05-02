
```
1. Windows Vault (Generic / Domain Credentials)
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Local\Microsoft\Vault\<GUID>\*.vcrd ve Policy.vpol
MITRE: T1555.404
Gözlem Notu: Windows Vault'ta saklanan web ve ağ credential dosyalarının sayısı ve son değişiklik zamanına bakılır.
```

```
2. Credential Manager Blob Dosyaları
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Roaming\Microsoft\Credentials\<GUID> ve C:\Users\<user>\AppData\Local\Microsoft\Credentials\<GUID>
MITRE: T1555.404
Gözlem Notu: DPAPI ile şifrelenmiş credential blob dosyalarının sayısına ve oluşturulma zamanlarına bakılır.
```

```
3. DPAPI Backup Key (Domain Controller)
Öncelik: Yüksek
Erişim: Live System
Konum → ntds.dit ve LSASS belleği (DC üzerinde)
MITRE: T1003.004
Gözlem Notu: Domain DPAPI backup key'inin dışa aktarılıp aktarılmadığına bakılır; tüm domain kullanıcılarının credential'ını decrypt etmeye yarar.
```

```
4. DPAPI Master Key Erişim İzleri
Öncelik: Orta
Konum → Security.evtx → Event ID 4662 (DPAPI object access); Sysmon → EID 10 (lsass.exe erişimi)
MITRE: T1003.004
Gözlem Notu: DPAPI master key'e programatik erişim izlerine bakılır; credential decrypt girişimini gösterir.
```

```
5. Windows Credential Manager UI Erişimi (cmdkey)
Öncelik: Orta
Konum → Prefetch (cmdkey.pf, vaultcmd.pf); PowerShell geçmişi
MITRE: T1555.404
Gözlem Notu: cmdkey /list veya vaultcmd ile credential enumerasyonu yapılıp yapılmadığına bakılır.
```

```
6. Chrome / Edge DPAPI State Dosyası
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Local State ve Microsoft\Edge\User Data\Local State
MITRE: T1555.003
Gözlem Notu: Tarayıcı parolalarını decrypt etmek için gereken DPAPI şifreli anahtarın erişim zamanına bakılır.
```

