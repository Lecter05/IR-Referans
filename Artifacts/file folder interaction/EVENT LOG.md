
## Dosya Paylaşımı / Erişim

```
1. Security.evtx — Event ID 4663 (Nesneye Erişim)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Dosya veya klasöre yapılan okuma, yazma ve silme işlemlerini kullanıcı ve süreç bazında kaydeder; audit policy gerektirir.
```

```
2. Security.evtx — Event ID 4656 (Handle Talebi)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Dosya veya nesneye handle açma girişimini kaydeder; başarılı olmasa bile erişim niyetini gösterir.
```

```
3. Security.evtx — Event ID 5140 (Ağ Paylaşımına Erişim)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Ağ paylaşımına erişen kullanıcının adını, kaynak IP'sini ve paylaşım yolunu kaydeder.
```

```
4. Security.evtx — Event ID 5145 (Paylaşım Dosyasına Erişim)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Ağ paylaşımındaki belirli bir dosyaya yapılan erişimin izin kontrolü sonucunu kaydeder.
```

```
5. Security.evtx — Event ID 4660 (Nesne Silindi)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Silinen nesnenin handle ID'sini kaydeder; 4656 ve 4663 ile korelasyon kurularak silinen dosya belirlenir.
```

```
6. Security.evtx — Event ID 4657 (Registry Değeri Değiştirildi)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Değiştirilen registry değerinin eski ve yeni değerini, işlemi yapan süreci kaydeder.
```

```
7. Security.evtx — Event ID 4658 (Handle Kapatıldı)
Öncelik: Düşük
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Açılan handle'ın kapatılma zamanını kaydeder; erişim süresini hesaplamak için 4656 ile eşleştirilir.
```

```
8. Security.evtx — Event ID 4659 (Handle Silme Talebiyle Kapatıldı)
Öncelik: Düşük
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Silme amacıyla açılan handle'ın kapatılma kaydını tutar.
```

```
9. Security.evtx — Event ID 4661 (SAM Nesnesine Erişim)
Öncelik: Düşük
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: SAM (Security Account Manager) nesnelerine yapılan erişimi kaydeder.
```

```
10. Security.evtx — Event ID 4670 (Nesne İzinleri Değiştirildi)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Dosya veya nesnenin DACL/SACL izinlerindeki değişikliği eski ve yeni değerleriyle kaydeder.
```

```
11. Security.evtx — Event ID 5142 (Ağ Paylaşımı Eklendi)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Yeni oluşturulan ağ paylaşımının adını ve yolunu kaydeder.
```

```
12. Security.evtx — Event ID 5143 (Ağ Paylaşımı Değiştirildi)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Mevcut ağ paylaşımının izin veya yapılandırma değişikliğini kaydeder.
```

```
13. Security.evtx — Event ID 5144 (Ağ Paylaşımı Silindi)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
Gözlem Notu: Silinen ağ paylaşımının adını ve silinme zamanını kaydeder.
```

---

## USB / Harici Medya

```
1. System.evtx — Event ID 20001 (Yeni Cihaz Kuruldu)
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\System.evtx
Gözlem Notu: Plug and Play tarafından kurulan yeni cihazın sürücü ve kurulum zamanını kaydeder.
```

```
2. System.evtx — Event ID 20003 (Cihaz Kaldırıldı)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\System.evtx
Gözlem Notu: Sistemden kaldırılan cihazın bilgisini ve kaldırma zamanını kaydeder.
```

```
3. System.evtx — Event ID 10000 / 10001 (USB Bağlantı/Ayrılma)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\System.evtx
Gözlem Notu: USB cihazının bağlanma ve ayrılma olaylarını zaman damgasıyla kaydeder.
```

---

## DriverFrameworks-UserMode

```
1. Event ID 2003 (USB Aygıt Başlatıldı)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-DriverFrameworks-UserMode%4Operational.evtx
Gözlem Notu: USB aygıtının başlatılma olayını ve device instance ID bilgisini kaydeder.
```

```
2. Event ID 2100 (PnP Aygıt Bağlandı)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-DriverFrameworks-UserMode%4Operational.evtx
Gözlem Notu: Plug and Play aygıtının sisteme bağlanma anını ve cihaz detaylarını kaydeder.
```

```
3. Event ID 2102 (PnP Aygıt Ayrıldı)
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-DriverFrameworks-UserMode%4Operational.evtx
Gözlem Notu: PnP aygıtının sistemden ayrılma zamanını kaydeder; USB bağlantı süresini hesaplar.
```

---

## NTFS Log

```
1. Microsoft-Windows-Ntfs Operational
Öncelik: Düşük
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-Ntfs%4Operational.evtx
Gözlem Notu: NTFS birim hatalarını, otomatik onarım ve bütünlük kontrolü olaylarını kaydeder.
```

---

## USB Analytic Logları

```
1. USBCore Log
Öncelik: Düşük
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-USB-USBHUB3-Analytic.evtx
Gözlem Notu: USB hub seviyesindeki detaylı cihaz iletişim olaylarını kaydeder; analytic kanal olduğundan özel etkinleştirme gerektirebilir.
```

```
2. USBDevice Log
Öncelik: Düşük
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-USB-USBPORT-Analytic.evtx
Gözlem Notu: USB port seviyesindeki cihaz iletişim detaylarını kaydeder.
```

---

## Shell / Explorer

```
1. Microsoft-Windows-Shell-Core Operational — Event ID 9707 / 9708
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-Shell-Core%4Operational.evtx
Gözlem Notu: Explorer shell üzerinden uygulama başlatma ve kapatma olaylarını kaydeder.
```

---

## Task Scheduler

```
1. Task Scheduler Operational
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-TaskScheduler%4Operational.evtx
Gözlem Notu: Zamanlanmış görevlerin dosya kopyalama veya taşıma script'lerini tetikleme olaylarını kaydeder.
```

---

## PowerShell / Script

```
1. PowerShell Operational — Event ID 4103 / 4104
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-PowerShell%4Operational.evtx
Gözlem Notu: Copy-Item, Move-Item, Remove-Item gibi dosya işlem cmdlet'lerinin tam komut metnini kaydeder.
```

---

## Windows Search

```
1. Search Operational
Öncelik: Düşük
Konum → C:\Windows\System32\winevt\Logs\Microsoft-Windows-Search-Operational.evtx
Gözlem Notu: Windows Search indeksleme hatalarını ve durum değişikliklerini kaydeder; indekslenen dosya kapsamını gösterir.
```
