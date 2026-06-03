#!/usr/bin/env bash
set -euo pipefail
WS="${VIVDIO_WORKSPACE:-/home/ubuntu/workspace}"
MSG="$(cat <<'EOF'
feat(ui): integrar @vivdio/design-system (vendor + tokens + PWA)

Pacote vendored em vendor/vivdio-design-system para builds Docker.
ThemeProvider, tokens WCAG, temas claro/escuro e docs/DESIGN_SYSTEM.md.
EOF
)"

commit_if_staged() {
  local repo="$1"
  cd "${WS}/${repo}"
  if git diff --cached --quiet; then
    echo "skip (empty) $repo"
    return 0
  fi
  git commit -m "$MSG"
  git push origin HEAD
  echo "ok $repo"
}

# --- SvelteKit apps (frontend | web | sveltekitapp) ---
for spec in \
  "fluxo-ai:frontend" \
  "vitrine-virtual:frontend" \
  "universal-study:frontend" \
  "tourism-app:frontend" \
  "clarear:frontend" \
  "scraper-leiloes:frontend" \
  "scraper-content:frontend" \
  "scraper-editais:web" \
  "app-redacao:sveltekitapp"; do
  repo="${spec%%:*}"
  sub="${spec#*:}"
  cd "${WS}/${repo}"
  git add \
    "${sub}/package.json" "${sub}/package-lock.json" \
    "${sub}/vendor" "${sub}/Dockerfile" \
    "${sub}/src" "${sub}/tailwind.config.js" "${sub}/tailwind.config.cjs" \
    "${sub}/vite.config.ts" "${sub}/svelte.config.js" \
    "${sub}/tsconfig.json" "${sub}/.npmrc" \
    docs/DESIGN_SYSTEM.md 2>/dev/null || true
  commit_if_staged "$repo"
done

# flowmind monorepo
cd "${WS}/flowmind"
git add packages/web/package.json packages/web/package-lock.json \
  packages/web/vendor packages/web/src packages/web/Dockerfile \
  packages/web/vite.config.ts package-lock.json docs/DESIGN_SYSTEM.md 2>/dev/null || true
commit_if_staged flowmind

# blog-vivdio
cd "${WS}/blog-vivdio"
git add vendor apps/admin/package.json apps/web/package.json \
  apps/admin/tailwind.config.js apps/web/src/styles/global.css \
  docs/DESIGN_SYSTEM.md 2>/dev/null || true
commit_if_staged blog-vivdio

# site-pessoal
cd "${WS}/site-pessoal"
git add vendor style.css script.js docs/DESIGN_SYSTEM.md 2>/dev/null || true
commit_if_staged site-pessoal

# pacote central
cd "${WS}/vivdio-design-system"
if [[ -d .git ]]; then
  git add -A
  git diff --cached --quiet || {
    git commit -m "feat: design system Vivdio v1 (tokens, Svelte 5, PWA, scripts vendor)"
    git push -u origin HEAD 2>/dev/null || echo "vivdio-design-system: push manual (sem remote)"
  }
fi

echo "commits finished"
