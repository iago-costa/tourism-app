#!/usr/bin/env node
/**
 * Validates design token CSS files declare required semantic variables.
 */
import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const required = [
  '--vd-color-bg',
  '--vd-color-fg',
  '--vd-color-primary',
  '--vd-font-sans',
  '--vd-space-4',
  '--vd-radius-md',
  '--vd-shadow-md',
  '--vd-touch-min'
];

const themes = readFileSync(join(root, 'tokens/themes.css'), 'utf8');
const tokens = readFileSync(join(root, 'tokens/tokens.css'), 'utf8');
const combined = tokens + themes;

const missing = required.filter((name) => !combined.includes(name));
if (missing.length) {
  console.error('[validate-tokens] Missing:', missing.join(', '));
  process.exit(1);
}

if (!themes.includes('[data-theme=')) {
  console.error('[validate-tokens] themes.css must define [data-theme] blocks');
  process.exit(1);
}

console.log('[validate-tokens] OK —', required.length, 'required tokens present');
