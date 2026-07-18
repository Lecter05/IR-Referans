from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP_JS_PATH = REPO_ROOT / "app.js"
STYLES_PATH = REPO_ROOT / "styles.css"


def app_text() -> str:
    return APP_JS_PATH.read_text(encoding="utf-8")


def styles_text() -> str:
    return STYLES_PATH.read_text(encoding="utf-8")


def test_search_results_carry_a_specific_content_occurrence_to_detail_panel() -> None:
    script = app_text()

    assert "occurrenceIndex" in script
    assert "focusAndOpen(node.id, focusRequest)" in script
    assert "showDetail(target, focusRequest)" in script
    assert "renderMarkdown(text, body, focusRequest)" in script


def test_markdown_search_match_is_wrapped_scrolled_and_visually_pinned() -> None:
    script = app_text()
    css = styles_text()

    assert "function highlightSearchMatches" in script
    assert "function focusSearchMatch" in script
    assert "document.createTreeWalker" in script
    assert "container.scrollTo" in script
    assert "content-search-highlight" in script
    assert ".content-search-highlight" in css
    assert ".content-search-highlight.active" in css


def test_detail_requests_are_cancelled_when_a_new_result_is_opened() -> None:
    script = app_text()

    assert "let detailRequestToken = 0" in script
    assert "const requestToken = ++detailRequestToken" in script
    assert "if (requestToken !== detailRequestToken) return" in script


def test_match_offsets_use_non_trimming_normalization() -> None:
    script = app_text()

    assert "function normalizeSearchSliceText" in script
    assert "const normalizedText = normalizeSearchSliceText(text)" in script
    assert "const normalizedContent = normalizeSearchSliceText(entry.content)" in script
