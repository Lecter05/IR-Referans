## WMI, THIRD-PARTY ARTIFACT'leri

```
1. WMI Persistent Event Subscriptions (MOF/CIM)
Öncelik: Yüksek
Konum → C:\Windows\System32\wbem\Repository\OBJECTS.DATA
Gözlem Notu: __EventFilter, CommandLineEventConsumer ve __FilterToConsumerBinding nesnelerinin varlığını kontrol eder. (T1047)
```

```
2. AMSI (Antimalware Scan Interface) Trace (Varsayılan: Kapalı — ETW kaydı gerektirir)
Öncelik: Yüksek
Erişim: Live System
Konum → ETW Provider: Microsoft-Antimalware-Scan-Interface
Gözlem Notu: PowerShell, VBScript, JScript ve .NET çalıştırmalarının AMSI'ye gönderilen ham içeriğini yakalar.
```

```
3. IIS / Web Sunucusu Logları (Webshell Execution)
Öncelik: Yüksek
Konum → C:\inetpub\logs\LogFiles\ (IIS varsayılanı)
Gözlem Notu: Webshell üzerinden çalıştırılan komutların HTTP istek parametrelerinde izini tutar. (T1059)
```

---

> Varsayılan: Kapalı ibaresi taşıyan artifact'lar, olay öncesinde etkinleştirilmemişse mevcut olmayabilir.
>
> "Erişim: Live System" yalnızca canlı sistem veya RAM dump gerektiren artifact'larda belirtilmiştir.  
>
> Öncelik değerleri, execution kanıtı sağlama güvenilirliği ifade eder.
