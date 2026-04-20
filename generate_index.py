#!/usr/bin/env python3
"""
generate_index.py
─────────────────
Repo klasör yapısını tarayarak aşağıdaki dosyaları üretir:
  • index.json        → ağaç / menü yapısı
  • search-index.json → tam metin arama indeksi

Kullanım:
  python generate_index.py

Exit code sözleşmesi:
  0 = başarı
  1 = slug çakışması var ama çıktı dosyaları üretildi
  2 = fatal hata

Önerilen dosya adı standardı:
  • Sadece küçük harf Latin karakterler kullanın (a-z)
  • Kelimeler arası ayraç olarak tire (-) kullanın
  • Boşluk, Türkçe karakter, büyük harf kullanmayın
  • Örnek: 'scheduled-tasks.md', 'rdp.md', 'golden-ticket.md'
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

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
    ".git", ".obsidian", "node_modules", ".github", "__pycache__", ".venv", "venv"
}
EXCLUDED_FILES = {
    ".gitignore", ".gitkeep", "README.md", "readme.md", SEARCH_OUTPUT_FILE, "order.txt"
}


def slugify(text: str) -> str:
    """
    Dosya/klasör adını URL-güvenli ASCII slug'a çevirir.

    Önce translate, sonra lower yapılır.
    Böylece "İ" gibi karakterler Python'da "i̇" (i + combining dot)
    üretip bozuk slug'a dönüşmez.

    Örnek:
      "BITS İstemci" -> "bits-istemci"
    """
    tr_map = str.maketrans("şçğıöüŞÇĞİÖÜ", "scgiouSCGIOU")
    text = text.translate(tr_map)
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text or "untitled"


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def markdown_to_search_text(text: str) -> str:
    """
    Markdown içeriğini arama için düz metne indirger.
    Çok agresif dönüştürme yapmadan gereksiz işaretleri temizler.
    """
    text = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)
    text = re.sub(r"```[a-zA-Z0-9_-]*\n", "", text)
    text = text.replace("```", "")
    text = text.replace("`", "")
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"^[>#*\-+]+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"[_*~]+", "", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return normalize_whitespace(text)


class SlugRegistry:
    def __init__(self):
        self._map: dict[str, str] = {}
        self.errors: list[str] = []

    def register(self, raw_slug: str, file_rel_path: str) -> str:
        if raw_slug not in self._map:
            self._map[raw_slug] = file_rel_path
            return raw_slug

        first = self._map[raw_slug]
        self.errors.append(
            f"  ÇAKIŞMA: slug='{raw_slug}'\n"
            f"    → {first}\n"
            f"    → {file_rel_path}"
        )

        parts = file_rel_path.replace("\\", "/").split("/")
        parent = slugify(parts[-2]) if len(parts) >= 2 else "dup"
        unique = f"{parent}-{raw_slug}"

        counter = 2
        candidate = unique
        while candidate in self._map:
            candidate = f"{unique}-{counter}"
            counter += 1

        self._map[candidate] = file_rel_path
        return candidate

    def print_report(self):
        if not self.errors:
            print("[OK] Slug çakışması yok.")
            return
        print("\n" + "═" * 60)
        print("⚠  SLUG ÇAKIŞMASI TESPİT EDİLDİ")
        print("   Aşağıdaki dosyalar aynı slug'u üretiyordu.")
        print("   Otomatik benzersizleştirme uygulandı.")
        print("   Kalıcı çözüm için dosya adlarını standartlaştırın.")
        print("═" * 60)
        for err in self.errors:
            print(err)
        print("═" * 60 + "\n")


def read_markdown_file(path: str, rel_path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return Path(path).read_text(encoding="utf-8-sig")
        except Exception as exc:
            print(f"[UYARI] Dosya okunamadı, arama indeksine eklenmedi: {rel_path} ({exc})")
            return ""
    except Exception as exc:
        print(f"[UYARI] Dosya okunamadı, arama indeksine eklenmedi: {rel_path} ({exc})")
        return ""


def scan_dir(abs_path: str, rel_base: str, registry: SlugRegistry, search_items: list[dict]) -> dict:
    name = os.path.basename(abs_path)
    node = {"name": name, "type": "folder", "children": []}

    try:
        entries = sorted(os.scandir(abs_path), key=lambda e: (e.is_file(), e.name.lower()))
    except PermissionError as exc:
        print(f"[UYARI] Erişim reddedildi: {abs_path} ({exc})")
        return node

    # order.txt varsa o sırayı kullan
    order_file = os.path.join(abs_path, "order.txt")
    if os.path.isfile(order_file):
        try:
            order_lines = Path(order_file).read_text(encoding="utf-8").splitlines()
            order_list = [l.strip() for l in order_lines if l.strip()]
            def order_key(e):
                try:
                    return order_list.index(e.name)
                except ValueError:
                    return len(order_list)
            entries = sorted(entries, key=order_key)
        except Exception as exc:
            print(f"[UYARI] order.txt okunamadı: {abs_path} ({exc})")

    for entry in entries:
        if entry.name in EXCLUDED_DIRS or entry.name in EXCLUDED_FILES:
            continue
        if entry.name.startswith("."):
            continue
        if entry.is_symlink():
            print(f"[UYARI] Symlink atlandı: {entry.path}")
            continue

        rel_path = f"{rel_base}/{entry.name}"

        if entry.is_dir(follow_symlinks=False):
            child = scan_dir(entry.path, rel_path, registry, search_items)
            if child["children"]:
                node["children"].append(child)

        elif entry.is_file() and entry.name.lower().endswith(".md"):
            file_stem = entry.name[:-3]
            raw_slug = slugify(file_stem)
            final_slug = registry.register(raw_slug, rel_path)

            file_node = {
                "name": file_stem,
                "type": "file",
                "slug": final_slug,
                "path": rel_path,
            }
            node["children"].append(file_node)

            raw_content = read_markdown_file(entry.path, rel_path)
            search_items.append({
                "name": file_stem,
                "slug": final_slug,
                "path": rel_path,
                "folder": rel_base,
                "content": markdown_to_search_text(raw_content),
            })

    return node


def count_nodes(node: dict) -> tuple[int, int]:
    total_files = 0
    total_folders = 0

    def _walk(n: dict):
        nonlocal total_files, total_folders
        if n["type"] == "file":
            total_files += 1
        else:
            total_folders += 1
            for c in n.get("children", []):
                _walk(c)

    _walk(node)
    return total_files, total_folders


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Repo klasör yapısından index.json ve search-index.json üret.")
    parser.add_argument(
        "--root-name",
        default=ROOT_NAME,
        help=f"Kök düğüm adı (varsayılan: {ROOT_NAME!r})",
    )
    parser.add_argument(
        "--output",
        default=OUTPUT_FILE,
        help=f"Ağaç çıktısı (varsayılan: {OUTPUT_FILE!r})",
    )
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


def write_json(path: str, data: dict | list) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def generate() -> int:
    args = parse_args()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    registry = SlugRegistry()

    scan_dirs = args.scan_dirs if args.scan_dirs else DEFAULT_SCAN_DIRS

    root_node = {"name": args.root_name, "type": "folder", "children": []}
    search_items: list[dict] = []

    found_any_scan_dir = False
    for dir_name in scan_dirs:
        abs_dir = os.path.join(script_dir, dir_name)
        if not os.path.isdir(abs_dir):
            print(f"[UYARI] Klasör bulunamadı, atlandı: {dir_name!r}")
            continue
        found_any_scan_dir = True
        child = scan_dir(abs_dir, dir_name, registry, search_items)
        if child["children"]:
            root_node["children"].append(child)

    if not found_any_scan_dir:
        print("[HATA] Taranacak hiçbir kök klasör bulunamadı.")
        return 2

    registry.print_report()

    index_output_path = os.path.join(script_dir, args.output)
    write_json(index_output_path, root_node)

    search_output_path = os.path.join(script_dir, args.search_output)
    write_json(search_output_path, {
        "rootName": args.root_name,
        "count": len(search_items),
        "items": search_items,
    })

    total_files, total_folders = count_nodes(root_node)
    print(f"[OK] {args.output} oluşturuldu → {index_output_path}")
    print(f"     Dosya: {total_files}  |  Klasör: {total_folders}")
    print(f"[OK] {args.search_output} oluşturuldu → {search_output_path}")
    print(f"     Arama kaydı: {len(search_items)}")

    if registry.errors:
        print("\n[UYARI] Çakışmalar düzeltildi ama dosya adlarını güncellemeniz önerilir.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(generate())
