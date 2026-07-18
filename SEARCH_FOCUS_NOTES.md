# Arama Sonucuna Odaklanma

## Eklenen davranış

1. Arama sonucundaki belirli bir metin satırına tıklanır.
2. İlgili Markdown dosyası sağ panelde açılır.
3. Panel, seçilen eşleşmenin bulunduğu konuma kaydırılır.
4. Aynı terimin içerikteki eşleşmeleri işaretlenir; seçilen eşleşme daha belirgin gösterilir.
5. Başlık satırına tıklanırsa içerikteki ilk eşleşmeye gidilir.

## Korunan davranışlar

- Mind-map görünümü ve animasyonları değiştirilmedi.
- Mevcut URL/hash bağlantıları değiştirilmedi.
- Markdown içerikleri ve oluşturulan indeks yapısı değiştirilmedi.
- Normal dosya açılışında panel yine en baştan açılır; otomatik kaydırma yalnız arama sonucu üzerinden yapılır.

## Güvenlik ve kararlılık

- Vurgular güvenli DOM düğümleriyle oluşturulur; HTML metni birleştirilmez.
- Hızlı biçimde farklı sonuçlara tıklandığında eski Markdown isteğinin yeni paneli ezmesi engellendi.
- Kopyalama düğmeleri ve arayüz metinleri içerik eşleşmesi olarak işaretlenmez.
- Hareket azaltma tercihi açık olan kullanıcılarda kaydırma animasyonsuz yapılır.

## Değiştirilen dosyalar

- `app.js`
- `styles.css`
- `tests/test_search_focus.py`
