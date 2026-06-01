#!/usr/bin/env node
/**
 * Adds @vivdio/design-system file: dependency to all frontend package.json files.
 */
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { dirname, join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

const WS = join(dirname(fileURLToPath(import.meta.url)), '../..');
const DS = join(WS, 'vivdio-design-system');

const targets = [
  'flowmind/packages/web/package.json',
  'scraper-editais/web/package.json',
  'scraper-leiloes/frontend/package.json',
  'universal-study/frontend/package.json',
  'tourism-app/frontend/package.json',
  'clarear/frontend/package.json',
  'scraper-content/frontend/package.json',
];

for (const rel of targets) {
  const pkgPath = join(WS, rel);
  if (!existsSync(pkgPath)) {
    console.warn('skip', rel);
    continue;
  }
  const pkgDir = dirname(pkgPath);
  const relDs = relative(pkgDir, DS).replace(/\\/g, '/');
  const dep = `file:${relDs}`;
  const raw = readFileSync(pkgPath, 'utf8');
  const pkg = JSON.parse(raw);
  pkg.dependencies ??= {};
  if (pkg.dependencies['@vivdio/design-system'] === dep) {
    console.log('ok', rel);
    continue;
  }
  pkg.dependencies['@vivdio/design-system'] = dep;
  const sorted = {
    ...pkg,
    dependencies: Object.fromEntries(
      Object.entries(pkg.dependencies).sort(([a], [b]) => a.localeCompare(b))
    ),
  };
  writeFileSync(pkgPath, JSON.stringify(sorted, null, 2) + '\n');
  console.log('updated', rel, '->', dep);
}
