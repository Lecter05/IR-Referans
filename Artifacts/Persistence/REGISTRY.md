## REGISTRY ARTIFACT'LARI

```
1. Run / RunOnce Keys (HKLM)
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run ve RunOnce
Gözlem Notu: Tüm kullanıcılar için logon sonrası otomatik çalışan değerlere bakılır.
```

```
2. Run / RunOnce Keys (HKCU)
Öncelik: Yüksek
Konum → HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run ve RunOnce
Gözlem Notu: Kullanıcıya özgü logon sonrası otomatik başlatma değerlerine bakılır.
```

```
3. Winlogon Helper DLL (Shell/Userinit/Notify)
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon → Shell, Userinit, Notify
Gözlem Notu: Shell değerinin explorer.exe dışında bir değer içerip içermediğine bakılır.
```

```
4. AppInit_DLLs
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows → AppInit_DLLs, LoadAppInit_DLLs
Gözlem Notu: User32.dll yükleyen her işleme enjekte edilen DLL yollarına bakılır.
```

```
5. Image File Execution Options (IFEO) Debugger
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\<exe> → Debugger
Gözlem Notu: Meşru bir exe adı altında başka bir binary'ye yönlendirme olup olmadığına bakılır.
```

```
6. Accessibility Features Hijack
Öncelik: Yüksek
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe → Debugger
Gözlem Notu: sethc.exe, utilman.exe, osk.exe için Debugger değerinin cmd.exe olup olmadığına bakılır.
```

```
7. COM Object Hijacking (InprocServer32 / LocalServer32)
Öncelik: Yüksek
Konum → HKCU\SOFTWARE\Classes\CLSID\{GUID}\InprocServer32 ve HKLM\SOFTWARE\Classes\CLSID\{GUID}\LocalServer32
Gözlem Notu: HKCU altındaki COM kayıtlarının HKLM'deki meşru kayıtları gölgeleyip gölgelemediğine bakılır.
```

```
8. Run Keys (Wow6432Node)
Öncelik: Orta
Konum → HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run
Gözlem Notu: 32-bit uygulamaların 64-bit sistemdeki Run kayıtlarına bakılır.
```

```
9. IFEO — SilentProcessExit / GlobalFlag
Öncelik: Orta
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\<exe> → MonitorProcess
Gözlem Notu: Bir proses kapandığında tetiklenen MonitorProcess değerine bakılır.
```

```
10. BootExecute
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Session Manager → BootExecute
Gözlem Notu: Varsayılan autocheck autochk * dışında bir değer olup olmadığına bakılır.
```

```
11. Shell Extensions (ShellServiceObjectDelayLoad)
Öncelik: Orta
Konum → HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad ve Explorer\ShellIconOverlayIdentifiers
Gözlem Notu: Explorer başlatıldığında yüklenen tanınmayan CLSID değerlerine bakılır.
```

```
12. Userinit / Shell (HKCU)
Öncelik: Orta
Konum → HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon → Shell
Gözlem Notu: Kullanıcı düzeyinde Shell veya Userinit override değerine bakılır.
```

```
13. Print Monitor DLL
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors\<n> → Driver
Gözlem Notu: Spoolsv.exe tarafından SYSTEM olarak yüklenen tanınmayan DLL'lere bakılır.
```

```
14. Security Support Provider (SSP) DLL
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa → Security Packages
Gözlem Notu: lsass.exe'ye yüklenen varsayılan dışı paket isimlerine bakılır.
```

```
15. Authentication Packages
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa → Authentication Packages
Gözlem Notu: Varsayılan msv1_0 dışında eklenen paketlere bakılır.
```

```
16. Notification Packages (Password Filter DLL)
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa → Notification Packages
Gözlem Notu: Parola değişikliğinde çağrılan credential theft DLL'lerine bakılır.
```

```
17. Explorer\Run (Policy)
Öncelik: Orta
Konum → HKLM ve HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
Gözlem Notu: Group Policy ile dağıtılan otomatik başlatma girdilerine bakılır.
```

```
18. UserInitMprLogonScript
Öncelik: Orta
Konum → HKCU\Environment → UserInitMprLogonScript
Gözlem Notu: Kullanıcı logon'unda çalışacak script yoluna bakılır.
```

```
19. Office Add-in Persistence
Öncelik: Orta
Konum → HKCU\SOFTWARE\Microsoft\Office\<ver>\<app>\Security\Trusted Locations ve Excel\Options → OPEN
Gözlem Notu: Office uygulamalarında otomatik yüklenen add-in veya OPEN key değerlerine bakılır.
```

```
20. RunServices / RunServicesOnce
Öncelik: Düşük
Konum → HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices
Gözlem Notu: Eski Windows sürümlerinden kalan ancak hâlâ okunabilen anahtara bakılır.
```

```
21. Screensaver Persistence
Öncelik: Düşük
Konum → HKCU\Control Panel\Desktop → SCRNSAVE.exe, ScreenSaveActive, ScreenSaverTimeout
Gözlem Notu: SCRNSAVE.exe değerinin beklenmeyen bir binary'ye işaret edip etmediğine bakılır.
```

```
22. NLP Development Platform DLL Override
Öncelik: Düşük
Konum → HKCU\SOFTWARE\Microsoft\CTF\LangBarAddin ve HKLM\SOFTWARE\Microsoft\Input\Locales
Gözlem Notu: Text Input Framework üzerinden yüklenen tanınmayan DLL'lere bakılır.
```

```
23. Netsh Helper DLL
Öncelik: Düşük
Konum → HKLM\SOFTWARE\Microsoft\NetSh → her alt değer
Gözlem Notu: netsh.exe çalıştırıldığında yüklenen tanınmayan DLL'lere bakılır.
```

```
24. Terminal Server InitialProgram
Öncelik: Düşük
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp → InitialProgram
Gözlem Notu: RDP oturumu açıldığında başlatılan program değerine bakılır.
```

```
25. App Paths Override
Öncelik: Düşük
Konum → HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\<exe>
Gözlem Notu: Meşru uygulama adı altında farklı bir binary'nin kayıt edilip edilmediğine bakılır.
```

```
26. KnownDLLs Hijacking
Öncelik: Düşük
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs
Gözlem Notu: Varsayılan Windows DLL listesine eklenen tanınmayan girdilere bakılır.
```

```
27. Font Drivers (GDI)
Öncelik: Düşük
Konum → HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Font Drivers
Gözlem Notu: GDI tarafından yüklenen olağandışı font driver DLL'lerine bakılır.
```
