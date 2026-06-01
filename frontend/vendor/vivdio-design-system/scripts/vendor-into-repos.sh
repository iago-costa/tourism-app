#!/usr/bin/env bash
# Copia o pacote para vendor/ em cada repo (build Docker não enxerga file:../../ fora do repo).
set -euo pipefail
WS="${VIVDIO_WORKSPACE:-/home/ubuntu/workspace}"
DS="${WS}/vivdio-design-system"
RSYNC=(rsync -a --delete
  --exclude node_modules --exclude .git --exclude coverage --exclude tests/visual/snapshots)

# vendor/ fica ao lado do app (frontend/, web/, sveltekitapp/) para caber no Docker context.
REPOS=(
  fluxo-ai:frontend
  vitrine-virtual:frontend
  app-redacao:sveltekitapp
  universal-study:frontend
  flowmind:packages/web
  scraper-leiloes:frontend
  scraper-content:frontend
  scraper-editais:web
  tourism-app:frontend
  clarear:frontend
)

for entry in "${REPOS[@]}"; do
  repo="${entry%%:*}"
  sub="${entry#*:}"
  target="${WS}/${repo}/${sub}/vendor/vivdio-design-system"
  mkdir -p "$(dirname "$target")"
  echo "vendor → ${repo}/${sub}/vendor/vivdio-design-system"
  "${RSYNC[@]}" "${DS}/" "${target}/"
done

# blog-vivdio monorepo: vendor na raiz do repo
target="${WS}/blog-vivdio/vendor/vivdio-design-system"
mkdir -p "$(dirname "$target")"
echo "vendor → blog-vivdio/vendor/vivdio-design-system"
"${RSYNC[@]}" "${DS}/" "${target}/"

# site-pessoal: tokens estáticos (sem npm)
mkdir -p "${WS}/site-pessoal/vendor/vivdio-design-system/tokens"
cp "${DS}/tokens/tokens.css" "${DS}/tokens/themes.css" "${DS}/tokens/grid.css" \
  "${WS}/site-pessoal/vendor/vivdio-design-system/tokens/"

node "$(dirname "$0")/strip-vendor-package.mjs"
echo "done"
