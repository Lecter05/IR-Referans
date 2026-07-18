
```
1. BITS (Background Intelligent Transfer Service)
Öncelik: Yüksek
Konum → Microsoft-Windows-Bits-Client%4Operational.evtx
Gözlem Notu: BITS iş oluşturma (3), tamamlanma (4), iptal (5), hata (59, 60) olayları; BITS ile dosya indirme/yükleme (T1197) persistence ve data exfiltration mekanizması olarak kullanılabilir; URL ve dosya yolu loglanır.
```

```
2. Windows Firewall with Advanced Security
Öncelik: Orta
Konum → Microsoft-Windows-Windows Firewall With Advanced Security%4Firewall.evtx
Gözlem Notu: Kural ekleme (2004), kural silme (2006), kural değiştirme (2005), firewall profili değişikliği (2010); saldırgan tarafından eklenen izin kuralları aranır.
```

```
3. DNS Client Events (Varsayılan: Kapalı)
Öncelik: Orta
Konum → Microsoft-Windows-DNS-Client%4Operational.evtx
Gözlem Notu: DNS çözümleme istekleri (Event ID 3006, 3008, 3020) süreç bazlı DNS görünürlüğü sağlar; Sysmon 22 tercih edilir ama Sysmon yoksa alternatiftir.
```

```
4. NTLM Operational (Varsayılan: Kapalı)
Öncelik: Orta
Konum → Microsoft-Windows-NTLM%4Operational.evtx
Gözlem Notu: NTLM kimlik doğrulama olayları (8001, 8002, 8003, 8004) NTLM relay ve pass-the-hash saldırılarının korelasyonunda faydalıdır.
```

```
5. SMBClient / SMBServer (Varsayılan: Kapalı — Analytical kanal)
Öncelik: Orta
Konum → Microsoft-Windows-SmbClient%4Security.evtx ve SmbServer
Gözlem Notu: SMB oturum başarısızlıkları (31001), bağlantı hataları (30800, 30803, 30804), sunucu tarafında paylaşım erişimi olayları lateral movement izlerini destekler.
```

```
6. DNS Server Analytical (Yalnızca DNS sunucu rolü; Varsayılan: Kapalı)
Öncelik: Yüksek
Konum → Microsoft-Windows-DNSServer%4Analytical.evtx
Gözlem Notu: DNS sorgu/yanıt logları (256, 257, 258, 259) DNS tünelleme ve C2 tespitinde kritiktir; yüksek hacim nedeniyle disk alanı izlenmelidir.
```

```
7. Winsock / Network Profile
Öncelik: Düşük
Konum → Microsoft-Windows-NetworkProfile%4Operational.evtx
Gözlem Notu: Ağ profili değişiklikleri (10000, 10001) yeni ağ bağlantılarını ve ağ türü değişikliklerini (public/private/domain) gösterir; timeline oluşturmada yardımcıdır.
```

```
8. WLAN AutoConfig
Öncelik: Düşük
Konum → Microsoft-Windows-WLAN-AutoConfig%4Operational.evtx
Gözlem Notu: Wi-Fi bağlantı başarı (8001) ve başarısızlık (8002), bağlantı kesilme (8003) olayları; SSID ve BSSID bilgisi fiziksel konum korelasyonunda kullanılır.
```

