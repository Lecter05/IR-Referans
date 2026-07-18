# Volatility 2 — V3'te Olmayan Plugin'ler

> Volatility 3 playbook'unu tamamlayıcı niteliktedir.
> Yalnızca V3'te bulunmayan veya sorunlu çalışan, IR sürecinde işe yarayan V2 plugin'lerini içerir.

---

## Genel Kullanım

```bash
python2 vol.py -f dump.mem imageinfo
```

Komut çıktısındaki `Instantiated` kısmındaki seçilip `--profile=`

```bash
python2 vol.py -f bellek.mem --profile=Win10x64_19041 <plugin> [--flags]
```

---

## apihooks

Inline hook, IAT hook ve EAT hook tespiti yapar. V3'e **hiç port edilmedi**.

```bash
python2 vol.py -f bellek.mem --profile=Win10x64_19041 apihooks --pid <PID>
```

- Hook Type sütununda `Inline/Trampoline` → fonksiyonun ilk baytları JMP ile değiştirilmiş.
- `ntdll.dll`, `kernel32.dll`, `kernelbase.dll` içindeki hook'lar ciddi alarm.
- Hook adresi herhangi bir modül dışına (unbacked memory) işaret ediyorsa → enjeksiyon göstergesi.
- AV/EDR ürünleri de API hook'lar — kendi ortamındaki güvenlik ürünlerini baseline olarak tanı.

---

## screenshot

GDI pencere koordinatlarından sanal masaüstü görüntüsü oluşturur. Piksel verisi değil, pencere çerçeveleri ve başlıklarıdır — ama saldırganın o anda neyi açık tuttuğunu gösterir.

```bash
python2 vol.py -f bellek.mem --profile=Win10x64_19041 screenshot --dump-dir ./screenshots/
```

---

## clipboard

Pano içeriğini bellekten kurtarır. Saldırganın kopyaladığı parola, komut veya URL'yi yakalayabilir.

```bash
python2 vol.py -f bellek.mem --profile=Win10x64_19041 clipboard
```

---

## editbox

Tüm GUI Edit ve RichEdit kontrol içeriklerini çıkarır. Herhangi bir penceredeki metin kutularını kapsar — Notepad dahil.

```bash
python2 vol.py -f bellek.mem --profile=Win10x64_19041 editbox
```

---

## cmdscan

`csrss.exe` veya `conhost.exe` belleğinde `COMMAND_HISTORY` yapılarını tarar. Yazılan komutları listeler.

```bash
python2 vol.py -f bellek.mem --profile=Win10x64_19041 cmdscan
```

---

## consoles

cmdscan'in yaptığına ek olarak **komut çıktılarını** da (screen buffer) kurtarır. Saldırganın `whoami`, `net user`, `ipconfig`, `dir` gibi keşif komutlarının çıktılarını doğrudan gösterir.

```bash
python2 vol.py -f bellek.mem --profile=Win10x64_19041 consoles
```

---

## shellbags

Explorer'ın eriştiği klasörlerin kaydını parse eder. Silinmiş klasörler, USB sürücüler, ağ paylaşımları dahil.

```bash
python2 vol.py -f bellek.mem --profile=Win10x64_19041 shellbags
```

**V3 alternatifi:** `windows.registry.hivelist --dump` ile UsrClass.dat hive'ını çıkar → Eric Zimmerman'ın SBECmd aracıyla offline parse et.

---

## shutdowntime

SYSTEM hive'dan son kapanma zamanını çıkarır.

```bash
python2 vol.py -f bellek.mem --profile=Win10x64_19041 shutdowntime
```

**V3 workaround:** `windows.registry.printkey --key "ControlSet001\Control\Windows"` çıktısında ShutdownTime değerini manuel FILETIME decode et.
