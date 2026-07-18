# Index Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the generated indexes and single-page mind-map safer, deterministic, searchable in Turkish, accessible, and resilient without changing the content workflow.

**Architecture:** Keep the current static GitHub Pages architecture. `generate_index.py` remains the sole source of `index.json` and `search-index.json`; canonical links become path-based while legacy aliases remain readable. `index.html` keeps its single-file deployment model but replaces unsafe dynamic HTML construction with DOM APIs and coordinates search-index loading through one shared promise.

**Tech Stack:** Python 3.11+, pytest, HTML5, vanilla JavaScript, D3 7.8.5, Marked 18.0.6, DOMPurify 3.0.6.

## Global Constraints

- Preserve static hosting; no server or build step is introduced.
- Existing Markdown content and hierarchy remain unchanged.
- Existing deep links continue to resolve through generated legacy aliases.
- Search must use Turkish locale casing (`tr-TR`).
- JSON writes must be atomic and UTF-8.
- Dynamic repository content must not be inserted into the DOM through unsanitized `innerHTML`.

---

### Task 1: Generator regression tests

**Files:**
- Create: `tests/test_generate_index.py`
- Modify: none

**Interfaces:**
- Consumes: public functions from `generate_index.py`
- Produces: regression coverage for canonical slugs, legacy aliases, order handling, and output consistency

- [ ] Write tests for path-based slugs and uniqueness.
- [ ] Write a test proving legacy aliases resolve duplicate file names.
- [ ] Write a test proving `order.txt` matching is case-insensitive and missing entries are reported.
- [ ] Write an end-to-end generation test that checks tree/search parity and duplicate-free canonical slugs.
- [ ] Run `pytest tests/test_generate_index.py -q` and confirm failure against the current implementation.

### Task 2: Deterministic and atomic index generation

**Files:**
- Modify: `generate_index.py`
- Modify: escaped Unicode filenames under content directories
- Regenerate: `index.json`
- Regenerate: `search-index.json`

**Interfaces:**
- Produces: `canonical_slug(rel_path: str) -> str`, `aliases: list[str]` on file nodes/search records, atomic JSON output

- [ ] Decode literal `#Uxxxx` sequences in filenames to their Unicode characters.
- [ ] Implement canonical slugs from the complete relative path.
- [ ] Retain old filename-based slugs as aliases using the previous collision behavior.
- [ ] Make `order.txt` matching case-insensitive and emit actionable warnings for duplicates/missing entries.
- [ ] Write output through a same-directory temporary file followed by `os.replace`.
- [ ] Regenerate both JSON files.
- [ ] Run generator tests and confirm pass.

### Task 3: Frontend regression tests

**Files:**
- Create: `tests/test_index_html.py`
- Modify: none

**Interfaces:**
- Consumes: `index.html`
- Produces: static and JavaScript syntax checks for security, loading coordination, localization, hash navigation, dependency pinning, and accessibility

- [ ] Test that dependency URLs are version-pinned.
- [ ] Test that search and breadcrumb rendering do not concatenate repository data into `innerHTML`.
- [ ] Test that one shared search-index promise is awaited before Markdown fallback warmup.
- [ ] Test Turkish normalization and `hashchange` support.
- [ ] Test required labels/roles on interactive controls.
- [ ] Extract inline application JavaScript and run `node --check`.
- [ ] Run `pytest tests/test_index_html.py -q` and confirm failure against the current HTML.

### Task 4: Safe and resilient frontend

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: canonical `slug` plus optional `aliases` from `index.json`
- Produces: safe DOM rendering, shared search loading promise, Turkish search, legacy deep-link support, accessible controls

- [ ] Pin Marked and all existing CDN libraries to exact versions.
- [ ] Add a restrictive CSP compatible with the static page and existing analytics.
- [ ] Replace dynamic overlay, error, breadcrumb, and search-result HTML interpolation with DOM construction/text nodes.
- [ ] Add `normalizeSearchText` and use it consistently for names, content, snippets, and queries.
- [ ] Add a shared `searchIndexPromise`; await it before fallback Markdown fetching.
- [ ] Index canonical slugs and aliases in a direct lookup map.
- [ ] Add `hashchange` handling and canonicalize legacy hashes when a document opens.
- [ ] Add clipboard failure feedback and fallback copying.
- [ ] Add mobile header rules and accessibility attributes/keyboard activation.
- [ ] Run frontend tests and JavaScript syntax validation.

### Task 5: Full verification and delivery

**Files:**
- Create: `IR-Referans-improved.zip`

**Interfaces:**
- Produces: ready-to-upload corrected repository archive and the four requested standalone files

- [ ] Run `pytest -q`.
- [ ] Run `python generate_index.py` twice and confirm byte-identical JSON outputs.
- [ ] Validate both JSON files with `python -m json.tool`.
- [ ] Run `node --check` on extracted application JavaScript.
- [ ] Verify all indexed Markdown paths exist and counts match.
- [ ] Package the corrected repository and copy the four requested files to a delivery folder.
