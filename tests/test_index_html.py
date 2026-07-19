from __future__ import annotations

import subprocess
from pathlib import Path

from bs4 import BeautifulSoup


REPO_ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = REPO_ROOT / "index.html"
APP_JS_PATH = REPO_ROOT / "app.js"
ANALYTICS_JS_PATH = REPO_ROOT / "analytics.js"
STYLES_PATH = REPO_ROOT / "styles.css"
SUMMARY_MARKDOWN_PATH = REPO_ROOT / "Analiz Notları" / "Memory Forensic" / "Volatility 3.md"

D3_SRI = "sha384-CjloA8y00+1SDAUkjs099PVfnY2KmDC2BZnws9kh8D/lX1s46w6EPhpXdqMfjK6i"
MARKED_SRI = "sha384-uGn1eBC40GtuBgao0epc/cz9O4Lo8/flg/10SW+69UjLI5nP31iT4UPc65Xz10Le"
DOMPURIFY_SRI = "sha384-piCcpDdJ7qVeK4Tv8Z6Hpcr3ZBIgP16TxQTPVfsLFdZ5uDgwc3Y8Ho7oUnqf12qu"


def html_text() -> str:
    return HTML_PATH.read_text(encoding="utf-8")


def app_text() -> str:
    return APP_JS_PATH.read_text(encoding="utf-8")


def styles_text() -> str:
    return STYLES_PATH.read_text(encoding="utf-8")


def soup() -> BeautifulSoup:
    return BeautifulSoup(html_text(), "html.parser")


def test_external_libraries_are_pinned_integrity_checked_and_lazy_when_possible() -> None:
    document = soup()
    d3_script = document.find("script", src=lambda value: value and "d3@" in value)

    assert d3_script is not None
    assert "d3@7.9.0" in d3_script.get("src", "")
    assert d3_script.has_attr("defer")
    assert d3_script.get("crossorigin") == "anonymous"
    assert d3_script.get("integrity") == D3_SRI

    script = app_text()
    assert "marked@18.0.6" in script
    assert "dompurify@3.4.12" in script
    assert "const MARKDOWN_LIBRARIES" in script
    assert "function ensureMarkdownLibraries" in script
    assert f"integrity: '{MARKED_SRI}'" in script
    assert f"integrity: '{DOMPURIFY_SRI}'" in script


def test_local_assets_and_metadata_are_declared() -> None:
    document = soup()

    stylesheet = document.find("link", attrs={"rel": "stylesheet", "href": "styles.css"})
    assert stylesheet is not None
    assert document.find("script", attrs={"src": "app.js", "defer": True}) is not None
    analytics = document.find("script", attrs={"src": "analytics.js"})
    assert analytics is not None
    assert analytics.has_attr("defer")
    favicon = document.find("link", attrs={"rel": "icon", "href": "favicon.svg"})
    assert favicon is not None

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
    assert "Promise.all([getMarkdown(target.path), ensureMarkdownLibraries()])" in script


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
    assert "function motionDuration" in script
    assert "reducedMotionQuery" in script
    assert "*{margin:0;padding:0;box-sizing:border-box;transition:" not in css
    assert "const duration = 250" in script
    assert "transition().duration(dur)" in script


def test_pan_zoom_hot_path_is_frame_limited_and_drops_filters_during_motion() -> None:
    script = app_text()
    css = styles_text()

    assert "function queueZoomTransform" in script
    assert ".on('zoom.render', e => queueZoomTransform(e.transform))" in script
    assert "window.requestAnimationFrame" in script
    assert "is-navigating" in script
    assert "svg.is-navigating .node-rect" in css
    assert "filter:none !important" in css


def test_search_does_not_expand_the_entire_tree_and_link_highlights_use_node_ids() -> None:
    script = app_text()
    trigger_body = script.split("async function triggerSearch()", 1)[1].split(
        "function focusAndOpen", 1
    )[0]

    assert "parent.parent.children = parent.parent._children" not in trigger_body
    assert "update(root, true)" not in trigger_body
    assert "activeSearchMatchIds.add(targetNode.id)" in trigger_body
    assert "activeSearchPathIds.add(current.id)" in trigger_body
    assert ".classed('highlighted', d => activeSearchPathIds.has(d.id))" in script
    assert "link.target" not in trigger_body


def test_global_map_shortcuts_leave_normal_controls_alone() -> None:
    script = app_text()

    assert "e.altKey || e.ctrlKey || e.metaKey" in script
    assert "button,a,input,textarea,select" in script
    assert "select,summary" in script
    assert '[role="separator"]' in script
    assert "<summary>" in SUMMARY_MARKDOWN_PATH.read_text(encoding="utf-8")


def test_hidden_panels_are_inert_and_runtime_state_stays_in_sync() -> None:
    document = soup()
    script = app_text()

    for panel_id in ("search-panel", "detail-panel"):
        panel = document.find(id=panel_id)
        assert panel is not None
        assert panel.get("aria-hidden") == "true"
        assert panel.has_attr("inert")

    assert "function setPanelOpen" in script
    assert "panel.setAttribute('inert', '')" in script
    assert "panel.removeAttribute('inert')" in script
    assert script.count("const shouldRestoreMapFocus = panel.contains(document.activeElement)") == 2
    assert "if (shouldRestoreMapFocus) syncActiveNodeFocus(true)" in script


def test_map_controls_wait_for_successful_initialization() -> None:
    document = soup()
    script = app_text()

    assert document.find(id="search-input").has_attr("disabled")
    for control_id in ("btn-zoom-in", "btn-zoom-out", "btn-zoom-reset", "btn-toggle-all"):
        assert document.find(id=control_id).has_attr("disabled")
    assert "setMapControlsDisabled(false)" in script


def test_tree_items_expose_roving_focus_and_expansion_state() -> None:
    script = app_text()

    assert ".attr('aria-level', d => d.depth + 1)" in script
    assert ".attr('aria-expanded'" in script
    assert "? 0 : -1" in script
    assert "focus({ preventScroll: true })" in script


def test_page_has_main_landmark_and_resizers_support_keyboard_input() -> None:
    document = soup()
    script = app_text()

    assert document.find("main", attrs={"class": "main"}) is not None
    for resizer_id in ("rsz-left", "rsz-right"):
        resizer = document.find(id=resizer_id)
        assert resizer.get("role") == "separator"
        assert resizer.get("tabindex") == "0"
        assert resizer.get("aria-label")
        assert int(resizer.get("aria-valuemin")) < int(resizer.get("aria-valuenow"))
        assert int(resizer.get("aria-valuenow")) < int(resizer.get("aria-valuemax"))
    assert "function resizePanelFromKeyboard" in script
    assert "function syncPanelResizeAccessibility" in script
    stop_resize_body = script.split("function stopPanelResize()", 1)[1].split(
        "function startPanelResize", 1
    )[0]
    assert "scheduleViewportRecenter(0)" in stop_resize_body


def test_analytics_loading_is_deferred_until_page_idle_time() -> None:
    analytics = ANALYTICS_JS_PATH.read_text(encoding="utf-8")

    assert "requestIdleCallback" in analytics
    assert "window.addEventListener('load', scheduleAnalytics" in analytics
    assert "document.createElement('script')" in analytics


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
