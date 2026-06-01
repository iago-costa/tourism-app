#!/usr/bin/env bash
set -euo pipefail
WS="${VIVDIO_WORKSPACE:-/home/ubuntu/workspace}"

commit_repo() {
  local repo="$1"
  shift
  local wd="${WS}/${repo}"
  [[ -d "${wd}/.git" ]] || return 0
  cd "$wd"
  if [[ -z "$(git status -s 2>/dev/null)" ]]; then
    echo "clean $repo"
    return 0
  fi
  git add "$@"
  if git diff --cached --quiet; then
    echo "nothing staged $repo"
    return 0
  fi
  git commit -m "$(cat <<'EOF'
feat(ui): integrar @vivdio/design-system (vendor + tokens + PWA)

Pacote vendored em vendor/vivdio-design-system para builds Docker.
ThemeProvider, tokens WCAG, temas claro/escuro e docs/DESIGN_SYSTEM.md.
EOF
)"
  git push origin HEAD
  echo "pushed $repo"
}

# app-redacao: apenas frontend DS (sem alterações backend pendentes)
commit_repo app-redacao \
  sveltekitapp/package.json sveltekitapp/package-lock.json \
  sveltekitapp/vendor sveltekitapp/src/app.css sveltekitapp/src/routes/+layout.svelte \
  sveltekitapp/src/routes/login sveltekitapp/vite.config.ts \
  sveltekitapp/Dockerfile docs/DESIGN_SYSTEM.md 2>/dev/null || \
commit_repo app-redacao \
  sveltekitapp/package.json sveltekitapp/package-lock.json \
  sveltekitapp/vendor sveltekitapp/src/app.css sveltekitapp/src/routes/+layout.svelte \
  sveltekitapp/vite.config.ts docs/DESIGN_SYSTEM.md

for repo in fluxo-ai vitrine-virtual universal-study flowmind scraper-leiloes scraper-content scraper-editais tourism-app clarear blog-vivdio site-pessoal; do
  case $repo in
    fluxo-ai|vitrine-virtual|universal-study|scraper-leiloes|scraper-content|tourism-app|clarear)
      sub=frontend
      [[ $repo == scraper-editais ]] && sub=web
      commit_repo "$repo" \
        "${sub}/package.json" "${sub}/package-lock.json" \
        "${sub}/vendor" "${sub}/src" "${sub}/Dockerfile" \
        docs/DESIGN_SYSTEM.md \
        2>/dev/null || commit_repo "$repo" docs/DESIGN_SYSTEM.md "${sub}/vendor" "${sub}/package.json"
      ;;
    flowmind)
      commit_repo flowmind \
        packages/web/package.json packages/web/package-lock.json \
        packages/web/vendor packages/web/src \
        packages/web/vite.config.ts packages/web/Dockerfile \
        package-lock.json docs/DESIGN_SYSTEM.md
      ;;
    scraper-editais)
      commit_repo scraper-editais \
        web/package.json web/package-lock.json web/vendor web/src web/Dockerfile docs/DESIGN_SYSTEM.md
      ;;
    blog-vivdio)
      commit_repo blog-vivdio \
        vendor apps/admin/package.json apps/web/package.json \
        apps/admin/tailwind.config.js apps/web/src/styles/global.css \
        docs/DESIGN_SYSTEM.md
      ;;
    site-pessoal)
      commit_repo site-pessoal \
        vendor style.css script.js docs/DESIGN_SYSTEM.md
      ;;
  esac
done

# workspace registry
if [[ -d "${WS}/.git" ]]; then
  cd "${WS}"
  git add .agents/orchestrator/workspace_registry.json 2>/dev/null || true
  git diff --cached --quiet || git commit -m "chore: registrar vivdio-design-system no workspace registry" && git push origin HEAD || true
fi

echo "all commits done"
