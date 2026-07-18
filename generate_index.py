#!/usr/bin/env python3
"""
Repo klasör yapısını tarayıp statik site için iki dosya üretir:

- index.json: D3 mind-map ağacı
- search-index.json: tam metin arama indeksi

Kullanım:
    python generate_index.py

Exit kodları:
    0 = başarı
    2 = fatal hata
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from pathlib import Path, PurePosixPath
from typing import Iterable

ROOT_NAME = "Windows Forensics"
DEFAULT_SCAN_DIRS = [
    "Mittre zinciri",
    "Artifacts",
    "Analiz Notları",
    "Referans",
]
OUTPUT_FILE = "index.json"
SEARCH_OUTPUT_FILE = "search-index.json"

EXCLUDED_DIRS = {
    ".git",
    ".obsidian",
    "node_modules",
    ".github",
    "__pycache__",
    ".venv",
    "venv",
    "docs",
    "tests",
}
EXCLUDED_FILES = {
    ".gitignore",
    ".gitkeep",
    "README.md",
    "readme.md",
    OUTPUT_FILE,
    SEARCH_OUTPUT_FILE,
    "order.txt",
}


def slugify(text: str) -> str:
    """Metni okunabilir, ASCII ve URL-güvenli bir parçaya dönüştürür."""
    tr_map = str.maketrans("şçğıöüŞÇĞİÖÜ", "scgiouSCGIOU")
    text = text.translate(tr_map).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "untitled"


def canonical_slug(rel_path: str) -> str:
    """Dosyanın tam göreli yolundan kalıcı bir hash yolu üretir.

    Örnek:
        Artifacts/Execution/REGISTRY.md -> artifacts/execution/registry
    """
    path = PurePosixPath(rel_path.replace("\\", "/"))
    parts = list(path.parts)
    if parts:
        parts[-1] = PurePosixPath(parts[-1]).stem
    return "/".join(slugify(part) for part in parts)


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def markdown_to_search_text(text: str) -> str:
    """Markdown içeriğini arama için sade metne indirger."""
    text = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)
    text = re.sub(r"```[a-zA-Z0-9_-]*\n", "", text)
    text = text.replace("```", "").replace("`", "")
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"^[>#*\-+]+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"[_*~]+", "", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return normalize_whitespace(text)


class LegacySlugRegistry:
    """Önceki sürümün slug davranışını alias üretmek için korur."""

    def __init__(self) -> None:
        self._map: dict[str, str] = {}
        self.collisions: list[tuple[str, str, str, str]] = []

    def register(self, raw_slug: str, file_rel_path: str) -> str:
        if raw_slug not in self._map:
            self._map[raw_slug] = file_rel_path
            return raw_slug

        first = self._map[raw_slug]
        parts = file_rel_path.replace("\\", "/").split("/")
        parent = slugify(parts[-2]) if len(parts) >= 2 else "dup"
        base = f"{parent}-{raw_slug}"
        candidate = base
        counter = 2
        while candidate in self._map:
            candidate = f"{base}-{counter}"
            counter += 1

        self._map[candidate] = file_rel_path
        self.collisions.append((raw_slug, first, file_rel_path, candidate))
        return candidate

    def print_report(self) -> None:
        if not self.collisions:
            print("[OK] Eski slug alias çakışması yok.")
            return

        print(f"[BİLGİ] {len(self.collisions)} eski slug çakışması alias ile korundu.")
        for raw_slug, first, duplicate, alias in self.collisions:
            print(f"  {raw_slug!r}: {first} | {duplicate} -> alias {alias!r}")


def _order_lines(order_file: Path) -> list[str]:
    try:
        return [line.strip() for line in order_file.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    except OSError as exc:
        print(f"[UYARI] order.txt okunamadı: {order_file} ({exc})")
        return []


def sorted_entries(abs_path: Path | str) -> list[os.DirEntry[str]]:
    """Klasör girdilerini order.txt'e göre, büyük/küçük harfe duyarsız sıralar."""
    folder = Path(abs_path)
    try:
        entries = list(os.scandir(folder))
    except PermissionError as exc:
        print(f"[UYARI] Erişim reddedildi: {folder} ({exc})")
        return []

    entries.sort(key=lambda entry: (entry.is_file(), entry.name.casefold()))
    order_file = folder / "order.txt"
    if not order_file.is_file():
        return entries

    order_list = _order_lines(order_file)
    if not order_list:
        return entries

    by_casefold: dict[str, list[os.DirEntry[str]]] = {}
    for entry in entries:
        by_casefold.setdefault(entry.name.casefold(), []).append(entry)

    seen_order_keys: set[str] = set()
    rank: dict[str, int] = {}
    for position, requested_name in enumerate(order_list):
        key = requested_name.casefold()
        if key in seen_order_keys:
            print(f"[UYARI] order.txt yinelenen kayıt: {order_file} -> {requested_name}")
            continue
        seen_order_keys.add(key)

        matches = by_casefold.get(key, [])
        if not matches:
            print(f"[UYARI] order.txt kaydı bulunamadı: {order_file} -> {requested_name}")
            continue
        if len(matches) > 1:
            print(f"[UYARI] Büyük/küçük harf dışında aynı ada sahip girdiler var: {folder} -> {requested_name}")
        rank[key] = position

    return sorted(
        entries,
        key=lambda entry: (
            rank.get(entry.name.casefold(), len(order_list)),
            entry.is_file(),
            entry.name.casefold(),
        ),
    )


def read_markdown_file(path: Path | str, rel_path: str) -> str:
    file_path = Path(path)
    for encoding in ("utf-8", "utf-8-sig"):
        try:
            return file_path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
        except OSError as exc:
            print(f"[UYARI] Dosya okunamadı, arama indeksine eklenmedi: {rel_path} ({exc})")
            return ""
    print(f"[UYARI] UTF-8 olmayan dosya arama indeksine eklenmedi: {rel_path}")
    return ""


def _register_canonical_slug(registry: dict[str, str], slug: str, rel_path: str) -> None:
    existing = registry.get(slug)
    if existing and existing != rel_path:
        raise ValueError(
            "Kanonik slug çakışması: "
            f"{slug!r}\n  -> {existing}\n  -> {rel_path}"
        )
    registry[slug] = rel_path


def scan_dir(
    abs_path: Path,
    rel_base: str,
    legacy_registry: LegacySlugRegistry,
    canonical_registry: dict[str, str],
    search_items: list[dict],
) -> dict:
    node = {"name": abs_path.name, "type": "folder", "children": []}

    for entry in sorted_entries(abs_path):
        if entry.name in EXCLUDED_DIRS or entry.name in EXCLUDED_FILES or entry.name.startswith("."):
            continue
        if entry.is_symlink():
            print(f"[UYARI] Symlink atlandı: {entry.path}")
            continue

        rel_path = f"{rel_base}/{entry.name}".replace("\\", "/")

        if entry.is_dir(follow_symlinks=False):
            child = scan_dir(
                Path(entry.path),
                rel_path,
                legacy_registry,
                canonical_registry,
                search_items,
            )
            if child["children"]:
                node["children"].append(child)
            continue

        if not (entry.is_file() and entry.name.lower().endswith(".md")):
            continue

        file_stem = Path(entry.name).stem
        slug = canonical_slug(rel_path)
        _register_canonical_slug(canonical_registry, slug, rel_path)

        legacy_slug = legacy_registry.register(slugify(file_stem), rel_path)
        aliases = [legacy_slug] if legacy_slug != slug else []

        file_node = {
            "name": file_stem,
            "type": "file",
            "slug": slug,
            "aliases": aliases,
            "path": rel_path,
        }
        node["children"].append(file_node)

        raw_content = read_markdown_file(entry.path, rel_path)
        search_items.append(
            {
                "name": file_stem,
                "slug": slug,
                "aliases": aliases,
                "path": rel_path,
                "folder": rel_base,
                "content": markdown_to_search_text(raw_content),
            }
        )

    return node


def count_nodes(node: dict) -> tuple[int, int]:
    total_files = 0
    total_folders = 0

    def walk(current: dict) -> None:
        nonlocal total_files, total_folders
        if current["type"] == "file":
            total_files += 1
            return
        total_folders += 1
        for child in current.get("children", []):
            walk(child)

    walk(node)
    return total_files, total_folders


def write_json(path: Path | str, data: dict | list) -> None:
    """JSON'u aynı klasörde geçici dosyaya yazıp atomik olarak değiştirir."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    temp_path: Path | None = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            prefix=f".{target.name}.",
            suffix=".tmp",
            dir=target.parent,
            delete=False,
        ) as handle:
            temp_path = Path(handle.name)
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, target)
    finally:
        if temp_path and temp_path.exists():
            temp_path.unlink()


def _resolve_output_path(base_dir: Path, output_path: Path | str) -> Path:
    path = Path(output_path)
    return path if path.is_absolute() else base_dir / path


def generate_indexes(
    *,
    base_dir: Path | str,
    scan_dirs: Iterable[str],
    root_name: str,
    output_path: Path | str,
    search_output_path: Path | str,
) -> int:
    base = Path(base_dir).resolve()
    root_node = {"name": root_name, "type": "folder", "children": []}
    search_items: list[dict] = []
    legacy_registry = LegacySlugRegistry()
    canonical_registry: dict[str, str] = {}
    found_any_scan_dir = False

    try:
        for dir_name in scan_dirs:
            abs_dir = base / dir_name
            if not abs_dir.is_dir():
                print(f"[UYARI] Klasör bulunamadı, atlandı: {dir_name!r}")
                continue
            found_any_scan_dir = True
            child = scan_dir(
                abs_dir,
                dir_name,
                legacy_registry,
                canonical_registry,
                search_items,
            )
            if child["children"]:
                root_node["children"].append(child)

        if not found_any_scan_dir:
            print("[HATA] Taranacak hiçbir kök klasör bulunamadı.")
            return 2

        legacy_registry.print_report()

        index_target = _resolve_output_path(base, output_path)
        search_target = _resolve_output_path(base, search_output_path)
        write_json(index_target, root_node)
        write_json(
            search_target,
            {
                "schemaVersion": 2,
                "rootName": root_name,
                "count": len(search_items),
                "items": search_items,
            },
        )

        total_files, total_folders = count_nodes(root_node)
        print(f"[OK] {index_target.name} oluşturuldu -> {index_target}")
        print(f"     Dosya: {total_files} | Klasör: {total_folders}")
        print(f"[OK] {search_target.name} oluşturuldu -> {search_target}")
        print(f"     Arama kaydı: {len(search_items)}")
        return 0
    except (OSError, ValueError) as exc:
        print(f"[HATA] İndeks üretilemedi: {exc}")
        return 2


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Repo klasör yapısından indeks dosyaları üret.")
    parser.add_argument("--root-name", default=ROOT_NAME, help=f"Kök düğüm adı (varsayılan: {ROOT_NAME!r})")
    parser.add_argument("--output", default=OUTPUT_FILE, help=f"Ağaç çıktısı (varsayılan: {OUTPUT_FILE!r})")
    parser.add_argument(
        "--search-output",
        default=SEARCH_OUTPUT_FILE,
        help=f"Arama çıktısı (varsayılan: {SEARCH_OUTPUT_FILE!r})",
    )
    parser.add_argument(
        "--scan-dir",
        action="append",
        dest="scan_dirs",
        help="Taranacak kök klasör. Birden fazla kez verilebilir.",
    )
    return parser.parse_args()


def generate() -> int:
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    return generate_indexes(
        base_dir=script_dir,
        scan_dirs=args.scan_dirs or DEFAULT_SCAN_DIRS,
        root_name=args.root_name,
        output_path=args.output,
        search_output_path=args.search_output,
    )


if __name__ == "__main__":
    sys.exit(generate())
