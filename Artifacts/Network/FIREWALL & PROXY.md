
```
1. Windows Firewall Log Dosyası
Öncelik: Yüksek
Konum → C:\Windows\System32\LogFiles\Firewall\pfirewall.log
MITRE: T1562.004
Gözlem Notu: Engellenen ve izin verilen bağlantılarda kaynak/hedef IP, port ve aksiyon (ALLOW/DROP) bilgilerine bakılır.
```

```
2. Firewall Profil Ayarları
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile, StandardProfile, PublicProfile → EnableFirewall
MITRE: T1562.004
Gözlem Notu: Firewall profillerinin (Domain/Private/Public) tamamen kapatılıp kapatılmadığına bakılır.
```

```
3. Firewall Kuralları (Registry)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\FirewallRules
MITRE: T1562.004
Gözlem Notu: Olağandışı allow kurallarında belirtilen program yolları, port aralıkları ve uzak IP'lere bakılır.
```

```
4. Windows Defender Firewall Event Log — Event ID 2003, 2004, 2005, 2006, 2009
Öncelik: Orta
Konum → Microsoft-Windows-Windows Firewall With Advanced Security%4Firewall.evtx
MITRE: T1562.004
Gözlem Notu: Kural ekleme (2004), kural silme (2006) ve profil değişikliği (2009) olaylarına bakılır.
```

```
5. WinHTTP Proxy Ayarları
Öncelik: Orta
Konum → netsh winhttp show proxy çıktısı ve HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\Connections → WinHttpSettings
MITRE: T1090.001
Gözlem Notu: Sistem düzeyinde WinHTTP proxy ayarının değiştirilip değiştirilmediğine bakılır.
```

```
6. PAC (Proxy Auto-Config) Dosyası İzleri
Öncelik: Orta
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings → AutoConfigURL ve C:\Users\<user>\AppData\Local\Microsoft\Windows\INetCache\ içindeki .pac dosyaları
MITRE: T1090.001
Gözlem Notu: Tanımlı PAC URL'sinin meşru olup olmadığına ve cache'deki PAC dosyasının içeriğine bakılır.
```

```
7. WPAD (Web Proxy Auto-Discovery) Ayarları
Öncelik: Orta
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\Wpad ve DNS/DHCP WPAD sorguları
MITRE: T1090.001
Gözlem Notu: WPAD'ın etkin olup olmadığına ve kötü amaçlı WPAD sunucusuna yönlendirilip yönlendirilmediğine bakılır.
```

```
8. IPsec Policy ve Kuralları
Öncelik: Düşük
Konum → HKLM\SOFTWARE\Policies\Microsoft\Windows\IPSec\Policy\Local ve netsh ipsec static show all
MITRE: T1090
Gözlem Notu: IPsec politikalarında trafik filtreleme veya tünel kurallarının eklenip eklenmediğine bakılır.
```
