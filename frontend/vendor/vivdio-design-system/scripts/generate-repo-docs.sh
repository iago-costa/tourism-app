#!/usr/bin/env bash
# Generates docs/DESIGN_SYSTEM.md in each Vivdio frontend repo.
set -euo pipefail
WS="${VIVDIO_WORKSPACE:-/home/ubuntu/workspace}"

write_doc() {
  local repo="$1" frontend="$2" stack="$3" status="$4" brand="$5"
  local dir="${WS}/${repo}"
  [[ -d "$dir" ]] || return 0
  mkdir -p "${dir}/docs"
  cat > "${dir}/docs/DESIGN_SYSTEM.md" <<EOF
# Design System — ${repo}

Pacote canônico: [\`@vivdio/design-system\`](../../vivdio-design-system) (workspace).

## Stack deste projeto

- **Frontend:** \`${frontend}\`
- **UI:** ${stack}
- **Status de adoção:** ${status}

## Marca / overrides

${brand}

## Uso rápido

\`\`\`bash
# em ${frontend}/package.json
"@vivdio/design-system": "file:../../vivdio-design-system"
\`\`\`

\`\`\`css
@import '@vivdio/design-system/styles.css';
\`\`\`

\`\`\`svelte
import { ThemeProvider, Button } from '@vivdio/design-system';
\`\`\`

## Migração do legado

Ver [MIGRATION.md](../../vivdio-design-system/docs/MIGRATION.md) e a seção específica para este tipo de stack.

## Manutenção

1. Atualizar versão do pacote (\`npm update @vivdio/design-system\` ou bump do \`file:\`).
2. Rodar \`npm run check\` no frontend.
3. Validar Lighthouse PWA e contraste (WCAG AA).
4. Registrar overrides de token apenas em \`app.css\` / \`tailwind.config\`, não em componentes locais.

## Alterações locais ao sistema base

| Data | Alteração | Motivo |
|------|-----------|--------|
| 2026-05-30 | Documento inicial | Adoção @vivdio/design-system v1.0.0 |

## Performance (PWA)

Metas: LCP < 2,5s · INP < 200ms · CLS < 0,1 — detalhes em [\`PERFORMANCE.md\`](../../vivdio-design-system/PERFORMANCE.md).

## Testes

- Unitários do pacote: \`cd ../../vivdio-design-system && npm test\`
- App: \`cd ${frontend} && npm run check\`
- Visual: Playwright conforme CI do repositório
EOF
  echo "wrote ${dir}/docs/DESIGN_SYSTEM.md"
}

write_doc "fluxo-ai" "frontend" "SvelteKit 5 + Tailwind v3" "**Integrado**" "ThemeProvider, preset Tailwind, tokens; login via ChatForm (legado)."
write_doc "vitrine-virtual" "frontend" "SvelteKit 5 + Tailwind v3" "**Integrado**" "ThemeProvider + brand laranja."
write_doc "app-redacao" "sveltekitapp" "SvelteKit 5 + Tailwind v4" "**Integrado**" "Tokens + PWA InstallPrompt + ThemeProvider."
write_doc "universal-study" "frontend" "SvelteKit 5 + CSS vanilla" "**Integrado** (tokens + ThemeProvider)" "Overrides \`--vd-color-primary: #0066cc\`; CSS legado coexistindo."
write_doc "flowmind" "packages/web" "SvelteKit 5 + CSS vanilla" "**Integrado**" "Tokens importados; tema escuro indigo."
write_doc "scraper-leiloes" "frontend" "SvelteKit 5 + CSS DS vanilla" "**Integrado**" "Âmbar \`--vd-color-primary\`; estilos \`.btn\` legados."
write_doc "scraper-content" "frontend" "SvelteKit 5 + CSS DS vanilla" "**Integrado**" "Dashboard escuro + OfflineIndicator."
write_doc "scraper-editais" "web" "SvelteKit 5 + CSS mínimo" "**Integrado**" "Tokens + ThemeProvider."
write_doc "tourism-app" "frontend" "SvelteKit 5" "**Integrado**" "Login com Button/Input/Card; app.css novo."
write_doc "clarear" "frontend" "SvelteKit 5" "**Integrado**" "Idem tourism-app."
write_doc "blog-vivdio" "apps/admin + apps/web" "React + Astro + Tailwind" "**Integrado** (tokens)" "Admin preset; Astro \`global.css\`."
write_doc "site-pessoal" "." "HTML estático" "**Integrado** (tokens + tema)" "\`style.css\` + \`script.js\` persistência tema."

echo "done"
