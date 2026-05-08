# Production Execution Checklist (Tourism + Clarear)

## 0) Definir release tags

```bash
export TOURISM_TAG=<tag-tourism>
export CLAREAR_TAG=<tag-clarear>
```

## 1) DNS (Cloudflare)

```bash
cd ~/workspace/tourism-app && task web:dns
cd ~/workspace/clarear && task web:dns
```

Validar:

```bash
dig +short tourism.vivdio.com
dig +short clarear.vivdio.com
```

## 2) Migrations

```bash
cd ~/workspace/tourism-app/backend && alembic upgrade head
cd ~/workspace/clarear/backend && alembic upgrade head
```

## 3) Deploy

```bash
cd ~/workspace/tourism-app && task web:deploy -- ${TOURISM_TAG}
cd ~/workspace/clarear && task web:deploy -- ${CLAREAR_TAG}
```

## 4) Smoke tests

```bash
cd ~/workspace/tourism-app && task web:smoke
cd ~/workspace/clarear && task web:smoke
```

## 5) Validação funcional manual

- Auth email/senha + `refresh` + `logout`
- OAuth Google
- Recuperação de conta (Resend)
- Checkout Stripe
- Webhook Stripe atualizando status de assinatura

## Rollback rápido (se smoke falhar)

Use a tag anterior estável:

```bash
cd ~/workspace/tourism-app && task web:rollback -- <tag-estavel-tourism>
cd ~/workspace/clarear && task web:rollback -- <tag-estavel-clarear>
```

Depois execute smoke novamente.
