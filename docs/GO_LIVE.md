# Tourism Go Live Runbook

## 1) Pré-requisitos

- Docker Swarm manager com rede `vivdio_proxy-net`
- Repositório atualizado em `~/workspace/tourism-app`
- Secrets configurados no GitHub Actions:
  - `CF_API_TOKEN`, `CF_ZONE_ID`
  - `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_SSH_KEY`
- Variáveis de aplicação em `backend/.env` / `.env.prod` com:
  - Google OAuth
  - Stripe (incluindo webhook secret)
  - Resend

## 2) DNS Cloudflare

```bash
task web:dns
```

Valide:

```bash
dig +short tourism.vivdio.com
```

## 3) Migration

```bash
cd backend
alembic upgrade head
```

Ou via GitHub Action `db-migrate.yml`.

## 4) Deploy

```bash
task web:deploy -- <tag>
```

## 5) Smoke Test

```bash
task web:smoke
```

## 6) Validação funcional manual

- Login por email/senha
- Refresh/logout
- OAuth Google
- Recuperação de conta (email chega)
- Checkout Stripe
- Webhook Stripe atualiza assinatura

## 7) Rollback rápido

```bash
task web:rollback -- <tag-estavel>
task web:smoke
```

Checklist consolidado com Tourism + Clarear: `docs/PROD_EXECUTION_CHECKLIST.md`
