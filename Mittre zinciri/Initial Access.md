

## Phishing — Spearphishing Attachment — T1566.001

Klasik .exe yerine artık .pdf, .one, .lnk, .iso, .html ekler kullanılıyor
çünkü bunlar AV tespitinden daha kolay kaçıyor.

**Yaygın ek türleri:**
- .lnk → PowerShell veya cmd çalıştırır
- .one (OneNote) → gömülü script veya HTA
- .iso / .img → içinde .lnk veya .exe, MOTW'yi bypass eder
- .html → HTML Smuggling ile base64 payload
- .pdf → link içerir, direkt zararlı kod taşımaz

**Nereye bakarsın:**
- Prefetch → outlook.exe, thunderbird.exe ardından powershell.exe, cmd.exe vb.
- $UsnJrnl → Temp veya Downloads klasörüne yeni dosya
- Sysmon ID 11 → Temp/Downloads'a dosya oluşturuldu
- Sysmon ID 1 → email client'ın child process'i

**IOC:**
- Email client (outlook.exe) → wscript.exe / powershell.exe / mshta.exe
- Temp veya Downloads klasöründen çalışan binary
- .lnk dosyasının target path'i uzun ve obfuscated komut içeriyor

**Dikkat:**
.iso ve .img mount edilince içindeki dosyalar "Zone.Identifier"(dosya internetten geldi) almaz.
LNK metadata'sı silinmiş olsa bile $MFT ve $UsnJrnl timestamp kalır.

---

## Phishing — Spearphishing Link — T1566.002

Email içindeki link zararlı siteye veya payload'a yönlendirir.
2024-2025'te ClickFix ve fakeCAPTCHA bu kategoride patlama yaptı.

**ClickFix / Paste-and-Run (T1204.004 — yeni teknik):**
Sahte hata mesajı veya CAPTCHA gösterip kullanıcıyı
Win+R → Ctrl+V → Enter yaptırıyor.
Kopyaladığı şey zararlı PowerShell komutu.
Çok etkili çünkü kullanıcı kendisi çalıştırıyor — AV bypass.

**Nereye bakarsın:**
- Browser downloads
- `AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt`
- Zone.Identifier → indirilen dosyanın referrer URL'i

**Dikkat:**
ClickFix saldırısında kullanıcı kendisi çalıştırdığı için
email filtreleri ve sandbox'lar genellikle yakalayamıyor.
PSReadline history kritik kanıt noktası oluyor.

---

## Valid Accounts — T1078


**Alt teknikler:**
- **T1078.001** Default Accounts — varsayılan admin/şifre
- **T1078.002** Domain Accounts — ele geçirilmiş AD hesabı
- **T1078.003** Local Accounts — yerel hesap, özellikle RDP için
- **T1078.004** Cloud Accounts — O365, Azure AD, AWS hesabı

**Kimlikler nasıl elde ediliyor:**
- Infostealer malware (LummaC2, Vidar, Stealc, Acreed) browser kayıtlı şifreler
- Phishing ile kimlik avı
- Credential stuffing — sızdırılmış listelerden deneme
- Dark web'de satın alma

---

## External Remote Services — T1133


**Yaygın hedefler:**
- RDP (3389/TCP) — brute force veya çalınmış credential
- VPN — SonicWall CVE-2024-40766, Fortinet CVE-2024-55591/CVE-2024-21762
- Citrix / NetScaler
- Exchange / Outlook Web Access

**Gerçek vaka — 2024-2025:**
Akira ransomware → SonicWall VPN exploit → 6 dakikada lateral movement
Qilin ransomware→ Fortinet FortiGate → 26 kamu kuruluşu

**Nereye bakarsın:**
- VPN/firewall logları → başarısız giriş denemeleri + başarılı giriş
- Security 4624 Type 3 veya 10 → remote logon, kaynak IP
- Security 1149 → RDP bağlantı kaynağı (pre-auth, username + IP)
- System/Application logları → servis crash veya exploit sonrası hata
- Prefetch → exploit aracı çalıştı mı?
- $UsnJrnl → exploit sonrası dosya bırakılmış mı?

**Dikkat:**
Bu teknik genellikle log olmayan katmanlarda gerçekleşir.
Firewall ve VPN logları olmadan tespit çok zorlaşır.
Patch yönetimi en kritik önlem — CVE açıklandıktan sonra
saldırganlar saatler içinde istismar başlatıyor.

---

## Drive-by Compromise — T1189

SEO poisoning saldırılarında kullanıcı farkında olmadan zararlı siteye gidiyor.

**Nasıl çalışıyor:**
- SEO poisoning → arama sonuçlarında sahte yazılım sitesi üste çıkıyor
- Malvertising → meşru reklam ağı üzerinden zararlı reklam
- Watering hole → hedef grubun ziyaret ettiği site ele geçiriliyor

**Oyster/Broomstick kampanyası (2025):**
SEO poisoning ile putty, 7zip gibi araçların sahte sitelerine yönlendirme.
İndirilen installer aslında zararlı DLL (twain_96.dll) içeriyor.
Rundll32.exe ile çalıştırılıyor.

**Nereye bakarsın:**
- Browser history → hangi site ziyaret edildi, timestamp
- Browser downloads → ne indirildi?
- Zone.Identifier → indirilen dosyanın kaynak URL'i
- Sysmon ID 1 → browser'dan spawn olan process
- Prefetch → rundll32.exe, mshta.exe, wscript.exe var mı?
- Amcache → yeni binary'nin hash'i

---

## Public-Facing Application Exploitation — T1190


**2024-2025'te öne çıkan CVE'ler:**
- CVE-2024-40766 — SonicWall VPN
- CVE-2024-55591 / CVE-2024-21762 — Fortinet FortiGate
- CVE-2023-27532 — Veeam Backup & Replication
- CVE-2021-34527 — PrintNightmare (hala kullanılıyor)
- Exchange Server CVE'leri — ProxyShell ailesi
