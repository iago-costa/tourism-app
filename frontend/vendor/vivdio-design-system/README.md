# @vivdio/design-system

Design system compartilhado do workspace Vivdio para PWAs SvelteKit responsivas.

## Recursos

- **Tokens** normalizados (cor, tipografia, espaçamento, sombra, raio) com alvo **WCAG 2.1 AA**
- **Temas** claro / escuro / sistema com persistência (`localStorage`)
- **Grid** mobile-first (`.vd-container`, `.vd-grid--*`)
- **Componentes Svelte 5** com i18n (pt/en) e a11y (ARIA, foco em modais, alvos touch 44px)
- **PWA**: `OfflineIndicator`, `InstallPrompt`, `PushNotificationBanner`
- **Tailwind preset** (`@vivdio/design-system/tailwind`) para apps Tailwind v3
- **Import seletivo** via exports do pacote (tree-shaking pelo bundler)

## Instalação (SvelteKit)

```bash
# no package.json do frontend
"@vivdio/design-system": "file:../../vivdio-design-system"
```

```css
/* app.css */
@import '@vivdio/design-system/styles.css';
```

```js
// tailwind.config.js
import vivdioPreset from '@vivdio/design-system/tailwind';

export default {
  presets: [vivdioPreset],
  content: ['./src/**/*.{html,svelte,ts}', './node_modules/@vivdio/design-system/src/**/*.svelte']
};
```

```svelte
<!-- +layout.svelte -->
<script>
  import { ThemeProvider, OfflineIndicator } from '@vivdio/design-system';
</script>

<ThemeProvider>
  <OfflineIndicator />
  <slot />
</ThemeProvider>
```

## Versionamento

[Semantic Versioning](https://semver.org/): `MAJOR` breaking de tokens/API, `MINOR` componentes novos compatíveis, `PATCH` correções.

## Documentação

- [CONTRIBUTING.md](./CONTRIBUTING.md) — como contribuir
- [PERFORMANCE.md](./PERFORMANCE.md) — métricas PWA (LCP, INP/FID, CLS)
- [docs/MIGRATION.md](./docs/MIGRATION.md) — migração do legado

## Validação

```bash
npm install
npm run check    # tokens + unit tests
npm test
```

## Licença

MIT
