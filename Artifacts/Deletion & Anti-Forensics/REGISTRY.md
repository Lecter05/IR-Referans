
```
1. UserAssist Sayacı Temizleme
Öncelik: Yüksek
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count
MITRE: T1070.004
Gözlem Notu: ROT13 ile encode edilmiş değerlerin toplu silinip silinmediğine veya sıfırlanıp sıfırlanmadığına bakılır.
```

```
2. RecentDocs Temizleme
Öncelik: Yüksek
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs
MITRE: T1070.004
Gözlem Notu: Alt anahtarların toplu silinmesi veya MRUListEx değerinin sıfırlanması durumuna bakılır.
```

```
3. BAM/DAM (Background Activity Moderator) Temizleme
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\<SID> (Win10 1809+)
MITRE: T1070.004
Gözlem Notu: Son çalıştırılan binary'lerin zaman damgalı kayıtlarının silinip silinmediğine bakılır.
```

```
4. Shimcache (AppCompatCache) Manipülasyonu
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache → AppCompatCache
MITRE: T1070.004
Gözlem Notu: Binary çalıştırma izlerinin cache'den silinip silinmediğine veya değiştirilip değiştirilmediğine bakılır.
```

```
5. Prefetch Devre Dışı Bırakma
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters → EnablePrefetcher
MITRE: T1562.001
Gözlem Notu: Prefetch'in devre dışı bırakılması için değerin 0'a ayarlanıp ayarlanmadığına bakılır.
```

```
6. Windows Defender Devre Dışı Bırakma
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Policies\Microsoft\Windows Defender → DisableAntiSpyware ve HKLM\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection → DisableRealtimeMonitoring
MITRE: T1562.001
Gözlem Notu: Defender'ın policy veya registry üzerinden kapatılıp kapatılmadığına bakılır.
```

```
7. Windows Event Log Servisi Devre Dışı Bırakma
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\EventLog → Start değeri
MITRE: T1562.002
Gözlem Notu: EventLog servisinin Start değerinin 4 (disabled) yapılıp yapılmadığına bakılır.
```

```
8. Audit Policy Kapatma (Registry)
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa → SCENoApplyLegacyAuditPolicy ve HKLM\SOFTWARE\Policies\Microsoft\Windows\System\Audit
MITRE: T1562.002
Gözlem Notu: Denetim politikalarının registry üzerinden devre dışı bırakılıp bırakılmadığına bakılır.
```

```
9. Sysmon Servisi Devre Dışı Bırakma / Kaldırma
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Services\Sysmon ve Sysmon64
MITRE: T1562.001
Gözlem Notu: Sysmon servis kaydının silinip silinmediğine veya Start değerinin değiştirilip değiştirilmediğine bakılır.
```

```
10. ETW Provider Devre Dışı Bırakma
Öncelik: Yüksek
Konum → HKLM\SYSTEM\CurrentControlSet\Control\WMI\Autologger\<LoggerName> → Enabled
MITRE: T1562.006
Gözlem Notu: ETW autologger oturumlarının Enabled değerinin 0 yapılıp yapılmadığına bakılır.
```

```
11. Windows Defender Exclusion Ekleme
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths, Processes, Extensions
MITRE: T1562.001
Gözlem Notu: Zararlı dosya veya dizin yollarının Defender exclusion listesine eklenip eklenmediğine bakılır.
```

```
12. ShellBags Manipülasyonu
Öncelik: Orta
Konum → HKCU\SOFTWARE\Microsoft\Windows\Shell\BagMRU ve HKCU\SOFTWARE\Microsoft\Windows\Shell\Bags
MITRE: T1070.004
Gözlem Notu: Klasör erişim geçmişinin toplu silinip silinmediğine veya tutarsız kayıtlara bakılır.
```

```
13. TypedPaths / TypedURLs Temizleme
Öncelik: Orta
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths ve HKCU\SOFTWARE\Microsoft\Internet Explorer\TypedURLs
MITRE: T1070.004
Gözlem Notu: Adres çubuğuna yazılan yol ve URL geçmişinin silinip silinmediğine bakılır.
```

```
14. RunMRU Temizleme
Öncelik: Orta
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
MITRE: T1070.004
Gözlem Notu: Run diyaloğu geçmişindeki komutların silinip silinmediğine bakılır.
```

```
15. LastVisitedMRU / OpenSaveMRU Temizleme
Öncelik: Orta
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU ve OpenSavePidlMRU
MITRE: T1070.004
Gözlem Notu: Dosya aç/kaydet diyaloğu geçmişinin toplu temizlenip temizlenmediğine bakılır.
```

```
16. Terminal Server Client MRU Temizleme
Öncelik: Orta
Konum → HKCU\SOFTWARE\Microsoft\Terminal Server Client\Default ve Servers
MITRE: T1070.004
Gözlem Notu: RDP bağlantı geçmişinin silinip silinmediğine bakılır.
```

```
17. MountPoints2 Temizleme
Öncelik: Orta
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2
MITRE: T1070.004
Gözlem Notu: USB ve ağ paylaşımı bağlantı izlerinin silinip silinmediğine bakılır.
```

```
18. USBSTOR / USB Kayıtları Temizleme
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR ve HKLM\SYSTEM\CurrentControlSet\Enum\USB
MITRE: T1070.004
Gözlem Notu: USB cihaz bağlantı geçmişinin registry'den silinip silinmediğine bakılır.
```

```
19. DisableLastAccess Ayarı Değişikliği
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\FileSystem → NtfsDisableLastAccessUpdate
MITRE: T1562.001
Gözlem Notu: Son erişim zaman damgası kaydını devre dışı bırakmak için değerin 1'e ayarlanıp ayarlanmadığına bakılır.
```

```
20. AMSI Bypass (Registry)
Öncelik: Orta
Konum → HKLM\SOFTWARE\Microsoft\AMSI\Providers ve HKCU\SOFTWARE\Microsoft\Windows Script\Settings → AmsiEnable
MITRE: T1562.001
Gözlem Notu: AMSI sağlayıcılarının kaldırılıp kaldırılmadığına veya AmsiEnable'ın 0 yapılıp yapılmadığına bakılır.
```

```
21. Firewall Kuralı Ekleme / Devre Dışı Bırakma
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\FirewallRules ve Microsoft-Windows-Windows Firewall With Advanced Security%4Firewall.evtx → EID 2003, 2004, 2005, 2006
MITRE: T1562.004
Gözlem Notu: Yeni eklenen allow kurallarına veya firewall profilinin tamamen kapatılıp kapatılmadığına bakılır.
```

```
22. Event Log Kanal Boyutu Sınırlama
Öncelik: Orta
Konum → HKLM\SOFTWARE\Policies\Microsoft\Windows\EventLog\<channel> → MaxSize ve Retention
MITRE: T1562.002
Gözlem Notu: Log kanal boyutunun çok küçük ayarlanarak (örn. 64KB) hızlı üzerine yazılma sağlanıp sağlanmadığına bakılır.
```

```
23. WordWheelQuery Temizleme
Öncelik: Düşük
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery
MITRE: T1070.004
Gözlem Notu: Explorer arama geçmişinin silinip silinmediğine bakılır.
```

```
24. Minifilter Altitude Manipülasyonu
Öncelik: Düşük
Konum → HKLM\SYSTEM\CurrentControlSet\Services\<driver>\Instances\<instance> → Altitude
MITRE: T1562.001
Gözlem Notu: Güvenlik ürünü minifilter driver'ının altitude değerinin değiştirilip değiştirilmediğine bakılır.
```
