
```
1. Dosya İsim Maskeleme (Masquerading)
Öncelik: Yüksek
Konum → Dosya sistemi genelinde; Prefetch ve Amcache
MITRE: T1036.005
Gözlem Notu: svchost.exe, explorer.exe gibi meşru isimlerin olağandışı dizinlerden (%TEMP%, %APPDATA%) çalıştırılıp çalıştırılmadığına bakılır.
```

```
2. Memory-Only Malware (Fileless)
Öncelik: Yüksek
Erişim: Live System
Konum → Sysmon EID 1 (CommandLine); PowerShell EID 4104; ETW; bellek analizi
MITRE: T1059.001
Gözlem Notu: Diske hiç yazılmayan payload'ların PowerShell, WMI veya .NET reflection ile bellekte çalıştırılıp çalıştırılmadığına bakılır.
```

```
3. Çift Uzantı / RLO (Right-to-Left Override) Kullanımı
Öncelik: Orta
Konum → $MFT dosya adları; $UsnJrnl; Prefetch
MITRE: T1036.002
Gözlem Notu: Dosya adlarında Unicode RLO karakteri (U+202E) veya çift uzantı (rapor.pdf.exe) kullanımına bakılır.
```

```
4. Packed / Obfuscated Binary'ler
Öncelik: Orta
Konum → Amcache (hash); dosya entropy analizi
MITRE: T1027.002
Gözlem Notu: Çalıştırılan dosyaların yüksek entropy değerine (>7.0) veya bilinen packer imzalarına (UPX, Themida) sahip olup olmadığına bakılır.
```

```
5. BitLocker / EFS ile Kanıt Şifreleme
Öncelik: Orta
Konum → HKLM\SOFTWARE\Policies\Microsoft\FVE; EFS sertifikaları; $EFS attribute
MITRE: T1486
Gözlem Notu: Belirli klasör veya dosyaların olay sonrası şifrelenip şifrelenmediğine ve şifreleme zamanlamasına bakılır.
```

```
6. Virtual Disk / Encrypted Container Kullanımı
Öncelik: Orta
Konum → Prefetch (veracrypt.pf, diskpart.pf, vhdx mount); Registry'de MountedDevices
MITRE: T1027
Gözlem Notu: VeraCrypt, BitLocker To Go veya VHD/VHDX container mount izlerinin Prefetch ve registry'de bulunup bulunmadığına bakılır.
```

```
7. Certutil ile Dosya İndirme / Decode İzleri
Öncelik: Orta
Konum → Prefetch → certutil.pf; %USERPROFILE%\AppData\LocalLow\Microsoft\CryptnetUrlCache\
MITRE: T1140
Gözlem Notu: certutil -urlcache veya certutil -decode komutlarının Prefetch ve CryptnetUrlCache'deki izlerine bakılır.
```

```
8. Process Hollowing / Injection İzleri
Öncelik: Orta
Erişim: Live System
Konum → Sysmon → EID 8 (CreateRemoteThread), EID 10 (ProcessAccess); bellek analizi malfind
MITRE: T1055
Gözlem Notu: Meşru bir process'e kod enjeksiyonu yapılıp yapılmadığına Sysmon thread ve process erişim loglarından bakılır.
```

```
9. Steganografi ile Veri Gizleme
Öncelik: Düşük
Konum → Büyük boyutlu görsel dosyalar; olağandışı ADS stream'leri
MITRE: T1027.003
Gözlem Notu: Görsel dosyaların beklenen boyuttan çok büyük olup olmadığına veya dosya sonunda ek veri bulunup bulunmadığına bakılır.
```

```
10. Secure Boot / UEFI Rootkit İzleri
Öncelik: Düşük
Konum → EFI System Partition → \EFI\Microsoft\Boot\ ve \EFI\Boot\
MITRE: T1542.003
Gözlem Notu: EFI bölümündeki bootloader dosyalarının hash'inin bilinen temiz değerlerle eşleşip eşleşmediğine bakılır.
```

```
11. Anti-VM / Anti-Sandbox Kontrolleri
Öncelik: Düşük
Konum → Sysmon EID 1 (CommandLine'da WMI sorguları); PowerShell EID 4104
MITRE: T1497.001
Gözlem Notu: Win32_ComputerSystem sorguları veya sandbox tespiti yapan komutların çalıştırılıp çalıştırılmadığına bakılır.
```
