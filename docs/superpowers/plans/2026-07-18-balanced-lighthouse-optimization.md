# Balanced Lighthouse Optimization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Improve mobile startup, maintainability, contrast, and SEO without changing the established visual design or normal interaction animations.

**Architecture:** Extract CSS and application JavaScript from `index.html`, defer noncritical JavaScript, load the search index only after search intent, deduplicate Markdown fetches, and replace the blocking startup overlay with a compact animated status indicator. Existing D3 node and panel animations remain unchanged for normal users.

**Tech Stack:** Static HTML/CSS/JavaScript, D3 7.8.5, Marked 18.0.6, DOMPurify 3.0.6, Python/pytest.

## Global Constraints

- Preserve the current mind-map design, colors, controls, and standard D3/panel animations.
- Do not add a build step or framework.
- Keep GitHub Pages relative-path compatibility.
- Do not self-host or redistribute font files.
- Preserve legacy and canonical deep links.

---

### Task 1: Asset extraction and deferred loading

**Files:**
- Modify: `index.html`
- Create: `styles.css`
- Create: `app.js`
- Create: `analytics.js`
- Modify: `tests/test_index_html.py`

- [ ] Write tests for local assets, deferred libraries, meta description, preconnects, and JavaScript syntax.
- [ ] Run tests and confirm failure.
- [ ] Extract CSS/JS and update HTML loading order and CSP.
- [ ] Run tests and confirm success.

### Task 2: Startup and deep-link data flow

**Files:**
- Modify: `app.js`
- Modify: `index.html`
- Modify: `styles.css`
- Modify: `tests/test_index_html.py`

- [ ] Write tests for nonblocking startup status, Markdown request deduplication, and early hash prefetch.
- [ ] Run tests and confirm failure.
- [ ] Implement compact startup status and shared Markdown request cache.
- [ ] Run tests and confirm success.

### Task 3: Lazy search and motion/contrast accessibility

**Files:**
- Modify: `app.js`
- Modify: `styles.css`
- Modify: `tests/test_index_html.py`

- [ ] Write tests proving the search index is not loaded by bootstrap and is requested on search intent.
- [ ] Write tests for contrast token and reduced-motion support.
- [ ] Run tests and confirm failure.
- [ ] Implement the behavior without changing normal animations.
- [ ] Run all tests and confirm success.

### Task 4: Generated index verification and delivery

**Files:**
- Regenerate: `index.json`
- Regenerate: `search-index.json`

- [ ] Run `python generate_index.py`.
- [ ] Run `pytest -q`.
- [ ] Run `node --check app.js` and `node --check analytics.js`.
- [ ] Validate JSON files and create delivery archive.
