        # Contexto do projeto — tourism-app

        Documento de referência para agentes especializados em `.agents/`. Leia antes de implementar mudanças.

        ## Produto

        App de turismo com OAuth Google, billing e webhooks

        ## Stack

        FastAPI async + SvelteKit + Alembic + OAuth + billing

        ## Estrutura

        - Backend: `backend/app/`
        - Frontend: `frontend/`

        ## Domínios sensíveis

        1. **OAuth tokens**
2. **webhooks billing**
3. **PII**

        ## Agentes recomendados

        | Tarefa | Agente em `.agents/agents/` |
        |--------|----------------------------|
        | API, models, serviços | `backend/backend-engineer.md` |
        | UI, rotas, componentes | `frontend/frontend-engineer.md` |
        | Auth, PII, segurança | `security/security-engineer.md` |
        | Deploy, Docker, CI | `devops/sre.md` |
        | RAG, prompts, IA | `ml-ai/llm-engineer.md` |

        ## Validação

        - Backend: pytest + ruff em backend/
        - Frontend: npm run check em frontend/

        ## Orquestração

        - Registry: `.agents/orchestrator/registry.json`
        - Workspace CLI: `python3 ../tools/agent_orchestrator/cli.py workspace-detect "..." --files tourism-app/path`
        - Regras Cursor: `.cursor/rules/agent-orchestrator.mdc`
