
```
1. Grup İlkesi Registry Verileri
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Policies\
Gözlem Notu: Uygulanan tüm bilgisayar tabanlı grup ilkesi ayarlarının kayıt defterindeki yansımasıdır.
```

```
2. Yerel GPO Dosyaları
Öncelik: Yüksek
Konum → C:\Windows\System32\GroupPolicy\
Gözlem Notu: Machine\Registry.pol ve User\Registry.pol dosyaları yerel grup ilkesi tanımlarını içerir.
```

```
3. GP Scripts (Startup/Shutdown)
Öncelik: Yüksek
Konum → C:\Windows\System32\GroupPolicy\Machine\Scripts\
Gözlem Notu: Grup İlkesi aracılığıyla başlangıç ve kapanışta çalıştırılan script dosyalarının bulunduğu dizindir.
```

```
4. GP Scripts (Logon/Logoff)
Öncelik: Yüksek
Konum → C:\Windows\System32\GroupPolicy\User\Scripts\
Gözlem Notu: Oturum açma ve kapama sırasında çalıştırılacak script dosyalarını içerir.
```

```
5. Audit Policy Yapılandırması
Öncelik: Yüksek
Konum → C:\Windows\System32\GroupPolicy\Machine\Microsoft\Windows NT\Audit\audit.csv
Gözlem Notu: Denetim politikasının detaylı alt kategori ayarlarını tanımlar; devre dışı bırakılmış denetim kategorileri T1562 göstergesidir.
```

```
6. Kullanıcı Grup İlkesi
Öncelik: Orta
Konum → HKCU\SOFTWARE\Policies\
Gözlem Notu: Kullanıcı tabanlı grup ilkesi ayarlarının kayıt defterindeki yansımasıdır.
```

```
7. GPO Geçmişi ve Önbelleği
Öncelik: Orta
Konum → C:\ProgramData\Microsoft\Group Policy\History\
Gözlem Notu: Domain ortamında uygulanan GPO'ların yerel önbellek kopyalarını ve script dosyalarını saklar.
```

```
8. RSoP (Resultant Set of Policy)
Öncelik: Orta
Erişim: Live System
Konum → gpresult /H çıktısı veya HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Group Policy\
Gözlem Notu: Sisteme uygulanmış tüm ilkelerin bileşik sonucunu ve kaynak GPO bilgisini gösterir.
```

```
9. AppLocker / SRP Politikaları
Öncelik: Orta
Konum → C:\Windows\System32\AppLocker\ veya HKLM\SOFTWARE\Policies\Microsoft\Windows\SrpV2\
Gözlem Notu: Uygulama kısıtlama politikalarının yapılandırmasını ve kurallarını içerir.
```

```
10. Security Templates
Öncelik: Düşük
Konum → C:\Windows\Security\Database\ ve C:\Windows\Security\Templates\
Gözlem Notu: Uygulanan güvenlik şablonları ve secedit veritabanı dosyasını (secedit.sdb) içerir.
```

