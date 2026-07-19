'use strict';
window.dataLayer = window.dataLayer || [];
window.gtag = window.gtag || function gtag(){ window.dataLayer.push(arguments); };
window.gtag('js', new Date());
window.gtag('config', 'G-8B0KKMF7YB');

function loadAnalytics() {
  if (document.getElementById('google-analytics-script')) return;
  const script = document.createElement('script');
  script.id = 'google-analytics-script';
  script.async = true;
  script.src = 'https://www.googletagmanager.com/gtag/js?id=G-8B0KKMF7YB';
  document.head.appendChild(script);
}

function scheduleAnalytics() {
  if ('requestIdleCallback' in window) {
    window.requestIdleCallback(loadAnalytics, { timeout: 3000 });
  } else {
    window.setTimeout(loadAnalytics, 0);
  }
}

if (document.readyState === 'complete') scheduleAnalytics();
else window.addEventListener('load', scheduleAnalytics, { once: true });
