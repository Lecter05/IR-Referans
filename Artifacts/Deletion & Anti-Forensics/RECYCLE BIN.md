
```
1. $Recycle.Bin Metadata ($I ve $R Dosyaları)
Öncelik: Yüksek
Konum → C:\$Recycle.Bin\<SID>\$I?????? ve $R??????
MITRE: T1070.004
Gözlem Notu: $I dosyalarındaki orijinal dosya adı, yol, boyut ve silme zamanı bilgilerine bakılır; $R dosyası silinmiş içeriğin kendisidir.
```

```
2. $Recycle.Bin Toplu Temizleme
Öncelik: Yüksek
Konum → C:\$Recycle.Bin\<SID>\ klasörü
MITRE: T1070.004
Gözlem Notu: Recycle Bin'in tamamen boşaltılıp boşaltılmadığına; $I/$R dosya çiftlerinin tutarsızlığına bakılır.
```

```
3. Recycle Bin Bypass ile Silme (rd /s /q, del /f, PowerShell Remove-Item)
Öncelik: Yüksek
Konum → $UsnJrnl ve $MFT kayıtları; komut geçmişi
MITRE: T1070.004
Gözlem Notu: Komut satırı ile Recycle Bin'e uğramadan yapılan toplu silme işlemlerinin izlerine bakılır.
```

```
4. $Recycle.Bin Dosyalarının Doğrudan Silinmesi
Öncelik: Orta
Konum → $MFT ve $UsnJrnl'de $Recycle.Bin altındaki silme kayıtları
MITRE: T1070.004
Gözlem Notu: Recycle Bin içindeki $I/$R dosyalarının dosya sistemi düzeyinde (Recycle Bin'i atlayarak) silinip silinmediğine bakılır.
```

```
5. Farklı Hacimlerdeki Recycle Bin
Öncelik: Düşük
Konum → D:\$Recycle.Bin\, E:\$Recycle.Bin\ vb.
MITRE: T1070.004
Gözlem Notu: Sistem dışı sürücülerdeki Recycle Bin klasörlerinin de kontrol edilip edilmediğine bakılır; sıklıkla gözden kaçar.
```
