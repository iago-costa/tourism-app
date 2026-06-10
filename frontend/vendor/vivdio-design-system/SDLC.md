# SDLC — vivdio-design-system

Repo: design system compartilhado (tokens, Svelte, PWA plugin).

## Checklist

- [x] `AGENTS.md`
- [x] `.agents/vivdio-design-system/CONTEXT.md`
- [x] `.cursor/rules/` (design-system-core)
- [x] `vite/pwa.mjs` — PWA unificado
- [x] `npm run check` (tokens + vitest)
- [ ] Publicar versão semver após breaking changes PWA

## Comandos

```bash
npm run check
npm run lint:tokens
node scripts/patch-vite-pwa.mjs   # a partir da raiz workspace
```

## Agente

Sem backend — `frontend-engineer` para componentes; `tech-lead` para tokens/API do pacote.

## Deploy

Vendor copiado para repos via `scripts/vendor-into-repos.sh`; não tem URL própria.
