'use strict';

// ================================================================
// TEMA
// ================================================================
function updateThemeButton(theme) {
  const button = document.getElementById('theme-btn');
  const icon = document.createElement('span');
  icon.textContent = theme === 'dark' ? '🌙' : '☀️';
  button.replaceChildren(icon, document.createTextNode(theme === 'dark' ? ' Koyu' : ' Açık'));
  button.setAttribute('aria-pressed', String(theme === 'light'));
}

(function initTheme() {
  const theme = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', theme);
  updateThemeButton(theme);
})();

document.getElementById('theme-btn').addEventListener('click', () => {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
  updateThemeButton(next);
});

// ================================================================
// OVERLAY / HATA YÖNETİMİ
// ================================================================
function createElement(tagName, className, text = '') {
  const element = document.createElement(tagName);
  if (className) element.className = className;
  if (text) element.textContent = text;
  return element;
}

function setPanelMessage(container, text, className = 'panel-message') {
  container.replaceChildren(createElement('div', className, text));
}

function setStartupStatus(text) {
  const status = document.getElementById('startup-status');
  if (!status) return;
  const label = status.querySelector('span:last-child');
  if (label) label.textContent = text;
  status.classList.remove('hidden');
}

function hideStartupStatus() {
  const status = document.getElementById('startup-status');
  if (status) status.classList.add('hidden');
}

function showOverlay(text) {
  const overlay = document.getElementById('app-overlay');
  overlay.classList.remove('hidden');
  overlay.replaceChildren(
    createElement('div', 'loader-spinner'),
    createElement('div', 'loader-text', text)
  );
}

function hideOverlay() {
  document.getElementById('app-overlay').classList.add('hidden');
}

function showFatalError(message, detail = '') {
  const overlay = document.getElementById('app-overlay');
  const card = createElement('div', 'error-overlay');
  card.appendChild(createElement('h3', '', '⚠ Yükleme Hatası'));
  card.appendChild(createElement('p', '', message));

  if (detail) {
    const detailLine = createElement('p');
    detailLine.style.marginTop = '10px';
    detailLine.appendChild(createElement('code', '', detail));
    card.appendChild(detailLine);
  }

  const help = createElement('p');
  help.style.marginTop = '16px';
  help.style.fontSize = '11px';
  help.append('Repo kökünde ');
  help.appendChild(createElement('code', '', 'index.json'));
  help.append(' dosyasının olduğundan emin olun. Ardından sayfayı yenileyin.');
  card.appendChild(help);

  overlay.classList.remove('hidden');
  overlay.replaceChildren(card);
}

// ================================================================
// ÖNBELLEK VE GLOBAL STATE
// ================================================================
const mdCache = new Map();   // path → markdown string
const mdRequestCache = new Map(); // path → Promise<string>
let root, svg, g, zoomBehavior;
let width, height;
let nodeCounter = 0;
let activeKbNode = null;
let isAllExpanded = false;
const duration = 250;

// Arama indeksi: sadece başlıklar (önce) + cache'e alınan içerikler (sonra)
const SEARCH_INDEX = new Map(); // nodeId → { name, type, path, content|null }
const SLUG_INDEX = new Map();   // canonical slug veya legacy alias → node
let searchIndexPromise = null;
let searchWarmupPromise = null;
let searchWarmupDone = false;
let searchRequestToken = 0;
let detailRequestToken = 0;
let resolveTreeReady;
const treeReadyPromise = new Promise(resolve => { resolveTreeReady = resolve; });

// ================================================================
// CANVAS ÖLÇÜM
// ================================================================
const _cv = document.createElement('canvas');
const _cx = _cv.getContext('2d');
function getTextWidth(text, fs) {
  _cx.font = `${fs}px "JetBrains Mono"`;
  return _cx.measureText(text).width;
}
function nodeWidth(d) {
  return Math.max(100, getTextWidth(d.data.name, d.depth === 0 ? 13 : 11) + 40);
}

// ================================================================
// INDEX.JSON YÜKLEME VE BAŞLATMA
// ================================================================
async function bootstrap() {
  setStartupStatus('Harita hazırlanıyor...');
  try {
    const response = await fetch('index.json');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    if (!data || data.type !== 'folder' || !Array.isArray(data.children)) {
      throw new Error('Geçersiz JSON formatı');
    }

    // Doğrudan içerik bağlantısında Markdown isteğini D3 çiziminden önce başlat.
    prefetchInitialHashContent(data);
    initD3(data);
    resolveTreeReady();
    hideStartupStatus();
  } catch (error) {
    hideStartupStatus();
    showFatalError('index.json dosyası yüklenemedi veya okunamadı.', error.message);
  }
}

async function loadSearchIndex() {
  try {
    const response = await fetch('search-index.json');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    if (!data || !Array.isArray(data.items)) throw new Error('Geçersiz arama indeksi');

    await treeReadyPromise;
    data.items.forEach(item => {
      const node = findNodeBySlug(item.slug);
      const entry = node ? SEARCH_INDEX.get(node.id) : null;
      if (entry) entry.content = item.content || '';
    });
    searchWarmupDone = true;
    return true;
  } catch (error) {
    console.warn('search-index.json yüklenemedi; Markdown fallback kullanılacak.', error);
    return false;
  }
}

function ensureSearchIndexRequested() {
  if (!searchIndexPromise) searchIndexPromise = loadSearchIndex();
  return searchIndexPromise;
}

// ================================================================
// MARKDOWN İSTEKLERİ VE İLK DERİN LİNK ÖN-YÜKLEMESİ
// ================================================================
async function getMarkdown(path) {
  if (mdCache.has(path)) return mdCache.get(path);
  if (mdRequestCache.has(path)) return mdRequestCache.get(path);

  const request = fetch(path)
    .then(response => {
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.text();
    })
    .then(text => {
      mdCache.set(path, text);
      return text;
    })
    .finally(() => mdRequestCache.delete(path));

  mdRequestCache.set(path, request);
  return request;
}

function currentDecodedHash() {
  const rawHash = window.location.hash.substring(1);
  if (!rawHash) return '';
  try {
    return decodeURIComponent(rawHash);
  } catch (error) {
    console.warn('Geçersiz URL hash değeri:', rawHash, error);
    return '';
  }
}

function findDataNodeBySlug(node, slug) {
  if (!node || !slug) return null;
  if (node.slug === slug || (node.aliases || []).includes(slug)) return node;
  for (const child of node.children || []) {
    const match = findDataNodeBySlug(child, slug);
    if (match) return match;
  }
  return null;
}

function prefetchInitialHashContent(data) {
  const slug = currentDecodedHash();
  const target = findDataNodeBySlug(data, slug);
  if (!target || target.type !== 'file' || !target.path) return Promise.resolve(null);
  return getMarkdown(target.path).catch(error => {
    console.warn(`İlk içerik ön-yüklemesi başarısız: ${target.path}`, error);
    return null;
  });
}

// ================================================================
// D3 BAŞLATMA (verisi dışarıdan gelir)
// ================================================================
function initD3(data) {
  const panel = document.getElementById('mindmap-panel');
  width = panel.clientWidth;
  height = panel.clientHeight;

  svg = d3.select('#svg');
  g = svg.append('g');

  zoomBehavior = d3.zoom()
    .scaleExtent([0.1, 3])
    .on('zoom', e => g.attr('transform', e.transform));
  svg.call(zoomBehavior).on('dblclick.zoom', null);

  root = d3.hierarchy(data, d => d.children);
  root.x0 = height / 2;
  root.y0 = 0;
  root.eachBefore(d => { d.id = ++nodeCounter; });

  // Arama indeksini başlıklar ile oluştur
  root.each(d => {
    SEARCH_INDEX.set(d.id, {
      name: d.data.name,
      type: d.data.type,
      path: d.data.path || null,
      content: null
    });

    if (d.data.slug) SLUG_INDEX.set(d.data.slug, d);
    (d.data.aliases || []).forEach(alias => {
      if (!SLUG_INDEX.has(alias)) SLUG_INDEX.set(alias, d);
    });
  });

  // Başlangıçta sadece kök açık
  root.children && root.children.forEach(collapse);
  update(root);

  svg.transition().duration(0).call(
    zoomBehavior.transform,
    d3.zoomIdentity.translate(width / 4, height / 2).scale(0.9)
  );

  checkUrlHash();

  // Panel boyutlandırınca haritayı yeniden ortala
  new ResizeObserver(() => {
    refreshViewportSize();
    if (activeKbNode && svg && svg.node()) {
      const currentScale = d3.zoomTransform(svg.node()).k;
      panToNode(activeKbNode, currentScale, 0);
    }
  }).observe(panel);
}

// ================================================================
// D3 AĞAÇ MANTIĞI
// ================================================================
function collapse(d) {
  if (d.children) { d._children = d.children; d.children = null; }
  if (d._children) d._children.forEach(collapse);
}

function expandAll(d) {
  if (d._children) { d.children = d._children; d._children = null; }
  if (d.children) d.children.forEach(expandAll);
}

function getAllNodes(d, list = []) {
  list.push(d);
  if (d.children) d.children.forEach(c => getAllNodes(c, list));
  if (d._children) d._children.forEach(c => getAllNodes(c, list));
  return list;
}

function findNodeById(id) {
  return getAllNodes(root).find(n => n.id === id);
}

function findNodeBySlug(slug) {
  return SLUG_INDEX.get(slug) || null;
}

function update(source, skipAnim = false) {
  const dur = skipAnim ? 0 : duration;
  const treeLayout = d3.tree().nodeSize([45, 200]);
  const treeData = treeLayout(root);
  const nodes = treeData.descendants();
  const links = treeData.descendants().slice(1);

  nodes.forEach(d => { d.y = d.depth * 220; });

  // NODES
  const node = g.selectAll('g.node').data(nodes, d => d.id);

  const nodeEnter = node.enter().append('g')
    .attr('class', d => {
      const lvl = d.depth === 0 ? 'node-root' : `node-l${Math.min(d.depth, 4)}`;
      return `node ${lvl}`;
    })
    .attr('transform', () => `translate(${source.y0},${source.x0})`)
    .attr('tabindex', 0)
    .attr('role', 'treeitem')
    .attr('aria-label', d => `${d.data.name}${d.data.type === 'file' ? ', içerik' : ', klasör'}`)
    .style('opacity', 0)
    .on('click', (event, d) => clickNode(d))
    .on('keydown', (event, d) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        event.stopPropagation();
        clickNode(d);
      }
    });

  nodeEnter.append('rect').attr('class', 'node-rect')
    .attr('y', -16).attr('height', 32).attr('rx', 16).attr('ry', 16);

  nodeEnter.append('text').attr('class', 'node-text')
    .attr('dy', '.35em').attr('x', 16)
    .text(d => d.data.name);

  nodeEnter.append('circle')
    .attr('class', d => d.data.type === 'file' ? 'content-indicator' : 'collapse-indicator')
    .attr('r', 0); // başlangıçta gizli, update'de ayarlanır

  const nodeUpdate = nodeEnter.merge(node);

  nodeUpdate.select('.node-rect')
    .attr('width', d => nodeWidth(d));

  nodeUpdate.select('circle')
    .attr('cx', d => nodeWidth(d) - 14)
    .attr('r', d => {
      if (d.data.type === 'file') return 4;
      if (d.children || d._children) return 3;
      return 0;
    });

  nodeUpdate.classed('kb-focus', d => activeKbNode && d.id === activeKbNode.id);

  nodeUpdate.transition().duration(dur)
    .attr('transform', d => `translate(${d.y},${d.x})`)
    .style('opacity', 1);

  node.exit().transition().duration(dur)
    .attr('transform', () => `translate(${source.y},${source.x})`)
    .style('opacity', 0).remove();

  // LINKS
  const link = g.selectAll('path.link').data(links, d => d.id);

  const diagFrom = { x: source.x0, y: source.y0 };
  link.enter().insert('path', 'g').attr('class', 'link')
    .attr('d', () => diagonal(diagFrom, diagFrom))
    .merge(link).transition().duration(dur)
    .attr('d', d => diagonal(d, d.parent));

  link.exit().transition().duration(dur)
    .attr('d', d => diagonal({ x: d.x, y: d.y }, { x: d.x, y: d.y }))
    .remove();

  nodes.forEach(d => { d.x0 = d.x; d.y0 = d.y; });
}

function diagonal(s, d) {
  const rw = d.data ? nodeWidth(d) : 0;
  const sx = s.y, sy = s.x;
  const tx = d.y + rw, ty = d.x;
  const mx = (sx + tx) / 2;
  return `M ${sx} ${sy} C ${mx} ${sy}, ${mx} ${ty}, ${tx} ${ty}`;
}

// ================================================================
// TIKLAMA VE KLAVYE
// ================================================================
function clickNode(d) {
  activeKbNode = d;
  if (d.children) { d._children = d.children; d.children = null; }
  else if (d._children) { d.children = d._children; d._children = null; }
  update(d);
  if (d.data.type === 'file') showDetail(d);
}

function refreshViewportSize() {
  const panel = document.getElementById('mindmap-panel');
  if (!panel) return;
  const nextWidth = panel.clientWidth;
  const nextHeight = panel.clientHeight;
  if (Number.isFinite(nextWidth) && nextWidth > 0) width = nextWidth;
  if (Number.isFinite(nextHeight) && nextHeight > 0) height = nextHeight;
}

function ensureNodeVisible(node) {
  if (!node) return false;
  let changed = false;
  let p = node.parent;
  while (p) {
    if (p._children) {
      p.children = p._children;
      p._children = null;
      changed = true;
    }
    p = p.parent;
  }
  if (changed) update(root, true);
  return changed;
}

function panToNode(node, scale = 1.3, speed = 500) {
  refreshViewportSize();

  if (!node) return false;
  if (!svg || !svg.node()) return false;
  if (!Number.isFinite(scale)) scale = 1.3;
  if (!Number.isFinite(width) || !Number.isFinite(height)) return false;
  if (!Number.isFinite(node.x) || !Number.isFinite(node.y)) return false;

  svg.transition().duration(speed).call(
    zoomBehavior.transform,
    d3.zoomIdentity
      .translate(width / 2 - node.y * scale, height / 2 - node.x * scale)
      .scale(scale)
  );
  return true;
}

function panToNodeWhenReady(node, scale = 1.3, speed = 500, tries = 4) {
  if (panToNode(node, scale, speed)) return;
  if (tries <= 0) return;

  requestAnimationFrame(() => {
    refreshViewportSize();
    if (root && node && (!Number.isFinite(node.x) || !Number.isFinite(node.y))) {
      update(root, true);
    }
    panToNodeWhenReady(node, scale, speed, tries - 1);
  });
}

function syncActiveNodeFocus() {
  if (!g) return;
  g.selectAll('.node').classed('kb-focus', d => activeKbNode && d.id === activeKbNode.id);
}

// Klavye
let isDetailHovered = false;
document.getElementById('detail-panel').addEventListener('mouseenter', () => isDetailHovered = true);
document.getElementById('detail-panel').addEventListener('mouseleave', () => isDetailHovered = false);

document.addEventListener('keydown', e => {
  const searchInput = document.getElementById('search-input');
  const isSearchFocused = document.activeElement === searchInput;

  if (e.key === 'Escape') {
    closePanel();
    clearSearch();
    searchInput.blur();
    return;
  }

  if (isSearchFocused) {
    if (e.key === 'Enter') searchInput.blur();
    return;
  }

  if (isDetailHovered && !document.getElementById('detail-panel').classList.contains('closed')
    && ['ArrowUp', 'ArrowDown'].includes(e.key)) {
    e.preventDefault();
    document.getElementById('d-body').scrollBy({ top: e.key === 'ArrowDown' ? 80 : -80, behavior: 'auto' });
    return;
  }

  if (!['ArrowUp','ArrowDown','ArrowLeft','ArrowRight','Enter'].includes(e.key)) return;
  if (!root) return;
  if (!activeKbNode) activeKbNode = root;
  e.preventDefault();

  const siblings = activeKbNode.parent
    ? (activeKbNode.parent.children || activeKbNode.parent._children)
    : null;
  const idx = siblings ? siblings.indexOf(activeKbNode) : -1;
  let layoutChanged = false;
  let nodeChanged = false;

  if (e.key === 'ArrowRight') {
    if (activeKbNode._children) {
      activeKbNode.children = activeKbNode._children;
      activeKbNode._children = null;
      layoutChanged = true;
    } else if (activeKbNode.children?.length) {
      activeKbNode = activeKbNode.children[0];
      nodeChanged = true;
    }
  } else if (e.key === 'ArrowLeft') {
    if (activeKbNode.children) {
      activeKbNode._children = activeKbNode.children;
      activeKbNode.children = null;
      layoutChanged = true;
    } else if (activeKbNode.parent) {
      activeKbNode = activeKbNode.parent;
      nodeChanged = true;
    }
  } else if (e.key === 'ArrowUp' && siblings && idx > 0) {
    activeKbNode = siblings[idx - 1];
    nodeChanged = true;
  } else if (e.key === 'ArrowDown' && siblings && idx < siblings.length - 1) {
    activeKbNode = siblings[idx + 1];
    nodeChanged = true;
  } else if (e.key === 'Enter') {
    clickNode(activeKbNode);
    panToNode(activeKbNode, d3.zoomTransform(svg.node()).k, 200);
    return;
  }

  if (layoutChanged) {
    update(activeKbNode);
  } else {
    g.selectAll('.node').classed('kb-focus', d => activeKbNode && d.id === activeKbNode.id);
  }

  if (nodeChanged && activeKbNode.data.type === 'file') {
    if (!document.getElementById('detail-panel').classList.contains('closed')) {
      showDetail(activeKbNode);
    }
  }

  panToNode(activeKbNode, d3.zoomTransform(svg.node()).k, 150);
});

// ================================================================
// DETAY PANELİ — MARKDOWN FETCH
// ================================================================
async function showDetail(d, focusRequest = null) {
  if (d.data.type !== 'file') return;

  const requestToken = ++detailRequestToken;
  const panel = document.getElementById('detail-panel');
  panel.classList.remove('closed');
  panel.setAttribute('aria-hidden', 'false');

  if (d.data.slug && window.location.hash.substring(1) !== d.data.slug) {
    history.replaceState(null, '', `#${d.data.slug}`);
  }

  const breadcrumb = document.getElementById('d-bc');
  const breadcrumbNodes = [];
  const ancestors = [];
  let current = d.parent;
  while (current) {
    ancestors.unshift(current);
    current = current.parent;
  }

  ancestors.forEach((ancestor, index) => {
    if (index > 0) breadcrumbNodes.push(createElement('span', 'bc-sep', '›'));
    const link = createElement('button', 'bc-link', ancestor.data.name);
    link.type = 'button';
    link.dataset.nid = String(ancestor.id);
    link.addEventListener('click', () => clickBreadcrumb(ancestor.id));
    breadcrumbNodes.push(link);
  });
  breadcrumb.replaceChildren(...(breadcrumbNodes.length ? breadcrumbNodes : [document.createTextNode('Ana Sayfa')]));

  document.getElementById('d-title').textContent = d.data.name;
  const body = document.getElementById('d-body');

  if (mdCache.has(d.data.path)) {
    renderMarkdown(mdCache.get(d.data.path), body, focusRequest);
    return;
  }

  setPanelMessage(body, 'Yükleniyor...', 'detail-loading');

  try {
    const text = await getMarkdown(d.data.path);
    if (requestToken !== detailRequestToken) return;
    const entry = SEARCH_INDEX.get(d.id);
    if (entry) entry.content = text.replace(/[#*`>_\[\]]/g, '');
    renderMarkdown(text, body, focusRequest);
  } catch (error) {
    if (requestToken !== detailRequestToken) return;
    const errorBox = createElement('div', 'detail-error');
    errorBox.append('Dosya yüklenemedi.', document.createElement('br'), document.createElement('br'));
    errorBox.appendChild(createElement('code', '', d.data.path));
    errorBox.append(document.createElement('br'), document.createElement('br'));
    errorBox.appendChild(createElement('small', '', `Hata: ${error.message}`));
    body.replaceChildren(errorBox);
  }
}

function renderMarkdown(text, container, focusRequest = null) {
  try {
    const safeHtml = DOMPurify.sanitize(marked.parse(text));
    const markdown = createElement('div', 'md');
    markdown.innerHTML = safeHtml;
    container.replaceChildren(markdown);
    container.scrollTop = 0;
    addCopyButtons(container);
    focusSearchMatch(container, focusRequest);
  } catch (error) {
    const errorBox = createElement('div', 'detail-error', 'İçerik render edilemedi.');
    errorBox.append(document.createElement('br'));
    errorBox.appendChild(createElement('small', '', error.message));
    container.replaceChildren(errorBox);
  }
}

async function copyText(text) {
  if (navigator.clipboard && window.isSecureContext) {
    await navigator.clipboard.writeText(text);
    return;
  }
  const textarea = document.createElement('textarea');
  textarea.value = text;
  textarea.setAttribute('readonly', '');
  textarea.style.position = 'fixed';
  textarea.style.opacity = '0';
  document.body.appendChild(textarea);
  textarea.select();
  const copied = document.execCommand('copy');
  textarea.remove();
  if (!copied) throw new Error('Kopyalama desteklenmiyor');
}

function setCopyButtonState(button, label, successful = false) {
  button.textContent = label;
  button.style.background = successful ? 'var(--accent2)' : '';
  button.style.color = successful ? '#fff' : '';
  window.setTimeout(() => {
    button.textContent = 'Kopyala';
    button.style.background = '';
    button.style.color = '';
  }, 2000);
}

function addCopyButtons(container) {
  container.querySelectorAll('pre').forEach(pre => {
    if (pre.parentElement.classList.contains('code-block-wrapper')) return;
    const wrapper = createElement('div', 'code-block-wrapper');
    pre.parentNode.insertBefore(wrapper, pre);
    wrapper.appendChild(pre);
    const button = createElement('button', 'copy-btn', 'Kopyala');
    button.type = 'button';
    button.setAttribute('aria-label', 'Kod bloğunu kopyala');
    button.addEventListener('click', async () => {
      const code = pre.querySelector('code');
      try {
        await copyText(code ? code.innerText : pre.innerText);
        setCopyButtonState(button, 'Kopyalandı!', true);
      } catch (error) {
        console.warn('Kopyalama başarısız:', error);
        setCopyButtonState(button, 'Kopyalanamadı');
      }
    });
    wrapper.appendChild(button);
  });
}

function clickBreadcrumb(id) {
  const node = findNodeById(id);
  if (!node) return;
  activeKbNode = node;
  let p = node;
  while (p) {
    if (p._children) { p.children = p._children; p._children = null; }
    p = p.parent;
  }
  update(root);
  syncActiveNodeFocus();
  panToNodeWhenReady(node, 1.1, 500);
  closePanel();
}

function closePanel(clearHash = true) {
  detailRequestToken += 1;
  const panel = document.getElementById('detail-panel');
  panel.classList.add('closed');
  panel.setAttribute('aria-hidden', 'true');
  if (clearHash && window.location.hash) {
    history.replaceState(null, '', window.location.pathname + window.location.search);
  }
  document.querySelectorAll('.active-snippet').forEach(element => element.classList.remove('active-snippet'));
  g && g.selectAll('.node').classed('kb-focus', false);
}

// ================================================================
// HASH İLE DERİN LİNK
// ================================================================
function checkUrlHash() {
  const hash = currentDecodedHash();
  if (!hash) {
    closePanel(false);
    return;
  }

  const target = findNodeBySlug(hash);
  if (target) {
    window.setTimeout(() => focusAndOpen(target.id), 0);
  } else {
    console.warn(`Hash "${hash}" için node bulunamadı.`);
  }
}

window.addEventListener('hashchange', checkUrlHash);

// ================================================================
// ZOOM KONTROLLERI
// ================================================================
document.getElementById('btn-zoom-in').addEventListener('click', () =>
  svg.transition().duration(300).call(zoomBehavior.scaleBy, 1.2));
document.getElementById('btn-zoom-out').addEventListener('click', () =>
  svg.transition().duration(300).call(zoomBehavior.scaleBy, 0.8));
document.getElementById('btn-zoom-reset').addEventListener('click', resetMap);
document.getElementById('btn-toggle-all').addEventListener('click', () => {
  if (isAllExpanded) { root.children && root.children.forEach(collapse); isAllExpanded = false; }
  else { expandAll(root); isAllExpanded = true; }
  update(root);
});
document.getElementById('btn-close-detail').addEventListener('click', closePanel);

function resetMap() {
  root && root.children && root.children.forEach(collapse);
  update(root, true);
  refreshViewportSize();
  svg.transition().duration(500).call(
    zoomBehavior.transform,
    d3.zoomIdentity.translate(width / 4, height / 2).scale(0.9)
  );
  activeKbNode = root;
  g && g.selectAll('.node').classed('kb-focus', false);
}

// ================================================================
// ARAMA
// ================================================================
function normalizeSearchText(value) {
  return String(value || '').normalize('NFC').toLocaleLowerCase('tr-TR').trim();
}

function normalizeSearchSliceText(value) {
  return String(value || '').normalize('NFC').toLocaleLowerCase('tr-TR');
}

function appendHighlightedText(container, text, term) {
  const normalizedText = normalizeSearchSliceText(text);
  const normalizedTerm = normalizeSearchText(term);
  if (!normalizedTerm) {
    container.appendChild(document.createTextNode(text));
    return;
  }

  let cursor = 0;
  let matchIndex = normalizedText.indexOf(normalizedTerm);
  while (matchIndex !== -1) {
    if (matchIndex > cursor) {
      container.appendChild(document.createTextNode(text.slice(cursor, matchIndex)));
    }
    const highlight = createElement('span', 'highlight', text.slice(matchIndex, matchIndex + normalizedTerm.length));
    container.appendChild(highlight);
    cursor = matchIndex + normalizedTerm.length;
    matchIndex = normalizedText.indexOf(normalizedTerm, cursor);
  }
  if (cursor < text.length) container.appendChild(document.createTextNode(text.slice(cursor)));
}


function findSearchMatchPositions(text, term) {
  const normalizedText = normalizeSearchSliceText(text);
  const normalizedTerm = normalizeSearchText(term);
  if (!normalizedTerm) return [];

  const positions = [];
  let index = normalizedText.indexOf(normalizedTerm);
  while (index !== -1) {
    positions.push({ start: index, end: index + normalizedTerm.length });
    index = normalizedText.indexOf(normalizedTerm, index + normalizedTerm.length);
  }
  return positions;
}

function highlightSearchMatches(rootElement, term) {
  if (!rootElement || !normalizeSearchText(term)) return [];

  const walker = document.createTreeWalker(rootElement, NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      const parent = node.parentElement;
      if (!parent || !node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
      if (parent.closest('script,style,button,.copy-btn,.content-search-highlight')) {
        return NodeFilter.FILTER_REJECT;
      }
      return NodeFilter.FILTER_ACCEPT;
    }
  });

  const textNodes = [];
  while (walker.nextNode()) textNodes.push(walker.currentNode);

  const highlights = [];
  let occurrenceIndex = 0;

  textNodes.forEach(textNode => {
    const sourceText = textNode.nodeValue;
    const positions = findSearchMatchPositions(sourceText, term);
    if (!positions.length) return;

    const fragment = document.createDocumentFragment();
    let cursor = 0;
    positions.forEach(position => {
      if (position.start > cursor) {
        fragment.appendChild(document.createTextNode(sourceText.slice(cursor, position.start)));
      }
      const mark = createElement(
        'mark',
        'content-search-highlight',
        sourceText.slice(position.start, position.end)
      );
      mark.dataset.searchOccurrence = String(occurrenceIndex);
      occurrenceIndex += 1;
      highlights.push(mark);
      fragment.appendChild(mark);
      cursor = position.end;
    });
    if (cursor < sourceText.length) {
      fragment.appendChild(document.createTextNode(sourceText.slice(cursor)));
    }
    textNode.replaceWith(fragment);
  });

  return highlights;
}

function focusSearchMatch(container, focusRequest) {
  if (!container || !focusRequest || !normalizeSearchText(focusRequest.term)) return null;

  const markdown = container.querySelector('.md');
  const highlights = highlightSearchMatches(markdown, focusRequest.term);
  if (!highlights.length) return null;

  const requestedIndex = Number.isInteger(focusRequest.occurrenceIndex)
    ? focusRequest.occurrenceIndex
    : 0;
  const target = highlights[requestedIndex] || highlights[0];
  target.classList.add('active');
  target.setAttribute('aria-current', 'true');

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      if (!target.isConnected) return;
      const containerRect = container.getBoundingClientRect();
      const targetRect = target.getBoundingClientRect();
      const targetTop = container.scrollTop + targetRect.top - containerRect.top;
      const top = Math.max(
        0,
        targetTop - (container.clientHeight / 2) + (targetRect.height / 2)
      );
      const reduceMotion = window.matchMedia
        && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      container.scrollTo({ top, behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  });

  return target;
}

let searchTimeout;
const searchInputElement = document.getElementById('search-input');
searchInputElement.addEventListener('focus', ensureSearchIndexRequested, { once: true });
searchInputElement.addEventListener('input', function () {
  document.getElementById('search-clear').style.display = this.value.length > 0 ? 'block' : 'none';
  window.clearTimeout(searchTimeout);
  searchTimeout = window.setTimeout(triggerSearch, 80);
});

document.getElementById('search-clear').addEventListener('click', clearSearch);
document.getElementById('search-panel-close').addEventListener('click', clearSearch);

async function warmSearchIndex() {
  if (searchWarmupDone) return;
  if (searchWarmupPromise) return searchWarmupPromise;

  const pending = [];
  SEARCH_INDEX.forEach((entry, nodeId) => {
    if (entry && entry.type === 'file' && entry.path && entry.content === null) {
      pending.push({ nodeId, entry });
    }
  });

  searchWarmupPromise = (async () => {
    const queue = [...pending];
    const worker = async () => {
      while (queue.length) {
        const item = queue.shift();
        try {
          const text = await getMarkdown(item.entry.path);
          item.entry.content = text.replace(/[#*`>_\[\]]/g, '');
        } catch (error) {
          console.warn(`Arama fallback dosyası yüklenemedi: ${item.entry.path}`, error);
        }
      }
    };
    await Promise.all(Array.from({ length: Math.min(6, queue.length || 1) }, worker));
    searchWarmupDone = true;
  })();

  try {
    await searchWarmupPromise;
  } finally {
    searchWarmupPromise = null;
  }
}

async function ensureSearchReadyIfNeeded(panel, results) {
  if (searchWarmupDone) return;
  await ensureSearchIndexRequested();
  if (searchWarmupDone) return;

  panel.classList.remove('closed');
  document.getElementById('search-count').textContent = 'İndeks hazırlanıyor...';
  setPanelMessage(results, 'Not içerikleri ilk arama için hazırlanıyor...');
  await warmSearchIndex();
}

function clearSearch() {
  searchRequestToken += 1;
  document.getElementById('search-input').value = '';
  document.getElementById('search-clear').style.display = 'none';
  document.getElementById('search-panel').classList.add('closed');
  if (svg) {
    svg.selectAll('.node').classed('search-match', false);
    svg.selectAll('.link').classed('highlighted', false);
  }
}

function collectSnippets(entry, term) {
  const snippets = [];
  const normalizedTerm = normalizeSearchText(term);
  if (normalizeSearchText(entry.name).includes(normalizedTerm)) {
    snippets.push({ text: entry.name, source: 'title', occurrenceIndex: null });
  }

  if (!entry.content) return snippets;
  const normalizedContent = normalizeSearchSliceText(entry.content);
  let index = normalizedContent.indexOf(normalizedTerm);
  let occurrenceIndex = 0;
  while (index !== -1 && occurrenceIndex < 3) {
    const start = Math.max(0, index - 30);
    const end = Math.min(entry.content.length, index + normalizedTerm.length + 50);
    let snippet = entry.content.slice(start, end);
    if (start > 0) snippet = `…${snippet}`;
    if (end < entry.content.length) snippet = `${snippet}…`;
    snippets.push({ text: snippet, source: 'content', occurrenceIndex });
    index = normalizedContent.indexOf(normalizedTerm, index + normalizedTerm.length);
    occurrenceIndex += 1;
  }
  return snippets;
}

function createSearchResultGroup(node, snippets, term, results) {
  const group = createElement('div', 'search-group');
  const title = createElement('button', 'search-group-title');
  title.type = 'button';
  title.dataset.nid = String(node.id);
  title.setAttribute('aria-label', `${node.data.name} içeriğini aç`);

  const titleText = createElement('span');
  titleText.appendChild(createElement('span', '', '› '));
  titleText.lastChild.style.color = 'var(--text-dim)';
  titleText.lastChild.style.fontSize = '10px';
  titleText.appendChild(document.createTextNode(node.data.name));
  title.append(titleText, createElement('span', 'badge', String(snippets.length)));
  group.appendChild(title);

  const firstContentMatch = snippets.find(item => item.source === 'content') || null;
  const activate = (element, selectedMatch = null) => {
    results.querySelectorAll('.active-snippet').forEach(item => item.classList.remove('active-snippet'));
    element.classList.add('active-snippet');
    const match = selectedMatch && selectedMatch.source === 'content'
      ? selectedMatch
      : firstContentMatch;
    const focusRequest = match
      ? { term, occurrenceIndex: match.occurrenceIndex }
      : null;
    focusAndOpen(node.id, focusRequest);
  };
  title.addEventListener('click', () => activate(title));

  snippets.forEach(item => {
    const snippet = createElement('button', 'search-snippet');
    snippet.type = 'button';
    snippet.dataset.nid = String(node.id);
    if (Number.isInteger(item.occurrenceIndex)) {
      snippet.dataset.occurrenceIndex = String(item.occurrenceIndex);
    }
    appendHighlightedText(snippet, item.text, term);
    snippet.addEventListener('click', () => activate(snippet, item));
    group.appendChild(snippet);
  });
  return group;
}

async function triggerSearch() {
  if (!root) return;
  const input = document.getElementById('search-input');
  const term = normalizeSearchText(input.value);
  const panel = document.getElementById('search-panel');
  const results = document.getElementById('search-results');

  svg.selectAll('.node').classed('search-match', false);
  svg.selectAll('.link').classed('highlighted', false);

  if (!term) {
    panel.classList.add('closed');
    return;
  }
  panel.classList.remove('closed');

  const requestToken = ++searchRequestToken;
  await ensureSearchReadyIfNeeded(panel, results);
  if (requestToken !== searchRequestToken) return;

  const currentTerm = normalizeSearchText(input.value);
  if (!currentTerm) {
    panel.classList.add('closed');
    return;
  }

  let totalMatches = 0;
  const matchedNodes = [];
  const fragment = document.createDocumentFragment();

  getAllNodes(root).forEach(node => {
    const entry = SEARCH_INDEX.get(node.id);
    if (!entry) return;
    const snippets = collectSnippets(entry, currentTerm);
    if (!snippets.length) return;

    totalMatches += snippets.length;
    matchedNodes.push(node);
    fragment.appendChild(createSearchResultGroup(node, snippets, currentTerm, results));
  });

  document.getElementById('search-count').textContent = `${totalMatches} Sonuç`;
  if (fragment.childNodes.length) results.replaceChildren(fragment);
  else setPanelMessage(results, 'Sonuç bulunamadı.');

  if (matchedNodes.length > 0) {
    matchedNodes.forEach(targetNode => {
      let parent = targetNode;
      while (parent.parent) {
        if (parent.parent._children) {
          parent.parent.children = parent.parent._children;
          parent.parent._children = null;
        }
        parent = parent.parent;
      }
    });
    update(root, true);
    window.setTimeout(() => {
      matchedNodes.forEach(targetNode => {
        svg.selectAll('.node').filter(node => node.id === targetNode.id).classed('search-match', true);
        let current = targetNode;
        while (current.parent) {
          svg.selectAll('.link')
            .filter(link => link && link.target && link.target.id === current.id)
            .classed('highlighted', true);
          current = current.parent;
        }
      });
    }, 60);
  }
}

function focusAndOpen(id, focusRequest = null) {
  const target = findNodeById(id);
  if (!target) return;

  activeKbNode = target;
  ensureNodeVisible(target);
  syncActiveNodeFocus();

  if (target.data.type === 'file') {
    showDetail(target, focusRequest);
  } else {
    closePanel();
    if (target._children) {
      target.children = target._children;
      target._children = null;
      update(target);
    }
    syncActiveNodeFocus();
  }

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      panToNodeWhenReady(target, 1.3, 500);
    });
  });
}

// ================================================================
// PANEL RESIZE
// ================================================================
let isResizingLeft = false, isResizingRight = false;

document.getElementById('rsz-left').addEventListener('mousedown', e => {
  isResizingLeft = true; document.body.classList.add('resizing'); e.preventDefault();
});
document.getElementById('rsz-right').addEventListener('mousedown', e => {
  isResizingRight = true; document.body.classList.add('resizing'); e.preventDefault();
});

document.addEventListener('mousemove', e => {
  if (isResizingLeft) {
    let w = Math.max(200, Math.min(window.innerWidth / 2, e.clientX));
    document.documentElement.style.setProperty('--search-width', w + 'px');
  }
  if (isResizingRight) {
    let w = Math.max(300, Math.min(window.innerWidth * 0.7, window.innerWidth - e.clientX));
    document.documentElement.style.setProperty('--detail-width', w + 'px');
  }
});

document.addEventListener('mouseup', () => {
  if (isResizingLeft || isResizingRight) {
    isResizingLeft = isResizingRight = false;
    document.body.classList.remove('resizing');
  }
});

// ================================================================
// BAŞLAT
// ================================================================
bootstrap();
