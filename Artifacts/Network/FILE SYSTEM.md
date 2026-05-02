
```
1. Hosts Dosyası
Öncelik: Yüksek
Konum → C:\Windows\System32\drivers\etc\hosts
MITRE: T1071.004
Gözlem Notu: Meşru domain'lerin farklı IP'lere yönlendirilip yönlendirilmediğine veya C2 gizleme girdilerine bakılır.
```

```
2. BITS Transfer Job Veritabanı
Öncelik: Yüksek
Konum → C:\ProgramData\Microsoft\Network\Downloader\qmgr0.dat ve qmgr1.dat
MITRE: T1105
Gözlem Notu: BITS job'larındaki kaynak URL, hedef dosya yolu ve transfer durumuna bakılır.
```

```
3. RDP Bitmap Cache Dosyaları
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Local\Microsoft\Terminal Server Client\Cache\*.bmc ve bcache*.bmc
MITRE: T1021.001
Gözlem Notu: RDP oturumlarından kalan bitmap tile'larında uzak masaüstü ekran görüntüsü kalıntılarına bakılır.
```

```
4. VPN Phonebook Dosyaları
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Roaming\Microsoft\Network\Connections\Pbk\rasphone.pbk ve C:\ProgramData\Microsoft\Network\Connections\Pbk\rasphone.pbk
MITRE: T1572
Gözlem Notu: VPN bağlantı profillerindeki sunucu adresi, protokol türü ve kimlik bilgilerine bakılır.
```

```
5. OpenSSH Known Hosts
Öncelik: Yüksek
Konum → C:\Users\<user>\.ssh\known_hosts
MITRE: T1021.004
Gözlem Notu: SSH ile bağlanılan sunucuların host key fingerprint'lerine ve IP/hostname bilgilerine bakılır.
```

```
6. OpenSSH Authorized Keys
Öncelik: Yüksek
Konum → C:\Users\<user>\.ssh\authorized_keys ve C:\ProgramData\ssh\administrators_authorized_keys
MITRE: T1098.004
Gözlem Notu: Yetkisiz eklenen public key'lere bakılır; saldırgan kalıcı SSH erişimi sağlamış olabilir.
```

```
7. TeamViewer Bağlantı Logları
Öncelik: Yüksek
Konum → C:\Program Files\TeamViewer\Connections_incoming.txt ve C:\Users\<user>\AppData\Roaming\TeamViewer\Connections.txt
MITRE: T1219
Gözlem Notu: Gelen ve giden bağlantıların partner ID, başlangıç/bitiş zamanı ve bağlantı türüne bakılır.
```

```
8. AnyDesk Bağlantı Logları
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Roaming\AnyDesk\ad.trace ve C:\ProgramData\AnyDesk\ad_svc.trace
MITRE: T1219
Gözlem Notu: AnyDesk bağlantı loglarındaki uzak ID, bağlantı zamanı ve dosya transfer kayıtlarına bakılır.
```

```
9. ngrok / Chisel / Ligolo Yapılandırma ve İzleri
Öncelik: Yüksek
Konum → Prefetch (ngrok.pf, chisel.pf); C:\Users\<user>\.ngrok2\ngrok.yml; Amcache
MITRE: T1572
Gözlem Notu: Tünel araçlarının Prefetch kaydı, yapılandırma dosyası ve Amcache girişlerine bakılır.
```

```
10. SRUM Ağ Kullanım Verileri
Öncelik: Yüksek
Konum → C:\Windows\System32\sru\SRUDB.dat → NetworkUsage ve NetworkConnections tabloları
MITRE: T1071
Gözlem Notu: Her uygulamanın byte bazında ağ kullanım miktarı ve bağlandığı ağ profil bilgilerine bakılır.
```

```
11. PowerShell Web İstek Geçmişi
Öncelik: Yüksek
Konum → PowerShell Operational Log → EID 4104; ConsoleHost_history.txt
MITRE: T1105
Gözlem Notu: Invoke-WebRequest, Invoke-RestMethod, DownloadString, DownloadFile komutlarının script block loglarındaki kaydına bakılır.
```

```
12. Kablosuz Ağ Profil Dosyaları
Öncelik: Yüksek
Konum → C:\ProgramData\Microsoft\Wlansvc\Profiles\Interfaces\{GUID}\*.xml
MITRE: T1016.001
Gözlem Notu: Kayıtlı WiFi profil XML dosyalarında SSID, şifreleme türü ve plaintext parola bilgilerine bakılır.
```

```
13. RDP Default.rdp Dosyası
Öncelik: Orta
Konum → C:\Users\<user>\Documents\Default.rdp
MITRE: T1021.001
Gözlem Notu: Varsayılan RDP bağlantı dosyasında kayıtlı sunucu adresi ve bağlantı ayarlarına bakılır.
```

```
14. OpenSSH Config
Öncelik: Orta
Konum → C:\Users\<user>\.ssh\config
MITRE: T1021.004
Gözlem Notu: SSH bağlantı kısayollarında tanımlı sunucu, port, kullanıcı ve proxy ayarlarına bakılır.
```

```
15. WinSCP INI Dosyası
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Roaming\WinSCP.ini veya C:\Program Files (x86)\WinSCP\WinSCP.ini
MITRE: T1021.004
Gözlem Notu: Kayıtlı oturumlardaki sunucu adresi, kullanıcı adı ve şifreli parola hash'lerine bakılır.
```

```
16. PuTTY Log Dosyaları
Öncelik: Orta
Konum → PuTTY session ayarlarında tanımlı log yolu (varsayılan: C:\Users\<user>\putty.log veya özel konum)
MITRE: T1021.004
Gözlem Notu: PuTTY oturum loglarının varlığına ve içeriğindeki komut geçmişine bakılır.
```

```
17. AnyDesk Yapılandırma ve ID
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Roaming\AnyDesk\system.conf ve C:\ProgramData\AnyDesk\system.conf
MITRE: T1219
Gözlem Notu: AnyDesk cihaz ID'si, şifre hash'i ve yapılandırma değişikliklerine bakılır.
```

```
18. Certutil URL Cache
Öncelik: Orta
Konum → C:\Users\<user>\AppData\LocalLow\Microsoft\CryptnetUrlCache\Content\ ve MetaData\
MITRE: T1105
Gözlem Notu: certutil -urlcache ile indirilen dosyaların cache'deki kalıntılarına bakılır.
```

```
19. curl / wget İndirme İzleri
Öncelik: Orta
Konum → Prefetch (curl.pf); ConsoleHost_history.txt; Amcache
MITRE: T1105
Gözlem Notu: Windows 10/11'de yerleşik curl.exe'nin Prefetch kaydına ve komut geçmişindeki URL'lere bakılır.
```

```
20. ETL Ağ Trace Dosyaları
Öncelik: Orta
Konum → C:\Windows\System32\LogFiles\WMI\*.etl ve netsh trace çıktıları
MITRE: T1071
Gözlem Notu: Sistemde çalıştırılmış ağ trace oturumlarının ETL dosyalarına bakılır.
```

```
21. LMHOSTS Dosyası
Öncelik: Düşük
Konum → C:\Windows\System32\drivers\etc\lmhosts.sam
MITRE: T1071
Gözlem Notu: NetBIOS ad çözümlemesi için eklenen elle tanımlı girdilere bakılır.
```

```
22. Windows Delivery Optimization Cache
Öncelik: Düşük
Konum → C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Microsoft\Windows\DeliveryOptimization\
MITRE: T1105
Gözlem Notu: Peer-to-peer güncelleme mekanizmasının suistimal edilip edilmediğine veya olağandışı dosya transfer izlerine bakılır.
```
