# Dengeli Optimizasyon Notları

Bu sürüm mevcut görünümü ve normal kullanıcı animasyonlarını korur. Değişiklikler ilk yükleme, arama, erişilebilirlik ve bakım kolaylığı üzerinde yoğunlaşır.

## Değişiklikler

- `index.html` içindeki CSS ve uygulama JavaScript'i `styles.css` ile `app.js` dosyalarına ayrıldı.
- Marked, DOMPurify, D3 ve uygulama JavaScript'i `defer` ile yükleniyor.
- Google Fonts ve jsDelivr için `preconnect` / `dns-prefetch` eklendi.
- Meta description eklendi.
- Tam ekran başlangıç katmanı yerine küçük ve animasyonlu bir durum göstergesi eklendi.
- Doğrudan Markdown bağlantısında içerik isteği D3 çiziminden önce başlatılıyor.
- Aynı Markdown dosyasının eşzamanlı olarak iki kez indirilmesi engellendi.
- `search-index.json` yalnızca kullanıcı arama alanına odaklandığında yükleniyor.
- Arama indeksi ile ağaç yüklenmesi arasındaki yarış durumu engellendi.
- Normal D3 ve panel animasyonları korundu; yalnızca `prefers-reduced-motion` isteyen kullanıcılar için azaltılıyor.
- Koyu ve açık temadaki düşük kontrastlı renkler güçlendirildi.
- Meta CSP içindeki çalışmayan `frame-ancestors` kaldırıldı ve uygulama kodu dış dosyaya alınarak `script-src` içindeki `unsafe-inline` kaldırıldı.

## GitHub Pages sınırı

`X-Frame-Options`, gerçek `frame-ancestors`, COOP ve benzeri HTTP yanıt başlıkları yalnızca HTML içinden güvenilir biçimde ayarlanamaz. Bunlar için Cloudflare Pages, Netlify veya özel bir sunucu/CDN katmanı gerekir.

## Sonraki isteğe bağlı adımlar

- D3 için yalnız kullanılan modülleri içeren özel bundle
- Service Worker ile çevrimdışı kullanım
- İçerik doğrulama ve kırık bağlantı kontrolü ekleyen GitHub Actions iş akışı
- Arama indeksini parçalara ayırma veya sıkıştırılmış istemci indeksi
