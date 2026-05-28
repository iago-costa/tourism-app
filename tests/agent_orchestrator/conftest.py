"""Fixtures comuns — testes genéricos do agent_orchestrator por repositório."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = REPO_ROOT / ".agents" / "orchestrator" / "registry.json"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _load_registry() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def _rule_by_id(registry_data: dict, rule_id: str) -> dict | None:
    for rule in registry_data.get("rules", []):
        if rule.get("id") == rule_id:
            return rule
    return None


@pytest.fixture(scope="session")
def registry_data() -> dict:
    assert REGISTRY_PATH.is_file(), f"Registry ausente: {REGISTRY_PATH}"
    return _load_registry()


@pytest.fixture(scope="session")
def project_id(registry_data: dict) -> str:
    return registry_data["project"]


@pytest.fixture(scope="session")
def core_rule_id(registry_data: dict) -> str:
    for rule in registry_data.get("rules", []):
        if rule.get("always_apply"):
            return rule["id"]
    return f"{registry_data['project']}-core"


def _sample_path_from_glob(glob: str) -> str:
    if glob.startswith("docker-compose"):
        return "docker-compose.yml"
    if glob.startswith("Dockerfile"):
        return "Dockerfile"
    if glob == "Makefile":
        return "Makefile"
    if glob == "nginx.conf":
        return "nginx.conf"
    if "**" in glob or "*" in glob:
        base = glob.split("*")[0].rstrip("/")
        if base:
            return f"{base}sample/file.py"
        return "sample/file.py"
    return glob


@pytest.fixture(scope="session")
def sample_paths(registry_data: dict) -> dict[str, str]:
    rule_ids = (
        "backend-python",
        "backend-typescript",
        "backend-nestjs",
        "backend-django",
        "frontend-svelte",
        "frontend-static",
        "frontend-monorepo",
        "devops-infra",
    )
    out: dict[str, str] = {}
    for rid in rule_ids:
        rule = _rule_by_id(registry_data, rid)
        globs = (rule or {}).get("path_globs") or []
        if globs:
            out[rid] = _sample_path_from_glob(globs[0])
    return out


@pytest.fixture(scope="session")
def backend_rule_id(sample_paths: dict[str, str]) -> str | None:
    for rid in (
        "backend-python",
        "backend-typescript",
        "backend-nestjs",
        "backend-django",
    ):
        if rid in sample_paths:
            return rid
    return None


@pytest.fixture(scope="session")
def frontend_rule_id(sample_paths: dict[str, str]) -> str | None:
    for rid in ("frontend-svelte", "frontend-static", "frontend-monorepo"):
        if rid in sample_paths:
            return rid
    return None
