/**
 * Vivdio workspace — Chaskiq embed loader (support.vivdio.com)
 * Usage:
 *   <meta name="chaskiq-app-id" content="YOUR_APP_KEY"/>
 *   <script src="/vivdio-chaskiq.js" defer></script>
 */
(function () {
  var script = document.currentScript;
  var cfg = window.VIVDIO_CHASKIQ || {};
  var appId =
    cfg.appId ||
    (script && script.getAttribute('data-chaskiq-app-id')) ||
    (document.querySelector('meta[name="chaskiq-app-id"]') &&
      document.querySelector('meta[name="chaskiq-app-id"]').content);
  var domain = (
    cfg.domain ||
    (script && script.getAttribute('data-chaskiq-domain')) ||
    (document.querySelector('meta[name="chaskiq-domain"]') &&
      document.querySelector('meta[name="chaskiq-domain"]').content) ||
    'https://support.vivdio.com'
  ).replace(/\/$/, '');

  if (!appId) return;

  window.chaskiqSettings = { app_id: appId, domain: domain };

  var g = document.createElement('script');
  g.src = domain + '/embed.js';
  g.defer = true;
  g.async = true;
  document.head.appendChild(g);
})();
