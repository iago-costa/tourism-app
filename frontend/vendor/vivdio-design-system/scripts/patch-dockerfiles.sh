#!/usr/bin/env bash
# Adiciona COPY vendor antes de npm ci nos Dockerfiles SvelteKit.
set -euo pipefail
WS="${VIVDIO_WORKSPACE:-/home/ubuntu/workspace}"

patch_df() {
  local f="$1"
  [[ -f "$f" ]] || return 0
  if grep -q 'COPY vendor' "$f"; then
    echo "skip $f"
    return 0
  fi
  sed -i '/^COPY package\*\.json/a COPY vendor ./vendor' "$f"
  echo "patched $f"
}

for f in \
  "$WS/fluxo-ai/frontend/Dockerfile" \
  "$WS/vitrine-virtual/frontend/Dockerfile" \
  "$WS/universal-study/frontend/Dockerfile" \
  "$WS/scraper-leiloes/frontend/Dockerfile" \
  "$WS/scraper-content/frontend/Dockerfile" \
  "$WS/tourism-app/frontend/Dockerfile" \
  "$WS/clarear/frontend/Dockerfile"; do
  patch_df "$f"
done

# app-redacao sveltekitapp
patch_df "$WS/app-redacao/sveltekitapp/Dockerfile" 2>/dev/null || true
# scraper-editais web
patch_df "$WS/scraper-editais/web/Dockerfile" 2>/dev/null || true
# flowmind
patch_df "$WS/flowmind/packages/web/Dockerfile" 2>/dev/null || true

echo "done"
