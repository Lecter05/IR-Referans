
```
1. Kablosuz Ağ Profil XML Dosyaları
Öncelik: Yüksek
Konum → C:\ProgramData\Microsoft\Wlansvc\Profiles\Interfaces\{GUID}\*.xml
MITRE: T1016.001
Gözlem Notu: XML dosyalarındaki SSID, kimlik doğrulama türü ve key material (şifre) alanlarına bakılır.
```

```
2. WLAN-AutoConfig Event Log — Event ID 8001, 8002, 8003, 11000, 11001
Öncelik: Yüksek
Konum → Microsoft-Windows-WLAN-AutoConfig%4Operational.evtx
MITRE: T1016.001
Gözlem Notu: WiFi bağlantı başarı/başarısızlık olaylarında SSID, BSSID ve bağlantı zamanına bakılır.
```

```
3. Kablosuz Ağ Profilleri (netsh çıktısı)
Öncelik: Yüksek
Erişim: Live System
Konum → netsh wlan show profiles çıktısı ve XML profil dosyaları
MITRE: T1016.001
Gözlem Notu: Kayıtlı tüm WiFi profil isimlerine ve parolalarının plaintext alınıp alınamayacağına bakılır.
```

```
4. Hosted Network / Mobile Hotspot İzleri
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\WlanSvc\Parameters\HostedNetworkSettings ve netsh wlan show hostednetwork
MITRE: T1016.001
Gözlem Notu: Sistemin sahte WiFi hotspot olarak yapılandırılıp yapılandırılmadığına bakılır.
```

```
5. WiFi Direct / Wi-Fi Sense Ayarları
Öncelik: Düşük
Konum → HKLM\SOFTWARE\Microsoft\WcmSvc\wifinetworkmanager\config (Win10)
MITRE: T1016.001
Gözlem Notu: WiFi parolalarının otomatik paylaşım ayarlarının etkin olup olmadığına bakılır (Win10 erken sürümler).
```
