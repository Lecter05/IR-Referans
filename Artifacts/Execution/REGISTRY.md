
> 18 Nisan 2026


## REGISTRY ARTIFACT'leri

```
1. Shimcache (AppCompatCache)
Öncelik: Yüksek
Konum → SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache
Gözlem Notu: Çalıştırılan veya yolu bilinen EXE'lerin son değişiklik zamanı ve dosya yolunu tutar; yeniden başlatmada diske yazılır.
```

```
2. Amcache.hve
Öncelik: Yüksek
Konum → C:\Windows\appcompat\Programs\Amcache.hve
Gözlem Notu: SHA1 hash, tam dosya yolu, boyut, yayıncı ve ilk çalıştırma zamanını içerir.
```

```
3. BAM (Background Activity Moderator)
Öncelik: Yüksek
Konum → SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\{SID}
Gözlem Notu: Her kullanıcı için son çalıştırılan EXE'nin tam yolunu ve UTC zaman damgasını tutar (Win10 1709+).
```

```
4. UserAssist
Öncelik: Yüksek
Konum → NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count
Gözlem Notu: GUI üzerinden çalıştırılan programların ROT13 ile kodlanmış adını, çalıştırma sayısını ve son çalıştırma zamanını tutar.
```

```
5. Services (Servis Kayıtları)
Öncelik: Yüksek
Konum → SYSTEM\CurrentControlSet\Services\<ServiceName>
Gözlem Notu: ImagePath, Start tipi ve ServiceDll değerlerini inceleyerek yeni eklenen veya değiştirilen servisleri tespit eder. (T1569.002)
```

```
6. Scheduled Task Registry Entries
Öncelik: Yüksek
Konum → SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks\{GUID}
Gözlem Notu: Zamanlanmış görevlerin Actions, Triggers ve son çalışma durumunu tutar. (T1053.005)
```

```
7. DAM (Desktop Activity Moderator)
Öncelik: Orta
Konum → SYSTEM\CurrentControlSet\Services\dam\State\UserSettings\{SID}
Gözlem Notu: BAM ile aynı yapıdadır; masaüstü oturumlarındaki çalıştırmaları ayrıca kaydeder.
```

```
8. RecentApps
Öncelik: Orta
Konum → NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Search\RecentApps
Gözlem Notu: Son çalıştırılan uygulamaların AppID, çalıştırma sayısı ve son erişim zamanını içerir (Win10; Win11'de kısıtlı).
```

```
9. RunMRU
Öncelik: Orta
Konum → NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
Gözlem Notu: Win+R (Run) diyaloguna yazılan komutların listesini MRU sırasıyla tutar.
```

```
10. AppCompatFlags\Compatibility Assistant (PCA)
Öncelik: Orta
Konum → NTUSER.DAT\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Compatibility Assistant\Store
Gözlem Notu: Program Compatibility Assistant tarafından algılanan çalıştırmaların tam yolunu ve zaman damgasını tutar.
```

```
11. Terminal Server Client\Servers (RDP Çalıştırma İzi)
Öncelik: Orta
Konum → NTUSER.DAT\Software\Microsoft\Terminal Server Client\Servers
Gözlem Notu: RDP ile bağlanılan uzak sunucularda çalıştırılan programlara dolaylı kanıt sağlar.
```

```
12. SessionManager\AppCertDlls
Öncelik: Orta
Konum → SYSTEM\CurrentControlSet\Control\Session Manager\AppCertDlls
Gözlem Notu: Her CreateProcess çağrısında yüklenen DLL yollarını tutar; kötüye kullanım halinde persistence ve execution kanıtıdır.
```

```
13. Image File Execution Options (IFEO)
Öncelik: Orta
Konum → SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\<exe>
Gözlem Notu: Debugger değeri atanmış EXE'ler, çalıştırma sırasında başka bir programın tetiklendiğini gösterir.
```

```
14. MUICache
Öncelik: Düşük
Konum → NTUSER.DAT\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache
Gözlem Notu: Çalıştırılan uygulamanın dil kaynağından (MUI) çekilen açıklama metnini ve tam yolunu tutar.
```

```
15. AppCompatFlags\Layers
Öncelik: Düşük
Konum → NTUSER.DAT\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers
Gözlem Notu: Uyumluluk modunda çalıştırılan programların tam yolunu ve uygulanan flag'leri gösterir.
```

```
16. CIDSizeMRU
Öncelik: Düşük
Konum → NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\CIDSizeMRU
Gözlem Notu: Dosya açma/kaydetme diyaloğu kullanan uygulamaların tam yolunu tutar; dolaylı çalıştırma kanıtıdır.
```

```
17. FeatureUsage
Öncelik: Düşük
Konum → NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\FeatureUsage
Gözlem Notu: Görev çubuğuna sabitlenen veya oradan başlatılan uygulamaların sayaçlarını tutar (Win10 1903+).
```

---

> Varsayılan: Kapalı ibaresi taşıyan artifact'lar, olay öncesinde etkinleştirilmemişse mevcut olmayabilir.
>
> "Erişim: Live System" yalnızca canlı sistem veya RAM dump gerektiren artifact'larda belirtilmiştir.  
>
> Öncelik değerleri, execution kanıtı sağlama güvenilirliği ifade eder.
