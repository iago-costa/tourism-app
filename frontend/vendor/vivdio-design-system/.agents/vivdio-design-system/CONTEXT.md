# vivdio-design-system — contexto

Pacote npm `@vivdio/design-system`: tokens CSS WCAG 2.1 AA, componentes Svelte 5, plugin PWA (`vite/pwa.mjs`), temas claro/escuro, i18n helpers.

## Consumo

Repos copiam vendor via `scripts/vendor-into-repos.sh`. Import:

- `@vivdio/design-system` — componentes
- `@vivdio/design-system/styles.css` — tokens + componentes CSS
- `@vivdio/design-system/vite/pwa` — plugin Vite PWA

## Validação

`npm run check` (tokens + vitest)
