# Confidence & Methodology Scoring

Loaded by the `research-entity` skill at the end of Step 8 (Report) when `--confidence-score` is enabled (default). Produces the `§23 Appendix — Confidence & Methodology` section in the dossier and the matching one-line summary in the user-facing report.

## Why a multi-dimensional score, not a single number

A single "92% confidence" misleads — it gets gamed, lulls the reader into false trust, and doesn't tell them WHERE the dossier is strong vs. weak. Per the skill's voice rules, transparency beats reassurance.

**Always-required components:**
1. Date-stamp (so the score is frozen at draft time, not interpreted as live)
2. Methodology version (so future revisions can be compared)
3. Per-dimension breakdown (reader sees what's strong vs. weak)
4. "What this score does NOT mean" disclaimer (limits are explicit)
5. Reproducibility note (anyone running the same skill should arrive at a similar score)

## The 5-dimension framework (100 points total)

| Dimension | Weight | What it measures |
|---|---:|---|
| **Multi-source corroboration** | 30 | % of §0–§2 hard claims that are dual-sourced OR properly labeled (`single-source`, `aggregator-derived`, `vendor-claimed`, `founder-self-claim`). |
| **Source verifiability** | 25 | Mix of register-verified entities, audited disclosures, primary-site direct fetches vs. founder-self-claims and aggregator-only. |
| **URL freshness** | 15 | % of cited URLs returning HTTP 200 (or bot-blocked-but-verified-valid). 0 × 404 is a hard floor. |
| **Hallucination audit** | 15 | Subagent audit pass rate; specifically, % of §0 framework claims supported by §2–§22 body content. |
| **Voice / format discipline** | 15 | % of voice rules upheld (no editorial trail, no promotional language in analytical voice, all 23 sections present, etc.). |
| **Composite** | **100** | Sum of dimension scores. |

**Note:** Mermaid diagram validation runs as a quality check during draft + export (see `mermaid-validation.md`) but does NOT contribute to the composite confidence score. Mermaid is a presentation concern, not a content-truth concern; bundling it into the score would conflate "is the dossier accurate?" with "do the diagrams render?". The two should remain decoupled.

## External verification penalty (for `--type=competitive|due-diligence`)

When the dossier is written from an external-evaluator perspective with no NDA-stage access (no audited financials, no top-10 customer list, no board minutes, no founder-confirmation of single-source claims), apply a **structural penalty** to acknowledge the ceiling:

- **`--type=competitive`** or **`--type=due-diligence`**: subtract **5 points** from the composite as an "External verification penalty" line. This caps the typical composite around 70–82 even when validation runs cleanly.
- **`--type=research`** or **`--type=partnership`** (with implicit insider context): no penalty applied; composite ranges 78–92 typical.
- **`--type=investment`**: penalty depends on whether founder/cap-table reference calls are made; default apply -5 unless reference calls are documented.

**How to surface in the dossier**: add a final row to the §23.1 dimension table titled **"External verification penalty"** with weight `—` and score `–5`, with a note explaining that it reflects the structural ceiling on what an external evaluator can verify without NDA-stage access. **Do NOT** name the row "Outsider transparency penalty" or compare to a hypothetical insider score — both are stylistic provenance leaks (see `voice-and-style.md` Competitive dossier voice).

**Why apply a penalty rather than just downscore each dimension?** The dimension scores measure *validation pipeline completion* (did we run the cross-validation? did we run the URL check?). The penalty measures *what's structurally unverifiable from outside* (audited ARR, top-10 customer concentration, real burn rate). These are different concepts — a perfectly-executed external dossier still has the structural gap, and conflating it with dimension downscores would obscure where the gap actually lives.

## Scoring rubric per dimension

### Multi-source corroboration (30 points)

| Score | Criterion |
|---|---|
| 28–30 | Every §0–§2 numeric or proper-noun claim has ≥2 independent sources cited inline |
| 24–27 | Most claims dual-sourced; single-source claims labeled `single-source` or `aggregator-derived` |
| 20–23 | Several single-source claims labeled but a few §0 first-mentions defer to body |
| 16–19 | Critical §0 claims unsourced or improperly labeled |
| ≤15 | Multiple §0 hard claims missing citations and labels |

### Source verifiability (25 points)

| Score | Criterion |
|---|---|
| 23–25 | Hard facts (incorporation dates, registration numbers, certifications) verified against official registers |
| 19–22 | Mix of register-verified and direct-from-source (Trust page, pricing page, official PR); founder-self-claims labeled |
| 15–18 | Mostly aggregator + primary-site; founder narratives uncritical |
| 11–14 | Aggregator-heavy; misframed founder narratives (e.g., conflating contractor relationship with equity ownership) |
| ≤10 | Repeats unverified claims as fact |

### URL freshness (15 points)

| Score | Criterion |
|---|---|
| 14–15 | 0 × 404; non-200 codes (403/000) verified as valid via browser-UA; explained inline |
| 12–13 | 0 × 404; some non-200 unverified |
| 9–11 | 1–2 × 404 fixed; some bot-blocks unverified |
| 6–8 | 3+ × 404 remaining |
| ≤5 | URL validation skipped |

### Hallucination audit (15 points)

| Score | Criterion |
|---|---|
| 14–15 | Audit run; ≥95% of §0 claims body-supported; specific gaps fixed |
| 12–13 | Audit run; ≥85% supported; remaining gaps labeled |
| 9–11 | Audit run; flagged items partially addressed |
| 6–8 | Audit run; flagged items not addressed |
| ≤5 | Audit not run |

### Voice / format discipline (15 points)

| Score | Criterion |
|---|---|
| 14–15 | 0 editorial-trail markers, 0 promotional in analytical voice, all 23 sections, §3.4 + §16.X present, mermaid portrait |
| 12–13 | 0 editorial-trail; promotional language present in attributed quotes only |
| 9–11 | Some editorial-trail markers; minor section gaps |
| 6–8 | Multiple voice violations |
| ≤5 | Promotional language in analytical voice; missing core sections |

## Comparison bands

For reader calibration:

| Document type | Typical composite |
|---|---:|
| Press-release-only summary | 35–50 |
| Aggregator-cited overview | 50–70 |
| Single-pass research dossier (no cross-validation) | 65–80 |
| External evaluator dossier with cross-validation + hallucination audit (public-source-only) | 70–82 |
| Multi-pass dossier with cross-validation + hallucination audit (NDA-stage access OR insider context) | 80–92 |
| Independently audited public-company filing-based dossier | 90–98 |

A typical `--depth=deep` run with cross-validation should land in the **80–92** band for `--type=research|partnership` (insider/relationship context), or in the **70–82** band for `--type=competitive|due-diligence` (external lens with the -5 External Verification Penalty applied).

## "What this score does NOT mean" — required disclaimer

The composite reflects **sourcing rigor, audit discipline, and validation pipeline completion** — not whether the underlying facts are true. Specifically the score does NOT mean:

- Founder-self-reported metrics (revenue, customer count, podcast view-count) are accurate; only that they are correctly labeled
- Vendor-claimed metrics (productivity, integration counts) are independently audited; only that the `vendor-claimed` label is applied
- Aggregator-only investor identities have been verified against the actual VC's portfolio; only that the gap is disclosed
- Single-source proprietary research (e.g., a vendor-issued state-of-the-industry report) reflects rigorous methodology; only that single-sourcing is flagged
- Founder origin-story claims are corroborated by third-party documentation; only that interview-based corroboration was found

This disclaimer is **non-negotiable** and must appear adjacent to the composite score.

## "What would raise the score" — required improvement table

Helps the user understand what targeted improvements would close gaps. **Focus on user-meaningful gaps** (founder-claim corroboration, aggregator dependencies, missing audited disclosures) — NOT on technical/infrastructure items like installing `mermaid-cli` or fixing >45-char-line mermaid warnings (those are skill-internal mechanics, not user-facing data quality concerns). Format:

| Gap | Current state | Could-be | Effort |
|---|---|---|---|
| Founder-claim corroboration | interview-sources | independent contemporaneous documentation | requires archive research |
| Aggregator-only investor identity | Tracxn-only | direct verification via investor portfolio | requires direct outreach OR paid lookup |
| First-mention citations in §1 | deferred to body | inline links | ~15 min editing |
| Live-pricing currency | snapshot | live-pricing-page citation | recurring quarterly refresh |
| Independent revenue audit | aggregator self-reports | annual audited statement disclosure | requires entity disclosure |
| Trustpilot / G2 / Glassdoor counts | bot-blocked direct fetch | scraped via authenticated session or paid API | requires paid access |

## Output format in the dossier

The skill writes this section as `§23 Appendix — Confidence & Methodology` at the end of the dossier (between §22 Glossary and the end-of-dossier marker). Structure:

1. **§23.1 Composite confidence** — the 5-dimension table + composite cell with date-stamp + a note that mermaid validation is decoupled
2. **§23.2 What this score does NOT mean** — the non-negotiable disclaimer
3. **§23.3 What would raise the score** — user-meaningful gaps + effort table (NOT technical / infrastructure items)
4. **§23.4 Comparison to baseline** — band table for reader calibration

The end-of-dossier marker should report the composite alongside line count + section count + URL count. Example:

```
End of dossier. 1,892 lines, 220+ cited URLs, 10 portrait mermaid diagrams, 23 sections + Confidence Appendix. Confidence: 86/100 as of 2026-04-27.
```

## When to load this file

Load `confidence-scoring.md` when:
- About to write §23 (always, unless `--no-confidence-score` is set)
- User asks "how confident are you?" / "what's the confidence score?" / "audit this"
- Comparing two dossier revisions (the score should improve revision-over-revision)

## Anti-patterns

- ❌ Single number without per-dimension breakdown — gameable, misleads
- ❌ Score without date-stamp — reader assumes it's live
- ❌ Score without "what this does NOT mean" disclaimer — reader over-trusts
- ❌ Score without comparison band — no calibration anchor
- ❌ Score with weights that don't sum to 100 — math is wrong, signals carelessness
- ❌ Inflating the composite to look better than the dimensions support — destroys reproducibility
- ❌ Hiding the score deep in §16 Risks — should be findable as a top-level §23
- ❌ Including technical / infrastructure items (`mmdc` install, mermaid-line-length, `mermaid-filter` setup) in "What would raise the score" — those are skill-internal mechanics, not user-facing data quality concerns. Stay focused on the user's perspective: what does the *content* lack?
- ❌ Bundling mermaid validation into the composite score — mermaid is a presentation concern, not a content-truth concern; conflating them misleads the reader about whether facts are correct
