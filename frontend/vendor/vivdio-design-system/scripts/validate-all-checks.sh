#!/usr/bin/env bash
# Roda npm run check nos frontends com @vivdio/design-system (requer npm install prévio).
set -uo pipefail
WS="${VIVDIO_WORKSPACE:-/home/ubuntu/workspace}"
cd "$WS/vivdio-design-system" && npm run check

declare -A dirs=(
  [vitrine]="vitrine-virtual/frontend"
  [fluxo]="fluxo-ai/frontend"
  [leiloes]="scraper-leiloes/frontend"
  [content]="scraper-content/frontend"
  [flowmind]="flowmind/packages/web"
  [editais]="scraper-editais/web"
)

for name in "${!dirs[@]}"; do
  d="${dirs[$name]}"
  echo "=== $name ($d) ==="
  if (cd "$WS/$d" && npm run check 2>&1 | tail -3); then
    echo ok
  else
    echo "fail (ver log)"
  fi
done
