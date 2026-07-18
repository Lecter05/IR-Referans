
### vssadmin.exe

Volume Shadow Copy yönetimi. Shadow copy silme — ransomware zincirinin klasik adımı.

**Komut:**
- vssadmin delete shadows /all /quiet

**IOC:** delete shadows parametresi, bcdedit ve wbadmin ile birlikte görülüyorsa ransomware zinciri

---

### bcdedit.exe

Boot Configuration Data yönetimi. Recovery devre dışı bırakma (ransomware)

**Komut:**
- bcdedit /set {default} recoveryenabled No
- bcdedit /set {default} bootstatuspolicy ignoreallfailures

**IOC:** recoveryenabled No, ransomware zincirinde bcdedit + vssadmin üçlüsü

---

### wbadmin.exe

Windows Backup yönetimi. Backup silme (ransomware)

**Komut:**
- wbadmin delete catalog -quiet
- wbadmin delete systemstatebackup

**IOC:** delete parametresi, ransomware zincirinde

---

### fsutil.exe

Dosya sistemi yönetimi. USN Journal silme — kritik forensic artifact yok edilir.

**Komut:**
- fsutil usn deletejournal /D C:

**IOC:** deletejournal parametresi = $UsnJrnl siliniyor, kritik artifact kaybı

---

### fltMC.exe
Filesystem filter driver yönetimi. Sysmon driver'ı devre dışı bırakma

**Komut:**
- fltMC.exe unload SysmonDrv

**IOC:** unload + SysmonDrv, bu komut sonrası Sysmon logları durur

---

### cipher.exe

Ne yapar: EFS dosya şifreleme. Boş disk alanını üzerine yazarak kurtarmayı engeller

**Komut:**
- cipher /w:C:\

**IOC:** /w: parametresi + disk yolu

---

### wmic.exe (Defense Evasion varyantı)

WMI yönetimi. Log silme ve sistem bilgisi toplamak için kullanılır. Volt Typhoon tarafından yoğun şekilde kullanıldığı belgelenmiş.

**Komut:**
- wmic shadowcopy delete
- wmic /namespace:\\root\subscription PATH __EventFilter delete

**IOC:** shadowcopy delete veya subscription silme komutu

---

### odbcconf.exe ⚠️ Yükselen

ODBC yapılandırması. Regsvr32'ye benzer şekilde DLL çalıştırır — AppLocker bypass. APT gruplarının radarına girmekte.

**Komut:**
- odbcconf.exe /a {REGSVR zararlı.dll}
- odbcconf.exe -f payload.rsp

**IOC:** /a {REGSVR parametresi, beklenmedik DLL yükleme