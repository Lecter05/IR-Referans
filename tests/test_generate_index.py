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


def test_utf8_bom_is_removed_before_markdown_frontmatter_processing(tmp_path: Path) -> None:
    markdown = tmp_path / "bom.md"
    markdown.write_bytes(
        b"\xef\xbb\xbf---\n"
        b"title: Hidden metadata\n"
        b"---\n"
        b"# Visible title\n"
        b"Body\n"
    )

    raw = module.read_markdown_file(markdown, "bom.md")

    assert not raw.startswith("\ufeff")
    assert module.markdown_to_search_text(raw) == "Visible title Body"


def test_excluded_file_names_are_matched_case_insensitively(tmp_path: Path) -> None:
    scan_dir = tmp_path / "Artifacts"
    scan_dir.mkdir()
    (scan_dir / "ReadMe.MD").write_text("repository documentation", encoding="utf-8")
    output = tmp_path / "index.json"
    search_output = tmp_path / "search-index.json"

    exit_code = module.generate_indexes(
        base_dir=tmp_path,
        scan_dirs=["Artifacts"],
        root_name="Root",
        output_path=output,
        search_output_path=search_output,
    )

    search = json.loads(search_output.read_text(encoding="utf-8"))
    assert exit_code == 0
    assert search["count"] == 0
    assert search["items"] == []


def test_casefold_equivalent_entries_have_a_deterministic_tie_break(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class FakeEntry:
        def __init__(self, name: str) -> None:
            self.name = name

        def is_file(self) -> bool:
            return False

    first_order = [FakeEntry("foo"), FakeEntry("Foo")]
    second_order = list(reversed(first_order))

    monkeypatch.setattr(module.os, "scandir", lambda _path: first_order)
    first_result = [entry.name for entry in module.sorted_entries(tmp_path)]
    monkeypatch.setattr(module.os, "scandir", lambda _path: second_order)
    second_result = [entry.name for entry in module.sorted_entries(tmp_path)]

    assert first_result == second_result == ["Foo", "foo"]


def test_json_pair_write_rolls_back_when_second_replace_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index_target = tmp_path / "index.json"
    search_target = tmp_path / "search-index.json"
    old_index = b"old index\n"
    old_search = b"old search\n"
    index_target.write_bytes(old_index)
    search_target.write_bytes(old_search)

    assert hasattr(module, "write_json_pair"), "write_json_pair() eksik"

    real_replace = module.os.replace
    replace_calls = 0

    def fail_second_replace(source: Path | str, target: Path | str) -> None:
        nonlocal replace_calls
        replace_calls += 1
        if replace_calls == 2:
            raise OSError("sentetik ikinci replace hatasi")
        real_replace(source, target)

    monkeypatch.setattr(module.os, "replace", fail_second_replace)

    with pytest.raises(OSError, match="sentetik ikinci replace hatasi"):
        module.write_json_pair(
            index_target,
            {"new": "index"},
            search_target,
            {"new": "search"},
        )

    assert index_target.read_bytes() == old_index
    assert search_target.read_bytes() == old_search
    assert not list(tmp_path.glob(".index.json.*"))
    assert not list(tmp_path.glob(".search-index.json.*"))


def test_json_pair_preserves_backup_when_rollback_itself_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index_target = tmp_path / "index.json"
    search_target = tmp_path / "search-index.json"
    old_index = b"old index\n"
    old_search = b"old search\n"
    index_target.write_bytes(old_index)
    search_target.write_bytes(old_search)

    real_replace = module.os.replace
    replace_calls = 0

    def fail_second_replace_and_rollback(source: Path | str, target: Path | str) -> None:
        nonlocal replace_calls
        replace_calls += 1
        if replace_calls == 2:
            raise OSError("sentetik ikinci replace hatasi")
        if replace_calls == 3:
            raise OSError("sentetik rollback hatasi")
        real_replace(source, target)

    monkeypatch.setattr(module.os, "replace", fail_second_replace_and_rollback)

    with pytest.raises(OSError, match="yedek korundu"):
        module.write_json_pair(
            index_target,
            {"new": "index"},
            search_target,
            {"new": "search"},
        )

    backups = list(tmp_path.glob(".index.json.*.bak"))
    assert len(backups) == 1
    assert backups[0].read_bytes() == old_index
    assert search_target.read_bytes() == old_search
    assert not list(tmp_path.glob(".search-index.json.*"))


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
