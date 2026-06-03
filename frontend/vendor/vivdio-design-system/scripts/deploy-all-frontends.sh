#!/usr/bin/env bash
# Redeploy produção dos apps com frontend integrado ao DS (requer .env.prod + SSH).
set -euo pipefail
WS="${VIVDIO_WORKSPACE:-/home/ubuntu/workspace}"
LOG="${TMPDIR:-/tmp}/vivdio-ds-deploy-$(date +%Y%m%d-%H%M%S).log"

REPOS=(
  fluxo-ai
  vitrine-virtual
  universal-study
  tourism-app
  clarear
  scraper-leiloes
  scraper-content
  scraper-editais
  app-redacao
  flowmind
  blog-vivdio
  site-pessoal
)

exec > >(tee -a "$LOG") 2>&1
echo "log: $LOG"

for repo in "${REPOS[@]}"; do
  script="${WS}/${repo}/scripts/deploy-prod.sh"
  if [[ ! -x "$script" && ! -f "$script" ]]; then
    echo "SKIP $repo (sem deploy-prod.sh)"
    continue
  fi
  echo "======== DEPLOY $repo ========"
  if (cd "${WS}/${repo}" && bash scripts/deploy-prod.sh); then
    echo "OK $repo"
  else
    echo "FAIL $repo (continua)"
  fi
done

echo "deploy batch done — $LOG"
