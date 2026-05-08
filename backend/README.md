# Explore Tourism Brasil Seguro — Backend

FastAPI async backend padronizado com SQLAlchemy 2, Alembic, OAuth Google, Stripe e Resend.

## Quick Start

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

API docs: `http://localhost:8000/docs`

## Core Endpoints

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `POST /api/v1/auth/refresh`
- `POST /api/v1/auth/logout`
- `GET /api/v1/auth/me`
- `GET /api/v1/auth/google/start`
- `GET /api/v1/auth/google/callback`
- `POST /api/v1/auth/recover-account`
- `POST /api/v1/auth/reset-password`
- `POST /api/v1/billing/checkout`
- `GET /api/v1/billing/me`
- `POST /api/v1/billing/webhook`

## Migrations

```bash
cd backend
alembic upgrade head
```

## Testes

```bash
cd backend
pytest -q
```

## Environment

Use `.env.example` como referência. Principais variáveis:

- `DATABASE_URL`
- `JWT_SECRET_KEY`
- `GOOGLE_OAUTH_CLIENT_ID`
- `GOOGLE_OAUTH_CLIENT_SECRET`
- `STRIPE_SECRET_KEY`
- `STRIPE_WEBHOOK_SECRET`
- `RESEND_API_KEY`
