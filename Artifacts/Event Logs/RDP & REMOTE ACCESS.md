
```
1. TerminalServices-LocalSessionManager
Öncelik: Yüksek
Konum → Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx
Gözlem Notu: RDP oturum başlatma (21), yeniden bağlanma (25), oturum kapatma (23, 24) ile kaynak IP ve kullanıcı bilgisi (T1021.001); Event 21 source IP ve kullanıcıyı birlikte gösterir.
```

```
2. TerminalServices-RemoteConnectionManager
Öncelik: Yüksek
Konum → Microsoft-Windows-TerminalServices-RemoteConnectionManager%4Operational.evtx
Gözlem Notu: RDP bağlantı denemesi (1149) kaynak IP ve kullanıcı adını gösterir; kimlik doğrulamadan önce loglanır, başarısız denemeleri de yakalar.
```

```
3. Security — RDP Korelasyonu
Öncelik: Yüksek
Konum → Security.evtx
Gözlem Notu: LogonType 10 (RemoteInteractive) ile 4624, NLA ile LogonType 3 (4624) ardından Type 10 geçişi; 4778 (session reconnect), 4779 (session disconnect) olayları RDP oturumlarını doğrular.
```

```
4. WinRM / PSRemoting Operational
Öncelik: Yüksek
Konum → Microsoft-Windows-WinRM%4Operational.evtx
Gözlem Notu: WinRM bağlantısı (6, 91 — hedef taraf), oturum oluşturma (31, 33), hata (142); PSRemoting lateral movement tespitinde (T1021.006) Security 4624 Type 3 ile korelasyon yapılır.
```

```
5. TerminalServices-RDPClient
Öncelik: Orta
Konum → Microsoft-Windows-TerminalServices-RDPClient%4Operational.evtx
Gözlem Notu: İstemci tarafında hedef sunucu bilgisi (1024, 1102) lateral movement tespitinde istemci perspektifini verir.
```

```
6. RemoteDesktopServices-RdpCoreTS
Öncelik: Orta
Konum → Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Operational.evtx
Gözlem Notu: Bağlantı denemesi (131 — kaynak IP), TLS/NLA müzakere (65, 66), bağlantı sonlandırma (102, 103); NLA bypass girişimlerinde anlamlıdır.
```

```
7. OpenSSH Operational (Win10 1809+ / Win11; varsayılan: yüklü ama log minimal)
Öncelik: Orta
Konum → OpenSSH%4Operational.evtx
Gözlem Notu: SSH bağlantı kabul/ret olayları; sshd servis başlatma ve kimlik doğrulama durumu incelenir; detaylı loglama sshd_config ile artırılmalıdır.
```

```
8. WinRM Analytic (Varsayılan: Kapalı)
Öncelik: Orta
Konum → Microsoft-Windows-WinRM%4Analytic.evtx
Gözlem Notu: Detaylı WinRM mesaj içeriği ve SOAP zarfları; Operational kanalından daha fazla detay içerir ancak büyük hacim üretir.
```
