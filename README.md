# 🌎 Explore Tourism Brasil Seguro

> Discover Brazil safely, conveniently, and with excitement.

A multilingual, smart, and safe mobile app designed to help tourists from all over the world discover the best tourist attractions in Brazil with confidence, comfort, and practicality.

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
├── frontend-react-native/      # React Native mobile app
│   ├── App.tsx                  # App entrypoint
│   ├── android/                 # Android native project
│   ├── ios/                     # iOS native project
│   ├── package.json             # Node dependencies
│   └── ...
├── docs/                        # App documentation & specs
├── .github/workflows/           # CI/CD pipelines
│   ├── ci.yml                   # Lint + test on every push
│   ├── android-deploy.yml       # Deploy to Google Play Store
│   └── ios-deploy.yml           # Deploy to Apple App Store
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
task dev      # Starts Docker services + Backend (port 8000) + Metro bundler (port 8081)
```

Then in a **separate terminal**, launch the app on an emulator:

```bash
task app:android    # Build & run on Android emulator/device
task app:ios        # Build & run on iOS simulator (macOS only)
```

### All Available Commands

```bash
task --list   # Show all available tasks
```

| Command | Description |
|---|---|
| `task dev` | Start services + backend + Metro bundler |
| `task app:android` | Launch on Android emulator |
| `task app:ios` | Launch on iOS simulator |
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
| `task install:web` | Install web frontend dependencies |
| `task dev:web` | Run SvelteKit web frontend |
| `task test:web` | Validate web frontend (`check` + `build`) |
| `task lint:web` | Validate web frontend (`check` + `build`) |
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

## 🔄 CI/CD

Automated pipelines via GitHub Actions:

| Workflow | Trigger | Target |
|---|---|---|
| `ci.yml` | Push to `main` / PRs | Lint + Tests |
| `android-deploy.yml` | Tags `v*` / Manual | Google Play Store |
| `ios-deploy.yml` | Tags `v*` / Manual | Apple App Store |
| `cd.yml` | Push/PR (`main`) | Web/API lint + build + deploy |
| `db-migrate.yml` | Push/Manual | Alembic migrations |
| `cloudflare-dns.yml` | Manual | DNS record for tourism.vivdio.com |

See [CI/CD Setup Guide](#cicd-secrets-setup) below for required secrets.

### CI/CD Secrets Setup

Configure these in **GitHub → Settings → Secrets and variables → Actions**:

#### Android (Google Play)
| Secret | Description |
|---|---|
| `ANDROID_KEYSTORE_BASE64` | Base64-encoded upload keystore (.jks) |
| `ANDROID_KEY_ALIAS` | Keystore alias |
| `ANDROID_KEY_PASSWORD` | Key password |
| `ANDROID_STORE_PASSWORD` | Store password |
| `GOOGLE_PLAY_SERVICE_ACCOUNT_JSON` | Google Play Console service account JSON |

#### iOS (App Store)
| Secret | Description |
|---|---|
| `IOS_CERTIFICATE_BASE64` | Base64-encoded .p12 signing certificate |
| `IOS_CERTIFICATE_PASSWORD` | Certificate password |
| `IOS_PROVISIONING_PROFILE_BASE64` | Base64-encoded provisioning profile |
| `APPSTORE_API_KEY_ID` | App Store Connect API key ID |
| `APPSTORE_ISSUER_ID` | App Store Connect issuer ID |
| `APPSTORE_API_PRIVATE_KEY` | App Store Connect API private key (.p8 content) |

## 📄 License

MIT
