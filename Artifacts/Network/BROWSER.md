
```
1. Chrome Tarama Geçmişi
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\History (SQLite)
MITRE: T1071.001
Gözlem Notu: urls ve visits tablolarında ziyaret edilen URL'ler, zaman damgaları ve ziyaret sayısına bakılır.
```

```
2. Chrome İndirme Geçmişi
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\History → downloads tablosu
MITRE: T1105
Gözlem Notu: İndirilen dosyaların URL'si, hedef yolu, boyutu ve indirme zamanına bakılır.
```

```
3. Edge (Chromium) Tarama Geçmişi
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Local\Microsoft\Edge\User Data\Default\History (SQLite)
MITRE: T1071.001
Gözlem Notu: Edge tarama geçmişindeki URL'ler ve zaman damgalarına bakılır.
```

```
4. Edge İndirme Geçmişi
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Local\Microsoft\Edge\User Data\Default\History → downloads tablosu
MITRE: T1105
Gözlem Notu: Edge üzerinden indirilen dosyaların kaynak URL ve hedef yoluna bakılır.
```

```
5. Firefox Tarama Geçmişi
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Roaming\Mozilla\Firefox\Profiles\<profile>\places.sqlite
MITRE: T1071.001
Gözlem Notu: moz_places ve moz_historyvisits tablolarında ziyaret edilen URL ve zaman bilgilerine bakılır.
```

```
6. Firefox İndirme Geçmişi
Öncelik: Yüksek
Konum → C:\Users\<user>\AppData\Roaming\Mozilla\Firefox\Profiles\<profile>\places.sqlite → moz_annos tablosu
MITRE: T1105
Gözlem Notu: Firefox üzerinden indirilen dosyaların kaynak URL ve hedef dosya yoluna bakılır.
```

```
7. Zone.Identifier (MOTW) Stream
Öncelik: Yüksek
Konum → İndirilen dosyaların ADS'indeki Zone.Identifier
MITRE: T1105
Gözlem Notu: İndirme kaynağı URL'si (ReferrerUrl), host (HostUrl) ve güvenlik bölgesi (ZoneId) bilgilerine bakılır.
```

```
8. Chrome Cache / Cookies
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\Cache\ ve Cookies (SQLite)
MITRE: T1071.001
Gözlem Notu: Cache'deki dosyalarda ve cookie veritabanında C2 veya exfiltration domain bilgilerine bakılır.
```

```
9. Chrome Saved Passwords / Autofill
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\Login Data ve Web Data (SQLite)
MITRE: T1555.003
Gözlem Notu: Kayıtlı parolaların ve otomatik doldurulan form verilerinin saldırgan tarafından erişilip erişilmediğine bakılır.
```

```
10. Firefox Cookies / Form Data
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Roaming\Mozilla\Firefox\Profiles\<profile>\cookies.sqlite ve formhistory.sqlite
MITRE: T1071.001
Gözlem Notu: Cookie ve form verilerinde şüpheli domain veya veri sızıntısı göstergelerine bakılır.
```

```
11. WebCache (IE / Edge Legacy)
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Local\Microsoft\Windows\WebCache\WebCacheV01.dat (ESE veritabanı)
MITRE: T1071.001
Gözlem Notu: Internet Explorer ve eski Edge'in tarama/indirme/cookie geçmişinin tamamına bakılır.
```
