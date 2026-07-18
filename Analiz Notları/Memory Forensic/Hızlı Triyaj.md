
> `dump.mem` kısmına kendi dosya ismini yazmayı unutma.

### 1 · İlk Erişim ve Çalıştırma

**Şüpheli Dizinler** — Temp, Public, ProgramData altındaki çalıştırılabilir dosyalar
```
strings dump.mem | egrep -i '[A-Za-z]:\\(Windows\\Temp|Users\\[^\\]+\\AppData\\(Local|Roaming)\\Temp|ProgramData|Users\\Public)\\[A-Za-z0-9_.-]+\.(exe|dll|ps1|bat|vbs|vbe|cmd|js|jse|wsf|wsh|hta|cpl|msc|msi|msp|chm|lnk|iso|img|cab|scr|pif)'
```

**LoLBins** — Windows'un kendi araçlarıyla indirme/çalıştırma (certutil, bitsadmin vb.)
```
strings dump.mem | egrep -i '(certutil.*-urlcache|bitsadmin.*transfer|mshta.*http|wmic.*process call create|rundll32.*javascript)'
```

**Fileless / Obfuscation** — Base64'lü PowerShell, bellekten kod çağırma
```
strings dump.mem | egrep -i '(powershell -e|-EncodedCommand|IEX |DownloadString|FromBase64String|AmsiScanBuffer)'
```

---

### 2 · Savunma Atlatma

**Modern Enjeksiyon** — Diske dokunmadan RAM'e yükleme izleri
```
strings dump.mem | egrep -i '(ReflectiveLoader|Invoke-ReflectivePEInjection|DynamicInvoke|SharpSploit|Costura\.AssemblyLoader)'
```

**İz Silme & Güvenlik Kapatma** — Log temizliği, Defender devre dışı bırakma
```
strings dump.mem | egrep -i '(wevtutil.* cl |Clear-EventLog|Remove-EventLog|Set-MpPreference.*-DisableRealtimeMonitoring)'
```

---

### 3 · Keşif

**AD & Ağ Keşfi** — BloodHound, port tarama, domain enumeration
```
strings dump.mem | egrep -i '(SharpHound|Invoke-BloodHound|Get-DomainController|Invoke-Portscan|PowerView)'
```

---

### 4 · Yetki Erişimi & Yanal Hareket

**Credential Dumping** — Bellekten parola/hash çekme araçları
```
strings dump.mem | egrep -i '(mimikatz|sekurlsa|lsadump|pypykatz|nanodump|handlekatz)'
```

**Pass-the-Hash / Ticket** — Parola bilmeden hesaplar arası geçiş
```
strings dump.mem | egrep -i '(sekurlsa::pth|Invoke-TheHash|Overpass-The-Hash|Rubeus.*ptt)'
```

---

### 5 · Komuta ve Kontrol (C2)

**C2 Frameworks** — Bilinen saldırgan yönetim paneli imzaları
```
strings dump.mem | egrep -i '(cobaltstrike|beacon|malleable|artifact\.exe|sliverpb|brute.?ratel|brc4|havoc\.exe|mythic|poshc2|covenant|faction\.dll)'
```

**URL'ler** — Potansiyel C2 / payload sunucu adresleri
```
strings dump.mem | egrep -oE 'https?://[A-Za-z0-9./?=_-]+'
```

---

### 6 · Veri Sızdırma

**Exfiltration Araçları** — Bulut upload, arşivleme, gizli dosya transferi
```
strings dump.mem | egrep -i '(rclone.*copy|megasync|Compress-Archive|curl.*--upload|winscp.*put)'
```

---

### 7 · Etki

**Ransomware** — Gölge kopya silme, kurtarma devre dışı bırakma
```
strings dump.mem | egrep -i '(vssadmin.*delete.*shadows|wbadmin.*delete.*catalog|bcdedit.*recoveryenabled.*no|wmic.*shadowcopy.*delete)'
```
