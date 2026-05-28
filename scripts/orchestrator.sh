#!/usr/bin/env bash
# Wrapper para tools/agent_orchestrator/cli.py (inclui detect-safe, load-safe)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$REPO_ROOT/tools/agent_orchestrator/cli.py" --repo "$REPO_ROOT" "$@"
