# Migração para @vivdio/design-system

## 1. Tailwind v3 (fluxo-ai, vitrine-virtual)

**Antes:** classes `.btn`, `.input`, `.card` copiadas em `app.css`.

**Depois:**

1. Dependência `file:../../vivdio-design-system`
2. `@import '@vivdio/design-system/styles.css'` no topo de `app.css`
3. `presets: [require('@vivdio/design-system/tailwind')]` em `tailwind.config.js`
4. Envolver `+layout.svelte` com `<ThemeProvider>`
5. Substituir gradualmente markup por `<Button>`, `<Input>`, etc.

Mapeamento legado → DS:

| Legado | Vivdio DS |
|--------|-----------|
| `.btn-primary` | `<Button variant="primary">` ou `.vd-btn--primary` |
| `.input` | `<Input>` ou `.vd-input` |
| `.card` | `<Card>` ou `.vd-card` |

## 2. Tailwind v4 (app-redacao)

Importar tokens no `@theme` ou usar variáveis:

```css
@import '@vivdio/design-system/tokens.css';
@import '@vivdio/design-system/themes.css';
```

Manter `--color-primary` do projeto mapeado para `--vd-color-primary` se necessário.

## 3. CSS vanilla (scraper-leiloes, scraper-content, universal-study)

1. Importar `styles.css` no `app.css`
2. Substituir `:root` duplicado por overrides de marca apenas (`--vd-color-primary`)
3. Adotar classes `.vd-*` em novas telas; refatorar telas antigas por rota

## 4. Scaffolds vazios (tourism-app, clarear)

Instalar pacote desde o início; não criar novo CSS ad-hoc.

## 5. blog-vivdio

- **apps/web (Astro):** importar `tokens.css` + `themes.css` em `global.css`
- **apps/admin (React):** preset Tailwind + componentes React futuros em `@vivdio/ui` (wrapper)

## 6. site-pessoal

Copiar apenas `tokens.css` + `themes.css` estáticos ou link CDN interno — sem Svelte.

## Rollback

Remover dependência e restaurar `app.css` do commit anterior; tema `data-theme` pode permanecer sem quebrar layout.
