
```
1. BSOD Memory Dump (Full)
Öncelik: Yüksek
Konum → C:\Windows\MEMORY.DMP
Gözlem Notu: Mavi ekran sırasındaki tüm fiziksel bellek dökümüdür; rootkit veya kernel exploit analizi için kullanılır.
```

```
2. BSOD Minidump
Öncelik: Yüksek
Konum → C:\Windows\Minidump\*.dmp
Gözlem Notu: Her mavi ekran olayı için oluşturulan küçük döküm dosyasıdır; hata kodu, sürücü ve stack trace bilgisini içerir.
```

```
3. WER ReportQueue
Öncelik: Orta
Konum → C:\ProgramData\Microsoft\Windows\WER\ReportQueue\
Gözlem Notu: Henüz Microsoft'a gönderilmemiş bekleyen hata raporlarının detaylı dosyalarını (Report.wer, minidump) içerir.
```

```
4. WER ReportArchive
Öncelik: Orta
Konum → C:\ProgramData\Microsoft\Windows\WER\ReportArchive\
Gözlem Notu: Gönderilmiş veya arşivlenmiş hata raporlarını saklar; geçmişe dönük crash analizi için kullanılır.
```

```
5. Application Crash Dump
Öncelik: Orta
Konum → C:\Users\<Kullanıcı>\AppData\Local\CrashDumps\
Gözlem Notu: WerFault tarafından oluşturulan uygulama düzeyinde döküm dosyalarıdır; exploit denemesine dair kanıt içerebilir.
```

```
6. LiveKernelReports
Öncelik: Orta
Konum → C:\Windows\LiveKernelReports\
Gözlem Notu: BSOD'ye yol açmadan oluşan kernel hata raporlarını içerir; sürücü sorunlarını ve kısmi kernel çökmelerini kaydeder.
```

```
7. Kullanıcı WER Raporları
Öncelik: Düşük
Konum → C:\Users\<Kullanıcı>\AppData\Local\Microsoft\Windows\WER\
Gözlem Notu: Kullanıcı bağlamında oluşan uygulama crash raporlarını ve hataya neden olan modül bilgisini içerir.
```

```
8. Reliability Monitor Verileri
Öncelik: Düşük
Konum → C:\ProgramData\Microsoft\RAC\PublishedData\
Gözlem Notu: Sistem kararlılık indeksi ve kronolojik hata geçmişi verilerini içerir.
```
