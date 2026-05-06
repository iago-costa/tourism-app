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

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend (React Native)

```bash
cd frontend-react-native
npm install

# iOS
npx react-native run-ios

# Android
npx react-native run-android
```

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
