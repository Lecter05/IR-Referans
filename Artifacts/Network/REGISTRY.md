
```
1. NetworkList\Profiles (Bağlanılan Ağ Geçmişi)
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles\{GUID}
MITRE: T1016
Gözlem Notu: Sistemin bağlandığı tüm ağların adı, ilk ve son bağlanma tarihi ile ağ türüne (public/private/domain) bakılır.
```

```
2. NetworkList\Signatures (Ağ İmzaları)
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Managed ve Unmanaged
MITRE: T1016
Gözlem Notu: Bağlanılan ağların MAC adresi (DefaultGatewayMac) ve DNS suffix bilgilerine bakılır.
```

```
3. Interfaces (IP Yapılandırması)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{GUID}
MITRE: T1016
Gözlem Notu: Her ağ arayüzünün IP adresi, subnet mask, default gateway, DNS sunucuları ve DHCP lease bilgilerine bakılır.
```

```
4. Proxy Ayarları (Kullanıcı)
Öncelik: Yüksek
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings → ProxyServer, ProxyEnable, AutoConfigURL
MITRE: T1090.001
Gözlem Notu: Manuel proxy adresi veya PAC dosyası tanımlanıp tanımlanmadığına ve bunun meşru olup olmadığına bakılır.
```

```
5. Proxy Ayarları (Sistem / GPO)
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Policies\Microsoft\Windows\CurrentVersion\Internet Settings ve HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\Connections → DefaultConnectionSettings
MITRE: T1090.001
Gözlem Notu: Group Policy ile dağıtılan proxy veya WinHTTP proxy ayarlarının değiştirilip değiştirilmediğine bakılır.
```

```
6. VPN Bağlantı Profilleri (RasMan)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\RasMan\PPP ve HKCU\SOFTWARE\Microsoft\RAS Phonebook
MITRE: T1572
Gözlem Notu: Tanımlı VPN bağlantı profillerinin adı, sunucu adresi ve bağlantı türüne bakılır.
```

```
7. MountPoints2 (Ağ Paylaşım Geçmişi)
Öncelik: Yüksek
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2
MITRE: T1021.002
Gözlem Notu: Bağlanılan UNC paylaşım yollarının (\\server\share) kayıtlarına bakılır.
```

```
8. Terminal Server Client (RDP Geçmişi)
Öncelik: Yüksek
Konum → HKCU\SOFTWARE\Microsoft\Terminal Server Client\Default ve Servers
MITRE: T1021.001
Gözlem Notu: RDP ile bağlanılan sunucu IP/hostname listesine ve her sunucu için kullanılan kullanıcı adına bakılır.
```

```
9. WinSCP / PuTTY Oturum Kayıtları
Öncelik: Yüksek
Konum → HKCU\SOFTWARE\Martin Prikryl\WinSCP 2\Sessions ve HKCU\SOFTWARE\SimonTatham\PuTTY\Sessions
MITRE: T1021.004
Gözlem Notu: SSH/SCP bağlantı geçmişinde sunucu adresi, port ve kullanıcı adı bilgilerine bakılır.
```

```
10. TeamViewer / AnyDesk / RemoteDesktop Kayıtları
Öncelik: Yüksek
Konum → HKCU\SOFTWARE\TeamViewer ve HKLM\SOFTWARE\TeamViewer ve HKLM\SOFTWARE\WOW6432Node\TeamViewer
MITRE: T1219
Gözlem Notu: Uzak erişim yazılımlarının kayıtlı bağlantı ID'leri ve son bağlantı bilgilerine bakılır.
```

```
11. PortProxy Kuralları
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\PortProxy\v4tov4\tcp
MITRE: T1090
Gözlem Notu: netsh interface portproxy ile oluşturulan port yönlendirme kurallarının varlığına bakılır.
```

```
12. Windows Remote Management (WinRM)
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WSMAN ve HKLM\SOFTWARE\Policies\Microsoft\Windows\WinRM
MITRE: T1021.006
Gözlem Notu: WinRM servisinin etkinleştirilip etkinleştirilmediğine ve TrustedHosts değerinin değiştirilip değiştirilmediğine bakılır.
```

```
13. DNS Client Cache (Registry)
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters
MITRE: T1071.004
Gözlem Notu: DNS cache yapılandırması ve MaxCacheTtl gibi manipüle edilmiş olabilecek parametrelere bakılır.
```

```
14. Winsock / LSP Kaydı
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\WinSock2\Parameters\Protocol_Catalog9 ve NameSpace_Catalog5
MITRE: T1090
Gözlem Notu: Ağ trafiğini intercept edebilecek kayıtlı LSP veya namespace sağlayıcılarına bakılır.
```

```
15. VPN Bağlantı Profilleri (Pbk Dosyası Referansı)
Öncelik: Orta
Konum → HKCU\SOFTWARE\Microsoft\RAS AutoDial\Addresses ve HKLM\SOFTWARE\Microsoft\RAS AutoDial
MITRE: T1572
Gözlem Notu: Otomatik VPN bağlantı tetikleyicisi olarak kayıtlı adres ve sunucu bilgilerine bakılır.
```

```
16. Map Network Drive MRU
Öncelik: Orta
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Map Network Drive MRU
MITRE: T1021.002
Gözlem Notu: Kullanıcının Map Network Drive ile bağlandığı sunucu ve paylaşım yollarına bakılır.
```

```
17. OpenSSH Known Hosts (Registry)
Öncelik: Orta
Konum → HKCU\SOFTWARE\OpenSSH\Agent
MITRE: T1021.004
Gözlem Notu: OpenSSH agent'ın registry'deki yapılandırma ve bilinen host kayıtlarına bakılır.
```

```
18. BITS Transfer Ayarları
Öncelik: Orta
Konum → HKLM\SOFTWARE\Policies\Microsoft\Windows\BITS ve HKLM\SYSTEM\CurrentControlSet\Services\BITS
MITRE: T1105
Gözlem Notu: BITS servis ayarlarının değiştirilip değiştirilmediğine veya transfer limitlerinin manipüle edilip edilmediğine bakılır.
```

```
19. SMB Yapılandırma Değişiklikleri
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters ve LanmanWorkstation\Parameters
MITRE: T1021.002
Gözlem Notu: SMBv1 etkinleştirilip etkinleştirilmediğine veya SMB imza gereksinimlerinin devre dışı bırakılıp bırakılmadığına bakılır.
```

```
20. RDP Bitmap Cache Ayarları
Öncelik: Düşük
Konum → HKCU\SOFTWARE\Microsoft\Terminal Server Client → BitmapPersistCacheSize
MITRE: T1021.001
Gözlem Notu: RDP bitmap cache'in devre dışı bırakılıp bırakılmadığına bakılır; devre dışı bırakma anti-forensics göstergesidir.
```

```
21. Hosts Dosyası Manipülasyonu (Registry İşaretçisi)
Öncelik: Düşük
Konum → HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters → DataBasePath
MITRE: T1071.004
Gözlem Notu: Hosts dosyasının varsayılan konumunun (%SystemRoot%\System32\drivers\etc) değiştirilip değiştirilmediğine bakılır.
```
