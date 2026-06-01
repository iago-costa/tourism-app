#!/usr/bin/env node
/** Remove devDependencies/scripts do package vendored (evita npm instalar Vitest/Svelte no app). */
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const WS = join(dirname(fileURLToPath(import.meta.url)), '../..');

const vendors = [
  'fluxo-ai/frontend/vendor/vivdio-design-system/package.json',
  'vitrine-virtual/frontend/vendor/vivdio-design-system/package.json',
  'app-redacao/sveltekitapp/vendor/vivdio-design-system/package.json',
  'universal-study/frontend/vendor/vivdio-design-system/package.json',
  'flowmind/packages/web/vendor/vivdio-design-system/package.json',
  'scraper-leiloes/frontend/vendor/vivdio-design-system/package.json',
  'scraper-content/frontend/vendor/vivdio-design-system/package.json',
  'scraper-editais/web/vendor/vivdio-design-system/package.json',
  'tourism-app/frontend/vendor/vivdio-design-system/package.json',
  'clarear/frontend/vendor/vivdio-design-system/package.json',
  'blog-vivdio/vendor/vivdio-design-system/package.json',
];

for (const rel of vendors) {
  const p = join(WS, rel);
  if (!existsSync(p)) continue;
  const j = JSON.parse(readFileSync(p, 'utf8'));
  delete j.devDependencies;
  delete j.scripts;
  writeFileSync(p, JSON.stringify(j, null, 2) + '\n');
}
