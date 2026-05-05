# Volatility 3 — Bellek Analizi Playbook

---

## Faz 1 — Bağlam Oluşturma

### windows.info
```bash
python3 vol.py -f dump.mem windows.info
```
Bellek imajının SystemTime değerinden olay zaman çizelgesinin referans noktası oluşturulur.

### windows.sessions

- **Session 0** — Servis oturumu, yalnızca SYSTEM olmalı. Beklenmedik kullanıcı hesabı var mı kontrol et.
- **Session 1+** — Etkileşimli kullanıcı oturumu. Hangi kullanıcılar oturum açmış incele.
- **Console** — Fiziksel konsol erişimi. Odak noktası — doğrudan klavye/ekran etkileşimi.

---

## Faz 2 — Süreç Analizi

### windows.psscan

Gizlenmiş ve yakın zamanda sonlanmış süreçleri yakalar. **Her vakada** pslist ile psscan diff'lenmelidir:

```bash
vol.py -f bellek.mem -r csv windows.pslist  > pslist.csv
vol.py -f bellek.mem -r csv windows.psscan > psscan.csv
sort pslist.csv > a; sort psscan.csv > b; diff a b > gizlenmis_surecler.txt
```

### windows.pslist
- System, smss.exe, wininit.exe, services.exe, lsass.exe → her birinden **yalnızca bir tane** olmalı.

<details>
<summary>🔎 Duplicate core process kontrol komutu — tıkla/aç</summary>

```bash
python3 vol.py -q -f ../memoryexmpl/dump.mem windows.pslist 2>/dev/null \
| awk '
$1~/^[0-9]+$/ {
    total++
    n=tolower($3)
    if(n~/^(system|wininit\.exe|services\.exe|lsass\.exe)$/) {
        c[n]++
        r[n]=r[n] sprintf("    PID=%s PPID=%s NAME=%s\n",$1,$2,$3)
    }
}
END {
    if(total==0) {
        print "[HATA] Volatility cikti uretmedi. Dump gecersiz veya desteklenmiyor olabilir."
        exit
    }
    for(n in c) {
        if(c[n]>1) { f=1; printf "[!] %s %dx\n%s",n,c[n],r[n] }
    }
    if(!f) print "OK: duplicate yok"
}
'
```

</details>

---

- İsim kamuflajı ara → svchostt.exe, Isass.exe (büyük i), scvhost.exe vb. Alttaki komutla yasal süreçleri filreleyip yasal olmayan süreçlerin ayrımı yapılabilir.

<details>
<summary>🔎 İsim kamuflajı tespit komutu — tıkla/aç</summary>

```bash
python3 vol.py -q -f ../memoryexmpl/dump.mem windows.pslist 2>/dev/null | awk '
BEGIN {
    # --- Cekirdek sistem ---
    w["system"]=1;          w["registry"]=1;        w["smss.exe"]=1
    w["csrss.exe"]=1;       w["wininit.exe"]=1;     w["winlogon.exe"]=1
    w["services.exe"]=1;    w["lsass.exe"]=1;       w["svchost.exe"]=1
    w["fontdrvhost.ex"]=1;  w["dwm.exe"]=1;         w["memcompression"]=1

    # --- Oturum / kullanici arayuzu ---
    w["sihost.exe"]=1;      w["taskhostw.exe"]=1;   w["ctfmon.exe"]=1
    w["explorer.exe"]=1;    w["userinit.exe"]=1;    w["logonui.exe"]=1

    # --- Shell / UWP altyapisi ---
    w["shellexperienc"]=1;  w["runtimebroker."]=1;  w["applicationfra"]=1
    w["dllhost.exe"]=1;     w["backgroundtask"]=1;  w["textinputhost."]=1
    w["startmenuexper"]=1;  w["windowsinterna"]=1;  w["smartscreen.ex"]=1
    w["systemsettings"]=1;  w["useroobebroker"]=1;  w["winstore.app.e"]=1

    # --- Servisler / altyapi ---
    w["spoolsv.exe"]=1;     w["msiexec.exe"]=1;     w["conhost.exe"]=1
    w["dashost.exe"]=1;     w["audiodg.exe"]=1;     w["msdtc.exe"]=1
    w["vssvc.exe"]=1;       w["wermgr.exe"]=1;      w["perfmon.exe"]=1
    w["timeout.exe"]=1;     w["sppsvc.exe"]=1;      w["wlms.exe"]=1
    w["uhssvc.exe"]=1;      w["wmiprvse.exe"]=1;    w["wmiadap.exe"]=1

    # --- Arama ---
    w["searchindexer."]=1;  w["searchprotocol"]=1;  w["searchfilterho"]=1
    w["searchapp.exe"]=1;   w["searchui.exe"]=1

    # --- Windows Defender ---
    w["msmpeng.exe"]=1;     w["mpcmdrun.exe"]=1;    w["nissrv.exe"]=1
    w["mpsigstub.exe"]=1;   w["securityhealth"]=1;  w["sgrmbroker.exe"]=1
    w["am_delta.exe"]=1

    # --- Windows Update / bakim ---
    w["wuauclt.exe"]=1;     w["mousocoreworke"]=1;  w["tiworker.exe"]=1
    w["trustedinstall"]=1;  w["compattelrunne"]=1;  w["devicecensus.e"]=1
    w["musnotificatio"]=1;  w["updateplatform"]=1

    # --- Microsoft uygulamalari ---
    w["msedge.exe"]=1;      w["microsoftedge."]=1;  w["microsoftedgeu"]=1
    w["microsoftedgec"]=1;  w["microsoftedges"]=1;  w["browser_broker"]=1
    w["onedrive.exe"]=1;    w["onedrivesetup."]=1;  w["yourphone.exe"]=1
    w["hxtsr.exe"]=1;       w["microsoft.phot"]=1;  w["microsoft.shar"]=1
    w["windows.warp.j"]=1
}
$1~/^[0-9]+$/ {
    total++
    if(!(tolower($3) in w)) {
        printf "[?] PID=%-6s PPID=%-6s NAME=%s\n", $1, $2, $3
        found++
    }
}
END {
    if(total==0) {
        print "[HATA] Volatility cikti uretmedi. Dump gecersiz veya desteklenmiyor olabilir."
        exit
    }
    if(!found) print "OK: tum surec adlari bilinen listede"
}
'
```

</details>

---

- svchost.exe süreçlerinin PPID'si **mutlaka** services.exe olmalı. Hızlı kontrol için Komutu kopyala

<details>
<summary>🔎 svchost.exe PPID kontrol komutu — tıkla/aç</summary>

```bash
python3 vol.py -q -f ../memoryexmpl/RogueProcessCase1.mem windows.pslist 2>/dev/null | awk '
$1~/^[0-9]+$/ {
    total++
    pid[$1]=$3
    if(tolower($3)=="services.exe") s=$1
    if(tolower($3)=="svchost.exe") { n++; sp[n]=$1; sppid[n]=$2 }
}
END {
    if(total==0) {
        print "[HATA] Volatility cikti uretmedi. Dump gecersiz veya desteklenmiyor olabilir."
        exit
    }
    if(s=="") {
        print "[UYARI] services.exe bulunamadi. Dump eksik veya bozuk olabilir. Sonuclar guvenilir degil."
        exit
    }
    found=0
    for(i=1;i<=n;i++) {
        if(sppid[i]!=s) {
            printf "[!] PID=%s PPID=%s PARENT=%s NAME=svchost.exe\n", sp[i], sppid[i], pid[sppid[i]]
            found=1
        }
    }
    if(!found) print "OK: svchost anomalisi yok"
}
'
```

</details>

### windows.pstree

Ebeveyn-çocuk ilişkilerini ağaç yapısında gösterir. Temp, ProgramData, Downloads gibi şüpheli dizinlerden çalışan süreçleri tespit et.

### windows.cmdline

Her sürecin başlatılma argümanlarını gösterir.

- powershell.exe, cmd.exe, wscript.exe, mshta.exe → argümanları mutlaka incele.
- svchost.exe → -k parametresi ile başlamayan örnekler şüphelidir.

---

## Faz 3 — Ağ Bağlantıları

### windows.netscan & windows.netstat

Yalnızca anlık aktif bağlantıları gösterir. İkisi de diff'lenmelidir:

```bash
vol.py -f bellek.mem -r csv windows.netstat > netstat.csv
vol.py -f bellek.mem -r csv windows.netscan > netscan.csv
sort netstat.csv > c; sort netscan.csv > d; diff c d > gizlenmis_ag.txt
```

**Şüpheli göstergeler:**

- notepad.exe, calc.exe, rundll32.exe, powershell.exe gibi süreçlerin dış IP'ye ESTABLISHED bağlantısı.
- Bilinen saldırı portları: 4444 (Metasploit), 8443 (Empire), 1337, 31337.
- DNS çözümlemesi olmayan ham IP adresleri.
- İş istasyonunda 80/443 üzerinde LISTENING durumunda bekleyen beklenmedik ikili dosyalar (örn. hfs.exe).

---

## Faz 4 — Kod Enjeksiyonu

### windows.malfind

Her sürecin VAD ağacını dolaşarak şu kriterlerin **üçünü birden** sağlayan bölgeleri raporlar:

1. PAGE_EXECUTE_READWRITE koruması
2. Private memory (VadS tag, PrivateMemory=1)
3. Herhangi bir dosyaya map edilmemiş

Eşleşen her VAD'ın ilk 64 baytı hex + disassembly olarak basılır.

**Uyarı:** Bazı yükleyiciler (Coreflood, Cobalt Strike loader vb.) PE başlığını sıfırlar veya önce RW tahsis edip ardından VirtualProtect ile RWX'e çevirir — bu durumda malfind sessiz kalabilir.

**Not:** MsMpEng.exe → Windows Defender süreci; false positive üretebilir.

**Şüpheli bulgu varsa izlenecek adımlar:**

```bash
# 1. Şüpheli bellek bölgesini dump et
vol.py -f bellek.mem windows.malfind --dump --pid <PID>

# 2. String analizi
strings dosya.dmp | grep -i 'http\|https\|cmd\|powershell'

# 3. Sandbox'a gönder (VirusTotal, Any.Run, Hybrid Analysis vb.)
```

### windows.hollowprocesses (ek kontrol)

Process Hollowing tespiti için kullanılır. Malfind sonuçlarını destekler.

### windows.vadinfo --pid PID (ek kontrol)

Belirli bir sürecin tüm VAD bölgelerini listeler. PAGE_EXECUTE_READWRITE korumalı bölgeleri filtrele.

---

## Faz 5 — Handle, DLL ve Dosya Analizi

### windows.handles --pid PID

Sürecin açık tuttuğu dosya, registry key ve mutant handle'larını listeler.

- **File:** Temp, ProgramData, Public gibi dizinlere bırakılan dosyaları ara.
- **Key:** Kalıcılık (persistence) yollarına işaret eden registry anahtarlarını kontrol et (Run, RunOnce, Services vb.).

### windows.dlllist & windows.ldrmodules

%TEMP%, %APPDATA%, C:\ProgramData\, Downloads veya kullanıcı profili altından yüklenen DLL'ler enjeksiyon göstergesidir.

**Şüpheli DLL bulunursa:**

```bash
# 1. Dosyanın bellekteki konumunu bul
vol.py -f bellek.mem windows.filescan | grep -i 'supheli.dll'

# 2. Dosyayı dump et (filescan'den alınan sanal adres ile)
vol.py -f bellek.mem windows.dumpfiles --virtaddr 0x<ADRES>
```

---

## Faz 6 — Kalıcılık ve Registry

### windows.svcscan

Kayıtlı servisleri listeler. Anormal dizinlerden çalışan servisleri filtrele:

```bash
vol.py -f bellek.mem windows.svcscan | \
  egrep -i 'TEMP|APPDATA|ProgramData|Downloads|PerfLogs|Public|Recycle\.Bin|Tasks|Spool|Startup|Wbem|System Volume Information'
```

Şüpheli binary bulunursa → windows.filescan + windows.dumpfiles --virtaddr ile dump et.

### windows.registry.hivelist

Bellekte bulunan registry hive'larını listeler. Offline analiz için dump edilebilir:

```bash
vol.py -f bellek.mem windows.registry.hivelist --dump -o hives/
```

### windows.hashdump

Yerel kullanıcı hesaplarının NTLM hash değerlerini döker.

- **aad3b435...** (LM kısmı) → LM hash devre dışı/yok.
- **31d6cfe0...** (NT kısmı) → Boş (şifresiz) parola.

**Önemli:** Domain hesapları hashdump çıktısında yer almaz. Bunlar için aşağıdaki eklentiler kullanılır (pycryptodome kurulu olmalı):

- **windows.lsadump** → LSA secrets — düz metin parolalar, VPN/servis şifreleri.
- **windows.cachedump** → MSCache v2 — önbelleğe alınmış domain kullanıcı hash'leri.

Elde edilen hash değerleri Hashcat veya John the Ripper ile kırılabilir.
