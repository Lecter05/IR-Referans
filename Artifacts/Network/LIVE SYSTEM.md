
```
1. DNS Cache (ipconfig /displaydns)
Öncelik: Yüksek
Erişim: Live System
Konum → ipconfig /displaydns çıktısı (volatile; sadece live system)
MITRE: T1071.004
Gözlem Notu: Çözümlenmiş DNS kayıtlarında C2 domain'leri veya olağandışı TLD'lere (.xyz, .top, .tk) bakılır.
```

```
2. NetBIOS / SMB Oturumları
Öncelik: Yüksek
Erişim: Live System
Konum → net session, net use, net view çıktıları (volatile)
MITRE: T1021.002
Gözlem Notu: Aktif SMB oturumları, bağlı paylaşımlar ve açık dosyalara bakılır.
```

```
3. Aktif Ağ Bağlantıları (netstat)
Öncelik: Yüksek
Erişim: Live System
Konum → netstat -anob çıktısı (volatile)
MITRE: T1071
Gözlem Notu: Dinleyen portlar, kurulan bağlantılar ve bunları oluşturan process'lere bakılır.
```

```
4. ARP Cache
Öncelik: Orta
Erişim: Live System
Konum → arp -a çıktısı (volatile; sadece live system)
MITRE: T1016
Gözlem Notu: ARP tablosundaki IP-MAC eşleşmelerinde olağandışı veya çakışan girdilere bakılır.
```
