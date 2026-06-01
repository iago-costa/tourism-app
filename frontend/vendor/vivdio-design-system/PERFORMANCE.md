# Performance — PWAs Vivdio

Métricas alvo para apps que consomem `@vivdio/design-system` em redes móveis instáveis.

## Core Web Vitals (produção)

| Métrica | Alvo | Notas |
|--------|------|--------|
| **LCP** | < 2,5 s | Hero/fontes: preload Inter; CSS tokens inline ou um único `styles.css` |
| **INP** (substitui FID) | < 200 ms | Botões usam CSS nativo; evitar handlers pesados no click |
| **CLS** | < 0,1 | Reservar espaço para banners PWA e modais; não inserir UI acima do fold tardio |

> FID < 100 ms permanece como referência legada; medir **INP** em Field Data (CrUX).

## Bundle

- Importar componentes por nome: `import { Button } from '@vivdio/design-system'`.
- Não importar `styles.css` duplicado se Tailwind já incluir preset.
- `sourcemap: false` em produção (config do app).

## PWA

- Service worker: cache shell + API stale-while-revalidate quando aplicável.
- `OfflineIndicator` leve (sem polling; eventos `online`/`offline`).
- `InstallPrompt` só após `beforeinstallprompt`.

## Checklist de release

- [ ] Lighthouse PWA ≥ 90 em staging
- [ ] LCP/CLS no mobile em 4G simulado
- [ ] Sem regressão visual (Playwright snapshots)
- [ ] `npm run lint:tokens` no pacote DS

## Ferramentas

- Chrome DevTools → Performance / Lighthouse
- WebPageTest mobile profile
- `npx playwright test` com projetos Mobile Chrome / Mobile Safari
