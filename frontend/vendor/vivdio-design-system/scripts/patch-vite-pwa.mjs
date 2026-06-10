#!/usr/bin/env node
/**
 * Patches SvelteKit vite.config.ts files to use @vivdio/design-system PWA plugin.
 */
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const WS = join(dirname(fileURLToPath(import.meta.url)), '../..');

const targets = [
  { rel: 'fluxo-ai/frontend/vite.config.ts', name: 'Plataforma Fluxo', theme: '#6366f1' },
  { rel: 'flowmind/packages/web/vite.config.ts', name: 'Flowmind', theme: '#0ea5e9' },
  { rel: 'vitrine-virtual/frontend/vite.config.ts', name: 'Vitrine Virtual', theme: '#ec4899' },
  { rel: 'scraper-editais/web/vite.config.ts', name: 'BuscaEditais', theme: '#2563eb' },
  { rel: 'scraper-leiloes/frontend/vite.config.ts', name: 'LeilaoRadar', theme: '#f59e0b' },
  { rel: 'universal-study/frontend/vite.config.ts', name: 'Universal Study', theme: '#8b5cf6' },
  { rel: 'tourism-app/frontend/vite.config.ts', name: 'Tourism', theme: '#14b8a6' },
  { rel: 'clarear/frontend/vite.config.ts', name: 'Clarear', theme: '#6366f1' },
  { rel: 'scraper-content/frontend/vite.config.ts', name: 'Scraper Content', theme: '#64748b' },
  { rel: 'app-redacao/sveltekitapp/vite.config.ts', name: 'Redação ENEM', theme: '#4f46e5' },
];

const importLine = "import { vivdioPwa } from '@vivdio/design-system/vite/pwa';";

for (const { rel, name, theme } of targets) {
  const path = join(WS, rel);
  if (!existsSync(path)) {
    console.warn('skip', rel);
    continue;
  }
  let src = readFileSync(path, 'utf8');
  if (src.includes('vivdioPwa')) {
    console.log('ok', rel);
    continue;
  }
  if (!src.includes(importLine)) {
    const lines = src.split('\n');
    const lastImport = lines.findLastIndex((l) => l.startsWith('import '));
    lines.splice(lastImport + 1, 0, importLine);
    src = lines.join('\n');
  }
  src = src.replace(
    /plugins:\s*\[sveltekit\(\)\]/,
    `plugins: [sveltekit(), vivdioPwa({ name: '${name}', themeColor: '${theme}' })]`
  );
  writeFileSync(path, src);
  console.log('patched', rel);
}
