#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${1:-https://tourism.vivdio.com}"

echo "[smoke] Base URL: ${BASE_URL}"

echo "[smoke] health"
curl -fsS "${BASE_URL}/health" | python3 -m json.tool >/dev/null

echo "[smoke] openapi"
curl -fsS "${BASE_URL}/openapi.json" >/dev/null

echo "[smoke] auth recover-account (no-op for unknown user)"
curl -fsS -X POST "${BASE_URL}/api/v1/auth/recover-account" \
  -H "Content-Type: application/json" \
  -d '{"email":"smoke-test@tourism.vivdio.com"}' >/dev/null

echo "[smoke] google oauth start"
curl -fsS "${BASE_URL}/api/v1/auth/google/start" | python3 -m json.tool >/dev/null

echo "[smoke] done"
