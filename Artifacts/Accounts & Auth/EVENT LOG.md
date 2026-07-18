
```
1. Hesap Oluşturma — Event ID 4720
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1136.001
Gözlem Notu: Yeni oluşturulan kullanıcı hesabının adı, oluşturan hesap ve oluşturma zamanına bakılır.
```

```
2. Hesap Silme — Event ID 4726
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1070.004
Gözlem Notu: Silinen hesap adı ve işlemi gerçekleştiren hesap bilgisine bakılır; saldırgan iz silmek için hesap silebilir.
```

```
3. Hesap Etkinleştirme / Devre Dışı Bırakma — Event ID 4722, 4725
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1078.001
Gözlem Notu: Devre dışı olan Guest veya varsayılan hesapların etkinleştirilip etkinleştirilmediğine bakılır.
```

```
4. Hesap Özelliği Değişikliği — Event ID 4738
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1098
Gözlem Notu: Hesap özelliklerinde (parola süresi dolmaz, parola değişikliği vb.) yapılan değişikliklere bakılır.
```

```
5. Güvenlik Grubu Üyelik Değişikliği — Event ID 4728, 4732, 4756
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1098
Gözlem Notu: Administrators, Domain Admins gibi yüksek yetkili gruplara eklenen hesaplara bakılır.
```

```
6. Parola Değişikliği — Event ID 4723, 4724
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1098
Gözlem Notu: Admin tarafından yapılan parola sıfırlama (4724) olaylarında hedef hesap ve sıfırlayan hesaba bakılır.
```

```
7. Başarılı Oturum Açma — Event ID 4624
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1078
Gözlem Notu: Logon Type (2=Interactive, 3=Network, 7=Unlock, 10=RDP, 11=CachedInteractive), kaynak IP, kullanıcı adı ve oturum zamanına bakılır.
```

```
8. Başarısız Oturum Açma — Event ID 4625
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1110
Gözlem Notu: Kısa sürede çok sayıda başarısız deneme, hata kodları (0xC000006A=yanlış parola, 0xC0000064=bilinmeyen kullanıcı) ve kaynak IP'ye bakılır.
```

```
9. Hesap Kilitleme — Event ID 4740, 4767
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1110
Gözlem Notu: Brute-force göstergesi olarak kilitlenen hesap adı ve kilitlenmeye neden olan kaynak bilgisayar adına bakılır.
```

```
10. Explicit Credential Kullanımı — Event ID 4648
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1078
Gözlem Notu: runas, PsExec veya RDP ile farklı kimlik bilgileriyle yapılan bağlantılarda kullanılan hesap ve hedef sunucuya bakılır.
```

```
11. Özel Ayrıcalık Atanması — Event ID 4672
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1134
Gözlem Notu: SeDebugPrivilege, SeTcbPrivilege, SeImpersonatePrivilege gibi hassas ayrıcalıkların hangi hesaba atandığına bakılır.
```

```
12. Token Manipülasyonu / Impersonation — Event ID 4624 Type 9, 4648
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1134.001
Gözlem Notu: Logon Type 9 olaylarında token çalma veya impersonation göstergelerine bakılır.
```

```
13. LSASS Erişimi — Sysmon Event ID 10
Öncelik: Yüksek
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
MITRE: T1003.001
Gözlem Notu: lsass.exe'ye erişen kaynak process adı, PID ve erişim mask'ına bakılır (Sysmon kuruluysa).
```

```
14. Kerberos TGT İstek (AS-REQ) — Event ID 4768
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1558.003
Gözlem Notu: AS-REP Roasting göstergesi olarak şifreleme türü (0x17=RC4) ve kaynak IP'ye bakılır.
```

```
15. Kerberos Service Ticket İstek (TGS-REQ) — Event ID 4769
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1558.003
Gözlem Notu: Kerberoasting göstergesi olarak aynı hesaptan çok sayıda service ticket isteği ve RC4 şifreleme kullanımına bakılır.
```

```
16. Kerberos Pre-Authentication Failure — Event ID 4771
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1110
Gözlem Notu: Kerberos pre-auth hatalarında hata kodu (0x18=yanlış parola) ve kaynak IP'ye bakılır; brute-force göstergesidir.
```

```
17. Kerberos Ticket Replay / Golden Ticket İpuçları
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx → Event ID 4769 (anormal ticket lifetime), 4624
MITRE: T1558.001
Gözlem Notu: Olağandışı uzun ömürlü TGT'lere, var olmayan kullanıcı adlarına veya SID geçmişi tutarsızlıklarına bakılır.
```

```
18. NTLM Authentication — Event ID 4624 (NTLM), 4776
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1550.002
Gözlem Notu: Pass-the-Hash göstergesi olarak NTLM kimlik doğrulamalarında kaynak workstation adı ve kullanılan hesap bilgisine bakılır.
```

```
19. NTLM Credential Validation — Event ID 4776
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1110
Gözlem Notu: NTLM doğrulama başarı/başarısızlık olaylarında hedef hesap ve kaynak bilgisayar adına bakılır.
```

```
20. Audit Policy Değişikliği — Event ID 4719
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1562.002
Gözlem Notu: Logon/Logoff veya account management audit kategorilerinin devre dışı bırakılıp bırakılmadığına bakılır.
```

```
21. Security Event Log Temizleme — Event ID 1102
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1070.001
Gözlem Notu: Security logunu temizleyen hesap bilgisine bakılır; credential theft kanıtlarını silme girişimi olabilir.
```

```
22. PowerShell Credential Kullanımı — Event ID 4104
Öncelik: Yüksek
Konum → Microsoft-Windows-PowerShell%4Operational.evtx
MITRE: T1003
Gözlem Notu: Get-Credential, Invoke-Mimikatz, sekurlsa::logonpasswords, DCSync gibi komutların script block loglarında kaydına bakılır.
```

```
23. LSASS Erişimi — Security Event ID 4663
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1003.001
Gözlem Notu: LSASS process'ine PROCESS_VM_READ erişiminde bulunan beklenmeyen process'lere bakılır.
```

```
24. RDP Oturum — Event ID 21, 22, 23, 24, 25
Öncelik: Yüksek
Konum → Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx
MITRE: T1078
Gözlem Notu: RDP oturum başarı/disconnect/reconnect olaylarında kaynak IP ve kullanıcı hesabına bakılır.
```

```
25. Gruptan Üye Çıkarma — Event ID 4729, 4733, 4757
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1098
Gözlem Notu: Güvenlik gruplarından çıkarılan üyelere bakılır; saldırgan iz gizleme amacıyla eklediği hesabı çıkarabilir.
```

```
26. Ayrıcalık Kullanımı — Event ID 4673, 4674
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1134
Gözlem Notu: SeDebugPrivilege kullanımının LSASS erişimine işaret edip etmediğine bakılır.
```

```
27. User Profile Service Log — Application EID 1, 2, 4
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Application.evtx → Event Source: User Profile Service
MITRE: T1136.001
Gözlem Notu: Yeni kullanıcı profili yükleme/oluşturma olaylarında beklenmeyen hesap adlarına bakılır.
```

```
28. Defender Credential Theft Algılama — Event ID 1116, 1117
Öncelik: Orta
Konum → Microsoft-Windows-Windows Defender%4Operational.evtx
MITRE: T1003
Gözlem Notu: HackTool:Win32/Mimikatz, Behavior:Win32/CredentialStealing gibi tehdit isimlerinin tespit edilip edilmediğine bakılır.
```
