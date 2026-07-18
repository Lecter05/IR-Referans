### 1 · IP ve MAC Filtreleri
**Adrese Göre Filtreleme**
```
ip.addr == 192.168.1.5                # belirli IP'ye gelen/giden tüm trafik
ip.src == 10.0.0.1                    # sadece kaynak IP
ip.dst == 10.0.0.1                    # sadece hedef IP
ip.addr == 192.168.1.0/24             # belirli subnet
ip.addr == 10.0.0.5 && ip.addr == 203.0.113.10   # iki IP arası konuşma
```
**İç Ağ Dışına Çıkan Trafik**
```
!(ip.dst == 10.0.0.0/8 or ip.dst == 172.16.0.0/12 or ip.dst == 192.168.0.0/16)
```
**MAC Adresi Filtreleri**
```
eth.src == 00:11:22:33:44:55          # kaynak MAC adresi
eth.dst == aa:bb:cc:dd:ee:ff          # hedef MAC adresi
```

---

### 2 · Port ve Protokol Filtreleri
**Port Bazlı Filtreleme**
```
tcp.port == 443                       # belirli TCP portu
udp.port == 53                        # belirli UDP portu
tcp.port >= 1024 && tcp.port <= 65535 # port aralığı
```
**Protokole Göre Filtreleme**
```
dns          # sadece DNS
http         # sadece HTTP
tls          # sadece TLS/SSL
arp          # sadece ARP
icmp         # sadece ICMP
dhcp         # sadece DHCP
smb2         # sadece SMB
ftp          # sadece FTP
ssh          # sadece SSH
ntlmssp      # NTLMSSP (domain bilgisi)
kerberos     # Kerberos
```

---

### 3 · HTTP Analiz Filtreleri
**İstek / Yanıt Ayrımı**
```
http.request                              # tüm HTTP istekleri
http.response                             # tüm HTTP yanıtları
http.request.method == "POST"             # sadece POST istekleri
http.request.method == "GET"              # sadece GET istekleri
```
**Host, URL ve İçerik**
```
http.host contains "example.com"          # belirli bir host
http.request.uri contains "/login"        # belirli URL yolu
http.content_type contains "application/zip"   # dosya türüne göre
http.content_type contains "image"        # resim dosyaları
http.user_agent contains "Firefox"        # User-Agent ile
```
**Yanıt Kodlarına Göre**
```
http.response.code == 200                             # başarılı yanıtlar
http.response.code >= 300 && http.response.code < 400  # yönlendirmeler
http.response.code >= 400                              # hata yanıtları
http.response.code >= 500                               # sunucu hataları
```

---

### 4 · TCP Bayrak ve Durum Filtreleri
**Bağlantı Aşamaları**
```
tcp.flags.syn == 1 && tcp.flags.ack == 0   # SYN paketleri (bağlantı başlangıcı)
tcp.flags.syn == 1 && tcp.flags.ack == 1   # SYN-ACK paketleri
tcp.flags.reset == 1                       # RST paketleri (bağlantı reddi)
tcp.flags.fin == 1                         # FIN paketleri (bağlantı sonu)
```
**Akış ve Anomali Takibi**
```
tcp.stream eq 5                                       # belirli TCP stream
tcp.analysis.flags && !tcp.analysis.window_update      # TCP hata bayrakları
tcp.analysis.retransmission                            # yeniden iletim
tcp.analysis.zero_window                               # sıfır pencere
tcp.analysis.duplicate_ack                              # duplicate ACK
```

---

### 5 · Genel Operatörler
**Karşılaştırma Operatörleri**
```
==                     # eşittir        → ip.addr == 10.0.0.1
!=                     # eşit değil      → ip.addr != 10.0.0.1
>  <  >=  <=           # karşılaştırma   → frame.len > 1500
```
**Metin ve Regex Operatörleri**
```
contains               # içerir (metin)  → http.host contains "evil"
matches                # regex eşleşme   → dns.qry.name matches "^[a-z0-9]{20,}"
```
**Mantıksal Operatörler**
```
&&  veya  and          # VE      → ip.src == 10.0.0.1 && tcp.port == 80
||  veya  or           # VEYA    → dns || http
!   veya  not          # DEĞİL   → !arp && !dns
in                      # liste içinde → tcp.port in {80, 443, 8080}
```
**Serbest Metin Arama**
```
frame contains "password"    # tüm pakette metin ara
```

---

### 6 · TLS/SSL Şifre Çözme
HTTPS trafiğini okuyabilmek için tarayıcının oturum anahtarlarını kaydetmesi gerekir.

**SSLKEYLOGFILE Kurulumu — Windows**
```
:: Ortam değişkeni oluştur:
:: Sistem Özellikleri → Gelişmiş → Ortam Değişkenleri → Yeni
:: Değişken adı:    SSLKEYLOGFILE
:: Değişken değeri: C:\Users\KullaniciAdi\sslkeys.log

:: veya CMD ile geçici:
set SSLKEYLOGFILE=C:\temp\sslkeys.log
start chrome.exe
```
**SSLKEYLOGFILE Kurulumu — Linux / macOS**
```bash
export SSLKEYLOGFILE=~/sslkeys.log
# Tarayıcıyı aynı terminalden başlat:
google-chrome &
# veya
firefox &
```
**Wireshark Ayarı**
```
Edit → Preferences → Protocols → TLS
  → (Pre)-Master-Secret log filename: <sslkeys.log dosyasının yolu>
  → OK
```
**Doğrulama Filtreleri**
```
http2                                          # şifre çözme başarılıysa HTTP/2 çerçeveleri görünür
http                                           # veya klasik HTTP
tls.handshake                                  # TLS handshake'leri
http.host == "api.example.com"                 # belirli bir host'un çözülmüş trafiği
```
**tshark ile Komut Satırından Çözme**
```bash
tshark -r capture.pcap \
  -o "tls.keylog_file:/home/user/sslkeys.log" \
  -Y "http" \
  -T fields -e http.request.uri
```
> ⚠️ Anahtar dosyası oturum sırlarını içerir; güvenli sakla, işin bitince sil. Üretim ortamında asla etkinleştirme.

---

### 7 · İstatistik Araçları (Statistics Menüsü)
**Genel Bakış**
```
Statistics → Capture File Properties   # dosya süresi, toplam paket/bayt; ilk bakış için
Statistics → Protocol Hierarchy        # protokol dağılımı (%); alışılmadık protokol tespiti
Statistics → Resolved Addresses        # IP → hostname eşlemeleri; hızlı referans
```
**Trafik Hacmi ve Aktivite**
```
Statistics → Conversations → IPv4      # IP çiftleri arası trafik hacmi; C2 şüphesi analizi
Statistics → Endpoints → IPv4          # her IP'nin gönderdiği/aldığı bayt; en aktif host
Statistics → I/O Graphs                # zaman-paket grafiği; beacon ve spike analizi
```
**Protokole Özel İstatistikler**
```
Statistics → DNS                       # sorgu istatistikleri, yanıt süreleri; tünelleme/DGA
Statistics → HTTP → Requests           # ziyaret edilen URL'ler; zararlı indirme tespiti
Statistics → HTTP → Request Sequences  # HTTP istek sırası; saldırı zincirini görselleştirme
Statistics → Flow Graph                # paket akış diyagramı; handshake ve oturum analizi
```
**I/O Graph ile Beacon Tespiti**
```
Statistics → I/O Graphs
  → "+" ile yeni grafik ekle
  → Display Filter: ip.addr == <şüpheli_ip>
  → Interval: 1 saniye veya 10 saniye

# Grafik düzenli periyodik spike'lar gösteriyorsa → C2 beaconing olabilir
```

---

### 8 · Dosya Çıkarma (Export Objects)
**Export Objects Menüleri**
```
File → Export Objects → HTTP     # web üzerinden indirilen dosyalar (exe, zip, js, html, resim)
File → Export Objects → SMB      # ağ paylaşımı üzerinden aktarılan dosyalar
File → Export Objects → TFTP     # TFTP üzerinden aktarılan dosyalar
File → Export Objects → IMF      # e-posta ekleri
File → Export Objects → DICOM    # tıbbi görüntüler
```
> Çıkarılan dosyaları VirusTotal veya sandbox'ta analiz et. Doğrudan ana sistemde açma.

---

### 9 · Stream Takibi (Follow Stream)
**Sağ Tık → Follow Menüsü**
```
Follow → TCP Stream       # TCP konuşmasını kronolojik oku (HTTP içerik, login bilgileri)
Follow → UDP Stream       # UDP konuşmasını oku (DNS, TFTP)
Follow → TLS Stream       # şifresi çözülmüş TLS oturumunu oku
Follow → HTTP Stream      # HTTP istek-yanıt çiftini oku
Follow → HTTP/2 Stream    # HTTP/2 çerçevelerini oku
```
> Stream penceresinde kırmızı = istemciden sunucuya, mavi = sunucudan istemciye.

---

### 10 · Capture Filtreleri (Yakalama Öncesi)
Display filtrelerinden farklıdır; yakalama başlamadan önce uygulanır ve gereksiz trafiği diske yazmaz.

**Capture Filter Söz Dizimi (BPF)**
```
host 192.168.1.5                    # belirli host
net 192.168.1.0/24                  # belirli ağ
port 80                             # belirli port
portrange 1-1024                    # port aralığı
tcp                                 # sadece TCP
udp                                 # sadece UDP
not port 53                         # DNS hariç
not arp                             # ARP hariç
host 10.0.0.1 and host 10.0.0.2     # iki host arası
not broadcast                       # broadcast hariç
```
> Display filter söz dizimi (`ip.addr`) ile capture filter söz dizimi (`host`) farklıdır, karıştırma.

---

### 11 · tshark Komut Satırı Referansı
**Yakalama**
```bash
tshark -i eth0 -w output.pcap                    # canlı yakalama
tshark -i eth0 -f "port 80" -w http_traffic.pcap  # belirli filtre ile yakalama
```
**Okuma ve Filtreleme**
```bash
tshark -r capture.pcap -Y "http.request"                         # display filter uygulama
tshark -r capture.pcap -Y "dns" -T fields -e dns.qry.name -e ip.src   # belirli alanları çıkarma
tshark -r capture.pcap -Y "ip.addr == 10.0.0.5" -w filtered.pcap      # eşleşenleri ayrı dosyaya kaydet
```
**Liste ve Sayım Çıktıları**
```bash
tshark -r capture.pcap -Y "http.request" -T fields -e http.host | sort -u
tshark -r capture.pcap -Y "dns.qry.name" -T fields -e dns.qry.name | sort | uniq -c | sort -rn
tshark -r capture.pcap -Y "http.user_agent" -T fields -e http.user_agent | sort -u
```
**İstatistikler**
```bash
tshark -r capture.pcap -q -z conv,ip           # en çok konuşan IP çiftleri
tshark -r capture.pcap -q -z io,phs            # protocol hierarchy
tshark -r capture.pcap -q -z endpoints,ip      # endpoint istatistikleri
```
**TLS Çözümlü Okuma**
```bash
tshark -r capture.pcap -o "tls.keylog_file:sslkeys.log" -Y "http"
```

---

### 12 · Yararlı Ayarlar
**İsim Çözümleme**
```
Edit → Preferences → Name Resolution
  ☑ Resolve network (IP) addresses     # IP'leri hostname olarak gösterir
  ☑ Resolve transport names            # port numaralarını servis adı olarak gösterir
```
**Sütun Özelleştirme (Önerilen Ek Sütunlar)**
```
Edit → Preferences → Columns → "+" ile ekle:

Başlık                Tür         Alan
Source Port           Custom      tcp.srcport
Dest Port             Custom      tcp.dstport
HTTP Host             Custom      http.host
Server Name (SNI)     Custom      tls.handshake.extensions_server_name
DNS Query             Custom      dns.qry.name
```
**Renklendirme Kuralları**
```
View → Coloring Rules
  → Özel kurallar ekleyerek şüpheli trafiği renklendir
  # örnek: "Suspicious DNS" → dns.qry.name.len > 50 → arka plan: kırmızı
```

---

### 13 · Kısayol Tuşları
**Genel Kısayollar**
```
Ctrl+E              # yakalamayı başlat/durdur
Ctrl+F              # paket içinde arama
Ctrl+G              # belirli paket numarasına git
Ctrl+M              # paketi işaretle
Ctrl+Shift+M        # sonraki işaretli pakete git
Ctrl+→ / Ctrl+←      # sonraki/önceki pakete
Ctrl+. / Ctrl+,      # sonraki/önceki display filter sonucu
Ctrl+Shift+E        # Expert Information paneli
```

---

### 14 · Analiz Senaryoları (Hızlı Başvuru)
**Senaryo A — Bu Makine Enfekte mi?**
```
1. ip.addr == <şüpheli_IP> ile filtrele
2. Statistics → Protocol Hierarchy → alışılmadık protokoller var mı?
3. Statistics → Conversations → bu IP en çok kimle konuşuyor?
4. dns.qry.name ile bu IP'den çıkan DNS sorgularına bak
5. http.request ile HTTP isteklerini incele
   → garip URL'ler, şüpheli User-Agent, encoded payload
6. Statistics → I/O Graphs → düzenli beaconing deseni var mı?
7. File → Export Objects → HTTP → indirilen dosyaları çıkar, hash'le, VirusTotal'e gönder
```
**Senaryo B — Veri Sızdırılmış mı?**
```
1. Statistics → Endpoints → en çok veri gönderen iç IP hangisi?
2. Statistics → Conversations → dışarıya en çok bayt gönderen konuşma?
3. http.request.method == "POST" && http.content_length > 5000
4. dns.qry.name.len > 50                    # DNS exfiltration kontrolü
5. ftp-data || smb2.cmd == 5                # dosya transfer protokolleri
6. Follow TCP Stream → gönderilen verinin içeriğini oku
```
**Senaryo C — Ağda Port Taraması Yapan Var mı?**
```
1. tcp.flags.syn == 1 && tcp.flags.ack == 0 ile SYN'leri filtrele
2. Statistics → Endpoints → en çok SYN gönderen IP?
3. Statistics → Conversations → aynı kaynak IP kaç farklı hedef porta SYN gönderiyor?
4. tcp.flags.reset == 1 ile RST yanıtlarını kontrol et (kapalı portlar)
5. icmp.type == 3 && icmp.code == 3         # port unreachable mesajları
```
**Senaryo D — Kimlik Bilgisi Çalınmış mı?**
```
1. frame contains "password"
2. frame contains "login"
3. frame contains "user"
4. http.request.method == "POST" → Follow HTTP Stream
5. ftp.request.command == "USER" || ftp.request.command == "PASS"
6. smtp.req.command == "AUTH"
7. http.authbasic                            # Basic auth header bilgisi
```

---

### 15 · Sık Kullanılan Birleşik Filtreler
**Gürültüyü Temizle** — analiz başlangıcı için
```
!(arp || dns || stp || cdp || lldp || igmp || icmpv6)
```
**Web Trafiği ve Gizli Kanal**
```
http || tls                                                              # sadece web trafiği
ip.src == 192.168.0.0/16 && !(ip.dst == 192.168.0.0/16) && !dns && !http && !tls
                                                                            # gizli kanal tespiti
```
**Bağlantı ve Paket Boyutu Anomalileri**
```
tcp.flags.syn == 1 && tcp.flags.ack == 0 && tcp.analysis.retransmission   # başarısız bağlantı denemeleri
frame.len > 1500                                                          # büyük paketler (exfiltration/dosya transferi)
frame.len < 100 && tcp                                                    # küçük ve sık paketler (C2 beacon)
```
**Şifreli Olmayan Kimlik Bilgisi Protokolleri**
```
ftp || telnet || http.authbasic || smtp
```

---

### 16 · Wireshark Expert Information Yorumlama
Sol alt köşedeki renkli daire (sarı/kırmızı) Expert Information'a erişim sağlar: `Analyze → Expert Information`

**Önem Seviyeleri**
```
Chat        Mavi         # bilgilendirme (normal akış)
Note        Açık mavi    # dikkat çekici ama muhtemelen normal
Warning     Sarı         # potansiyel sorun (retransmission, out-of-order)
Error       Kırmızı      # kesin hata (malformed paket, checksum hatası)
```
**Sık Karşılaşılan Uyarılar**
```
TCP Retransmission                  # paket kayboldu, yeniden gönderildi → ağ sorunu/tıkanıklık
TCP Out-Of-Order                    # paketler sırasız geldi
TCP Duplicate ACK                   # kayıp paket için tekrar ACK → hızlı yeniden iletimi tetikleyebilir
TCP Zero Window                     # alıcı buffer doldu, veri kabul edemez
TCP RST                             # bağlantı zorla kesildi
TCP Previous Segment Not Captured   # yakalama sırasında paket kaçırıldı
```
