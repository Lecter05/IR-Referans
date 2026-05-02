
```
1. System Log — Ana Olay Kaydı
Öncelik: Yüksek
Konum → %SystemRoot%\System32\winevt\Logs\System.evtx
Gözlem Notu: Servis kurulumu (7045), servis durumu değişikliği (7036), sürücü yükleme (7034, 7040), beklenmedik kapatma (6008), saat değişikliği (1), Windows Update (19, 20, 43), disk hataları (7, 11, 15, 51, 153) incelenir.
```

```
2. System — Service Installation
Öncelik: Yüksek
Konum → System.evtx
Gözlem Notu: Event ID 7045 yeni servis kurulumunu gösterir (T1543.003); ServiceName, ImagePath ve ServiceType alanları kötü amaçlı servis tespitinde kritiktir; özellikle cmd.exe/powershell.exe içeren ImagePath'ler şüphelidir.
```

```
3. System — Kernel Driver Load
Öncelik: Orta
Konum → System.evtx
Gözlem Notu: Event ID 7034 (servis beklenmedik şekilde sonlandı) ve 7040 (başlatma türü değişikliği) olayları; Win11 22H2+ sürümlerde imzasız sürücü yükleme girişimleri ek uyarı üretir.
```

```
4. System — Time Manipulation
Öncelik: Orta
Konum → System.evtx
Gözlem Notu: Event ID 1 (sistem saati değişikliği) timestamp manipülasyonuna işaret edebilir; PreviousTime ve NewTime alanları karşılaştırılır.
```

```
5. System — Group Policy Processing
Öncelik: Düşük
Konum → System.evtx
Gözlem Notu: Event ID 1500, 1501, 1502 (GP işleme hataları/başarıları) domain ortamında politika uygulanma durumunu doğrulamak için incelenir.
```
