# AGENTS.md

## Propósito do projeto

O **tourism-app** é uma aplicação full-stack para experiências/atrações, com autenticação, assinaturas/cobrança e integrações (OAuth e webhooks). O objetivo do agente é evoluir funcionalidades preservando segurança e consistência entre backend e frontend.

## Stack e tecnologias

- Backend: Python 3.11+ (FastAPI), SQLAlchemy async, Alembic
- Auth: OAuth Google + tokens (refresh/access) e reset de senha
- Billing: rotas de cobrança e webhooks
- Frontend: SvelteKit (TypeScript)
- Deploy: Docker + docker-compose
- CI/CD: GitHub Actions

## Estrutura (alto nível)

- `backend/app/`: models, routes, services, config
- `backend/alembic/`: migrações
- `frontend/`: SvelteKit (rotas e lib)
- `docs/`: checklists e overview
- `scripts/`: deploy e smoke tests

## Agentes de IA e responsabilidades

- Trae AI (agente de engenharia)
  - Manter contratos e validações de auth/billing, com foco em segurança.
  - Atualizar migrações e testes quando alterar schema/comportamento.
  - Validar com checks existentes (pytest/ruff quando disponível e check do frontend).
- Cursor (assistente no editor)
  - Auxiliar com edição de rotas SvelteKit e ajustes rápidos, respeitando tipagem.
- Agentes especializados (quando usados via .agents/)
  - Backend Engineer: auth, billing, webhooks, modelos e rotas.
  - Frontend Engineer: UI e integração com API.
  - DevOps/SRE: deploy, pipelines, observabilidade.
  - Security Engineer: revisão de tokens, webhooks e PII.

## Fluxo de trabalho colaborativo (padrão)

1. Identificar a camada correta (route vs service vs model).
2. Implementar a menor mudança que atende ao requisito.
3. Se alterar schema: criar migração Alembic e ajustar rotas/serviços.
4. Atualizar/adicionar testes.
5. Validar:
   - Backend (`backend/`): `pytest` (e Ruff se instalado/configurado)
   - Frontend (`frontend/`): `npm run check`
6. Registrar a mudança: resumo do impacto e passos para verificar.

## Regras do agente Trae AI (limites)

- Nunca inserir segredos/tokens no repositório ou logs.
- Handlers de webhook devem ser idempotentes e validar assinatura/origem.
- Evitar mudanças breaking em contratos sem atualizar consumidores.
- Não reformatar arquivos inteiros; diffs pequenos.

## Critérios de validação

- Autenticação e rotas críticas funcionam sem regressões.
- Webhooks toleram replays/duplicidade e não duplicam eventos.
- Migrações aplicam sem erro e preservam dados.
- Frontend passa no check.

## Segurança e conformidade

- Minimizar logging de PII e dados financeiros.
- Aplicar princípio do menor privilégio em chaves e integrações.
