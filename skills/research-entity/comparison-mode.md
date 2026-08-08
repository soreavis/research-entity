# Comparison / Diff Mode — `--compare=A.md,B.md[,C.md]`

Loaded by the `research-entity` skill when `--compare=` is set OR `--year-over-year` is requested. Produces a side-by-side comparison dossier rather than a single-entity dossier.

Two distinct modes:

1. **Side-by-side comparison** — `--compare=A.md,B.md` produces a comparison of Entity A vs. Entity B (typically a vendor evaluation: "Entity-A vs. Entity-B"). Pulls existing dossiers from disk; does not re-research.
2. **Year-over-year diff** — `--compare=current.md,previous.md` (or `--year-over-year` with the dossier's prior version) produces a "what changed since last review" delta report.

## Mode 1: Side-by-side comparison

### Output structure (15 sections — different from single-entity 23-section template)

**§0 Executive Comparison** — BLUF + Comparative Scorecard (15 rows × N columns) + Verdict matrix (per-stakeholder recommendation: investor / buyer / operator / etc.)

**§1 Side-by-side Scorecard** — every Scorecard row from the input dossiers normalized into one table. Each entity's cell carries a labelled signal (`🟢 Strong` / `🟡 Small` / `🔴 Absent` / `⚪ N/A`) — never a bare dot, per the signal-label discipline in `voice-and-style.md`. Labels must be comparable across entities on the same row: if entity A is `🟢 Established` and entity B is `🟡 Early`, the two words should sit on the same conceptual axis.

**§2 Funding & Investor Comparison** — total raised, latest round, investor names, valuation if disclosed

**§3 Product Comparison** — feature parity table; what each does that the other doesn't

**§4 Pricing Comparison** — entry tier, mid tier, enterprise; published vs. quote-only

**§5 Customer Base Comparison** — logo overlap, segment focus, geographic split

**§6 Tech Architecture Comparison** — model used, multi-tenant vs. single-tenant, MCP/agent support, integration count

**§7 Security & Compliance Comparison** — SOC 2, ISO 27001, GDPR, HIPAA, FedRAMP, PCI-DSS, SOC 2 Type I vs. Type II

**§8 Community & Reception Comparison** — G2 rating + count, Capterra rating + count, Glassdoor, Reddit / HN presence

**§9 Risk Profile Comparison** — Heat Map deltas; lawsuits, breaches, layoffs

**§10 Strategic Position** — quadrant overlay (where each sits on price-vs-completeness)

**§11 Growth Velocity** — funding rounds, employee count over time, product release cadence

**§12 Decision Framework** — when to choose A vs. B (per-stakeholder bullets)

**§13 Verdict** — short narrative recommendation per stakeholder type

**§14 Sources** — combined source list across both inputs

**§15 Methodology** — input dossier dates, comparison rules, residual gaps

### Workflow

```
/research-entity --compare=./<entity-A>-research.md,./<entity-B>-research.md --output=./<entity-A>-vs-<entity-B>.md
```

1. Load each input dossier; parse §0 Scorecard, §2 Company Fundamentals, §4 Funding, §8 Pricing, §11 Community
2. Build Comparative Scorecard: union of rows from each dossier; flag rows missing from one
3. Detect divergence: highlight cells where the values differ by >1 order of magnitude (likely an error in one input)
4. Generate per-stakeholder Verdict matrix (investor / buyer / operator / engineer / legal / press)
5. Output to `--output` path
6. Convert URLs to clickable; preserve original citation labels (so reader knows which dossier each fact came from)

### Verdict matrix template

| Stakeholder | Choose A if... | Choose B if... | Choose neither if... |
|---|---|---|---|
| **Investor** | A's funding stage + market timing + team are stronger | B's traction is more proven | Both lack PMF signal |
| **Enterprise buyer** | A's compliance posture + integrations match your stack | B's pricing fit + customer references match yours | Neither has SOC 2 |
| **Operator** | A's pricing + tool consolidation math saves more | B's onboarding + support is rated higher | Both require dedicated headcount |
| **Channel partner** | A's margin + co-sell motion is better | B's channel program is more mature | Neither has named partner manager |
| **Engineer** | A's API + SDK + docs are more capable | B's community / ecosystem is larger | Neither has open source |

## Mode 2: Year-over-year diff

### When to use

- Quarterly portfolio review: re-run /research-entity on a watchlist company; compare to prior version
- Annual partnership review: confirm partner is still healthy
- Pre-renewal sanity check: did the vendor regress on any metric?

### Workflow

```
/research-entity --compare=./acme-2026-04-research.md,./acme-2025-04-research.md --year-over-year --output=./acme-yoy-2025-2026.md
```

OR (auto-detect prior dossier):

```
/research-entity "Acme Corp" --year-over-year   # finds latest acme-research.md, runs full research, then diffs
```

### Output structure (10 sections)

**§0 Executive Summary** — BLUF + Top 5 changes (3 sentences each) + Confidence delta

**§1 Scorecard Deltas** — every Scorecard row with ↑ / ↓ / → arrow, magnitude, source

**§2 Funding Deltas** — new rounds, valuation step-ups, investor changes

**§3 Team Deltas** — exec hires/departures (especially CXO turnover); employee count delta

**§4 Product Deltas** — new features shipped, deprecated features, roadmap signals

**§5 Customer Deltas** — new logos, lost logos (case-study removals), case-study refresh patterns

**§6 Pricing Deltas** — tier changes, packaging changes, removal of free tier

**§7 Risk Deltas** — new lawsuits / breaches / layoffs / regulatory actions; cleared old risks

**§8 Sentiment Deltas** — G2/Capterra/Glassdoor rating change, review-count growth

**§9 Verdict** — narrative summary; "should you change your evaluation?"

### Delta detection rules

- Numeric rows: compute % change. Flag ↑↑ / ↑ / → / ↓ / ↓↓ at thresholds 10% / 1% / -1% / -10%
- Boolean rows: flag YES → NO transitions (e.g., SOC 2 was held, now expired)
- List rows (customers, integrations): compute set-difference; flag additions and removals
- Free-text rows: prompt the model to summarize the delta in 1 sentence

### Special: case-study removal pattern

When a customer logo from §9 disappears between versions, this is often a stronger signal than a new logo addition — it typically means the customer churned. Surface these prominently in §5.

```bash
# Set difference of customer logos
comm -23 <(grep -oE 'class="customer-logo">[^<]+' "$PREV" | sort -u) \
         <(grep -oE 'class="customer-logo">[^<]+' "$CURR" | sort -u) \
  > /tmp/lost-customers.txt
```

## Output formats

Default: MD (with `--export=md`). Comparison mode supports the same `--export=` flags as single-entity mode:

- `--export=html` — comparison HTML with side-by-side columns; sticky headers
- `--export=pdf` — comparison PDF; landscape orientation OK for wide tables
- `--export=both` — both

Note: comparison MD has wider tables than single-entity dossiers; HTML/PDF rendering should accommodate.

## Confidence in comparison mode

Comparison confidence inherits from the lower of the two inputs:

- If input A has §23 confidence = 87 and input B has §23 confidence = 72, the comparison confidence is capped at 72 (limited by the weaker source)
- Display both inputs' §23 confidence scores in §15 Methodology
- Add a "Comparison-specific risks" subsection: cross-dossier definitional drift (e.g., "A counts ARR differently than B")

## Anti-patterns

- ❌ Comparing two dossiers with different `--depth` levels without flagging it ("A is `--depth=deep`, B is `--depth=quick`; the comparison is biased toward A")
- ❌ Comparing dossiers >12 months apart without freshness adjustment (the older one is stale)
- ❌ Trying to compare 5+ entities in one run — too wide for any output format; do pairwise instead
- ❌ Auto-running `--year-over-year` without prompting the user (re-running research is expensive — confirm)

## Auto-schedule integration

After a year-over-year diff, offer `/schedule` to set up quarterly re-runs:

> "Detected meaningful deltas (↑3 customers, ↓1 SOC 2 status, +1 lawsuit). Want me to /schedule a quarterly re-run for this entity? Recommend cron: `0 9 1 */3 *` (9am on the 1st of every 3rd month)."

## When to load this file

- `--compare=` flag set with ≥2 paths
- `--year-over-year` flag set
- User asks "what changed since last time?" / "compare X to Y"
