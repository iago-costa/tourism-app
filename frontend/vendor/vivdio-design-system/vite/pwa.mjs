import { VitePWA } from 'vite-plugin-pwa';

/**
 * Standard Vivdio PWA config for SvelteKit apps.
 * @param {{ name?: string, shortName?: string, themeColor?: string, description?: string }} opts
 */
export function vivdioPwa(opts = {}) {
  const name = opts.name ?? 'Vivdio App';
  const shortName = opts.shortName ?? name.split(' ')[0];
  const themeColor = opts.themeColor ?? '#6366f1';

  return VitePWA({
    registerType: 'autoUpdate',
    includeAssets: ['favicon.ico', 'apple-touch-icon.png', 'icon-192.png', 'icon-512.png'],
    manifest: {
      name,
      short_name: shortName,
      description: opts.description ?? name,
      theme_color: themeColor,
      background_color: '#0f172a',
      display: 'standalone',
      start_url: '/',
      icons: [
        { src: 'icon-192.png', sizes: '192x192', type: 'image/png', purpose: 'any maskable' },
        { src: 'icon-512.png', sizes: '512x512', type: 'image/png', purpose: 'any maskable' },
      ],
    },
    workbox: {
      globPatterns: ['**/*.{js,css,html,ico,png,svg,webp,woff2,json}'],
      navigateFallback: '/',
    },
    devOptions: { enabled: false },
  });
}
