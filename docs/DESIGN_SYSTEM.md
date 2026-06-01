# Design System — tourism-app

Pacote canônico: [`@vivdio/design-system`](../../vivdio-design-system) (workspace).

## Stack deste projeto

- **Frontend:** `frontend`
- **UI:** SvelteKit 5
- **Status de adoção:** **Integrado**

## Marca / overrides

Login com Button/Input/Card; app.css novo.

## Uso rápido

```bash
# em frontend/package.json
"@vivdio/design-system": "file:../../vivdio-design-system"
```

```css
@import '@vivdio/design-system/styles.css';
```

```svelte
import { ThemeProvider, Button } from '@vivdio/design-system';
```

## Migração do legado

Ver [MIGRATION.md](../../vivdio-design-system/docs/MIGRATION.md) e a seção específica para este tipo de stack.

## Manutenção

1. Atualizar versão do pacote (`npm update @vivdio/design-system` ou bump do `file:`).
2. Rodar `npm run check` no frontend.
3. Validar Lighthouse PWA e contraste (WCAG AA).
4. Registrar overrides de token apenas em `app.css` / `tailwind.config`, não em componentes locais.

## Alterações locais ao sistema base

| Data | Alteração | Motivo |
|------|-----------|--------|
| 2026-05-30 | Documento inicial | Adoção @vivdio/design-system v1.0.0 |

## Performance (PWA)

Metas: LCP < 2,5s · INP < 200ms · CLS < 0,1 — detalhes em [`PERFORMANCE.md`](../../vivdio-design-system/PERFORMANCE.md).

## Testes

- Unitários do pacote: `cd ../../vivdio-design-system && npm test`
- App: `cd frontend && npm run check`
- Visual: Playwright conforme CI do repositório
