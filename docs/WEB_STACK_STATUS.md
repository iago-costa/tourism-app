# Tourism Web Stack Status

## Pronto

- Frontend web SvelteKit em `frontend/`
- Backend FastAPI async + SQLAlchemy 2 + Alembic
- OAuth Google (`/auth/google/start` + `/auth/google/callback`)
- Auth com `register/login/refresh/logout/me`
- Recuperação de conta com Resend (`recover-account` + `reset-password`)
- Stripe checkout e webhook com idempotência (`webhook_events`)
- CI/CD web (`cd.yml`) + migração (`db-migrate.yml`) + DNS (`cloudflare-dns.yml`)
- Deploy script Swarm + Traefik em `scripts/deploy.sh` e `docker-compose.prod.yml`
- Testes de integração mínimos em `backend/tests/test_auth_billing.py`

## Falta configurar secrets/infra

- `GOOGLE_OAUTH_CLIENT_ID` e `GOOGLE_OAUTH_CLIENT_SECRET`
- `STRIPE_SECRET_KEY`, `STRIPE_PRICE_MONTHLY_ID`, `STRIPE_WEBHOOK_SECRET`
- `RESEND_API_KEY` e domínio de envio validado
- `CF_API_TOKEN` e `CF_ZONE_ID` no GitHub
- `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_SSH_KEY` no GitHub

## Execução rápida

```bash
task setup
task db:upgrade
task dev:back
task dev:web
```

## Produção

```bash
task web:dns
task web:deploy -- <tag>
task web:smoke
```

Runbook detalhado: `docs/GO_LIVE.md`
