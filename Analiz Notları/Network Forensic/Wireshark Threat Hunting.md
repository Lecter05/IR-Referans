### 1 · Port Tarama ve Ağ Keşfi
**Standart SYN Taraması** — çok sayıda SYN, az SYN-ACK
```
tcp.flags.syn == 1 && tcp.flags.ack == 0
```
**Gizli Tarama Varyantları (IDS Atlatma)** — NULL, XMAS, FIN taramaları
```
tcp.flags == 0x000
tcp.flags.fin == 1 && tcp.flags.push == 1 && tcp.flags.urg == 1
tcp.flags.fin == 1 && tcp.flags.ack == 0 && tcp.flags.syn == 0
```
**Kapalı Port Yanıtları** — hızlı RST cevapları
```
tcp.flags.reset == 1 && tcp.flags.ack == 1
```
**ARP ve ICMP Keşif** — ağ haritalama denemeleri
```
arp.opcode == 1
icmp.type == 8
```
> **GUI ipucu:** `Statistics → Conversations → TCP` üzerinden "Port B" sütununa göre sıralayarak tek kaynaktan çok sayıda farklı porta bağlantı denemesi olup olmadığını kontrol et.

---

### 2 · C2 (Komuta-Kontrol) Tespiti
**Beaconing Tespiti** — düzenli aralıklı sinyal kalıpları
```
Statistics → Conversations → IPv4 → sütuna göre sırala
Statistics → I/O Graphs → ip.addr == <şüpheli_ip>
```
**C2 İşaret Filtreleri** — küçük pencereli SYN, standart dışı portta HTTP, uzun süreli bağlantılar
```
tcp.flags.syn == 1 && tcp.flags.ack == 0 && tcp.window_size <= 1024
http && !(tcp.port == 80 || tcp.port == 443 || tcp.port == 8080)
tls.handshake.type == 1 && !(ip.dst == 10.0.0.0/8 || ip.dst == 172.16.0.0/12 || ip.dst == 192.168.0.0/16)
tcp.time_delta > 3600
```

---

### 3 · TLS/SSL & Sertifika Analizi (Şifreli C2 Avı)
**Sertifika ve SNI Analizi** — self-signed sertifika ve şüpheli hostname
```
tls.handshake.type == 11
tls.handshake.extensions_server_name
tls.handshake.extensions_server_name contains ".xyz"
tls.handshake.extensions_server_name matches "[a-z0-9]{20,}\\."
```
**JA3 / JA4 Parmak İzi** — bilinen malware imzasıyla eşleştirme
```
tls.handshake.ja3
tls.handshake.ja3s
tls.handshake.ja4
tls.handshake.ja3 == "<bilinen_kotucul_ja3_hash>"
```
**Zayıf / Eski TLS Sürümü** — SSLv3, TLS 1.0
```
tls.handshake.version == 0x0300
tls.handshake.version == 0x0301
```
**ALPN ve Sertifika Alanları**
```
tls.handshake.extensions_alpn_str
x509sat.printableString
x509sat.uTF8String
x509ce.dNSName
```
> **GUI ipucu:** Sertifika paketinde `Issuer` ile `Subject` (CN) aynıysa self-signed'dır. `Edit → Preferences → Protocols → TLS` altına anahtar log dosyası verirsen trafiği çözebilirsin.

---

### 4 · DNS Anomali ve Tünelleme Tespiti
**Başarısız / Şüpheli Sorgular** — DGA ve NXDOMAIN belirtileri
```
dns
dns.flags.rcode == 3
dns.flags.rcode != 0
```
**Tünelleme Belirtileri** — uzun sorgular, TXT/NULL kayıtlar, base32/64 subdomain
```
dns.qry.name.len > 50
dns.qry.type == 16
dns.qry.type == 10
dns.qry.name matches "[A-Za-z0-9]{30,}"
dns.len > 200
```
**Şüpheli TLD ve Anahtar Kelimeler**
```
dns.qry.name contains ".xyz"
dns.qry.name contains ".top"
dns.qry.name contains ".tk"
dns.qry.name contains ".cc"
dns.qry.name contains ".pw"
dns.qry.name contains "update"
dns.qry.name contains "cdn"
dns.qry.name contains "api"
```
**DNS Hijack Kontrolü ve DoH Atlatma**
```
dns && ip.dst != <iç_dns_sunucusu>
tls.handshake.extensions_server_name contains "dns.google"
tls.handshake.extensions_server_name contains "cloudflare-dns"
tls.handshake.extensions_server_name contains "doh"
```
> **DNS Analiz İpucu:** `Statistics → DNS` menüsünden sorgu istatistiklerine bak. Ortalama sorgu uzunluğu 20-30 karakter olmalı; 50+ karakter tünelleme belirtisi.

---

### 5 · Veri Sızdırma (Data Exfiltration) Tespiti
**Protokol Bazlı Büyük Veri Transferleri**
```
http.request.method == "POST" && http.content_length > 5000
dns.len > 200
icmp && data.len > 64
ftp-data && !(ip.dst == 10.0.0.0/8 || ip.dst == 172.16.0.0/12 || ip.dst == 192.168.0.0/16)
```
**Standart Dışı Şifreli Trafik ve SMB Transferi**
```
tls && !(tcp.port in {443, 993, 995, 587, 465})
smb2.cmd == 5
```

---

### 6 · Tünelleme & Gizli Kanallar
**Katman/Protokol Tünelleri** — GRE, IP-in-IP, Teredo
```
gre
ip.proto == 4
ip.proto == 41
teredo
```
**Israrlı ICMP Kalıbı** — boyuttan bağımsız süreklilik örüntüsü
```
icmp.type == 8 && ip.dst == <supheli_dis_ip>
```

---

### 7 · Şüpheli User-Agent Tespiti
**Script Tabanlı Erişimler ve Saldırgan Araçları**
```
http.user_agent contains "curl"
http.user_agent contains "wget"
http.user_agent contains "python"
http.user_agent contains "powershell"
http.user_agent contains "Go-http-client"
http.user_agent contains "Java/"
```
**Bot/Crawler ve Boş User-Agent**
```
http.user_agent contains "scanner"
http.user_agent contains "nikto"
http.user_agent contains "sqlmap"
http.user_agent contains "nmap"
http.user_agent contains "masscan"
http.user_agent contains "dirbuster"
http.user_agent == ""
```

---

### 8 · Web Saldırı Tespiti (SQLi, XSS, RCE ve Ötesi)
**SQL Injection / XSS**
```
http.request.uri contains "SELECT"
http.request.uri contains "UNION"
http.request.uri contains "DROP"
http.request.uri contains "' OR "
http.request.uri contains "1=1"
http.request.uri contains "<script>"
http.request.uri contains "alert("
```
**Dizin Gezinme ve Dosya Dahil Etme (LFI/RFI)**
```
http.request.uri contains "../"
http.request.uri contains "/etc/passwd"
http.request.uri contains "php://"
http.request.uri contains "file://"
http.request.uri contains "data://"
http.request.uri contains "boot.ini"
http.request.uri contains "win.ini"
```
**Log4Shell / JNDI ve Komut Enjeksiyonu**
```
frame contains "jndi:"
frame contains "jndi:ldap"
http contains "${jndi"
http.request.uri contains ";cmd"
http.request.uri contains "|bash"
http.request.uri contains "powershell"
http.request.uri contains "/bin/sh"
```
**Zararlı Dosya İndirme**
```
http.request.uri matches "(?i)\\.(exe|dll|scr|ps1|bat|hta|jar|vbs)$"
http.content_type contains "application/x-msdownload"
http.content_type contains "application/x-dosexec"
```
**Şüpheli Metotlar, Hata Yığınları ve XXE**
```
http.request.method == "PUT"
http.request.method == "DELETE"
http.request.method == "TRACE"
http.request.method == "CONNECT"
http.response.code == 401
http.response.code == 403
http.response.code == 404
http.response.code == 500
http.authorization contains "Basic"
http contains "<!ENTITY"
```
> **GUI ipucu:** 404 yığını görürsen `Statistics → HTTP → Requests` ile hangi yolların tarandığını çıkar. Bilinen webshell adları için `http.request.uri contains "shell"` ile hızlı süz.

---

### 9 · Kerberos Saldırıları (Active Directory)
**Mesaj Tipleri ve Akış Takibi**
```
kerberos.msg_type == 10   # AS-REQ
kerberos.msg_type == 11   # AS-REP
kerberos.msg_type == 12   # TGS-REQ
kerberos.msg_type == 13   # TGS-REP
kerberos.msg_type == 30   # KRB-ERROR
```
**Kerberoasting ve AS-REP Roasting** — RC4 (etype 23) ile bilet talebi
```
kerberos.msg_type == 13 && kerberos.etype == 23
kerberos.msg_type == 11 && kerberos.etype == 23
```
**Zayıf Şifreleme ve SPN Hasadı**
```
kerberos.etype == 23
kerberos.etype == 1 || kerberos.etype == 3
kerberos.msg_type == 13 && !(kerberos.SNameString == "krbtgt")
```
**Hedefli Sorgular**
```
kerberos.CNameString == "<kullanici>"
kerberos.SNameString contains "MSSQL"
```
> **GUI ipucu:** Bilet talepleri normalde AES (17/18) olmalı. RC4 (23) görürsen o hesabı incele. Port 88'de tek kaynaktan çok sayıda TGS-REQ toplu Kerberoasting işaretidir.

---

### 10 · NTLM Kimlik Doğrulama & Lateral Movement
**NTLM El Sıkışma Adımları**
```
ntlmssp
ntlmssp.messagetype == 0x00000001   # NEGOTIATE
ntlmssp.messagetype == 0x00000002   # CHALLENGE
ntlmssp.messagetype == 0x00000003   # AUTHENTICATE
```
**Kullanıcı / Domain / Hash Çıkarma**
```
ntlmssp.auth.username
ntlmssp.auth.domain
ntlmssp.auth.hostname
ntlmssp.auth.ntresponse
```
**SMB Üzerinden Lateral Movement**
```
smb2.cmd == 3 && (smb2.tree contains "ADMIN$" || smb2.tree contains "IPC$" || smb2.tree contains "C$")
smb2.filename contains "PSEXESVC"
smb2.filename contains "PAExec"
smb2.filename contains ".exe" && smb2.filename contains "svc"
```
**Named Pipes ve DCE/RPC**
```
smb2.filename == "svcctl"
smb2.filename == "atsvc"
smb2.filename == "winreg"
smb2.filename == "samr"
smb2.filename == "lsarpc"
dcerpc
```
**DCSync Avı**
```
drsuapi
```
> **GUI ipucu:** DC olmayan bir host `drsuapi` çağrısı yapıyorsa DCSync olabilir. `File → Export Objects → SMB` ile `PSEXESVC.exe` gibi dosyaları çıkarabilirsin.

---

### 11 · Açık Metin Kimlik Bilgisi Yakalama
**FTP / Telnet**
```
ftp.request.command == "USER" || ftp.request.command == "PASS"
ftp.response.code == 530
telnet
```
**POP3 / IMAP / SMTP**
```
pop.request.command == "USER" || pop.request.command == "PASS"
imap.request contains "LOGIN"
smtp.req.command == "AUTH"
```
**LDAP ve SNMP**
```
ldap.protocolOp == 0
snmp.community
```
> **GUI ipucu:** `Tools → Credentials` (Wireshark 3.1+) FTP/HTTP/IMAP/POP/SMTP için yakalanan kimlik bilgilerini tek pencerede listeler; tıklayınca ilgili pakete atlar.

---

### 12 · Brute Force & Parola Saldırıları
**SSH / RDP Bağlantı Yığınları**
```
ssh
tcp.port == 22 && tcp.flags.syn == 1 && tcp.flags.ack == 0
tcp.port == 3389 && tcp.flags.syn == 1 && tcp.flags.ack == 0
cotp
```
**Kerberos Spraying ve Servis Başarısız Girişleri**
```
kerberos.msg_type == 30
ftp.response.code == 530
http.response.code == 401
```
> **GUI ipucu:** `Statistics → Conversations → TCP` içinde **Packets/Duration** kolonuna göre sırala; tek kaynaktan aynı porta çok sayıda kısa bağlantı brute force işaretidir.

---

### 13 · ARP Zehirleme / MITM
**Gratuitous Reply ve Çakışan IP Tespiti**
```
arp.opcode == 2
arp.duplicate-address-detected
arp.duplicate-address-frame
```
> **GUI ipucu:** `Analyze → Expert Information` içinde "duplicate use of ... detected" uyarısı ARP spoofing'in en net göstergesidir. Tek bir MAC'in birçok IP'yi sahiplenmesine dikkat et.

---

### 14 · DHCP Saldırıları
**Starvation ve Rogue Sunucu Tespiti**
```
dhcp
dhcp.option.dhcp == 1   # DISCOVER
dhcp.option.dhcp == 2   # OFFER
dhcp.option.dhcp == 3   # REQUEST
dhcp.option.dhcp == 5   # ACK
```
> **GUI ipucu:** `Statistics → Endpoints → Ethernet` ile kısa sürede çok sayıda benzersiz MAC = starvation. Birden fazla farklı IP'den OFFER geliyorsa rogue sunucu var.

---

### 15 · TCP / Protokol Anomalileri
**Wireshark Analiz Bayrakları**
```
tcp.analysis.flags
tcp.analysis.retransmission
tcp.analysis.zero_window
tcp.analysis.duplicate_ack
malformed
```
> **GUI ipucu:** `Analyze → Expert Information` tüm anomalileri (retransmission, malformed, checksum) severity'ye göre gruplar. NULL/XMAS/FIN taramaları (bkz. Bölüm 1) IDS atlatma amaçlıdır.

---

### 16 · Wireshark GUI'ye Özel Tehdit Avı Teknikleri
**Menü ve Araç Kısayolları**
```
Statistics → Protocol Hierarchy
Statistics → Conversations → sort by Bytes/Duration
Statistics → Endpoints (Map sekmesi / GeoIP)
File → Export Objects → HTTP / SMB / TFTP / IMF
Follow → TCP / HTTP / TLS Stream
Tools → Credentials
View → Coloring Rules
```
**Faydalı Kolonlar** — sağ tık → Column Preferences
```
tls.handshake.extensions_server_name
tls.handshake.ja3
http.host
dns.qry.name
```
