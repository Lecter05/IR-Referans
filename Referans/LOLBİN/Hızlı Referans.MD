

⚠️ = Trend / APT tercihli

| Binary | Kullanım | Şüpheli Durum |
|---|---|---|
| **EXECUTE** | | |
| mshta.exe | Execute | + URL veya vbscript: argümanı |
| rundll32.exe | Execute | + javascript: veya imzasız DLL |
| regsvr32.exe | Execute | + /i:http + scrobj.dll |
| wmic.exe ⚠️ | Execute | process call create veya /FORMAT:http:// |
| wscript.exe | Execute | //e: flag ile uzantı maskeleme |
| cscript.exe | Execute | //e: flag ile uzantı maskeleme |
| msiexec.exe | Execute / Download | /i http:// veya UNC path |
| msbuild.exe | Execute | Temp'te proje dosyası |
| installutil.exe | Execute | /logfile= /LogToConsole=false /U |
| csc.exe | Execute / Compile | Temp'te .cs → .exe derleme |
| jsc.exe | Execute / Compile | Temp'te JScript derleme |
| ilasm.exe | Execute / Compile | IL kaynak kodu derleme |
| cmstp.exe | Execute / UAC Bypass | + .inf dosyası |
| forfiles.exe | Execute | /c parametresinde cmd veya powershell |
| mavinject.exe | Execute / Inject | /INJECTRUNNING + DLL |
| wuauclt.exe ⚠️ | Execute | /UpdateDeploymentProvider + /RunHandlerComServer |
| mmc.exe ⚠️ | Execute / Lateral | -Embedding argümanı |
| odbcconf.exe ⚠️ | Execute | /a {REGSVR + DLL} |
| hh.exe | Execute | + .chm dosyası veya uzak URL |
| pcalua.exe | Execute | -a + zararlı binary veya UNC path |
| bash.exe | Execute | -c ile komut çalıştırma, WSL bypass |
| at.exe | Execute | Deprecated task scheduler, kesin şüpheli |
| atbroker.exe | Execute | + zararlı binary argümanı |
| conhost.exe | Execute | --headless + cmd komutu |
| control.exe | Execute | + imzasız .cpl dosyası |
| explorer.exe | Execute | /root, + UNC path |
| extexport.exe | Execute | + imzasız DLL yükleme |
| ftp.exe | Execute | -s: script dosyası |
| gpscript.exe | Execute | /logon veya /startup ile script |
| ie4uinit.exe | Execute | -BaseSettings ile INF çalıştırma |
| ieexec.exe | Execute | + uzak .NET EXE URL |
| infdefaultinstall.exe | Execute | + .inf dosyası |
| msconfig.exe | Execute | /5 ile cmd spawn |
| msdt.exe | Execute | + MSI veya PCWDiagnostic |
| pcwrun.exe | Execute | + binary argümanı |
| presentationhost.exe | Execute | + uzak .xbap URL |
| rasautou.exe | Execute | + imzasız DLL |
| regasm.exe | Execute | + imzasız .NET DLL |
| register-cimprovider.exe | Execute | + imzasız DLL |
| regsvcs.exe | Execute | + imzasız .NET DLL |
| runonce.exe | Execute | /AlternateShellStartup ile |
| runscripthelper.exe | Execute | + script dosyası |
| scriptrunner.exe | Execute | -appvscript + binary |
| settingsynchhost.exe | Execute | + binary argümanı |
| syncappvpublishingserver.exe | Execute | Inline PowerShell komutu |
| verclsid.exe | Execute | + CLSID ile COM hijacking |
| wab.exe | Execute | + imzasız DLL yükleme |
| xwizard.exe | Execute | RunWizard /u + {CLSID} |
| addinutil.exe | Execute | + .NET add-in DLL |
| aspnet_compiler.exe | Execute / AWL Bypass | + proje dosyası |
| microsoft.workflow.compiler.exe | Execute / AWL Bypass | + XOML/VB.Net dosyası |
| dfsvc.exe | Execute / AWL Bypass | ClickOnce ile uzak binary |
| msedge.exe | Execute | --headless + uzak URL |
| customshellhost.exe | Execute | + binary argümanı |
| change.exe | Execute | + binary argümanı |
| stordiag.exe | Execute | + binary argümanı |
| workfolders.exe | Execute | + binary argümanı |
| ttdinject.exe | Execute | /launch + DLL yükleme |
| dnscmd.exe | Execute | /serverlevelplugindll + DLL |
| **DOWNLOAD** | | |
| certutil.exe ⚠️ | Download | -urlcache -split -f |
| bitsadmin.exe | Download / Persist | + URL + lokal path |
| MpCmdRun.exe | Download | -DownloadFile parametresi |
| powershell.exe | Execute / Download | -enc / IEX / DownloadString |
| CertReq.exe ⚠️ | Download / Upload | -Post + dış URL |
| finger.exe | Download | dış IP port 79 bağlantısı |
| findstr.exe | Download | UNC path + > yönlendirmesi |
| desktopimgdownldr.exe | Download | /lockscreenurl:http:// |
| expand.exe | Download / Copy | + UNC path kaynak |
| extrac32.exe | Download / Copy | + UNC path kaynak |
| appinstaller.exe | Download | + uzak .appinstaller URL |
| cmdl32.exe | Download | özel config ile dosya indirme |
| diantz.exe | Download | + UNC path kaynak |
| gfxdownloadwrapper.exe | Download | + URL argümanı |
| ieexec.exe | Download | + uzak .NET EXE URL |
| imewdbld.exe | Download | + URL argümanı |
| ldifde.exe | Download | + URL |
| makecab.exe | Download | + UNC path kaynak |
| configsecuritypolicy.exe | Download / Upload | + URL argümanı |
| datasvcutil.exe | Upload | + dış URL |
| **DUMP / CREDENTIAL** | | |
| ntdsutil.exe ⚠️ | Dump | ifm create |
| diskshadow.exe | Dump | + script dosyası argümanı |
| esentutl.exe | Dump / Copy | /y + ntds.dit veya SAM |
| reg.exe | Persist / Dump | save SAM/SYSTEM/SECURITY |
| cmdkey.exe | Credential | /list ile kayıtlı credential listeleme |
| tttracer.exe | Dump | process memory dump |
| **PERSISTENCE** | | |
| schtasks.exe | Persistence | /create + Temp/AppData path |
| sc.exe | Persistence | binPath= Temp veya kullanıcı dizini |
| bitsadmin.exe | Persistence | SetNotifyCmdLine parametresi |
| at.exe | Persistence | Deprecated, görülmesi şüpheli |
| **UAC BYPASS** | | |
| fodhelper.exe | UAC Bypass | ms-settings registry key yazımı |
| eventvwr.exe | UAC Bypass | mscfile registry key yazımı |
| ComputerDefaults.exe | UAC Bypass | ms-settings registry key yazımı |
| sdclt.exe | UAC Bypass | App Paths\control.exe key yazımı |
| eudcedit.exe | UAC Bypass | mscfile registry key yazımı |
| iscsicpl.exe | UAC Bypass | + imzasız DLL |
| **ANTI-FORENSICS** | | |
| vssadmin.exe ⚠️ | Anti-Forensics | delete shadows /all /quiet |
| bcdedit.exe ⚠️ | Anti-Forensics | recoveryenabled No |
| wbadmin.exe ⚠️ | Anti-Forensics | delete catalog / systemstatebackup |
| fsutil.exe | Anti-Forensics | usn deletejournal |
| cipher.exe | Anti-Forensics | /w: + disk yolu |
| **DEFENSE EVASION** | | |
| fltMC.exe | Defense Evasion | unload SysmonDrv |
| **NETWORK / DISCOVERY** | | |
| netsh.exe ⚠️ | Firewall / Proxy | portproxy veya firewall rule ekleme |
| nltest.exe ⚠️ | Discovery | /domain_trusts veya /dclist |
| **COPY / MASQUERADE** | | |
| robocopy.exe | Copy | + UNC kaynak veya hedef |
| replace.exe | Copy | + UNC kaynak dosyası |
| print.exe | Copy | + UNC path ile dosya kopyalama |
| colorcpl.exe | Copy / Masquerade | imzalı binary ile dosya kopyalama |
| esentutl.exe | Copy | /y ile kilitli dosya kopyalama |
| **SURVEILLANCE** | | |
| psr.exe | Surveillance | Problem Steps Recorder — ekran kaydı |
| **ADS (Alternate Data Streams)** | | |
| cmd.exe | ADS | type file > target:stream |
| bitsadmin.exe | ADS | /setcustomheaders ile ADS yazma |
| certutil.exe | ADS | -urlcache ile ADS'e indirme |
| makecab.exe | ADS | sıkıştırılmış veriyi ADS'e yazma |
| extrac32.exe | ADS | extract ile ADS'e çıkarma |

