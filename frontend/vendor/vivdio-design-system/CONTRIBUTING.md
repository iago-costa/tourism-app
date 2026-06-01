# Guia de contribuição — @vivdio/design-system

## Princípios

1. **Acessibilidade primeiro** — todo componente precisa de rótulo, contraste AA e suporte a teclado.
2. **Mobile / PWA** — alvos touch ≥ 44px; evitar dependências pesadas.
3. **Compatibilidade** — mudanças breaking só em major; deprecar com aviso por um minor.

## Fluxo

1. Abra issue descrevendo token ou componente.
2. Implemente em `src/lib/` ou `tokens/` com testes em `*.test.ts`.
3. Rode `npm run check`.
4. Atualize `CHANGELOG.md` (Keep a Changelog).
5. Sincronize `docs/MIGRATION.md` se houver breaking change.

## Tokens

- Prefixo obrigatório: `--vd-`
- Cores semânticas (`--vd-color-fg`), não apenas paleta bruta em componentes.
- Validar com `npm run lint:tokens`.

## Componentes Svelte

- Svelte 5 runes (`$props`, `$derived`, `$state`).
- Mensagens de UI via `t()` em `i18n.ts` (não strings fixas em produção).
- Exportar no `src/lib/index.ts` apenas APIs estáveis.

## Versionamento semântico

| Mudança | Versão |
|--------|--------|
| Remover/renomear token ou prop pública | MAJOR |
| Novo componente ou token opcional | MINOR |
| Fix a11y, CSS, docs | PATCH |

## Testes obrigatórios

- Unit: `vitest` para utilitários (`theme`, `i18n`, `a11y`).
- Integração: apps piloto rodam `npm run check` após bump.
- Visual: Playwright (`playwright.visual.config.ts`) em CI quando snapshots existirem.

## Performance

Consulte [PERFORMANCE.md](./PERFORMANCE.md) antes de adicionar JS ao bundle crítico.
