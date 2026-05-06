# Explore Tourism Brasil Seguro — Backend

FastAPI-based REST API for the tourism app.

## Quick Start

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs available at: http://localhost:8000/docs

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── config.py         # Settings (env-driven)
│   └── routes/
│       ├── __init__.py
│       ├── health.py     # Health check
│       ├── auth.py       # Authentication
│       ├── attractions.py # Tourist attractions
│       └── reviews.py    # Reviews & ratings
├── requirements.txt
├── Dockerfile
└── README.md
```

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `DATABASE_URL` | `sqlite:///./tourism.db` | Database connection string |
| `SECRET_KEY` | `CHANGE-ME-in-production` | JWT signing key |
| `ALLOWED_ORIGINS` | `["*"]` | CORS allowed origins |
| `DEBUG` | `false` | Debug mode |
