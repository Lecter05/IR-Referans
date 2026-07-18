
```
1. Sysmon — Process Creation (Event ID 1)
Öncelik: Yüksek
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: ParentImage, CommandLine, User, IntegrityLevel, Hashes alanları; LOLBin kullanımı, komut satırı parametreleri ve parent-child ilişkileri analiz edilir.
```

```
2. Sysmon — Network Connection (Event ID 3)
Öncelik: Yüksek
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: Kaynak/hedef IP, port, süreç bilgisi; C2 trafiği, lateral movement ve data exfiltration tespitinde kritiktir.
```

```
3. Sysmon — Process Access / LSASS (Event ID 10)
Öncelik: Yüksek
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: TargetImage olarak lsass.exe'ye erişim credential dumping'e (T1003.001) işaret eder; GrantedAccess maskesi (0x1010, 0x1FFFFF) analiz edilir.
```

```
4. Sysmon — Registry Events (Event ID 12, 13, 14)
Öncelik: Yüksek
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: Run/RunOnce, Services, Image File Execution Options gibi persistence noktalarındaki registry değişiklikleri izlenir (T1546, T1543).
```

```
5. Sysmon — Process Tampering (Event ID 25)
Öncelik: Yüksek
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: Process hollowing, herpaderping, doppelgänging gibi image tampering tekniklerini tespit eder.
```

```
6. Sysmon — Tüm Olaylar (Genel Bakış)
Öncelik: Yüksek
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: Süreç oluşturma (1), dosya oluşturma zamanı değişikliği (2), ağ bağlantısı (3), servis durumu (4), süreç sonlandırma (5), sürücü yükleme (6), görüntü yükleme (7), CreateRemoteThread (8), RawAccessRead (9), ProcessAccess (10), dosya oluşturma (11), registry (12-14), dosya stream (15), yapılandırma (16), named pipe (17-18), WMI (19-21), DNS (22), dosya silme (23, 26), clipboard (24), tampering (25), block executable (27), file executable (29) incelenir.
```

```
7. Sysmon — DNS Query (Event ID 22)
Öncelik: Orta
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: Süreç bazlı DNS sorguları kaydedilir; C2 domain çözümleme, DNS tünelleme ve DGA tespitinde kullanılır.
```

```
8. Sysmon — File Delete (Event ID 23, 26)
Öncelik: Orta
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: Silinen dosyaların hash ve yol bilgisi; Event ID 23 arşivlenen kopyayı (DeletedFiles klasörü) tutar, 26 yalnızca log kaydı oluşturur.
```

```
9. Sysmon — File Block Executable (Event ID 27)
Öncelik: Orta
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: Yapılandırmaya göre belirli dizinlere yazılan çalıştırılabilir dosyaların engellenmesini gösterir; dropper tespiti için faydalıdır.
```

```
10. Sysmon — Clipboard Capture (Event ID 24) (Varsayılan: Kapalı)
Öncelik: Düşük
Konum → Microsoft-Windows-Sysmon%4Operational.evtx
Gözlem Notu: Clipboard değişikliklerini ve içeriğinin hash'ini kaydeder; veri sızıntısı senaryolarında yardımcı olabilir.
```
