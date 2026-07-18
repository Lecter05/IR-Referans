
```
1. ProfileList (Kullanıcı Profil Kayıtları)
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\<SID>
MITRE: T1136.001
Gözlem Notu: Sistemde oluşturulmuş tüm kullanıcı profillerinin SID'si, profil yolu ve son yükleme zamanına bakılır.
```

```
2. SAM Domain Account (Yerel Hesaplar)
Öncelik: Yüksek
Konum → HKLM\SAM\SAM\Domains\Account\Users\<RID>
MITRE: T1003.002
Gözlem Notu: Yerel hesapların RID değeri, hesap adı, oluşturulma tarihi, son oturum açma ve parola değiştirme zamanlarına bakılır.
```

```
3. SAM Domain Groups
Öncelik: Yüksek
Konum → HKLM\SAM\SAM\Domains\Account\Aliases ve Builtin\Aliases
MITRE: T1136.001
Gözlem Notu: Administrators (RID 544) ve Remote Desktop Users (RID 555) gibi grupların üye listesine eklenen hesaplara bakılır.
```

```
4. LogonUI / Last Logged On User
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI → LastLoggedOnUser, LastLoggedOnSAMUser
MITRE: T1078
Gözlem Notu: Sistemde en son oturum açan kullanıcı adının beklenmeyen bir hesap olup olmadığına bakılır.
```

```
5. Winlogon Credentials
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon → DefaultUserName, DefaultPassword, AutoAdminLogon
MITRE: T1078.001
Gözlem Notu: Otomatik oturum açma için plaintext parola saklanıp saklanmadığına bakılır.
```

```
6. Cached Domain Logon Credentials
Öncelik: Yüksek
Konum → HKLM\SECURITY\Cache → NL$1, NL$2 ... NL$10
MITRE: T1003.005
Gözlem Notu: Domain controller'a erişim olmadan oturum açılabilmesi için cache'lenen kimlik bilgisi sayısına ve varlığına bakılır.
```

```
7. LSA Policy Secrets Referansı
Öncelik: Yüksek
Konum → HKLM\SECURITY\Policy\Secrets\<SecretName>
MITRE: T1003.004
Gözlem Notu: Service account parolaları, DPAPI anahtarları ve diğer LSA secret kayıtlarının varlığına bakılır.
```

```
8. WDigest UseLogonCredential
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest → UseLogonCredential
MITRE: T1003.001
Gözlem Notu: WDigest'in plaintext parola saklama özelliğinin 1 yapılarak etkinleştirilip etkinleştirilmediğine bakılır (Win10/11'de varsayılan 0).
```

```
9. Security Packages (SSP Ekleme)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa → Security Packages ve HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig → Security Packages
MITRE: T1547.005
Gözlem Notu: Varsayılan dışı eklenen SSP DLL'lerine bakılır; memdump gibi zararlı SSP credential theft sağlar.
```

```
10. Notification Packages (Password Filter)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa → Notification Packages
MITRE: T1556.002
Gözlem Notu: Parola değişikliğinde cleartext parolayı yakalayan zararlı password filter DLL'lerine bakılır.
```

```
11. RunAsPPL (LSA Protection)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa → RunAsPPL
MITRE: T1003.001
Gözlem Notu: LSA korumasının devre dışı bırakılıp bırakılmadığına bakılır; değerin 0 yapılması credential dump'ı kolaylaştırır.
```

```
12. SpecialAccounts (Gizli Hesap)
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList
MITRE: T1078.001
Gözlem Notu: Oturum açma ekranından gizlenen hesapların (değer 0 yapılanlar) varlığına bakılır.
```

```
13. AutoLogon Credentials
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon → AutoAdminLogon, DefaultUserName, DefaultPassword, DefaultDomainName
MITRE: T1078.001
Gözlem Notu: Registry'de plaintext saklanan otomatik oturum açma kimlik bilgilerine bakılır.
```

```
14. User Account Control (UAC) Ayarları
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System → EnableLUA, ConsentPromptBehaviorAdmin, LocalAccountTokenFilterPolicy
MITRE: T1548.002
Gözlem Notu: UAC'ın kapatılıp kapatılmadığına (EnableLUA=0) veya uzak UAC filtrasyonunun devre dışı bırakılıp bırakılmadığına (LocalAccountTokenFilterPolicy=1) bakılır.
```

```
15. CachedLogonsCount Ayarı
Öncelik: Orta
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon → CachedLogonsCount
MITRE: T1003.005
Gözlem Notu: Cache'lenen credential sayısının varsayılan (10) değerinden artırılıp artırılmadığına bakılır.
```

```
16. Credential Guard Yapılandırması
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa → LsaCfgFlags ve HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard → EnableVirtualizationBasedSecurity
MITRE: T1003
Gözlem Notu: Credential Guard'ın devre dışı bırakılıp bırakılmadığına ve VBS ayarlarının değiştirilip değiştirilmediğine bakılır.
```

```
17. Authentication Packages
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa → Authentication Packages
MITRE: T1547.002
Gözlem Notu: Varsayılan msv1_0 dışında eklenen kimlik doğrulama paketlerine bakılır.
```

```
18. Restrict NTLM Ayarları
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa\MSV1_0 → RestrictSendingNTLMTraffic, NtlmMinClientSec, NtlmMinServerSec
MITRE: T1550.002
Gözlem Notu: NTLM kısıtlamalarının gevşetilip gevşetilmediğine ve NTLMv1'e izin verilip verilmediğine bakılır.
```

```
19. LmCompatibilityLevel
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa → LmCompatibilityLevel
MITRE: T1550.002
Gözlem Notu: Değerin 5'ten (NTLMv2 only) düşürülerek zayıf LM/NTLMv1 kullanımına izin verilip verilmediğine bakılır.
```

```
20. Kerberos Yapılandırması
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters → AllowTgtSessionKey, MaxTicketAge
MITRE: T1558
Gözlem Notu: TGT session key dışa aktarımının etkinleştirilip etkinleştirilmediğine ve ticket ömürlerinin değiştirilip değiştirilmediğine bakılır.
```

```
21. Credential Delegation (CredSSP)
Öncelik: Orta
Konum → HKLM\SOFTWARE\Policies\Microsoft\Windows\CredentialsDelegation → AllowDefaultCredentials, AllowDefCredentialsWhenNTLMOnly
MITRE: T1550
Gözlem Notu: Credential delegation'ın wildcard (*) ile tüm sunuculara izin verecek şekilde ayarlanıp ayarlanmadığına bakılır.
```

```
22. Remote Desktop Users Grup Üyeliği
Öncelik: Orta
Konum → HKLM\SAM\SAM\Domains\Builtin\Aliases\00000237 (RID 555)
MITRE: T1136.001
Gözlem Notu: Remote Desktop Users grubuna eklenen beklenmeyen hesaplara bakılır.
```
