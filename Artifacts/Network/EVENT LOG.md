
```
1. Security.evtx — Event ID 4624 Type 3 (Network Logon)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1021.002
Gözlem Notu: Type 3 (network) oturum açmalarında kaynak IP, kullanıcı adı ve kimlik doğrulama paketine bakılır.
```

```
2. Security.evtx — Event ID 4624 Type 10 (RDP Logon)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1021.001
Gözlem Notu: Logon Type 10 olaylarında kaynak IP adresi ve kullanıcı hesabına bakılır.
```

```
3. Security.evtx — Event ID 4648 (Explicit Credential Logon)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1021
Gözlem Notu: Farklı kimlik bilgileri ile yapılan bağlantılarda hedef sunucu ve kullanılan hesap bilgilerine bakılır.
```

```
4. Security.evtx — Event ID 5140, 5145 (Network Share Access)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1021.002
Gözlem Notu: Paylaşılan klasörlere erişen kaynak IP, kullanıcı ve erişilen dosya yoluna bakılır.
```

```
5. TerminalServices-LocalSessionManager — Event ID 21, 24, 25
Öncelik: Yüksek
Konum → Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx
MITRE: T1021.001
Gözlem Notu: RDP oturum başlatma olaylarında kaynak IP adresi ve kullanıcı adına bakılır.
```

```
6. TerminalServices-RDPClient — Event ID 1024, 1102
Öncelik: Yüksek
Konum → Microsoft-Windows-TerminalServices-RDPClient%4Operational.evtx
MITRE: T1021.001
Gözlem Notu: İstemciden başlatılan RDP bağlantılarında hedef sunucu adresine bakılır.
```

```
7. WinRM / PowerShell Remoting Logları
Öncelik: Yüksek
Konum → Microsoft-Windows-WinRM%4Operational.evtx → EID 6, 91, 161 ve Microsoft-Windows-PowerShell%4Operational.evtx → EID 53, 4104, 40961, 40962
MITRE: T1021.006
Gözlem Notu: WinRM bağlantılarında kaynak IP ve çalıştırılan uzak komutlara bakılır.
```

```
8. BITS-Client Operational — Event ID 3, 59, 60
Öncelik: Yüksek
Konum → Microsoft-Windows-Bits-Client%4Operational.evtx
MITRE: T1105
Gözlem Notu: BITS transfer olaylarında kaynak URL, hedef dosya yolu ve transfer boyutuna bakılır.
```

```
9. DNS Client Operational — Event ID 3006, 3008
Öncelik: Yüksek
Konum → Microsoft-Windows-DNS-Client%4Operational.evtx
MITRE: T1071.004
Gözlem Notu: DNS sorgu loglarında çözümlenen domain adları ve dönen IP adreslerine bakılır (Win10 1709+, varsayılan kapalı olabilir).
```

```
10. WLAN-AutoConfig — Event ID 8001, 8002, 8003
Öncelik: Yüksek
Konum → Microsoft-Windows-WLAN-AutoConfig%4Operational.evtx
MITRE: T1016.001
Gözlem Notu: Kablosuz ağ bağlantı/kopma olaylarında SSID, BSSID, şifreleme türü ve bağlantı zamanına bakılır.
```

```
11. Sysmon — Network Connection (Event ID 3)
Öncelik: Yüksek
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
MITRE: T1071
Gözlem Notu: Ağ bağlantısı kuran process adı, kaynak/hedef IP:port ve protokol bilgisine bakılır (Sysmon kuruluysa).
```

```
12. Sysmon — DNS Query (Event ID 22)
Öncelik: Yüksek
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
MITRE: T1071.004
Gözlem Notu: DNS sorgusu yapan process ve sorgulanan domain adına bakılır (Sysmon kuruluysa).
```

```
13. VPN / RAS Logları — Event ID 20221–20226
Öncelik: Yüksek
Konum → Application.evtx → Event Source: RasClient
MITRE: T1572
Gözlem Notu: VPN bağlantı kurma/kopma olaylarında sunucu adresi, protokol ve başarı/hata durumuna bakılır.
```

```
14. OpenSSH Server Log
Öncelik: Yüksek
Konum → OpenSSH%4Operational.evtx (Win10 1809+ / Win11 eğer OpenSSH Server etkinse)
MITRE: T1021.004
Gözlem Notu: SSH bağlantı olaylarında kaynak IP, kullanıcı adı ve kimlik doğrulama yöntemine bakılır.
```

```
15. Security.evtx — Event ID 4946, 4947, 4950 (Firewall Rule Değişiklikleri)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1562.004
Gözlem Notu: Yeni eklenen veya değiştirilen firewall kurallarının adı ve kapsamına bakılır.
```

```
16. Security.evtx — Event ID 5152, 5156, 5157 (Windows Filtering Platform)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1071
Gözlem Notu: Engellenen veya izin verilen ağ bağlantılarında kaynak/hedef IP ve port bilgilerine bakılır.
```

```
17. NTLM Operational Log
Öncelik: Orta
Konum → Microsoft-Windows-NTLM%4Operational.evtx
MITRE: T1021
Gözlem Notu: NTLM kimlik doğrulama olaylarında kaynak ve hedef bilgilerine bakılır; NTLM relay saldırı göstergesi olabilir.
```

```
18. SMBClient / SMBServer Logları
Öncelik: Orta
Konum → Microsoft-Windows-SmbClient%4Operational.evtx ve Microsoft-Windows-SMBServer%4Operational.evtx
MITRE: T1021.002
Gözlem Notu: SMB bağlantı hatalarında hedef sunucu ve paylaşım bilgilerine bakılır.
```

```
19. Sysmon — Pipe Connected / Created (Event ID 17, 18)
Öncelik: Orta
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
MITRE: T1021.002
Gözlem Notu: Named pipe oluşturma ve bağlantı olaylarında lateral movement göstergelerine bakılır.
```

```
20. Windows Firewall Event Log — Event ID 2003, 2004, 2005, 2006
Öncelik: Orta
Konum → Microsoft-Windows-Windows Firewall With Advanced Security%4Firewall.evtx
MITRE: T1562.004
Gözlem Notu: Firewall kural ekleme, silme veya profil kapatma olaylarına bakılır.
```

```
21. LDAP Client Trace
Öncelik: Düşük
Erişim: Live System
Konum → Microsoft-Windows-LDAP-Client/Debug ETL; varsayılan kapalı
MITRE: T1071
Gözlem Notu: LDAP sorgu trace'lerinin etkinleştirilip etkinleştirilmediğine ve Active Directory keşif sorgularına bakılır.
```
