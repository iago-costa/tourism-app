#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEPLOY_PROD_REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LIB="${DEPLOY_PROD_REPO_ROOT}/../cluster/scripts/deploy-prod-lib.sh"
[[ -f "$LIB" ]] || LIB="$HOME/workspace/cluster/scripts/deploy-prod-lib.sh"
# shellcheck source=/dev/null
source "$LIB"

cd "$DEPLOY_PROD_REPO_ROOT"
deploy_prod_require_manager

DEPLOY_PROD_REPO_NAME="tourism-app"
DEPLOY_PROD_STACK_NAME="tourism"
DEPLOY_PROD_COMPOSE_FILE="docker-compose.prod.yml"
DEPLOY_PROD_ENV_FILE=".env.prod"
DEPLOY_PROD_HEALTH_URL="https://tourism.vivdio.com"
DEPLOY_PROD_TAG="$(deploy_prod_git_tag "${1:-}")"

deploy_prod_banner

deploy_prod_build "ghcr.io/iago-costa/tourism-app-backend" "backend" "backend/Dockerfile" "$DEPLOY_PROD_TAG"
deploy_prod_build "ghcr.io/iago-costa/tourism-app-frontend" "frontend" "frontend/Dockerfile" "$DEPLOY_PROD_TAG"
export APP_IMAGE_BACKEND="ghcr.io/iago-costa/tourism-app-backend:${DEPLOY_PROD_TAG}"
export APP_IMAGE_FRONTEND="ghcr.io/iago-costa/tourism-app-frontend:${DEPLOY_PROD_TAG}"

deploy_prod_stack_deploy
sleep 30
deploy_prod_health || true
deploy_prod_finish
