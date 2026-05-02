
```
1. Kerberos TGT Request (AS-REQ) — Event ID 4768
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1558.004
Gözlem Notu: AS-REP Roasting için şifreleme türünün RC4 (0x17) olup olmadığına ve pre-auth devre dışı hesaplara bakılır.
```

```
2. Kerberos TGS Request (TGS-REQ) — Event ID 4769
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1558.003
Gözlem Notu: Kerberoasting belirtisi olarak aynı kullanıcıdan kısa sürede çok sayıda farklı SPN'ye RC4 ticket isteğine bakılır.
```

```
3. Golden Ticket Göstergeleri
Öncelik: Yüksek
Konum → Security.evtx → Event ID 4769 (anormal lifetime), 4624 (domain admin logon olağandışı kaynak)
MITRE: T1558.001
Gözlem Notu: TGT ömrünün domain policy'den çok uzun olmasına, bilinmeyen hesap adlarına veya SID anomalisine bakılır.
```

```
4. Silver Ticket Göstergeleri
Öncelik: Yüksek
Konum → Security.evtx → Event ID 4624 (Type 3, TGS olmadan doğrudan service access), 4634
MITRE: T1558.002
Gözlem Notu: DC'de karşılık gelen TGS isteği olmadan yapılan service erişimlerine bakılır.
```

```
5. Pass-the-Hash (PtH) Göstergeleri
Öncelik: Yüksek
Konum → Security.evtx → Event ID 4624 (NTLM, LogonType 3/9, LogonProcess: NtLmSsp), 4776
MITRE: T1550.002
Gözlem Notu: NTLM ağ oturum açmalarında kaynak workstation adının hedef ile uyumsuz olmasına ve LmPackageName'in NTLM V1/V2 olmasına bakılır.
```

```
6. Pass-the-Ticket (PtT) Göstergeleri
Öncelik: Yüksek
Konum → Security.evtx → Event ID 4768, 4769 (farklı IP'den aynı hesap), 4624 (Kerberos logon anormal kaynak)
MITRE: T1550.003
Gözlem Notu: Aynı Kerberos ticket'ının farklı IP adreslerinden kullanılıp kullanılmadığına bakılır.
```

```
7. DCSync İzleri — Event ID 4662
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1003.006
Gözlem Notu: DC olmayan bir bilgisayardan gelen replication erişim isteklerine (Properties: 1131f6aa-..., 1131f6ad-...) bakılır.
```

```
8. Overpass-the-Hash (Pass-the-Key)
Öncelik: Orta
Konum → Security.evtx → Event ID 4768 (RC4 yerine AES256 veya tam tersi anormal şifreleme değişimi)
MITRE: T1550.002
Gözlem Notu: NTLM hash ile Kerberos TGT edinilip edinilmediğine, AS-REQ'deki şifreleme türü anomalisine bakılır.
```

```
9. NTLM Operational Log
Öncelik: Orta
Konum → Microsoft-Windows-NTLM%4Operational.evtx
MITRE: T1550.002
Gözlem Notu: NTLM kimlik doğrulama olaylarında kaynak/hedef bilgi ve NTLM sürümüne bakılır.
```

```
10. Skeleton Key İzleri
Öncelik: Düşük
Erişim: Live System
Konum → Security.evtx → Event ID 4673 (SeDebugPrivilege DC üzerinde); LSASS modül listesi
MITRE: T1556.001
Gözlem Notu: DC üzerinde LSASS'a yüklenen beklenmeyen modüllere ve her hesap için tek parola ile logon olaylarına bakılır.
```
