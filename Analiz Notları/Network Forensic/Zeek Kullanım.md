### 1 · DNS Sorguları (`dns`)
```
query          # sorgulanan domain
qtype_name     # kayıt tipi (A, TXT, NULL...)
rcode_name     # sonuç (NOERROR, NXDOMAIN)
answers        # dönen cevap(lar)
```

> Çok sayıda `NXDOMAIN`, uzun/rastgele `query`, aşırı `TXT`/`NULL` sorgusu şüphelidir. (DGA / DNS tünelleme)

---

### 2 · TLS / Şifreli Trafik (`ssl`)
```
server_name          # gidilen host (SNI)
version               # TLS sürümü (eski sürüm = şüpheli)
ja3 / ja3s            # istemci / sunucu TLS parmak izi
validation_status     # sertifika geçerli mi (self-signed?)
```
> Bilinen kötücül `ja3` hash'iyle eşleştir; `validation_status` "self signed / unable to get local issuer" ise dikkat et. JA3 alanı, ilgili paket kuruluysa dolar. (şifreyi çözmeden C2 avı)
---

### 3 · Zeek'in Kendi Tespitleri (`notice`)
```
note         # tespit tipi (ör. Scan::Port_Scan)
msg          # açıklama metni
src / dst    # kaynak / hedef IP
```
> Zeek'in kendi mantığıyla ürettiği tespitler: port tarama, zayıf sertifika, brute force ve benzerleri.

---

### 4 · Threat Intel / IOC Eşleşmeleri (`intel`)
```
indicator          # eşleşen IOC (IP / domain / hash)
indicator_type      # IOC tipi
seen.where           # hangi logda görüldü
sources              # hangi beslemeden geldi
```
> IOC listesi yüklüyse ağda geçen her eşleşme buraya düşer. Ava buradan başlamak en hızlısıdır.

---

### 5 · NTLM Kimlik Doğrulama (`ntlm`)
SMB trafiği görüldüğünde Zeek bu logu diğer AD loglarıyla birlikte üretir.

```
username       # doğrulanan kullanıcı
hostname       # istemci makine
domainname     # domain
success        # başarılı mı
```
> Tek kaynaktan çok sayıda farklı hedefe kimlik doğrulama şüphelidir. (Pass-the-Hash ve yatay hareket)

---

### 6 · Kerberos Akışı (`kerberos`)
```
request_type   # AS / TGS
client         # istek yapan hesap
service        # istenen servis (SPN)
cipher         # şifreleme tipi (rc4 = roasting işareti)
success        # başarılı mı
```
> `cipher` alanı rc4-hmac ve `service` krbtgt dışı bir yığın gösteriyorsa Kerberoasting işaretidir.

---

### 7 · SMB Paylaşım ve Dosya Erişimi (`smb_mapping` / `smb_files`)
```
path      # bağlanılan paylaşım (ADMIN$, IPC$, C$)
name      # erişilen dosya adı (smb_files)
action    # işlem (dosya aç / yaz)
```
> `ADMIN$` veya `C$` bağlantısı + karşıya `.exe` yazımı = PsExec tarzı yatay hareket.

---

### 8 · DCE/RPC Çağrıları (`dce_rpc`)
```
endpoint     # RPC arayüzü (svcctl, atsvc, drsuapi...)
operation    # çağrılan işlem
```
> `svcctl` uzak servis çalıştırmayı, `atsvc` zamanlanmış görevi, `drsuapi` + `DRSGetNCChanges` ise DCSync'i işaret eder.

---

### 9 · SSH Oturumları (`ssh`)
```
auth_success       # giriş başarılı mı
auth_attempts       # deneme sayısı
client / server     # sürüm bilgisi
```
> Tek kaynaktan yüksek `auth_attempts` ve bol başarısız giriş, brute force işaretidir.

---

### 10 · RDP Bağlantıları (`rdp`)
```
cookie                # denenen kullanıcı adı (mstshash)
result                 # bağlantı sonucu
security_protocol      # kullanılan güvenlik katmanı
```
> Bol bağlantı denemesi RDP brute force'u gösterir; `cookie` alanı denenen kullanıcı adlarını açık taşır.

---

### 11 · Diğer Faydalı Loglar
**Kısa Referans**
```
x509                 # sertifika detayı (subject/issuer, geçerlilik tarihi) — ssl ile eşleştirip self-signed tespiti yap
dhcp                 # host_name + mac + atanan IP — makine/IP eşlemesi ve host takibi
ftp                  # user/password açık gelir — komut ve kimlik bilgisi avı
tunnel               # tunnel_type (Teredo, GRE...) — tünelleme/izleme atlatma tespiti
pe                   # taşınan çalıştırılabilir dosya analizi (malware); files logu ile birlikte gelir
ldap / ldap_search   # AD sorguları — kullanıcı/SPN enumerasyon izi
```
