# 🌎 Explore Tourism Brasil Seguro

> Discover Brazil safely, conveniently, and with excitement.

A multilingual, smart, and safe web platform designed to help tourists from all over the world discover the best tourist attractions in Brazil with confidence, comfort, and practicality.

---

## 📂 Project Structure

```
tourism-app/
├── backend/                    # FastAPI REST API
│   ├── app/                    # Application code
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile              # Container build
│   └── README.md               # Backend docs
├── frontend/                   # SvelteKit web frontend (tourism.vivdio.com)
├── docs/                        # App documentation & specs
├── .github/workflows/           # CI/CD pipelines
│   ├── cd.yml                   # Web/API lint + build + deploy
│   ├── db-migrate.yml           # Alembic migrations
│   └── cloudflare-dns.yml       # DNS automation
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- [Task](https://taskfile.dev) (`task` CLI)
- [Docker](https://docs.docker.com/get-docker/) (for PostgreSQL + Redis)
- Python 3.12+
- Node.js 18+

### First-Time Setup

```bash
task setup    # Creates venv, installs deps, starts Docker services
```

### Development

```bash
task dev      # Starts Docker services + Backend (port 8000) + Web frontend (port 5173)
```

### All Available Commands

```bash
task --list   # Show all available tasks
```

| Command | Description |
|---|---|
| `task dev` | Start services + backend + web frontend |
| `task services` | Start Docker infra (Postgres + Redis) |
| `task services:stop` | Stop Docker infra |
| `task setup` | Full first-time setup |
| `task test` | Run all tests |
| `task lint` | Lint backend + frontend |
| `task db:shell` | Connect to Postgres via psql |
| `task status` | Show status of all services |
| `task clean` | Remove venv, node_modules, volumes |

### Web Stack Commands (SvelteKit + FastAPI)

| Command | Description |
|---|---|
| `task dev:web` | Run SvelteKit web frontend |
| `task web:dns` | Update Cloudflare DNS for tourism.vivdio.com |
| `task web:deploy -- <tag>` | Deploy production stack (Swarm/Traefik) |
| `task web:smoke` | Run post-deploy smoke tests |

## 📱 Key Features

- 🌍 **Multilingual Interface** — Auto-translation in 7+ languages
- 🗺️ **Interactive Maps** — Real-time routing like Google Maps
- 📸 **Real Images** — Updated photos of tourist sites
- 🔒 **Safety Indicators** — Public data + user reviews
- ✨ **Smart Recommendations** — Personalized by traveler profile
- 🧳 **Ready-made Itineraries** — 1-day, 3-day, and 1-week tours
- 📍 **Offline Mode** — Maps and info without internet
- 🆘 **Emergency Button** — Police, hospitals, consulates

## 🔄 CI/CD & Deploy

### DNS

| Domínio | Serviço |
|---------|---------|
| `tourism.vivdio.com` | Frontend (SvelteKit) + Backend (FastAPI) |

### Docker Swarm — Serviços

| Service | Imagem GHCR | Porta | Função |
|---------|-------------|-------|--------|
| `tourism_frontend` | `ghcr.io/iago-costa/tourism-app-frontend` | 3000 | SvelteKit |
| `tourism_backend` | `ghcr.io/iago-costa/tourism-app-backend` | 8000 | FastAPI |
| `tourism_db` | `postgres:16-alpine` | 5432 | PostgreSQL |
| `tourism_redis` | `redis:7-alpine` | 6379 | Broker / cache |

Proxy: **Traefik v3** na rede `vivdio_proxy-net` com TLS automático.

### Deploy manual

```bash
cd ~/workspace/tourism-app
git fetch origin main && git reset --hard origin/main
./scripts/deploy.sh <image-tag>
```

### Rollback

```bash
./scripts/deploy.sh <short-sha-anterior>
```

### Automated pipelines via GitHub Actions

| Workflow | Trigger | Target |
|---|---|---|
| `cd.yml` | Push/PR (`main`) | Web/API lint + build + deploy |
| `ci.yml` | Push/PR (`main`) | Lint + test (backend + frontend) |
| `db-migrate.yml` | Push/Manual | Alembic migrations |
| `cloudflare-dns.yml` | Manual | DNS record for tourism.vivdio.com |
| `ios-deploy.yml` | Tag `v*` | Build IPA + TestFlight/App Store |
| `android-deploy.yml` | Tag `v*` | Build AAB + Google Play |

See [CI/CD Setup Guide](#cicd-secrets-setup) below for required secrets.

### CI/CD Secrets Setup

Configure these in **GitHub → Settings → Secrets and variables → Actions**:

#### Web/API
| Secret | Description |
|---|---|
| `DEPLOY_HOST` | Host do servidor de deploy |
| `DEPLOY_USER` | Usuário SSH de deploy |
| `DEPLOY_SSH_KEY` | Chave SSH privada |
| `CF_API_TOKEN` | Token Cloudflare DNS Edit |
| `CF_ZONE_ID` | Zone ID da vivdio.com |

## 📄 License

MIT
