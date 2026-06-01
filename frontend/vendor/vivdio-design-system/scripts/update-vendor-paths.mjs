#!/usr/bin/env node
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const WS = join(dirname(fileURLToPath(import.meta.url)), '../..');

// file:./vendor — vendor/ fica no mesmo diretório do package.json (frontend/, web/, …)
const targets = [
  { pkg: 'fluxo-ai/frontend/package.json', dep: 'file:./vendor/vivdio-design-system' },
  { pkg: 'vitrine-virtual/frontend/package.json', dep: 'file:./vendor/vivdio-design-system' },
  { pkg: 'app-redacao/sveltekitapp/package.json', dep: 'file:./vendor/vivdio-design-system' },
  { pkg: 'universal-study/frontend/package.json', dep: 'file:./vendor/vivdio-design-system' },
  { pkg: 'flowmind/packages/web/package.json', dep: 'file:./vendor/vivdio-design-system' },
  { pkg: 'scraper-leiloes/frontend/package.json', dep: 'file:./vendor/vivdio-design-system' },
  { pkg: 'scraper-content/frontend/package.json', dep: 'file:./vendor/vivdio-design-system' },
  { pkg: 'scraper-editais/web/package.json', dep: 'file:./vendor/vivdio-design-system' },
  { pkg: 'tourism-app/frontend/package.json', dep: 'file:./vendor/vivdio-design-system' },
  { pkg: 'clarear/frontend/package.json', dep: 'file:./vendor/vivdio-design-system' },
  { pkg: 'blog-vivdio/apps/admin/package.json', dep: 'file:../../vendor/vivdio-design-system' },
  { pkg: 'blog-vivdio/apps/web/package.json', dep: 'file:../../vendor/vivdio-design-system' },
];

for (const { pkg, dep } of targets) {
  const p = join(WS, pkg);
  if (!existsSync(p)) continue;
  const j = JSON.parse(readFileSync(p, 'utf8'));
  j.dependencies ??= {};
  j.dependencies['@vivdio/design-system'] = dep;
  writeFileSync(p, JSON.stringify(j, null, 2) + '\n');
  console.log('updated', pkg);
}
