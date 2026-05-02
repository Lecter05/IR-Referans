
```
1. RDP Prefetch İzleri
Öncelik: Yüksek
Konum → C:\Windows\Prefetch\mstsc.pf (istemci) ve rdpclip.pf, tstheme.pf (sunucu tarafı)
MITRE: T1021.001
Gözlem Notu: mstsc.exe Prefetch dosyasının son çalışma zamanı ve çalıştırılma sayısına bakılır.
```

```
2. PSExec / RemCom İzleri
Öncelik: Yüksek
Konum → Prefetch (psexec.pf, psexesvc.pf); System.evtx → EID 7045 (PSEXESVC servis kurulumu); $MFT (PSEXESVC.exe)
MITRE: T1021.002
Gözlem Notu: PSEXESVC servisinin kurulma olayına ve hedef sistemdeki Prefetch kaydına bakılır.
```

```
3. WMI Remote Execution İzleri
Öncelik: Yüksek
Konum → Prefetch (wmic.pf, wmiprvse.pf); WMI-Activity Operational → EID 5857, 5861
MITRE: T1021.003
Gözlem Notu: Uzaktan WMI çalıştırmalarında wmiprvse.exe altında başlatılan process ve kaynak IP bilgisine bakılır.
```

```
4. SSH Client (Windows OpenSSH) İzleri
Öncelik: Yüksek
Konum → Prefetch (ssh.pf); C:\Users\<user>\.ssh\known_hosts; ConsoleHost_history.txt
MITRE: T1021.004
Gözlem Notu: Windows yerleşik ssh.exe'nin Prefetch kaydı ve known_hosts dosyasındaki bağlantı izlerine bakılır.
```

```
5. Üçüncü Parti Remote Access Araçları Prefetch İzleri
Öncelik: Yüksek
Konum → Prefetch (teamviewer*.pf, anydesk.pf, screenconnect*.pf, logmein*.pf, splashtop*.pf, rustdesk.pf)
MITRE: T1219
Gözlem Notu: Uzak erişim yazılımlarının Prefetch kayıtlarının varlığına, çalıştırılma sayısına ve son çalışma zamanına bakılır.
```

```
6. ScreenConnect (ConnectWise Control) İzleri
Öncelik: Yüksek
Konum → C:\Program Files (x86)\ScreenConnect Client*\; Prefetch; Amcache
MITRE: T1219
Gözlem Notu: ScreenConnect client dizininin varlığına ve bağlantı loglarına bakılır.
```

```
7. Impacket / Cobalt Strike Araç İzleri
Öncelik: Yüksek
Konum → Prefetch (smbexec_*.pf, atexec_*.pf); $MFT ve $UsnJrnl'de olağandışı dosya isimleri; Amcache
MITRE: T1021.002
Gözlem Notu: Bilinen saldırı araçlarının dosya sistemi ve Prefetch kalıntılarına bakılır.
```

```
8. RDP BAM/DAM Kaydı
Öncelik: Orta
Konum → HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\<SID> → mstsc.exe girdisi
MITRE: T1021.001
Gözlem Notu: mstsc.exe'nin BAM kaydındaki son çalışma zaman damgasına bakılır.
```

```
9. RDP Clipboard İzleri
Öncelik: Orta
Konum → Prefetch (rdpclip.pf); clipboard event logları
MITRE: T1021.001
Gözlem Notu: RDP oturumu sırasında clipboard paylaşımı yapılıp yapılmadığına rdpclip.exe izlerinden bakılır.
```

```
10. Remote Registry Erişimi
Öncelik: Orta
Konum → Security.evtx → EID 4663 (registry erişimi) ve HKLM\SYSTEM\CurrentControlSet\Services\RemoteRegistry → Start
MITRE: T1021
Gözlem Notu: RemoteRegistry servisinin etkinleştirilip etkinleştirilmediğine ve uzaktan registry erişim olaylarına bakılır.
```

```
11. DCOM / MMC Remote Execution
Öncelik: Orta
Konum → Prefetch (mmc.pf, dllhost.pf); Security.evtx → EID 4624 Type 3; DCOM operational logs
MITRE: T1021.003
Gözlem Notu: DCOM üzerinden uzaktan çalıştırılan uygulamaların Prefetch ve ağ oturum izlerine bakılır.
```

```
12. WS-Management / PowerShell Remoting Transcript
Öncelik: Orta
Konum → C:\Users\<user>\Documents\PowerShell_transcript.*.txt (transcript etkinse)
MITRE: T1021.006
Gözlem Notu: PowerShell transcript dosyalarında uzak oturumlarda çalıştırılan komutların tam kaydına bakılır.
```

```
13. RustDesk İzleri
Öncelik: Orta
Konum → C:\Users\<user>\AppData\Roaming\RustDesk\config\*.toml ve log dosyaları
MITRE: T1219
Gözlem Notu: RustDesk yapılandırma dosyalarında bağlantı ID'si ve relay sunucu bilgilerine bakılır.
```
