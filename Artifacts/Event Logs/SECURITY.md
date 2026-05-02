
```
1. Security Log — Logon Events (Detay)
Öncelik: Yüksek
Konum → %SystemRoot%\System32\winevt\Logs\Security.evtx
Gözlem Notu: 4624'te LogonType alanı kritiktir (Type 2=Interactive, 3=Network, 7=Unlock, 10=RemoteInteractive/RDP, 11=CachedInteractive); 4648 explicit credentials ile oturum açmayı, 4672 yönetici token atanmasını gösterir.
```

```
2. Security Log — Ana Olay Kaydı
Öncelik: Yüksek
Konum → %SystemRoot%\System32\winevt\Logs\Security.evtx
Gözlem Notu: Başarılı/başarısız oturum açma (4624, 4625), hesap oluşturma (4720), grup üyeliği değişikliği (4728, 4732, 4756), parola sıfırlama (4724), oturum kapatma (4634, 4647), kimlik doğrulama paketi (4776), Kerberos TGT/TGS (4768, 4769, 4771), denetim politikası değişikliği (4719), güvenlik günlüğü temizleme (1102) izlenir.
```

```
3. Security — Process Tracking
Öncelik: Yüksek
Konum → Security.evtx
Gözlem Notu: Yeni süreç oluşturma (4688) ve komut satırı kaydı (4688 + CommandLine audit policy etkinse), süreç sonlandırma (4689) incelenir; 4688'de ParentProcessName alanı Win10 1703+ sürümlerde mevcuttur.
```

```
4. Security — Account Management
Öncelik: Yüksek
Konum → Security.evtx
Gözlem Notu: Yerel hesap oluşturma/silme (4720, 4726), grup ekleme (4732, 4728, 4756), hesap etkinleştirme/devre dışı bırakma (4722, 4725), bilgisayar hesabı değişikliği (4741, 4742, 4743) takip edilir.
```

```
5. Security — Policy & Audit Changes
Öncelik: Yüksek
Konum → Security.evtx
Gözlem Notu: Denetim ilkesi değişikliği (4719) saldırganın iz silme girişimine (T1562.002), güvenlik günlüğü temizleme (1102) log tampering'e (T1070.001) işaret eder.
```

```
6. Security — Scheduled Task Events
Öncelik: Yüksek
Konum → Security.evtx
Gözlem Notu: Zamanlanmış görev kaydı (4698), güncellenmesi (4702), silinmesi (4699) persistence mekanizmasına (T1053.005) işaret eder; görev XML içeriği 4698 içinde yer alır.
```

```
7. Security — Object Access & File Auditing
Öncelik: Orta
Konum → Security.evtx
Gözlem Notu: Dosya erişimi (4663), dosya silme (4660), kayıt defteri erişimi (4657), paylaşım erişimi (5140, 5145), çıkarılabilir medya (4663 + Removable Storage SACL) olaylarına bakılır; SACL yapılandırılmadıysa bu olaylar üretilmez.
```

```
8. Security — Windows Firewall Rule Changes
Öncelik: Orta
Konum → Security.evtx
Gözlem Notu: Firewall kuralı ekleme (4946), değiştirme (4947), silme (4948), firewall kapatma (4950) olayları ağ savunmasının zayıflatılmasına işaret edebilir.
```
