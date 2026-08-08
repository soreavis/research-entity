# Voice & Style Rules

Loaded by the `research-entity` skill during Step 4 (Draft) and any post-draft revision. These rules govern how the dossier reads — they are non-negotiable.

## Voice = single source of truth, declarative

The final document reads as authoritative reference. State verified facts as facts.

**Do NOT include editorial trail:**
- ❌ "Originally stated", "this was wrong", "Important correction:", "Key correction:", "NEW in this revision", "previously flagged as", "now reframes", "the dossier originally said".
- ❌ "We initially thought X but it turns out Y" — pick Y, state Y.
- ❌ "Updated 2026-04-27 from prior version" — version-control comments belong in git, not the dossier.

If a fact was wrong in an earlier draft, **fix the fact and move on.** Don't narrate the correction in the published document.

**Do use:**
- ✅ Plain declarative sentences with sources cited
- ✅ Conditional language for unresolved conflicts ("Per official sources, founded in 2011; the LinkedIn entry shows 2007 — the earlier date may reflect informal predecessor activity")
- ✅ Confidence labels (`single-source`, `vendor-claimed`, `founder self-claim`, `aggregator-derived`) inline
- ✅ Analyst-opinion disclaimer at top of §0 for SWOT/Heat-Map/Playbook content

## Precision discipline (8 numeric / temporal / causal anti-hallucination rules)

These rules catch the most common LLM hallucination modes that source-citation alone doesn't catch. Apply during Step 4 (Draft) and re-check in Step 5 (Validate).

### Rule P1 — Numeric range vs point-estimate

When source-uncertainty is high (`single-source` / `aggregator-derived` / `vendor-claimed` / `founder-self-claim`), prefer ranges over false-precision points:

| ❌ False precision | ✅ Range with uncertainty |
|---|---|
| "$23.4M ARR" (single-source Latka) | "~$15-25M ARR (`single-source / founder-self-reported`)" |
| "287 employees" (aggregator-derived) | "85-500 employee range across aggregators; LinkedIn band 51-200 most defensible" |
| "1,247 customers" (vendor-claimed) | "vendor reports 'over 1,000 customers' (`vendor-claimed`); not independently verified" |

LLMs systematically fabricate decimal precision (`$23.4M`) to sound authoritative; ranges expose the underlying uncertainty.

### Rule P2 — "As of date" annotations on time-sensitive data

Every claim about funding / pricing / certifications / employee counts / customer logos / public reviews carries an "as of <date>" annotation:

```markdown
- **Pricing**: €50/seat/month Starter (as of 2026-04-27)
- **ISO 27001:2022 certificate**: valid (as of 2026-04-27 trust page; certificate expiration not publicly disclosed)
- **Capterra reviews**: 216 at 4.6/5 (as of 2026-04-27 — Capterra review counts grow ~10/quarter for active vendors)
```

Catches LLM tendency to mix data from different time periods (e.g., Q1 2024 employee count + Q4 2025 pricing presented as one snapshot).

### Rule P3 — Negation-evidence (absence of evidence ≠ evidence of absence)

When a search returns no findings, label it as such — do NOT claim the underlying fact doesn't exist:

| ❌ Wrong inference | ✅ Correct labeling |
|---|---|
| "<entity> has not been sued" | "No public lawsuits found in CourtListener federal records (state-court records not exhaustively searched)" |
| "<entity> has had no breaches" | "No breach disclosures found in haveibeenpwned, databreaches.net, or state AG breach-notification archives (does not preclude undisclosed incidents)" |
| "No layoffs" | "No layoff events found on layoffs.fyi or thelayoff.com search (mid-market private vendors are sometimes not listed)" |
| "The company is profitable" | "Founder claims profitability; no audited income statement available to verify" |

This is the most subtle hallucination class because the surface form looks like a fact when it's actually an absence-of-evidence claim.

### Rule P4 — Quotation chain-of-custody

Every verbatim quote MUST include 4 elements: speaker name + role + date + source URL. Quotes missing any element are dropped (LLMs hallucinate quotes more than other content):

```markdown
✅ Good:
> "<entity-product> is the main worktool used by our sales team today."
> — Wilhelm Liljencrantz, Sales & Business Manager, Rentals United, [FeaturedCustomers testimonial](https://www.featuredcustomers.com/...) (date: 2024-03)

❌ Bad (missing date + source):
> "It's the best CRM we've ever used."
> — A satisfied customer
```

### Rule P5 — Recency check on "current" / "recent" / "<this year>" claims

Any claim using time-words must be paired with a source date. If source is >12 months old, flag the recency claim:

| ❌ Stale claim presented as current | ✅ Source-dated claim |
|---|---|
| "<entity> currently has X,XXX customers" | "Per Latka (June 2024 — 22 months old), founder reports X,XXX customers" |
| "Recent layoffs at the company" | "Per layoffs.fyi search (2026-04-27), no entries (does not preclude pre-2024 events)" |

### Rule P6 — Self-consistency cross-section check

Same fact must match across all dossier sections (e.g., employee count in §3 must match §16 must match §0 Scorecard). Run a pre-ship grep for numeric discrepancies:

```bash
# Example: check employee count consistency
grep -inE "[0-9]+ employees|employee count|headcount" "$DOSSIER" | sort -u
# If multiple distinct numbers appear, reconcile or flag explicitly.

# Example: check funding total consistency
grep -oE "\\\$[0-9.]+M" "$DOSSIER" | sort | uniq -c | sort -rn
# Same dollar amount should appear consistently; divergent appearances = inconsistency to fix.
```

(Per `lessons.md` #20 — real production case where same cumulative funding number appeared as 4 different values.)

### Rule P7 — Specific-number-no-source HALT

Any specific number ($X.X million / X.X% / X people / X integrations) without an inline citation HALTS the draft — do NOT paraphrase the precision away. The model must either:
- Provide a citation, OR
- Drop the specific number, OR
- Replace with a sourced range

Forbidden forms:
- "approximately 200 customers" (without source) → forbidden, halt
- "around 50% market share" (without source) → forbidden, halt
- "roughly $30M raised" (without source) → forbidden, halt

The "approximately" / "around" / "roughly" qualifier does NOT excuse missing source.

### Rule P8 — Causal-claim-needs-explicit-causation-source

"X caused Y" requires a source that explicitly states the causation, not just temporal correlation. LLMs systematically fabricate causation from correlation:

| ❌ Causation hallucinated from correlation | ✅ Causation labeled correctly |
|---|---|
| "The 2024 pricing freeze drove customer growth" | "<entity> froze pricing in 2024; customer-count claim grew during 2024 ([Latka Jun 2024](url)). The two are temporally correlated; no source attributes one to the other." |
| "<entity-AI-product> launch caused the rebrand" | "<entity-AI-product> launched MMM-YYYY; rebrand to <new-name> MMM-YYYY — these are sequential events; no causal source identified." |

Causal claims without explicit-causation source must be reframed as correlations or sequential-events.

## Citation discipline

**Source-backing is non-negotiable.** Every claim that can be backed by a public source MUST have a citation. If you can't find a source, **drop the claim** — don't publish unsourced.

What needs a citation:
- ✅ Every numeric fact (dates, dollar amounts, counts, percentages)
- ✅ Every proper noun used as a fact (company, person, product names)
- ✅ Every quoted statement (with attribution)
- ✅ Every claim about another company (competitor funding, product launches, customer logos)
- ✅ Every certification / compliance / regulatory claim
- ✅ Every recent press / wire / analyst reference

What does NOT need a citation:
- ❌ Analyst opinion (SWOT/Heat-Map/Playbook) — bucketed under §0 framework disclaimer
- ❌ Synthesis labeled as inference ("Reading these together suggests...")
- ❌ Generic statements without specific facts ("CRMs typically integrate with email")

**Citation format depends on `--citations=<style>`** (load `citations.md` for full rules):
- `inline` (default): `[Source Name](url)` — appears immediately after the claim. Best for digital reading.
- `footnotes`: `[^tag]` reference, definition at document bottom. Best for source-heavy `--depth=deep` dossiers; deduplicates the same URL referenced N times.
- `endnotes`: §19-only references. Academic style.

**Confidence labels (apply regardless of citation style):**
- Vendor-claimed metrics (productivity, contact-DB sizes, podcast rank) → labeled `vendor-claimed` inline
- Founder self-claims (career revenue, growth rates, exit values) → labeled `founder self-claim` inline
- Single-source aggregator data → labeled `single-source` or `aggregator-derived` inline
- Analyst judgments (SWOT/Heat-Map/Playbook) → bucketed under §0 disclaimer (don't repeat the label per row)

## No promotional language in analytical voice

- ❌ "revolutionary", "best-in-class", "industry-leading", "unprecedented", "game-changing", "next-generation"
- ❌ "first mainstream X" / "only company doing Y" / "the future of Z" without market-wide verification
- ❌ "multi-billion-dollar IPO" / "skyrocketing growth" / hyperbole

If the entity uses promotional language, **quote it with attribution** rather than adopting it: `the company describes itself as "industry-leading" (vendor-claimed)`.

C-level readers discount promotional language immediately. Stay analytical.

## Signal-label discipline (Scorecard and every other status column)

**A signal cell is never a bare colour.** Every cell in a Signal / Status / Verdict column MUST be written as `<dot> <Label>` — a colour dot followed by a one-or-two-word verdict.

| ❌ Bare dot — forbidden | ✅ Dot + label — required |
|---|---|
| `🟢` | `🟢 Strong` |
| `🟡` | `🟡 Unverified` |
| `🔴` | `🔴 Absent` |
| `⚪` | `⚪ N/A` |

### Why this is a hard rule

A bare dot forces the reader back into the Assessment cell to work out what the colour means, which defeats the purpose of a scan-first summary table. It also hides analytical laziness: three amber dots in a row look considered, whereas `🟡 Small`, `🟡 Unverified`, `🟡 Watch` immediately expose that they are three *different* kinds of amber. The label is where the judgement actually lives — the colour is only its severity.

The label must also survive being read **alone**. A reader skimming only the Signal column should come away with a coherent one-word-per-row summary of the entity.

### The four states

| Dot | Meaning | Use when |
|---|---|---|
| 🟢 | Confirmed strength | Verified against a primary source and favourable |
| 🟡 | Qualified / caution | True but partial, unverified, small, dated, or single-source |
| 🔴 | Weakness or contradiction | Absent, contradicted by a primary source, or materially adverse |
| ⚪ | No signal available | Genuinely not applicable or not measurable — **never force a dimension into green/amber/red to avoid using this** |

### Label vocabulary bank

Pick the label that describes *this dimension*, not a generic grade. Extend freely; these are starting points.

- **🟢** Strong · Established · Verified · Real · Clean · Focused · Distinctive · Proven · Current · Compliant · Transparent · Independent · Corroborated
- **🟡** Small · Watch · Unverified · Partial · Thin · Emerging · Dated · Single-source · Mixed · Early · Vendor-claimed · Inconclusive
- **🔴** Absent · Contradicted · Unproven · Opaque · Stale · None · Disputed · Undisclosed · Blocked · Drifting
- **⚪** N/A · Not applicable · Not disclosed · Unmeasurable

### Rules

1. **Never a bare dot.** Every signal cell is dot + label.
2. **1–2 words, ≤ 14 characters.** Longer belongs in the Assessment cell.
3. **Dimension-specific.** The label answers "what should I conclude about *this row*," not "is this good or bad."
4. **Consistent with the Assessment cell.** A `🟢 Strong` next to a hedged assessment is a defect — reconcile one or the other.
5. **Vary the vocabulary.** If the same label repeats more than ~3× in a 15-row Scorecard, the labels are not doing analytical work. Re-read each row and differentiate.
6. **⚪ is a legitimate answer.** Reaching for it honestly beats manufacturing a colour.
7. **Applies to every status column in the dossier** — §0 Scorecard, Heat Map, §16 Red-Flag Scan severity, negative-space scan, benchmark comparisons, freshness decay. One convention throughout.
8. **Never let the label overstate the evidence.** If a fact is `vendor-claimed`, the signal cannot be `🟢 Verified`; `🟡 Vendor-claimed` is the honest cell.

### Worked example

```markdown
| # | Dimension | Assessment | Signal | Source |
|---|---|---|---|---|
| 1 | **Corporate substance** | Registered entity, <jurisdiction>, active filings | 🟢 Established | [Register](url) |
| 2 | **Team scale** | 2–10 employees; no public job postings | 🟡 Small | [LinkedIn](url) |
| 3 | **Verified funding** | No filing on record; only capital is a competition prize | 🔴 Undisclosed | [Filing search](url) |
| 4 | **Analyst coverage** | Category defined this year; no vendor inclusion claimed | ⚪ N/A | §15.2 |
```

Read the Signal column alone: *Established · Small · Undisclosed · N/A*. That is a usable summary. `🟢 · 🟡 · 🔴 · ⚪` is not.

### Pre-ship scan (run in Step 5)

```bash
F="$1"   # path to dossier .md
# Extract every table cell containing a status dot and assert a label follows it.
BARE=$(grep -nE '\|[[:space:]]*(🟢|🟡|🔴|⚪)[[:space:]]*\|' "$F")
if [ -n "$BARE" ]; then
  echo "❌ bare signal dots with no label:"; echo "$BARE" | head -20
else
  echo "✓ all signal cells carry a label"
fi
# Repetition check — a label used >3× in one table is under-differentiated
grep -oE '(🟢|🟡|🔴|⚪) [A-Z][A-Za-z/-]+' "$F" | sort | uniq -c | sort -rn | awk '$1>3 {print "⚠️  over-used label:", $0}'
```

## Mermaid portrait-printable rules

All mermaid diagrams MUST follow these rules. The skill will run static + dynamic validation (see `mermaid-validation.md`) and fail the export if any diagram violates these.

1. **`flowchart TB` only.** No `LR`. No landscape variants.
2. **Vertical chains of subgraphs.** One subgraph per row, connected top-to-bottom. NO side-by-side subgraphs — they fail to print readably.
3. **Node labels ≤ 6 lines, ≤ 45 chars per line.** Use `<br/>` for line breaks.
4. **Bold via `<b>...</b>`** (NOT `**...**`). Mermaid does not parse markdown inside node labels.
5. **Line breaks via `<br/>`** (NOT `\n`).
6. **Quote node text with special chars.** If the label contains `(`, `)`, `[`, `]`, `:`, `;`, `,`, wrap in double quotes: `A["Vendor (founded 2020)"]`.
7. **Avoid `gantt`, `timeline`, `journey`.** Use `flowchart TB` with sequential nodes for timelines.
8. **Subgraph nesting depth ≤ 3.** Flatten if deeper.
9. **At least 1 node per subgraph.** Empty subgraphs render badly or get dropped.
10. **No reserved keywords as unquoted node IDs.** `end`, `subgraph`, `direction` must be quoted if used.

## Comment / inline-note discipline

- Don't add `<!-- comments -->` in the rendered MD; they become invisible in HTML but visible in PDF / printed output.
- Don't leave `TODO:` / `FIXME:` markers — fix or remove.
- Don't include `(see line X)` cross-references — they break when MD is reformatted.

## Naming conventions

- Use the entity's official trade name in the body, even if its legal name differs (e.g., the trade name `<Brand>` rather than the full legal-and-doing-business-as chain `<Parent Corp.> dba <Brand> dba <Legacy Brand>`). Mention the legal name once in §2 Company Fundamentals.
- For people: full name on first mention, last name only thereafter.
- For investors / VCs: full firm name on first mention, abbreviated thereafter (e.g., "Sequoia Capital" → "Sequoia").
- For products: capitalize as the company does; don't pluralize unless the product page does.

## Date formatting

- Use ISO format `YYYY-MM-DD` for absolute dates in tables and citations.
- Use prose dates ("April 9, 2026") in the BLUF and prose paragraphs.
- Always convert relative dates ("last month", "Thursday") to absolute dates when capturing user-provided info.

## Source / link formatting

- Inline link: `[Anchor text](url)` — never bare URLs in the body
- Source-list entries: `- [Title](url)` — categorized in §19
- Citations after a fact: e.g., `founded 2011 ([Entity About](https://www.example.com/about/))`

## Glossary discipline (§22)

The §22 Glossary is **not optional cosmetic content** — it is the reader's onramp. Every acronym or jargon term used in the body must have a glossary entry. The skill must scan for gaps before ship.

### What must be in the glossary

- Every all-caps acronym used in the body (CRM, GDPR, HIPAA, SOC 2, ISO 27001, etc.)
- Every jargon term that a non-domain reader would Google (BLUF, SWOT, ICP, GTM, agentic, etc.)
- Every entity-specific product / module name (entity-specific product names — replace per dossier)
- Every register-specific identifier (FN for Austria, HRB for Germany, ICO for Slovakia, KvK for Netherlands, etc.) — these are jurisdictional codes a reader from a different country won't recognize
- Every funding-round designation (Seed, Series A, Series B, Series C — bundled into one entry is fine)
- Every dossier-framework component (Scorecard, Heat Map, Watchlist, Playbook)
- Every compliance / standards body (FedRAMP, PCI DSS, OWASP, BCDR, RBAC, BYOK)

### Glossary-completeness scan (REQUIRED in Step 5)

Run this scan after Draft (Step 4) and before Export (Step 7). It identifies acronyms used in the body that don't have a glossary entry:

```bash
OUTPUT="$1"   # path to dossier .md

# Extract every all-caps acronym (2+ chars) used in the body, count occurrences
BODY_ACRONYMS=$(grep -oE '\b[A-Z][A-Z0-9/&]{1,}\b' "$OUTPUT" | sort | uniq -c | sort -rn | awk '$1 >= 2 {print $2}')

# Extract every term defined in §22 Glossary
GLOSSARY_TERMS=$(awk '/^## 22\. Glossary/,/^---$/' "$OUTPUT" | grep -oE '\| \*\*[^*]+\*\*' | sed 's/| \*\*//; s/\*\*//')

# Find acronyms used 2+ times that are NOT defined
echo "$BODY_ACRONYMS" | while read -r term; do
  [ -z "$term" ] && continue
  if ! echo "$GLOSSARY_TERMS" | grep -qF "$term"; then
    USED=$(grep -cE "\b$term\b" "$OUTPUT")
    echo "⚠️  $term: used $USED× in body, missing from glossary"
  fi
done

# Also check specific jargon-style terms (case-sensitive)
for term in "BLUF" "Heat Map" "Scorecard" "Watchlist" "agentic" "Series A" "Series B" "Seed" "MCP Server"; do
  if grep -qE "\b$term\b" "$OUTPUT" 2>/dev/null; then
    if ! echo "$GLOSSARY_TERMS" | grep -qF "$term"; then
      echo "⚠️  '$term' used in body but missing from glossary"
    fi
  fi
done

# Entity-specific product names — populate this list per dossier
# (replace with the actual entity's product/module names before running)
for term in "<Product1>" "<Product2>" "<Module>"; do
  if grep -qF "$term" "$OUTPUT"; then
    if ! awk '/^## 22\. Glossary/,/^---$/' "$OUTPUT" | grep -qF "$term"; then
      echo "⚠️  Entity-specific '$term' used but missing from glossary"
    fi
  fi
done
```

### Glossary writing rules

- **Alphabetize** entries (A → Z, ignoring articles)
- **One row per term** in a 2-column markdown table: `| **Term** | Definition |`
- **First-line definition** — what the acronym stands for or the literal definition
- **Second-line context** — when relevant for this dossier (e.g., "the entity does NOT support BYOK" / "FedRAMP is a US government certification" / "the entity's AI engine uses 'advanced OpenAI models'")
- **Cross-reference** related glossary terms in-line with `→ See ENTRY`
- **No verbose definitions** — keep each entry to 1-3 sentences
- **Never include a term in the glossary that doesn't appear in the body** (avoid clutter)

### Anti-patterns

- ❌ Skipping the glossary-completeness scan — readers WILL hit a term they don't know
- ❌ Glossary with <20 entries on a `--depth=deep` dossier — likely missing acronyms
- ❌ Defining terms that don't appear in the body — clutter
- ❌ Using country-specific business-register codes (FN, HRB, ICO, KvK, CVR, etc.) without defining them — readers from other countries can't Google these efficiently
- ❌ Including the Glossary as the LAST item in §22 with no §23 confidence appendix — Glossary should not be the closing impression

## Decision-tree scoring template (for §17 Strategic Analysis)

When the dossier includes a decision-tree mermaid in §17 Strategic Analysis (the typical "should you evaluate?" flow), pair it with a **scoring framework** beneath the diagram. The framework makes the tree's outcomes interpretable rather than purely qualitative.

The scoring framework includes 4 tables:

1. **Decision criteria (gates)** — for each branch question, what it asks, why it matters, pass threshold
2. **Outcome scoring (5 dimensions, 100 points)** — name the 5 dimensions weighted to 100 (typical: pricing fit / product fit / AI-integration fit / compliance fit / brand fit, with weights varying per audience)
3. **Outcome bands** — each leaf node mapped to a fit-score range (e.g., 80–95 strong fit / 55–75 standard fit / 40–60 conditional / 25–45 mismatch) with confidence color and recommendation per band
4. **How to apply** — step-by-step process for the reader to walk the tree, score the 5 dimensions on their specific case, multiply by weight, sum, and compare to bands. Also: the disclaimer that the fit-score is **directional, not predictive** — actual procurement outcomes depend on factors outside any framework (existing-vendor sunk cost, internal champion strength, RFP timing).

This pattern was added after a real production run found the unannotated decision tree was insufficient — readers wanted concrete metrics to back the qualitative "Strong fit" / "Mismatch" labels.

## Competitive / Due-Diligence dossier voice (additional rules)

When `--type=competitive` or `--type=due-diligence`, additional voice rules apply on top of the base voice rules above:

### Use neutral verdict labels, NOT lens-qualified labels

The fact that the dossier was written from an external-evaluator perspective is implicit in the `--type` flag — it should NOT be repeatedly stated in section headers / verdicts / observations. Stylistic tells reveal authorial provenance.

| ❌ Avoid | ✅ Use |
|---|---|
| "Outsider verdict:" | "Verdict:" |
| "Outsider observation:" | "Observation:" |
| "Outsider conclusion:" | "Conclusion:" |
| "Outsider questions to ask in diligence:" | "Questions to ask in diligence:" |
| "Outsider-evaluator interpretation:" | "Interpretation:" |
| "(Outsider Reverse-Engineered)" | "(Reverse-Engineered from Public Signals)" |
| "(Outsider Deep-Dive)" | "(Deep-Dive)" |
| "(Outsider Sample-Inferred)" | "(Sample-Inferred from Public Logo Wall)" |
| "what the outsider sees" | "what an external evaluator sees" / "what is publicly observable" |
| "outsider cannot verify" | "cannot be verified externally" |
| "for an outsider this means" | "for an external evaluator this means" |

A truly external dossier doesn't need to label itself "outsider" — it just IS one. The repeated label suggests a contrasting "insider" view exists, which leaks dossier provenance.

### No lens comparisons

Do NOT reference what a hypothetical alternative-lens version of the same dossier would score. Do NOT include language like:
- ❌ "Where the prior `--type=research` revision scored 86/100..."
- ❌ "an insider self-portrait would achieve (~86/100)"
- ❌ "the 10-point delta is the outsider verification gap"
- ❌ "Insider lens of the same dossier scored 86/100"
- ❌ "verification gap" as a comparative term
- ❌ "(move to insider lens)" as an option to raise confidence

These reveal the dossier has a comparison reference frame, which only makes sense if the author has access to the alternative perspective. A pure external dossier wouldn't know.

### No skill / tool / slash-command self-references in dossier text

The dossier should not reference the skill, command names, or harness tooling that produced it:
- ❌ "The skill that produced this dossier explicitly audits for hallucinated claims"
- ❌ "/schedule cron=... /research-entity ..."
- ❌ "would benefit from `/schedule` cron"
- ❌ "load `audits.md` audit"
- ❌ "per `risk-scan.md`" — internal segment-file references must NOT appear in the published dossier
- ❌ Any reference to `--type=`, `--depth=`, `--audit=`, etc. in body text
- ❌ Any reference to `--no-revalidate`, convert-only mode, or wizard

For refresh cadence, use tool-agnostic language ("recommended cadence: quarterly review") rather than scheduling-tool syntax. For internal section references that come from segment files, paraphrase the source instead of citing the segment-file name.

### No editorial trail (extra-strict for competitive)

The base voice rules already prohibit editorial trail. For competitive dossiers, this is extra-strict because editorial-trail markers reveal multi-revision history:
- ❌ "added to first-mentions in this revision"
- ❌ "in this revision"
- ❌ "previously labeled"
- ❌ "in the prior version"
- ❌ "we revised this to..."

If the dossier went through revisions, that history belongs in git, not in the dossier. State the current fact as if it had always been the fact.

## Anti-leak / depersonalization scan (REQUIRED in Step 5 for `--type=competitive|due-diligence`)

A competitive / due-diligence dossier must read as a third-party external evaluation with **no traceable provenance to its author**. Run this scan before ship; fail any dossier that hits.

### 12 leak categories

```bash
F="$1"   # path to dossier .md

check() {
  local label="$1" pat="$2"
  if grep -iE "$pat" "$F" >/dev/null 2>&1; then
    echo "❌ $label: HIT"
    grep -inE "$pat" "$F" | head -3
    return 1
  else
    echo "✓ $label: clean"
    return 0
  fi
}

ALL=0

# 1. Personal names — replace with the author's first name + last name
check "Personal names" "<firstname>|<lastname>|<userhandle>" || ALL=1

# 2. Personal email — replace with the author's email handle / domain
check "Personal email domains" "@<entity-domain>\.com|@<author-domain>\.com" || ALL=1

# 3. Lens-qualified labels (outsider / insider / self-portrait)
check "Outsider/insider/self-portrait terms" "outsider|insider|self-portrait" || ALL=1

# 4. Skill / slash-command references
check "Skill/slash-command refs" "the skill|/research-entity|/schedule|--type=research|--no-revalidate|load \`[a-z-]+\.md\`" || ALL=1

# 5. Claude artifacts (memory / project paths / settings)
check "Claude artifacts" "claude\.md|MEMORY\.md|user_employer|originSession|PROMPTS\.md|\.claude/" || ALL=1

# 6. Conversation / meta references
check "Conversation refs" "you (mentioned|asked|provided|said|noted)|as (we|you) discussed|per your|on user request|per the user" || ALL=1

# 7. Insider author voice (we / our / us as the entity-author, NOT in attributed quotes)
# Note: lines starting with > or | are quotes/tables — exclude them
INSIDER_HITS=$(grep -nE "^[^>|].*\b(we (own|run|operate|sell|build|ship|are|will)|our (company|product|customers|team|revenue|brand))\b" "$F" | grep -viE "^[0-9]+:>|^[0-9]+:\|" || true)
if [ -n "$INSIDER_HITS" ]; then
  echo "❌ Insider author voice: HIT"
  echo "$INSIDER_HITS" | head -3
  ALL=1
else
  echo "✓ Insider author voice: clean"
fi

# 8. Personal location ties
check "Personal location" "I (live|work|am based) in|currently based|my home|my office" || ALL=1

# 9. Editorial trail markers
check "Editorial trail" "this session|prior iteration|in this revision|we (revised|updated|added|fixed) (this|that|the)" || ALL=1

# 10. Authorial self-reference
check "Authorial self-ref" "as someone who|speaking as|from where I sit|in my experience at|having worked at" || ALL=1

# 11. Meta production references
check "Meta production" "this dossier was (created|generated|produced)|this analysis was prepared|this report was commissioned" || ALL=1

# 12. Lens comparisons (insider vs outsider scoring)
check "Lens comparisons" "verification gap|insider lens|outsider lens|insider score|outsider score" || ALL=1

if [ "$ALL" = "0" ]; then
  echo "✅ ALL 12 CATEGORIES CLEAN — DOSSIER IS DEPERSONALIZED"
else
  echo "⚠️ DEPERSONALIZATION FAILED — fix leaks before ship"
fi
```

### What to substitute (per-dossier setup)

Before running the scan, replace the placeholders in patterns 1-2 with the actual author identifiers:
- `<firstname>` / `<lastname>` — author's first/last name
- `<userhandle>` — any other handle, username, or LinkedIn ID
- `<entity-domain>` — entity's email domain (if researching the author's own employer)
- `<author-domain>` — author's email domain (if known)

If running the skill on the author's own employer (`--type=research`), the author identifiers must be loaded from a memory file or supplied at runtime; never bake author identity into the skill.

### What to do when a leak is found

1. **Identify the source.** Is it (a) authorial-voice slip, (b) tool reference, (c) editorial-trail marker, (d) lens comparison?
2. **Rewrite, don't comment out.** The scan is a hard gate; do not add `<!-- -->` to hide leaks. Rewrite to be tool-agnostic, lens-agnostic, name-agnostic.
3. **Re-run the scan** after each fix. Most fixes uncover at least one more downstream reference.
4. **Validate quotes are preserved.** Lines starting with `>` (blockquote) or `|` (table-cell) often contain attributed verbatim quotes from external speakers — those "we" / "our" / "I'm" mentions are documented evidence and must be preserved with attribution.

### Distinguishing leaks from legitimate content

| Pattern | Leak | NOT a leak |
|---|---|---|
| "we operate the platform" | If author voice | If inside a <founder-name>/exec quote with attribution |
| "outsider verdict" | Always — stylistic provenance tell | — |
| "in this revision" | Always — editorial trail | — |
| "our customers" | If author voice | If inside a customer-quote with attribution |
| `/schedule` or `/research-entity` | Always — tool reference | — |
| "internal R&D phase" | NOT a leak — factual | If describing the entity's history |
| "internal champion" | NOT a leak — procurement vocabulary | — |
| "Internal" as SWOT column label | NOT a leak — analytical framework | — |

The simplest test: would this exact phrase plausibly appear in a dossier written by a competitor's intelligence analyst with no insider access? If no, it's a leak.

## When to load this file

Load `voice-and-style.md` when:
- About to enter Step 4 (Draft)
- About to revise any prior draft
- About to write any §0 framework content
- About to add a mermaid diagram
- About to write any verdict / observation / conclusion section in a `--type=competitive|due-diligence` dossier (apply the lens-neutral label rule)
- Step 5 (Validate) — to run the depersonalization scan
- Reviewing the final draft for tone / voice consistency
