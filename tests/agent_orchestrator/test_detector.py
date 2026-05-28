"""Testes genéricos de detecção — leem .agents/orchestrator/registry.json do repo."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.agent_orchestrator.detector import detect_rules
from tools.agent_orchestrator.errors import NoMatchingRuleError
from tools.agent_orchestrator.loader import load_bundle


def test_detect_backend_rule(backend_rule_id, sample_paths):
    if not backend_rule_id:
        pytest.skip("Registry sem regra de backend")
    path = sample_paths[backend_rule_id]
    det = detect_rules(
        "Corrigir API backend router endpoint migração",
        [path],
        repo_root=REPO_ROOT,
    )
    assert det.primary_rule_id == backend_rule_id
    assert det.selected_agent.role == "backend-engineer"
    assert det.used_fallback is False
    assert det.scores.get(backend_rule_id, 0) >= 2


def test_detect_frontend_rule(frontend_rule_id, sample_paths):
    if not frontend_rule_id:
        pytest.skip("Registry sem regra de frontend")
    path = sample_paths[frontend_rule_id]
    det = detect_rules(
        "Ajustar componente SvelteKit no dashboard",
        [path],
        repo_root=REPO_ROOT,
    )
    assert det.primary_rule_id == frontend_rule_id
    assert det.selected_agent.role in ("frontend-engineer", "ui-engineer")


def test_detect_devops_docker(sample_paths):
    if "devops-infra" not in sample_paths:
        pytest.skip("Registry sem devops-infra")
    det = detect_rules(
        "Atualizar labels Traefik no docker-compose de produção",
        [sample_paths["devops-infra"]],
        repo_root=REPO_ROOT,
    )
    assert det.primary_rule_id == "devops-infra"
    assert det.selected_agent.role == "sre"


def test_always_apply_core_in_result(core_rule_id):
    det = detect_rules("Qualquer coisa", repo_root=REPO_ROOT)
    assert core_rule_id in det.always_apply_rules


def test_strict_no_match_raises():
    with pytest.raises(NoMatchingRuleError) as exc:
        detect_rules(
            "xyz abc 123",
            [],
            repo_root=REPO_ROOT,
            allow_fallback=False,
        )
    assert exc.value.suggestions


def test_fallback_for_vague_message(registry_data):
    det = detect_rules("me ajuda", repo_root=REPO_ROOT, allow_fallback=True)
    assert det.used_fallback is True
    assert det.selected_agent.role == registry_data["default_agent"]["role"]


def test_load_bundle_loads_agent_files(backend_rule_id, sample_paths):
    if not backend_rule_id:
        pytest.skip("Registry sem regra de backend")
    bundle = load_bundle(
        "Implementar endpoint pytest no backend",
        [sample_paths[backend_rule_id]],
        repo_root=REPO_ROOT,
    )
    assert bundle.agent_role == "backend-engineer"
    assert any("backend-engineer" in f for f in bundle.files_loaded)
    assert "Orquestração" in bundle.instructions_for_main_agent


def test_security_blocks_env_path():
    from tools.agent_orchestrator.security import is_safe_repo_path

    assert is_safe_repo_path(REPO_ROOT, REPO_ROOT / ".env") is False
    assert is_safe_repo_path(REPO_ROOT, REPO_ROOT / "AGENTS.md") is True


def test_sanitize_redacts_api_key_pattern():
    from tools.agent_orchestrator.security import sanitize_content

    out = sanitize_content("key=sk-abcdefghijklmnopqrstuvwxyz123456")
    assert "[REDACTED]" in out
