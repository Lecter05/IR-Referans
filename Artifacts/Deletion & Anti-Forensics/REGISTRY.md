
**UserAssist Sayacı Temizleme**
Konum: HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count
Öncelik: Yüksek | Erişim: Her ikisi | MITRE: T1070.004
Gözlem Notu: ROT13 ile encode edilmiş değerlerin toplu silinip silinmediğine veya sıfırlanıp sıfırlanmadığına bakılır.

**RecentDocs Temizleme**
Konum: HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs
Öncelik: Yüksek | Erişim: Her ikisi | MITRE: T1070.004
Gözlem Notu: Alt anahtarların toplu silinmesi veya MRUListEx değerinin sıfırlanması durumuna bakılır.

**ShellBags Manipülasyonu**
Konum: HKCU\SOFTWARE\Microsoft\Windows\Shell\BagMRU ve HKCU\SOFTWARE\Microsoft\Windows\Shell\Bags
Öncelik: Orta | Erişim: Her ikisi | MITRE: T1070.004
Gözlem Notu: Klasör erişim geçmişinin toplu silinip silinmediğine veya tutarsız kayıtlara bakılır.

**TypedPaths / TypedURLs Temizleme**
Konum: HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths ve HKCU\SOFTWARE\Microsoft\Internet Explorer\TypedURLs
Öncelik: Orta | Erişim: Her ikisi | MITRE: T1070.004
Gözlem Notu: Adres çubuğuna yazılan yol ve URL geçmişinin silinip silinmediğine bakılır.

**RunMRU Temizleme**
Konum: HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
Öncelik: Orta | Erişim: Her ikisi | MITRE: T1070.004
Gözlem Notu: Run diyaloğu geçmişindeki komutların silinip silinmediğine bakılır.

**LastVisitedMRU / OpenSaveMRU Temizleme**
Konum: HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU ve OpenSavePidlMRU
Öncelik: Orta | Erişim: Her ikisi | MITRE: T1070.004
Gözlem Notu: Dosya aç/kaydet diyaloğu geçmişinin toplu temizlenip temizlenmediğine bakılır.

**BAM/DAM (Background Activity Moderator) Temizleme**
Konum: HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\<SID> (Win10 1809+)
Öncelik: Yüksek | Erişim: Her ikisi | MITRE: T1070.004
Gözlem Notu: Son çalıştırılan binary'lerin zaman damgalı kayıtlarının silinip silinmediğine bakılır.

**Shimcache (AppCompatCache) Manipülasyonu**
Konum: HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache → AppCompatCache
Öncelik: Yüksek | Erişim: Her ikisi | MITRE: T1070.004
Gözlem Notu: Binary çalıştırma izlerinin cache'den silinip silinmediğine veya değiştirilip değiştirilmediğine bakılır.

**Terminal Server Client MRU Temizleme**
Konum: HKCU\SOFTWARE\Microsoft\Terminal Server Client\Default ve Servers
Öncelik: Orta | Erişim: Her ikisi | MITRE: T1070.004
Gözlem Notu: RDP bağlantı geçmişinin silinip silinmediğine bakılır.

**MountPoints2 Temizleme**
Konum: HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2
Öncelik: Orta | Erişim: Her ikisi | MITRE: T1070.004
Gözlem Notu: USB ve ağ paylaşımı bağlantı izlerinin silinip silinmediğine bakılır.

**USBSTOR / USB Kayıtları Temizleme**
Konum: HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR ve HKLM\SYSTEM\CurrentControlSet\Enum\USB
Öncelik: Orta | Erişim: Her ikisi | MITRE: T1070.004
Gözlem Notu: USB cihaz bağlantı geçmişinin registry'den silinip silinmediğine bakılır.

**WordWheelQuery Temizleme**
Konum: HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery
Öncelik: Düşük | Erişim: Her ikisi | MITRE: T1070.004
Gözlem Notu: Explorer arama geçmişinin silinip silinmediğine bakılır.

**DisableLastAccess Ayarı Değişikliği**
Konum: HKLM\SYSTEM\CurrentControlSet\Control\FileSystem → NtfsDisableLastAccessUpdate
Öncelik: Orta | Erişim: Her ikisi | MITRE: T1562.001
Gözlem Notu: Son erişim zaman damgası kaydını devre dışı bırakmak için değerin 1'e ayarlanıp ayarlanmadığına bakılır.

**Prefetch Devre Dışı Bırakma**
Konum: HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters → EnablePrefetcher
Öncelik: Yüksek | Erişim: Her ikisi | MITRE: T1562.001
Gözlem Notu: Prefetch'in devre dışı bırakılması için değerin 0'a ayarlanıp ayarlanmadığına bakılır.

**Windows Defender Devre Dışı Bırakma**
Konum: HKLM\SOFTWARE\Policies\Microsoft\Windows Defender → DisableAntiSpyware ve HKLM\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection → DisableRealtimeMonitoring
Öncelik: Yüksek | Erişim: Her ikisi | MITRE: T1562.001
Gözlem Notu: Defender'ın policy veya registry üzerinden kapatılıp kapatılmadığına bakılır.

**Windows Event Log Servisi Devre Dışı Bırakma**
Konum: HKLM\SYSTEM\CurrentControlSet\Services\EventLog → Start değeri
Öncelik: Yüksek | Erişim: Her ikisi | MITRE: T1562.002
Gözlem Notu: EventLog servisinin Start değerinin 4 (disabled) yapılıp yapılmadığına bakılır.

**Audit Policy Kapatma (Registry)**
Konum: HKLM\SYSTEM\CurrentControlSet\Control\Lsa → SCENoApplyLegacyAuditPolicy ve HKLM\SOFTWARE\Policies\Microsoft\Windows\System\Audit
Öncelik: Yüksek | Erişim: Her ikisi | MITRE: T1562.002
Gözlem Notu: Denetim politikalarının registry üzerinden devre dışı bırakılıp bırakılmadığına bakılır.

**Sysmon Servisi Devre Dışı Bırakma / Kaldırma**
Konum: HKLM\SYSTEM\CurrentControlSet\Services\Sysmon ve Sysmon64
Öncelik: Yüksek | Erişim: Her ikisi | MITRE: T1562.001
Gözlem Notu: Sysmon servis kaydının silinip silinmediğine veya Start değerinin değiştirilip değiştirilmediğine bakılır.

**ETW Provider Devre Dışı Bırakma**
Konum: HKLM\SYSTEM\CurrentControlSet\Control\WMI\Autologger\<LoggerName> → Enabled
Öncelik: Yüksek | Erişim: Her ikisi | MITRE: T1562.006
Gözlem Notu: ETW autologger oturumlarının Enabled değerinin 0 yapılıp yapılmadığına bakılır.

**AMSI Bypass (Registry)**
Konum: HKLM\SOFTWARE\Microsoft\AMSI\Providers ve HKCU\SOFTWARE\Microsoft\Windows Script\Settings → AmsiEnable
Öncelik: Orta | Erişim: Her ikisi | MITRE: T1562.001
Gözlem Notu: AMSI sağlayıcılarının kaldırılıp kaldırılmadığına veya AmsiEnable'ın 0 yapılıp yapılmadığına bakılır.
