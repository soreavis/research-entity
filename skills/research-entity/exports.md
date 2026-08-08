# HTML & PDF Export Pipeline

Loaded by the `research-entity` skill during Step 7 (Export) when `--export=html|pdf|both` is set, or in convert-only mode.

## HTML export

Self-contained HTML with sticky-sidebar TOC + scrollspy + print CSS. No external CSS dependency (no StackEdit CDN; works offline).

Key features:
- 320px sticky sidebar TOC (left), generated client-side from h2/h3 headings
- 1100px content max-width
- Scrollspy: active heading gets `.toc-active` highlight; pane auto-scrolls to keep active visible
- Smooth scroll on TOC click
- Responsive: collapses to single-column under 1024px
- Print stylesheet hides TOC, expands content, page-breaks around h2 + mermaid
- Mermaid via CDN (`mermaid@10`), initialized after DOM ready

```bash
OUTPUT_HTML="${OUTPUT%.md}.html"
ENTITY_TITLE="${ENTITY:-Research Dossier}"

cat > "$OUTPUT_HTML" <<HTML_HEAD
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${ENTITY_TITLE} — Research Dossier</title>
<style>
  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", sans-serif;
    line-height: 1.55;
    color: #1a1a1a;
    background: #fff;
  }
  .layout { display: flex; min-height: 100vh; }
  .toc-pane {
    width: 320px;
    flex-shrink: 0;
    border-right: 1px solid #e5e7eb;
    background: #f9fafb;
    overflow-y: auto;
    position: sticky;
    top: 0;
    max-height: 100vh;
    padding: 1.5em 1em;
    font-size: 0.85em;
  }
  .toc-pane h2.toc-title {
    margin: 0 0 1em 0;
    font-size: 0.85em;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #64748b;
    border: none;
    padding: 0;
  }
  .toc-pane ul { list-style: none; padding: 0; margin: 0; }
  .toc-pane li { margin: 0.15em 0; }
  .toc-pane a {
    display: block;
    padding: 0.35em 0.6em;
    color: #475569;
    text-decoration: none;
    border-radius: 3px;
    transition: color 120ms ease, background-color 120ms ease, font-weight 120ms ease;
    line-height: 1.4;
  }
  .toc-pane a:hover { background: #e0f2fe; color: #0369a1; }
  .toc-pane a.toc-active { color: #0369a1; font-weight: 600; background: rgba(3, 102, 214, 0.1); }
  .toc-pane li ul {
    padding-left: 0.9em;
    border-left: 2px solid #e5e7eb;
    margin: 0.15em 0 0.4em 0.4em;
    font-size: 0.95em;
  }
  .content { flex: 1; min-width: 0; padding: 2.5em 3em; max-width: 1100px; }
  .content h1, .content h2, .content h3 { color: #0f172a; line-height: 1.25; margin-top: 1.8em; }
  .content h1 { font-size: 2em; border-bottom: 3px solid #0ea5e9; padding-bottom: .3em; }
  .content h2 { font-size: 1.5em; border-bottom: 1px solid #e5e7eb; padding-bottom: .2em; }
  .content h3 { font-size: 1.2em; }
  .content table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: .9em; }
  .content th, .content td { border: 1px solid #e5e7eb; padding: .6em .8em; text-align: left; vertical-align: top; }
  .content th { background: #f8fafc; font-weight: 600; }
  .content code { background: #f1f5f9; padding: .15em .4em; border-radius: 3px; font-size: .9em; }
  .content pre { background: #f8fafc; padding: 1em; border-radius: 4px; overflow-x: auto; }
  .content blockquote {
    border-left: 4px solid #0ea5e9; margin: 1em 0; padding: .5em 1em;
    background: #f0f9ff; font-style: italic;
  }
  .content a { color: #0369a1; text-decoration: none; }
  .content a:hover { text-decoration: underline; }
  .content hr { border: none; border-top: 1px solid #e5e7eb; margin: 2em 0; }
  .mermaid { background: #fafafa; border-radius: 6px; padding: 1em; margin: 1.5em 0; text-align: center; }
  .mermaid > svg { display: inline-block; max-width: 100%; }
  @media (max-width: 1024px) {
    .layout { flex-direction: column; }
    .toc-pane { width: auto; max-height: none; position: static; border-right: none; border-bottom: 1px solid #e5e7eb; }
    .content { padding: 1.5em; max-width: none; }
  }
  @media print {
    .toc-pane { display: none; }
    .content { padding: 0; max-width: none; font-size: 10pt; }
    .content h1 { page-break-before: auto; }
    .content h2 { page-break-before: always; }
    .content h2:first-of-type { page-break-before: auto; }
    .mermaid, table { page-break-inside: avoid; }
    .content a { color: #1a1a1a; text-decoration: none; }
  }
</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>mermaid.initialize({ startOnLoad: true, theme: 'neutral', flowchart: { useMaxWidth: true } });</script>
</head>
<body>
<div class="layout">
  <nav class="toc-pane" aria-label="Table of contents">
    <h2 class="toc-title">Contents</h2>
    <ul id="toc-list"></ul>
  </nav>
  <main class="content">
HTML_HEAD

# Convert MD body via pandoc; preserve mermaid blocks as <div class="mermaid">
pandoc "$OUTPUT" -f markdown+yaml_metadata_block -t html5 \
  --no-highlight --section-divs \
  | sed 's|<pre><code class="language-mermaid">|<div class="mermaid">|g' \
  | sed 's|</code></pre>|</div>|g' \
  >> "$OUTPUT_HTML"

cat >> "$OUTPUT_HTML" <<'HTML_FOOT'
  </main>
</div>
<script>
(function () {
  function init() {
    var tocList = document.getElementById('toc-list');
    if (!tocList) return;
    var headings = document.querySelectorAll('.content h2[id], .content h3[id]');
    if (!headings.length) return;
    var currentH2Ul = null;
    headings.forEach(function (h) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent.trim();
      li.appendChild(a);
      if (h.tagName === 'H2') {
        tocList.appendChild(li);
        var sub = document.createElement('ul');
        li.appendChild(sub);
        currentH2Ul = sub;
      } else if (h.tagName === 'H3' && currentH2Ul) {
        currentH2Ul.appendChild(li);
      } else {
        tocList.appendChild(li);
      }
    });

    var tocLinks = {};
    document.querySelectorAll('.toc-pane a[href^="#"]').forEach(function (link) {
      var id = decodeURIComponent(link.getAttribute('href').slice(1));
      tocLinks[id] = link;
    });
    var trackable = [];
    headings.forEach(function (h) { if (tocLinks[h.id]) trackable.push(h); });
    if (!trackable.length) return;

    var tocPane = document.querySelector('.toc-pane');
    var active = null;
    function setActive(h) {
      if (h === active) return;
      if (active && tocLinks[active.id]) tocLinks[active.id].classList.remove('toc-active');
      var link = tocLinks[h.id];
      if (link) {
        link.classList.add('toc-active');
        if (tocPane) {
          var lr = link.getBoundingClientRect();
          var pr = tocPane.getBoundingClientRect();
          if (lr.top < pr.top || lr.bottom > pr.bottom) {
            tocPane.scrollTop += lr.top - pr.top - pr.height / 2 + lr.height / 2;
          }
        }
      }
      active = h;
    }
    function update() {
      var cutoff = (window.pageYOffset || document.documentElement.scrollTop) + 120;
      var current = trackable[0];
      for (var i = 0; i < trackable.length; i++) {
        var top = trackable[i].getBoundingClientRect().top + (window.pageYOffset || document.documentElement.scrollTop);
        if (top <= cutoff) current = trackable[i]; else break;
      }
      setActive(current);
    }
    var ticking = false;
    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () { ticking = false; update(); });
    }, { passive: true });
    window.addEventListener('resize', update);
    update();
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
}());
</script>
</body>
</html>
HTML_FOOT
```

## PDF export

Pandoc + xelatex (preferred — full Unicode) with mermaid-filter for native diagram rendering. Falls back to Chrome headless on the HTML if xelatex isn't available.

```bash
OUTPUT_PDF="${OUTPUT%.md}.pdf"

if command -v mermaid-filter >/dev/null 2>&1 && command -v xelatex >/dev/null 2>&1; then
  pandoc "$OUTPUT" -o "$OUTPUT_PDF" \
    --pdf-engine=xelatex \
    -F mermaid-filter \
    -V geometry:"margin=2cm" \
    -V mainfont="Helvetica Neue" \
    -V monofont="Menlo" \
    -V fontsize=10pt \
    --toc --toc-depth=2 \
    --highlight-style=tango
elif command -v xelatex >/dev/null 2>&1; then
  pandoc "$OUTPUT" -o "$OUTPUT_PDF" \
    --pdf-engine=xelatex \
    -V geometry:"margin=2cm" \
    -V mainfont="Helvetica Neue" \
    -V monofont="Menlo" \
    -V fontsize=10pt \
    --toc --toc-depth=2
  echo "Note: mermaid-filter not installed; mermaid diagrams rendered as code blocks."
  echo "Install via: npm install -g mermaid-filter"
elif command -v google-chrome >/dev/null 2>&1 || command -v chromium >/dev/null 2>&1; then
  CHROME=$(command -v google-chrome || command -v chromium)
  "$CHROME" --headless --disable-gpu --print-to-pdf="$OUTPUT_PDF" "file://$OUTPUT_HTML"
else
  echo "ERROR: No PDF engine found. Install xelatex (TeXLive/MacTeX) or Chrome/Chromium."
  exit 1
fi
```

## Pre-flight checks

Before exporting:
- HTML: requires `pandoc` (`brew install pandoc`)
- PDF: requires `pandoc` + (`xelatex` OR Chromium). Best results: `xelatex` + `mermaid-filter` (`npm install -g mermaid-filter`)
- If user requests `--export=pdf` and `xelatex` isn't installed, **report clearly** and offer HTML-only fallback (HTML prints to PDF cleanly via browser print dialog with `Save as PDF`)

## Mermaid validation gate

Always run `mermaid-validation.md` static check **before** exporting. If diagrams fail, **report failures and ask whether to proceed**:
- HTML render failures show as broken boxes — export but warn
- PDF render failures with mermaid-filter cause pandoc to crash — must fix before export

## When to load this file

Load `exports.md` when:
- `--export=html|pdf|both` is set (any value)
- In convert-only mode (always — that's the whole purpose)
- Asked to "regenerate the HTML / PDF" or "re-export"
