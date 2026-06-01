#!/usr/bin/env node
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const WS = join(dirname(fileURLToPath(import.meta.url)), '../..');
const EXCLUDE = ' "../../vivdio-design-system/node_modules"';

const viteFiles = [
  'flowmind/packages/web/vite.config.ts',
  'scraper-editais/web/vite.config.ts',
  'scraper-leiloes/frontend/vite.config.ts',
  'universal-study/frontend/vite.config.ts',
  'tourism-app/frontend/vite.config.ts',
  'clarear/frontend/vite.config.ts',
  'scraper-content/frontend/vite.config.ts',
  'app-redacao/sveltekitapp/vite.config.ts',
];

const tsconfigs = viteFiles.map((v) => v.replace('vite.config.ts', 'tsconfig.json'));

for (const rel of viteFiles) {
  const p = join(WS, rel);
  if (!existsSync(p)) continue;
  let s = readFileSync(p, 'utf8');
  if (!s.includes("noExternal: ['@vivdio/design-system']")) {
    if (s.includes('plugins: [sveltekit()]')) {
      s = s.replace(
        /plugins: \[sveltekit\(\)\],/,
        "plugins: [sveltekit()],\n\tssr: {\n\t\tnoExternal: ['@vivdio/design-system']\n\t},"
      );
    } else if (s.includes('plugins: [')) {
      s = s.replace(
        /(plugins: \[[^\]]+\]),/,
        "$1,\n\tssr: {\n\t\tnoExternal: ['@vivdio/design-system']\n\t},"
      );
    }
    writeFileSync(p, s);
    console.log('vite', rel);
  }
}

for (const rel of tsconfigs) {
  const p = join(WS, rel);
  if (!existsSync(p)) continue;
  let s = readFileSync(p, 'utf8');
  if (!s.includes('vivdio-design-system/node_modules')) {
    s = s.replace(
      /"exclude": \["node_modules"\]/,
      `"exclude": ["node_modules",${EXCLUDE.trim()}]`
    );
    if (!s.includes('vivdio-design-system')) {
      s = s.replace(/"exclude": \[([^\]]*)\]/, (m, inner) => {
        if (inner.includes('vivdio')) return m;
        return `"exclude": [${inner}${inner.trim() ? ', ' : ''}"../../vivdio-design-system/node_modules"]`;
      });
    }
    writeFileSync(p, s);
    console.log('tsconfig', rel);
  }
}
