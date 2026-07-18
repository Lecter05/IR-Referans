## DİĞER / NADİR ARTIFACT'LAR

```
1. Active Setup (StubPath)
Öncelik: Orta
Konum → HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\{GUID} → StubPath
Gözlem Notu: Kullanıcı ilk logon'unda çalıştırılan StubPath komutuna bakılır.
```

```
2. Chrome/Edge Extension Persistence
Öncelik: Orta
Konum → %LOCALAPPDATA%\Google\Chrome\User Data\Default\Extensions\ ve %LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Extensions\
Gözlem Notu: Web mağazası dışından yüklenen (sideloaded) veya şüpheli izinli uzantılara bakılır.
```

```
3. Windows 11 Settings → Startup
Öncelik: Orta
Erişim: Live System
Konum → Task Manager → Startup sekmesi / Settings → Apps → Startup
Gözlem Notu: Win11 Settings'de Startup uygulamaları listesindeki tanınmayan girişlere bakılır.
```

```
4. COM — TreatAs Hijacking
Öncelik: Düşük
Konum → HKLM\SOFTWARE\Classes\CLSID\{GUID}\TreatAs

Gözlem Notu: TreatAs alt anahtarının meşru bir CLSID'yi zararlı bir CLSID'ye yönlendirip yönlendirmediğine bakılır.
```

```
5. Time Provider DLL
Öncelik: Düşük
Konum → HKLM\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\<n> → DllName
Gözlem Notu: w32time servisi tarafından yüklenen özel DLL'lere bakılır.
```

```
6. Browser Helper Object (BHO)
Öncelik: Düşük
Konum → HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects\{CLSID}
Gözlem Notu: Internet Explorer / Edge Legacy açılışında yüklenen CLSID'lere bakılır.
```

```
7. Winsock Layered Service Provider (LSP)
Öncelik: Düşük
Konum → HKLM\SYSTEM\CurrentControlSet\Services\WinSock2\Parameters\Protocol_Catalog9
Gözlem Notu: Ağ trafiğine araya giren kayıtlı LSP DLL'lerine bakılır.
```

```
8. Port Monitor DLL
Öncelik: Düşük
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors
Gözlem Notu: Print Spooler ile SYSTEM olarak yüklenen özel monitor DLL'lerine bakılır.
```

```
9. Windows Sandbox AutoStart
Öncelik: Düşük
Konum → C:\Users\<user>\*.wsb dosyaları
Gözlem Notu: Sandbox konfigürasyon dosyalarında MappedFolder ve LogonCommand değerlerine bakılır.
```

```
10. AppX/MSIX Startup Task
Öncelik: Düşük
Konum → Paket Manifest → desktop:Extension Category="windows.startupTask"
Gözlem Notu: UWP/MSIX paketlerindeki startupTask deklarasyonlarına bakılır (Win10/11).
```
