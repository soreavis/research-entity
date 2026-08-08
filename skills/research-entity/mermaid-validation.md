# Mermaid Diagram Validation

Loaded by the `research-entity` skill after Step 4 (Draft) and again after any post-draft edit. Mermaid blocks fail to render for predictable reasons; this file documents those reasons and provides both a fast static checker and an optional dynamic-render check.

## Why this matters

Real production runs surfaced these mermaid rendering failures:
- `**bold**` syntax inside node labels — mermaid renders the `**` literally instead of bolding
- `\n` instead of `<br/>` for line breaks — mermaid keeps `\n` as a literal character
- `flowchart LR` (landscape) — produces unreadable wide diagrams when printed portrait
- Side-by-side subgraphs — fail to print readably even when the flowchart direction is `TB`
- Special characters (`(`, `)`, `[`, `]`, `:`, `;`) inside node text — break parsing without quotes
- Lines longer than ~50 chars in nodes — wrap awkwardly and force the diagram horizontal
- Reserved keywords (`end`, `subgraph`, `direction`) used as node IDs without quotes
- Missing closing brackets on subgraphs
- HTML entities not properly escaped (`&` should be `&amp;`)
- Diagram body with embedded `>` quote characters — interpreted as edge syntax
- Empty subgraphs (no nodes inside) — silently dropped or rendered as empty boxes
- More than 3 levels of nested subgraphs — typically render unreadably

## Static validation (no dependencies)

Run this immediately after Step 4 (Draft) and after any post-draft edit:

```bash
# Extract every mermaid block into a temp directory, one file per block
OUTPUT="$1"   # path to the dossier .md file
TMP=$(mktemp -d)
awk '
  /^```mermaid$/ { in_block=1; n++; out=sprintf("%s/diagram-%02d.mmd", "'"$TMP"'", n); next }
  /^```$/ && in_block { in_block=0; out=""; next }
  in_block { print > out }
' "$OUTPUT"

ERRORS=0
for f in "$TMP"/diagram-*.mmd; do
  [ -f "$f" ] || continue
  NAME=$(basename "$f")

  # Check 1: no `**bold**` inside labels (use <b>...</b> instead)
  if grep -qE '\[.*\*\*[^*]+\*\*' "$f"; then
    echo "ERROR [$NAME]: '**bold**' inside node label — replace with <b>...</b>"
    ERRORS=$((ERRORS+1))
  fi

  # Check 2: no literal \n inside labels (use <br/>)
  if grep -qE '\[[^]]*\\n' "$f"; then
    echo "ERROR [$NAME]: literal '\\n' in node — replace with <br/>"
    ERRORS=$((ERRORS+1))
  fi

  # Check 3: no flowchart LR (must be TB)
  if grep -qE '^flowchart\s+LR\b|^graph\s+LR\b' "$f"; then
    echo "ERROR [$NAME]: 'flowchart LR' — must be 'flowchart TB' for portrait"
    ERRORS=$((ERRORS+1))
  fi

  # Check 4: no gantt / timeline / journey (don't print well portrait)
  if grep -qE '^gantt\b|^timeline\b|^journey\b' "$f"; then
    echo "ERROR [$NAME]: gantt/timeline/journey — use flowchart TB with sequential nodes instead"
    ERRORS=$((ERRORS+1))
  fi

  # Check 4b: no quadrantChart / sankey / mindmap / xychart (poor renderer support — many viewers
  # show the source as raw code instead of rendering). Production failure 2026-04-27.
  if grep -qE '^quadrantChart\b|^quadrant-chart\b|^sankey\b|^mindmap\b|^xychart-beta\b' "$f"; then
    echo "ERROR [$NAME]: quadrantChart/sankey/mindmap/xychart — many markdown renderers do not support these blocks. Use a 2x2 markdown table for quadrants, or flowchart TB with subgraph-per-quadrant. See mermaid-validation.md rule #7."
    ERRORS=$((ERRORS+1))
  fi

  # Check 5: long lines in nodes (>55 chars between square brackets — likely wraps badly)
  if grep -qE '\[[^]]{55,}\]' "$f"; then
    echo "WARN  [$NAME]: node label > 55 chars — split with <br/>"
    ERRORS=$((ERRORS+1))
  fi

  # Check 6: empty subgraph (subgraph X[ ... ] with no node lines before next subgraph or end)
  if awk '
    /^[[:space:]]*subgraph/ { name=$0; lines=0; next }
    /^[[:space:]]*end[[:space:]]*$/ { if (lines==0) { print "EMPTY: " name; bad=1 } name=""; lines=0; next }
    name && /^[[:space:]]*[A-Za-z0-9_].*[[:space:]]*$/ { lines++ }
    END { exit (bad ? 1 : 0) }
  ' "$f"; then :; else
    echo "ERROR [$NAME]: empty subgraph — add ≥1 node or remove the subgraph"
    ERRORS=$((ERRORS+1))
  fi

  # Check 7: unbalanced subgraph/end count
  SG=$(grep -cE '^[[:space:]]*subgraph' "$f")
  END=$(grep -cE '^[[:space:]]*end[[:space:]]*$' "$f")
  if [ "$SG" != "$END" ]; then
    echo "ERROR [$NAME]: $SG 'subgraph' but $END 'end' — unbalanced"
    ERRORS=$((ERRORS+1))
  fi

  # Check 8: nested-subgraph depth (> 3 levels typically renders badly)
  DEPTH=$(awk '
    /^[[:space:]]*subgraph/ { d++; if (d>m) m=d }
    /^[[:space:]]*end[[:space:]]*$/ { d-- }
    END { print m }
  ' "$f")
  if [ "${DEPTH:-0}" -gt 3 ]; then
    echo "WARN  [$NAME]: subgraph nesting depth = $DEPTH — flatten to ≤3"
    ERRORS=$((ERRORS+1))
  fi

  # Check 9: special chars inside unquoted node text
  if grep -qE '\[[^"]*[(){}][^]]*\]' "$f"; then
    echo "WARN  [$NAME]: parens/brackets in unquoted node text — wrap label in quotes: A[\"text (foo)\"]"
    ERRORS=$((ERRORS+1))
  fi
done

echo "----"
if [ "$ERRORS" -eq 0 ]; then
  echo "✅ All $n mermaid diagrams pass static validation"
else
  echo "⚠️  $ERRORS issue(s) found across $n diagrams — fix before exporting"
  exit 1
fi
```

This finishes in <2 seconds and catches the most common rendering failures without requiring external tools.

## Dynamic validation (optional, requires `@mermaid-js/mermaid-cli`)

For higher confidence, also run the dynamic render check. This actually executes mermaid against each diagram and confirms it renders to SVG without errors:

```bash
# Pre-flight: install once if not present
if ! command -v mmdc >/dev/null 2>&1; then
  npm install -g @mermaid-js/mermaid-cli
fi

ERRORS=0
for f in "$TMP"/diagram-*.mmd; do
  [ -f "$f" ] || continue
  NAME=$(basename "$f" .mmd)
  OUT="$TMP/$NAME.svg"

  if mmdc -i "$f" -o "$OUT" --quiet 2>/tmp/mmdc-err; then
    SIZE=$(stat -f%z "$OUT" 2>/dev/null || stat -c%s "$OUT" 2>/dev/null)
    if [ "${SIZE:-0}" -lt 200 ]; then
      echo "WARN  [$NAME]: SVG output suspiciously small (${SIZE}B) — likely rendered empty"
      ERRORS=$((ERRORS+1))
    else
      echo "✅ [$NAME]: rendered ($SIZE bytes)"
    fi
  else
    ERR_MSG=$(cat /tmp/mmdc-err 2>/dev/null | head -3)
    echo "❌ [$NAME]: render failed — $ERR_MSG"
    ERRORS=$((ERRORS+1))
  fi
done

echo "----"
[ "$ERRORS" -eq 0 ] && echo "✅ All $n diagrams render via mmdc" || echo "⚠️  $ERRORS render failure(s)"
```

This takes ~1-2 seconds per diagram and confirms actual render success.

## Mermaid portrait-printable rules (canonical)

These are the rules the draft itself must follow:

1. **`flowchart TB` only.** No `LR`. No landscape variants.
2. **Vertical chains of subgraphs.** One subgraph per row, connected top-to-bottom. NO side-by-side subgraphs — they fail to print readably.
3. **Node labels ≤ 6 lines, ≤ 45 chars per line.** Use `<br/>` for line breaks; check each line's character count.
4. **Bold via `<b>...</b>`** (NOT `**...**`). Mermaid does not parse markdown inside node labels.
5. **Line breaks via `<br/>`** (NOT `\n`).
6. **Quote node text with special chars.** If the label contains `(`, `)`, `[`, `]`, `:`, `;`, `,`, wrap in double quotes:
   ```
   A["Vendor (founded 2020)"]   # correct
   A[Vendor (founded 2020)]     # breaks
   ```
7. **NEVER use `quadrantChart`, `sankey`, `mindmap`, or `xychart-beta`.** This is a hard ban — not a soft preference. Many markdown renderers (basic preview tools, GitHub-rendered MD, several IDE previewers, default browser print, pandoc-md-to-pdf) **do not support these block types and render them as raw code**. Even when they do render, label-overlap in dense quadrants makes the result unreadable. **Portrait alternatives** for the most common need (competitive positioning quadrant):
   - **Best (renders everywhere):** a 2×2 markdown table with axis labels in row-1 / col-1 headers and vendors listed inside cells.
   - **Acceptable visual:** `flowchart TB` with one subgraph per quadrant + vendors as separate nodes inside each subgraph + a TOP → MID → BOT vertical chain encoding the y-axis.
   - Always pair with a "How to read this" caption below explaining strategic implication.
8. **Avoid `gantt`, `timeline`, `journey`.** None print portrait well. Use `flowchart TB` with sequential nodes for timelines:
   ```mermaid
   flowchart TB
     T1[2020: Founded]
     T2[2022: Series A]
     T3[2024: GA launch]
     T1 --> T2 --> T3
   ```
9. **Subgraph nesting depth ≤ 3.** Flatten if deeper.
10. **At least 1 node per subgraph.** Empty subgraphs render badly or get dropped.
11. **Test mermaid renders** by counting node character widths; if any line in a node exceeds ~50 chars, split it.

## When to load this file

Load `mermaid-validation.md` when:
- About to enter Step 5 (URL validation) — run mermaid validation as part of pre-export checks
- Before any HTML or PDF export (`--export=html|pdf|both`)
- After post-draft edits that touched mermaid blocks
- When asked to "redo / refresh / fix" any diagram

## Convert-only mode integration

In convert-only mode (an existing MD is being re-rendered to HTML/PDF), still run the static check on the input MD. If it fails, **do NOT silently fix** the user's MD — report the failures separately and let the user decide whether to fix the source or proceed with broken diagrams.
