"""Testes de fallback resiliente — heuristic_detect e detect_resilient."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.agent_orchestrator.fallback import (
    detect_resilient,
    heuristic_detect,
    is_subagent_failure_message,
    load_resilient,
)


@pytest.mark.parametrize(
    "text",
    [
        "Tool failed to execute",
        "failed to spawn subagent",
        "rate limit exceeded",
        "Request timed out",
        "429 Too Many Requests",
        "could not start agent",
    ],
)
def test_is_subagent_failure_message(text: str) -> None:
    assert is_subagent_failure_message(text) is True


def test_is_subagent_failure_message_negative() -> None:
    assert is_subagent_failure_message("implementar endpoint FastAPI") is False


def test_heuristic_detect_backend_python() -> None:
    result = heuristic_detect(
        "Corrigir router FastAPI e migração Alembic",
        ["backend/app/routers/chat.py"],
        repo_id="fluxo-ai",
    )
    assert result.mode == "heuristic"
    assert result.primary_rule_id == "backend-python"
    assert result.agent_role == "backend-engineer"
    assert result.agent_path == "agents/backend/backend-engineer.md"
    assert ".agents/agents/backend/backend-engineer.md" in result.files_to_read
    assert ".cursor/rules/fluxo-ai-core.mdc" in result.files_to_read


def test_heuristic_detect_frontend_svelte() -> None:
    result = heuristic_detect(
        "Ajustar componente SvelteKit no dashboard",
        ["frontend/src/routes/+page.svelte"],
        repo_id="app-redacao",
    )
    assert result.primary_rule_id == "frontend-svelte"
    assert result.agent_role == "frontend-engineer"
    assert result.agent_path == "agents/frontend/frontend-engineer.md"


def test_heuristic_detect_devops() -> None:
    result = heuristic_detect(
        "Atualizar Traefik no docker-compose de produção",
        ["docker-compose.prod.yml"],
        repo_id="cluster",
    )
    assert result.primary_rule_id == "devops-infra"
    assert result.agent_role == "sre"
    assert result.agent_path == "agents/devops/sre.md"


def test_heuristic_detect_vague_falls_back_to_tech_lead() -> None:
    result = heuristic_detect("me ajuda", [], repo_id="app-redacao")
    assert result.agent_role == "tech-lead"
    assert result.agent_path == "agents/leadership/tech-lead.md"
    assert result.used_fallback is True


def test_detect_resilient_with_bad_repo_root() -> None:
    bad_root = Path("/nonexistent/repo/root/that/does/not/exist")
    result = detect_resilient(
        "Implementar endpoint pytest no backend FastAPI",
        ["backend/app/main.py"],
        repo_root=bad_root,
        repo_id="app-redacao",
    )
    assert result.mode == "heuristic"
    assert result.error is not None
    assert result.primary_rule_id == "backend-python"
    assert result.agent_path == "agents/backend/backend-engineer.md"


def test_load_resilient_with_bad_repo_root() -> None:
    bad_root = Path("/nonexistent/repo/root/that/does/not/exist")
    result = load_resilient(
        "Deploy docker stack",
        ["docker-compose.yml"],
        repo_root=bad_root,
        repo_id="cluster",
    )
    assert result.mode in ("heuristic", "minimal")
    assert result.instructions
    assert "NÃO tente spawnar subagents" in result.instructions
    assert result.agent_role == "sre"
