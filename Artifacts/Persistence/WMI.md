## WMI ARTIFACT'LARI

```
1. WMI EventFilter
Öncelik: Yüksek
Erişim: Live System
Konum → ROOT\subscription → __EventFilter nesneleri
Kullanım:  Win + R > wbemtest  > Bağlan (Connect) > ad boşluğu bunu yaz root\subscription > Örnekleri sırala > __EventFilter yaz. >  Query (CIM_STRING) burada sorguyu incele şüpheli herhangi birşey varmı ? 
Gözlem Notu: Get-WMIObject ile __EventFilter sınıfındaki aktif sorgu filtrelerine bakılır.
```

```
2. WMI EventConsumer
Öncelik: Yüksek
Erişim: Live System
Konum → ROOT\subscription → CommandLineEventConsumer, ActiveScriptEventConsumer
Gözlem Notu: CommandLineEventConsumer'daki ExecutablePath ve CommandLineTemplate değerlerine bakılır.
```

```
3. WMI FilterToConsumerBinding
Öncelik: Yüksek
Erişim: Live System
Konum → ROOT\subscription → __FilterToConsumerBinding
Gözlem Notu: Filter-Consumer eşleşmesinin var olup olmadığına bakılır; eşleşme kalıcılığı aktif eder.
```
