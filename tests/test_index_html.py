from __future__ import annotations

import subprocess
from pathlib import Path

from bs4 import BeautifulSoup


REPO_ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = REPO_ROOT / "index.html"
APP_JS_PATH = REPO_ROOT / "app.js"
ANALYTICS_JS_PATH = REPO_ROOT / "analytics.js"
STYLES_PATH = REPO_ROOT / "styles.css"


def html_text() -> str:
    return HTML_PATH.read_text(encoding="utf-8")


def app_text() -> str:
    return APP_JS_PATH.read_text(encoding="utf-8")


def styles_text() -> str:
    return STYLES_PATH.read_text(encoding="utf-8")


def soup() -> BeautifulSoup:
    return BeautifulSoup(html_text(), "html.parser")


def test_external_libraries_are_version_pinned_and_deferred() -> None:
    scripts = [tag for tag in soup().find_all("script") if tag.get("src")]
    library_scripts = [
        tag for tag in scripts
        if "googletagmanager" not in tag.get("src", "") and tag.get("src") != "analytics.js"
    ]
    sources = [tag.get("src") for tag in library_scripts]

    assert any("marked@18.0.6" in src for src in sources)
    assert any("dompurify@3.0.6" in src for src in sources)
    assert any("d3@7.8.5" in src for src in sources)
    assert all("@" in src or src.endswith(("app.js", "analytics.js")) for src in sources)

    for tag in library_scripts:
        assert tag.has_attr("defer"), tag.get("src")


def test_local_assets_and_metadata_are_declared() -> None:
    document = soup()

    stylesheet = document.find("link", attrs={"rel": "stylesheet", "href": "styles.css"})
    assert stylesheet is not None
    assert document.find("script", attrs={"src": "app.js", "defer": True}) is not None
    analytics = document.find("script", attrs={"src": "analytics.js"})
    assert analytics is not None
    assert not analytics.has_attr("defer")

    description = document.find("meta", attrs={"name": "description"})
    assert description is not None
    assert "olay müdahalesi" in description.get("content", "").lower()


def test_font_and_cdn_preconnects_are_declared() -> None:
    document = soup()
    preconnects = {
        tag.get("href")
        for tag in document.find_all("link", attrs={"rel": "preconnect"})
    }

    assert "https://fonts.googleapis.com" in preconnects
    assert "https://fonts.gstatic.com" in preconnects
    assert "https://cdn.jsdelivr.net" in preconnects


def test_content_security_policy_is_declared_without_ignored_frame_ancestors() -> None:
    policy = soup().find("meta", attrs={"http-equiv": "Content-Security-Policy"})
    assert policy is not None
    content = policy.get("content", "")
    assert "default-src 'self'" in content
    assert "frame-ancestors" not in content
    assert "script-src 'self' 'unsafe-inline'" not in content


def test_repository_text_is_rendered_with_dom_nodes_not_html_interpolation() -> None:
    script = app_text()

    assert "results.innerHTML = html" not in script
    assert "bcEl.innerHTML" not in script
    assert "ov.innerHTML" not in script
    assert "appendHighlightedText" in script
    assert "document.createTextNode" in script


def test_search_index_is_requested_only_after_search_intent() -> None:
    script = app_text()
    bootstrap_body = script.split("async function bootstrap()", 1)[1].split("async function loadSearchIndex()", 1)[0]

    assert "searchIndexPromise = loadSearchIndex()" not in bootstrap_body
    assert "function ensureSearchIndexRequested" in script
    assert "ensureSearchIndexRequested()" in script
    assert "addEventListener('focus', ensureSearchIndexRequested" in script
    assert "await ensureSearchIndexRequested()" in script
    assert "const treeReadyPromise" in script
    assert "await treeReadyPromise" in script


def test_initial_deep_link_prefetch_and_markdown_requests_are_deduplicated() -> None:
    script = app_text()

    assert "const mdRequestCache = new Map()" in script
    assert "async function getMarkdown" in script
    assert "function prefetchInitialHashContent" in script
    assert "prefetchInitialHashContent(data)" in script
    assert "return getMarkdown(target.path)" in script


def test_startup_status_is_nonblocking_and_fatal_overlay_starts_hidden() -> None:
    document = soup()
    overlay = document.find(id="app-overlay")
    status = document.find(id="startup-status")

    assert overlay is not None and "hidden" in overlay.get("class", [])
    assert status is not None
    assert status.get("role") == "status"
    assert status.get("aria-live") == "polite"


def test_turkish_search_normalization_and_hash_navigation_are_supported() -> None:
    script = app_text()

    assert "function normalizeSearchText" in script
    assert "toLocaleLowerCase('tr-TR')" in script
    assert "window.addEventListener('hashchange'" in script
    assert "aliases" in script


def test_motion_and_contrast_accessibility_are_supported_without_removing_normal_animations() -> None:
    css = styles_text()
    script = app_text()

    assert "--text-dim:#7c879f" in css
    assert "--text-dim:#5f6872" in css
    assert "--accent3:#c43e00" in css
    assert "@media (prefers-reduced-motion: reduce)" in css
    assert "*{margin:0;padding:0;box-sizing:border-box;transition:" not in css
    assert "const duration = 250" in script
    assert "transition().duration(dur)" in script


def test_interactive_controls_have_accessible_names() -> None:
    document = soup()
    required_ids = [
        "search-input",
        "search-clear",
        "theme-btn",
        "search-panel-close",
        "btn-zoom-in",
        "btn-zoom-out",
        "btn-zoom-reset",
        "btn-toggle-all",
        "btn-close-detail",
    ]

    for element_id in required_ids:
        element = document.find(id=element_id)
        assert element is not None
        assert element.get("aria-label"), element_id

    assert document.find(id="search-count").get("aria-live") == "polite"
    assert document.find(id="detail-panel").get("aria-hidden") == "true"


def test_application_javascript_has_valid_syntax() -> None:
    for script_path in (APP_JS_PATH, ANALYTICS_JS_PATH):
        result = subprocess.run(
            ["node", "--check", str(script_path)],
            text=True,
            capture_output=True,
            check=False,
        )
        assert result.returncode == 0, result.stderr
