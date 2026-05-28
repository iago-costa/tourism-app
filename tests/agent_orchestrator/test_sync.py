"""Testes genéricos de sincronização IDE."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = REPO_ROOT / ".agents" / "orchestrator" / "registry.json"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.agent_orchestrator.sync_rules import sync_all_ide_rules


def _rule_by_id(registry_data: dict, rule_id: str) -> dict | None:
    for rule in registry_data.get("rules", []):
        if rule.get("id") == rule_id:
            return rule
    return None


def test_sync_creates_ide_rule_files(core_rule_id, sample_paths):
    registry_data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    written = sync_all_ide_rules(REPO_ROOT)
    assert written, "sync_all_ide_rules deve escrever ao menos um arquivo"

    assert (REPO_ROOT / f".antigravity/rules/{core_rule_id}.md").is_file()

    for rule_id in sample_paths:
        rule = _rule_by_id(registry_data, rule_id)
        if not rule:
            continue
        trae = rule.get("trae_rule", "")
        if trae:
            assert (REPO_ROOT / trae).is_file(), f"Trae rule ausente: {trae}"
        assert any(rule_id in w for w in written), f"sync não mencionou {rule_id}"
