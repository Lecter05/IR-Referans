
```
1. $MFT Zaman Damgası Tutarsızlığı ($STANDARD_INFORMATION vs $FILE_NAME)
Öncelik: Yüksek
Konum → $MFT → her dosya kaydının $SI ve $FN attribute'ları
MITRE: T1070.006
Gözlem Notu: $STANDARD_INFORMATION zaman damgasının $FILE_NAME'den eski olması timestomping göstergesidir; $FN kullanıcı tarafından değiştirilemez.
```

```
2. $UsnJrnl ile Timestamp Karşılaştırma
Öncelik: Yüksek
Konum → $UsnJrnl:$J kayıtları ile $MFT zaman damgaları
MITRE: T1070.006
Gözlem Notu: USN journal'daki oluşturma zamanı ile $MFT'deki created time arasındaki tutarsızlığa bakılır.
```

```
3. Timestomp Araçları İzleri
Öncelik: Yüksek
Konum → Prefetch (timestomp.pf, nircmd.pf, powershell.pf); Amcache; $UsnJrnl
MITRE: T1070.006
Gözlem Notu: Bilinen timestomping araçlarının (timestomp, NirCmd, Set-ItemProperty) çalıştırılma izlerine bakılır.
```

```
4. $LogFile ile Timestamp Doğrulama
Öncelik: Orta
Konum → C:\$LogFile
MITRE: T1070.006
Gözlem Notu: NTFS transaction logundaki operasyon zamanları ile dosya zaman damgaları arasındaki uyumsuzluğa bakılır.
```

```
5. Nanosaniye Hassasiyet Anomalisi
Öncelik: Orta
Konum → $MFT → $STANDARD_INFORMATION zaman damgaları
MITRE: T1070.006
Gözlem Notu: Nanosaniye bileşeninin tamamen sıfır olması (00:00:00.0000000) veya tüm dosyaların aynı nanosaniye değerine sahip olması durumuna bakılır.
```

```
6. Mantıksız Zaman Sıralaması
Öncelik: Orta
Konum → $MFT → Created, Modified, Accessed, Entry Modified zaman damgaları
MITRE: T1070.006
Gözlem Notu: Bir dosyanın oluşturulma tarihinin değiştirilme tarihinden sonra olması gibi mantık dışı sıralamalara bakılır.
```

```
7. PE Header Compile Time ile Dosya Sistemi Uyumsuzluğu
Öncelik: Orta
Konum → PE dosyalarının TimeDateStamp alanı ile $MFT zaman damgası
MITRE: T1070.006
Gözlem Notu: Executable'ın compile timestamp'ının dosya oluşturma zamanından çok farklı olup olmadığına bakılır.
```
