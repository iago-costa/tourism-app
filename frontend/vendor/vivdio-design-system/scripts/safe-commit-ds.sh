#!/usr/bin/env bash
set -euo pipefail
WS="${VIVDIO_WORKSPACE:-/home/ubuntu/workspace}"
MSG='feat(ui): integrar @vivdio/design-system (vendor + tokens + PWA)

Pacote vendored em vendor/vivdio-design-system para builds Docker.
ThemeProvider, tokens WCAG, temas claro/escuro e docs/DESIGN_SYSTEM.md.'

safe_add() {
  local repo="$1" sub="$2"
  cd "${WS}/${repo}"
  [[ -f docs/DESIGN_SYSTEM.md ]] && git add docs/DESIGN_SYSTEM.md
  for f in package.json package-lock.json Dockerfile vite.config.ts tsconfig.json \
    tailwind.config.js tailwind.config.cjs svelte.config.js .npmrc app.css; do
    [[ -f "${sub}/${f}" ]] && git add "${sub}/${f}"
  done
  git add "${sub}/src"
  [[ -d "${sub}/vendor" ]] && git add -f "${sub}/vendor"
}

for spec in \
  vitrine-virtual:frontend \
  universal-study:frontend \
  tourism-app:frontend \
  clarear:frontend \
  scraper-leiloes:frontend \
  scraper-content:frontend \
  scraper-editais:web \
  app-redacao:sveltekitapp; do
  repo="${spec%%:*}"
  sub="${spec#*:}"
  safe_add "$repo" "$sub"
  cd "${WS}/${repo}"
  if git diff --cached --quiet; then
    echo "SKIP $repo"
  else
    git commit -m "$MSG"
    git push origin HEAD
    echo "OK $repo"
  fi
done

cd "${WS}/flowmind"
[[ -f docs/DESIGN_SYSTEM.md ]] && git add docs/DESIGN_SYSTEM.md
for f in package.json package-lock.json Dockerfile vite.config.ts; do
  [[ -f "packages/web/${f}" ]] && git add "packages/web/${f}"
done
git add packages/web/src
[[ -d packages/web/vendor ]] && git add -f packages/web/vendor
git add package-lock.json 2>/dev/null || true
if ! git diff --cached --quiet; then
  git commit -m "$MSG"
  git push origin HEAD
  echo "OK flowmind"
fi

echo "safe commits done"
