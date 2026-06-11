# SDLC — tourism-app

Turismo OAuth

## Checklist Cursor Agent

- [x] `AGENTS.md` + `.agents/tourism-app/CONTEXT.md`
- [x] `.cursor/rules/` (orchestrator + core + fallback)
- [x] `Taskfile.yml`
- [x] CI GitHub Actions
- [ ] Stack migration: ver `orchestrator/docs/STACK_MIGRATION.md`

## Notas

—

## Validação

```bash
cd tourism-app && task test
```

## Stack

FastAPI+SvelteKit

## Orquestração

```bash
python3 tools/agent_orchestrator/cli.py workspace-detect "tarefa" --files tourism-app/
```
