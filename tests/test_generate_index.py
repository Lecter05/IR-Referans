from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("generate_index", REPO_ROOT / "generate_index.py")
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def collect_files(node: dict) -> list[dict]:
    items: list[dict] = []

    def walk(current: dict) -> None:
        if current["type"] == "file":
            items.append(current)
            return
        for child in current.get("children", []):
            walk(child)

    walk(node)
    return items


def test_canonical_slug_uses_complete_relative_path() -> None:
    assert module.canonical_slug("Artifacts/Execution/REGISTRY.md") == "artifacts/execution/registry"
    assert module.canonical_slug("Artifacts/Persistence/REGISTRY.md") == "artifacts/persistence/registry"


def test_legacy_registry_preserves_previous_duplicate_aliases() -> None:
    registry = module.LegacySlugRegistry()

    assert registry.register("registry", "Artifacts/Execution/REGISTRY.md") == "registry"
    assert registry.register("registry", "Artifacts/Persistence/REGISTRY.md") == "persistence-registry"
    assert registry.register("registry", "Artifacts/Network/REGISTRY.md") == "network-registry"


def test_order_file_is_case_insensitive_and_reports_missing_entries(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    folder = tmp_path / "Example"
    folder.mkdir()
    (folder / "BROWSER.md").write_text("browser", encoding="utf-8")
    (folder / "REGISTRY.md").write_text("registry", encoding="utf-8")
    (folder / "order.txt").write_text("browser.MD\nMISSING.md\nREGISTRY.md\n", encoding="utf-8")

    entries = module.sorted_entries(folder)

    assert [entry.name for entry in entries if entry.name != "order.txt"] == ["BROWSER.md", "REGISTRY.md"]
    captured = capsys.readouterr().out
    assert "MISSING.md" in captured
    assert "bulunamadı" in captured.lower()


def test_atomic_json_write_is_deterministic(tmp_path: Path) -> None:
    target = tmp_path / "index.json"
    data = {"name": "İçerik", "children": [{"name": "A"}]}

    module.write_json(target, data)
    first = target.read_bytes()
    module.write_json(target, data)

    assert target.read_bytes() == first
    assert not list(tmp_path.glob(".index.json.*.tmp"))


def test_repository_indexes_have_unique_canonical_slugs_and_matching_search_records(tmp_path: Path) -> None:
    output = tmp_path / "index.json"
    search_output = tmp_path / "search-index.json"

    exit_code = module.generate_indexes(
        base_dir=REPO_ROOT,
        scan_dirs=module.DEFAULT_SCAN_DIRS,
        root_name=module.ROOT_NAME,
        output_path=output,
        search_output_path=search_output,
    )

    assert exit_code == 0
    tree = json.loads(output.read_text(encoding="utf-8"))
    search = json.loads(search_output.read_text(encoding="utf-8"))
    files = collect_files(tree)

    slugs = [item["slug"] for item in files]
    assert len(slugs) == len(set(slugs))
    assert len(files) == search["count"] == len(search["items"])
    assert {item["path"] for item in files} == {item["path"] for item in search["items"]}
    assert all(isinstance(item.get("aliases"), list) for item in files)
