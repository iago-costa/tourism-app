#!/usr/bin/env bash
set -euo pipefail

APP_DIR="$HOME/workspace/tourism-app"
IMAGE_TAG="${1:-latest}"

REGISTRY="${REGISTRY_OVERRIDE:-ghcr.io/iago-costa/tourism-app}"
export APP_IMAGE_BACKEND="${REGISTRY}-backend:${IMAGE_TAG}"
export APP_IMAGE_FRONTEND="${REGISTRY}-frontend:${IMAGE_TAG}"

cd "$APP_DIR"
docker compose -f docker-compose.prod.yml config > /tmp/tourism-resolved.yml
sed -i '/^name:/d' /tmp/tourism-resolved.yml
docker stack deploy -c /tmp/tourism-resolved.yml --with-registry-auth tourism
rm -f /tmp/tourism-resolved.yml
