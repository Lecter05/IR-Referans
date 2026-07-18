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
- İsim kamuflajı ara → svchostt.exe, Isass.exe, scvhost.exe gibi benzer süreç adlarını tespit et.
- svchost.exe süreçlerinin PPID'si **mutlaka** services.exe olmalı.

<details>
<summary>🔎 tıkla/aç</summary>

```bash
(
    dump="${DUMP:-../memoryexmpl/dump.mem}"
    vol="${VOL:-vol.py}"

    csv_file=$(mktemp) || exit 2
    log_file=$(mktemp) || { rm -f "$csv_file"; exit 2; }
    trap 'rm -f "$csv_file" "$log_file"' EXIT

    if ! PYTHONUTF8=1 python3 "$vol" -q -r csv -f "$dump" windows.pslist \
        >"$csv_file" 2>"$log_file"; then
        msg=$(sed -n '1p' "$log_file")
        [ -n "$msg" ] \
            && echo "[HATA] windows.pslist çalışmadı: $msg" >&2 \
            || echo "[HATA] windows.pslist çalışmadı." >&2
        exit 2
    fi

    python3 - "$csv_file" <<'PY'
import csv
import os
import re
import sys
import unicodedata
from collections import Counter
from datetime import datetime, timezone

CRITICAL = (
    "system", "smss.exe", "wininit.exe",
    "services.exe", "lsass.exe",
)

TARGETS = (
    "system", "registry", "smss.exe", "csrss.exe",
    "wininit.exe", "winlogon.exe", "services.exe",
    "lsass.exe", "svchost.exe", "spoolsv.exe",
    "explorer.exe", "userinit.exe", "dllhost.exe",
    "conhost.exe", "taskhostw.exe", "sihost.exe",
    "ctfmon.exe", "dwm.exe", "wmiprvse.exe",
    "msmpeng.exe", "rundll32.exe",
)

CONFUSABLE = str.maketrans({
    "0": "o", "1": "l", "5": "s",
    "а": "a", "е": "e", "о": "o", "р": "p",
    "с": "c", "х": "x", "у": "y", "і": "i",
    "ј": "j", "ѕ": "s", "к": "k", "м": "m",
    "т": "t", "в": "b", "н": "h", "ӏ": "l",
    "ı": "i", "α": "a", "ε": "e", "ο": "o",
    "ρ": "p", "χ": "x", "ι": "i", "κ": "k",
    "τ": "t", "ν": "v",
})


def normalize(value):
    return unicodedata.normalize(
        "NFKC", value
    ).strip().casefold()


def skeleton(value):
    value = unicodedata.normalize("NFKD", normalize(value))
    value = "".join(
        character
        for character in value
        if unicodedata.category(character) not in {"Cf", "Mn"}
    )
    return value.translate(CONFUSABLE)


def distance(first, second, limit=1):
    if abs(len(first) - len(second)) > limit:
        return limit + 1

    previous_previous = None
    previous = list(range(len(second) + 1))

    for row_number, first_character in enumerate(first, 1):
        current = [row_number] + [0] * len(second)
        row_minimum = current[0]

        for column_number, second_character in enumerate(second, 1):
            current[column_number] = min(
                previous[column_number] + 1,
                current[column_number - 1] + 1,
                previous[column_number - 1]
                + (first_character != second_character),
            )

            if (
                previous_previous is not None
                and row_number > 1
                and column_number > 1
                and first_character == second[column_number - 2]
                and first[row_number - 2] == second_character
            ):
                current[column_number] = min(
                    current[column_number],
                    previous_previous[column_number - 2] + 1,
                )

            row_minimum = min(
                row_minimum, current[column_number]
            )

        if row_minimum > limit:
            return limit + 1

        previous_previous, previous = previous, current

    return previous[-1]


def impersonation_target(raw_name):
    name = normalize(raw_name)

    if name in TARGETS:
        return None

    name_skeleton = skeleton(raw_name)
    matches = []

    for target in TARGETS:
        target_skeleton = skeleton(target)

        if name_skeleton == target_skeleton:
            matches.append((0, target))
            continue

        if min(
            distance(name, target),
            distance(name_skeleton, target_skeleton),
        ) <= 1:
            matches.append((1, target))
            continue

        stem, extension = os.path.splitext(name)
        target_stem, target_extension = os.path.splitext(target)

        if stem == target_stem and extension != target_extension:
            matches.append((2, target))
            continue

        if (
            re.fullmatch(
                re.escape(target_stem) + r"[-_.]?\d{1,3}",
                stem,
            )
            and extension in {
                target_extension, "", ".exe", ".com", ".scr"
            }
        ):
            matches.append((3, target))

    return min(matches)[1] if matches else None


def parse_time(value):
    value = (value or "").strip()

    if value.casefold() in {
        "", "n/a", "not available", "none", "-"
    }:
        return None

    if value.endswith(" UTC"):
        value = value[:-4] + "+00:00"
    elif value.endswith("Z"):
        value = value[:-1] + "+00:00"

    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return None

    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)

    return parsed.timestamp()


try:
    handle = open(
        sys.argv[1],
        encoding="utf-8-sig",
        newline="",
    )
except OSError:
    print("[HATA] Volatility çıktısı okunamadı.", file=sys.stderr)
    raise SystemExit(2)

rows = []

with handle:
    reader = csv.DictReader(handle)
    fields = {
        (field or "").strip()
        for field in (reader.fieldnames or [])
    }

    if not {
        "PID", "PPID", "ImageFileName"
    }.issubset(fields):
        print(
            "[HATA] windows.pslist CSV çıktısı geçersiz.",
            file=sys.stderr,
        )
        raise SystemExit(2)

    for line_number, raw in enumerate(reader, 2):
        if None in raw:
            print(
                f"[HATA] CSV satırı bozuk: {line_number}",
                file=sys.stderr,
            )
            raise SystemExit(2)

        row = {
            (key or "").strip(): (value or "").strip()
            for key, value in raw.items()
        }

        pid = row.get("PID", "")
        ppid = row.get("PPID", "")
        image = row.get("ImageFileName", "")

        if not pid.isdigit() or not ppid.isdigit() or not image:
            print(
                f"[HATA] CSV satırı bozuk: {line_number}",
                file=sys.stderr,
            )
            raise SystemExit(2)

        rows.append({
            "pid": int(pid),
            "ppid": int(ppid),
            "image": image,
            "name": normalize(image),
            "create": parse_time(row.get("CreateTime")),
            "exit": parse_time(row.get("ExitTime")),
        })

if not rows:
    print(
        "[HATA] windows.pslist süreç üretmedi.",
        file=sys.stderr,
    )
    raise SystemExit(2)

pid_counts = Counter(row["pid"] for row in rows)
duplicate_pids = sorted(
    pid for pid, count in pid_counts.items() if count > 1
)

if duplicate_pids:
    print(
        "[HATA] Yinelenen PID: "
        + ",".join(map(str, duplicate_pids)),
        file=sys.stderr,
    )
    raise SystemExit(2)

by_pid = {row["pid"]: row for row in rows}
alerts = []

# Kritik süreçlerin sayısı
for name in CRITICAL:
    matches = [row for row in rows if row["name"] == name]

    if not matches:
        alerts.append((0, 0, f"[!] EKSİK: {name}"))

    elif len(matches) > 1:
        pid_text = ",".join(
            str(row["pid"])
            for row in sorted(
                matches, key=lambda item: item["pid"]
            )
        )
        alerts.append(
            (0, 0, f"[!] ÇOKLU: {name} PID={pid_text}")
        )

# Sistem süreci adı taklitleri
for row in rows:
    target = impersonation_target(row["image"])

    if target:
        alerts.append((
            1,
            row["pid"],
            f"[!] TAKLİT: PID={row['pid']} "
            f"NAME={row['image']} -> {target}",
        ))

# svchost.exe ebeveyn kontrolü
services = [
    row for row in rows
    if row["name"] == "services.exe"
]
service_pids = {row["pid"] for row in services}

for service in services:
    if service["exit"] is not None:
        alerts.append((
            1,
            service["pid"],
            f"[!] SONLANMIŞ: services.exe "
            f"PID={service['pid']}",
        ))

if services:
    expected = ",".join(map(str, sorted(service_pids)))

    for row in rows:
        if row["name"] != "svchost.exe":
            continue

        if row["ppid"] not in service_pids:
            parent = by_pid.get(row["ppid"])

            if parent:
                parent_text = (
                    f"{parent['image']}({row['ppid']})"
                )
            else:
                parent_text = (
                    f"BULUNAMADI({row['ppid']})"
                )

            alerts.append((
                1,
                row["pid"],
                f"[!] EBEVEYN: PID={row['pid']} "
                f"svchost.exe <- {parent_text}; "
                f"beklenen services.exe({expected})",
            ))

        if len(services) == 1:
            service = services[0]

            if (
                row["create"] is not None
                and service["create"] is not None
                and row["create"] < service["create"]
            ):
                alerts.append((
                    1,
                    row["pid"],
                    f"[!] ZAMAN: PID={row['pid']} "
                    "svchost.exe services.exe'den "
                    "önce başlamış",
                ))

if alerts:
    for _, _, message in sorted(alerts):
        print(message)

    raise SystemExit(1)

print("OK: şüpheli süreç bulunmadı")
PY
)
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
