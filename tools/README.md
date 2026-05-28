# Tools — tourism-app

Ferramentas locais deste repositório. O motor **agent_orchestrator** é um symlink para o workspace compartilhado.

## agent_orchestrator

```bash
# Dentro do repo
./scripts/orchestrator.sh detect "sua mensagem" --files backend/app/foo.py
./scripts/orchestrator.sh load "implementar feature" --files frontend/src/routes/+page.svelte
./scripts/orchestrator.sh detect-safe "mensagem" --files path --json
./scripts/orchestrator.sh load-safe "mensagem" --files path --json
./scripts/orchestrator.sh sync

# Workspace (paths com prefixo tourism-app/)
python3 ../tools/agent_orchestrator/cli.py workspace-detect "mensagem" --files tourism-app/path/to/file
python3 ../tools/agent_orchestrator/cli.py workspace-load "mensagem" --files tourism-app/path
python3 ../tools/agent_orchestrator/cli.py workspace-detect-safe "mensagem" --files tourism-app/path --json
python3 ../tools/agent_orchestrator/cli.py workspace-load-safe "mensagem" --files tourism-app/path --json
```

## Makefile (se presente)

```bash
make orchestrator-detect MSG='corrigir API FastAPI' ORCH_FILES='--files backend/app/main.py'
make orchestrator-sync
make test-orchestrator
```

Registry: `.agents/orchestrator/registry.json`
