
```
1. Active Directory Replication Metadata (DCSync)
Öncelik: Yüksek
Konum → Security.evtx → Event ID 4662 (DS-Replication); DC'de repadmin /showchanges
MITRE: T1003.006
Gözlem Notu: DC olmayan kaynaklardan gelen replikasyon isteklerine bakılır.
```

```
2. Domain Trust Oluşturma / Değiştirme — Event ID 4706, 4707, 4716
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1484.002
Gözlem Notu: Yeni domain trust ilişkisi oluşturulup oluşturulmadığına veya mevcut trust'ın değiştirilip değiştirilmediğine bakılır.
```

```
3. SID History Enjeksiyonu — Event ID 4765, 4766
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1134.005
Gözlem Notu: Bir hesaba yüksek yetkili bir SID'nin (Domain Admins SID) history olarak eklenip eklenmediğine bakılır.
```

```
4. msDS-AllowedToDelegateTo Değişikliği (Constrained Delegation)
Öncelik: Yüksek
Konum → Security.evtx → Event ID 5136 (attribute: msDS-AllowedToDelegateTo)
MITRE: T1134.001
Gözlem Notu: Constrained delegation ayarının beklenmeyen hesaplara eklenip eklenmediğine bakılır.
```

```
5. Unconstrained Delegation Hesapları
Öncelik: Yüksek
Erişim: Live System
Konum → AD attribute: userAccountControl flag TRUSTED_FOR_DELEGATION (0x80000)
MITRE: T1134.001
Gözlem Notu: DC dışında unconstrained delegation yetkisine sahip bilgisayar veya servis hesaplarına bakılır.
```

```
6. Resource-Based Constrained Delegation (RBCD)
Öncelik: Yüksek
Konum → Security.evtx → Event ID 5136 (attribute: msDS-AllowedToActOnBehalfOfOtherIdentity)
MITRE: T1134.001
Gözlem Notu: RBCD attribute'unun beklenmeyen bilgisayar hesaplarına eklenip eklenmediğine bakılır.
```

```
7. Password Spray / Brute Force (Domain)
Öncelik: Yüksek
Konum → Security.evtx → Event ID 4771, 4625, 4776
MITRE: T1110.003
Gözlem Notu: Kısa sürede farklı hesaplara aynı kaynak IP'den gelen başarısız oturum açma dalgalarına bakılır.
```

```
8. krbtgt Hesabı Parola Değişikliği — Event ID 4724
Öncelik: Yüksek
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1558.001
Gözlem Notu: krbtgt hesabının parola değişikliğinin meşru bir operasyon mu yoksa Golden Ticket temizliği/oluşturma hazırlığı mı olduğuna bakılır.
```

```
9. AdminSDHolder Değişiklikleri — Event ID 4662, 4780
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1098
Gözlem Notu: AdminSDHolder ACL'sine eklenen beklenmeyen hesaplara bakılır; kalıcı admin erişimi sağlar.
```

```
10. Group Policy Değişikliği — Event ID 5136, 5137, 5141
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1098
Gözlem Notu: GPO değişikliklerinde credential-related ayarların (parola politikası, logon script vb.) değiştirilip değiştirilmediğine bakılır.
```

```
11. Service Principal Name (SPN) Değişikliği — Event ID 5136
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1558.003
Gözlem Notu: SPN eklenmesi veya değiştirilmesi olaylarında Kerberoasting hazırlığı olup olmadığına bakılır.
```

```
12. Computer Account Oluşturma — Event ID 4741
Öncelik: Orta
Konum → C:\Windows\System32\winevt\Logs\Security.evtx
MITRE: T1136.002
Gözlem Notu: Normal kullanıcıların ms-DS-MachineAccountQuota kullanarak bilgisayar hesabı oluşturup oluşturmadığına bakılır.
```

```
13. DSRM (Directory Services Restore Mode) Hesabı Kullanımı
Öncelik: Düşük
Konum → HKLM\SYSTEM\CurrentControlSet\Control\Lsa → DsrmAdminLogonBehavior; Security.evtx → Event ID 4794
MITRE: T1078
Gözlem Notu: DSRM hesabının ağ logon için etkinleştirilip etkinleştirilmediğine (DsrmAdminLogonBehavior=2) bakılır.
```

