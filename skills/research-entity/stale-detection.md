# Stale-Data Detection + Confidence Decay

Loaded by the `research-entity` skill at Step 8 (Confidence Scoring) when an existing dossier is present (convert-only mode) OR when a prior dossier with a known `research_date` is being read for any reason. Computes per-source freshness, decays the composite confidence, and recommends whether re-research is needed.

## Why this matters

A dossier confidence score is a *point-in-time* claim. Without explicit decay, a 2-year-old dossier still shows "87/100 confidence" — but the underlying funding round may have closed, the team page may have changed, the SOC 2 cert may have lapsed, the customer logos may have churned, the pricing may have changed.

This module:
1. Detects which sources in the dossier are stale by source-type-specific TTL
2. Decays the composite confidence based on age + how-staleness-sensitive the inputs are
3. Outputs a clear recommendation: "still fresh" / "soft-refresh recommended" / "hard re-research needed"
4. Optionally triggers `/schedule` for an auto-refresh cadence

## Source-type TTLs

| Source type | TTL (days) | Decay rate after TTL | Why |
|---|---:|---:|---|
| **Funding rounds (Crunchbase/PitchBook)** | 90 | -2/30d | Rounds close monthly; stale by 90 days |
| **Pricing page (entity)** | 60 | -3/30d | SaaS prices change quarterly often |
| **Customer logo wall** | 90 | -1/30d | Logos churn slowly |
| **Trust page certifications (SOC 2, ISO)** | 180 | -2/30d | Annual recerts; lapse possible after 12mo |
| **Founder bio** | 365 | -0.5/30d | Slow to change; CEO change is rare |
| **Press / news mentions** | 90 | -2/30d | News cycles fast |
| **Reviews (G2, Capterra, Trustpilot)** | 60 | -1/30d | Counts and ratings move monthly |
| **GitHub activity** | 30 | -1/30d | Stars and contributors change weekly |
| **LinkedIn hiring** | 30 | -1/30d | Job postings change weekly |
| **Lawsuit / regulatory** | 30 | -3/30d | New filings monthly; high stakes |
| **SEC filings (10-K)** | 365 | 0 | Annual cycle; only stale on transition |
| **SEC filings (10-Q)** | 90 | -2/30d | Quarterly cycle |
| **Glossary terms** | 730 | 0 | Definitions stable |
| **Business register entries** | 365 | -0.5/30d | Entity changes slow |

## Computation

```bash
DOSSIER_DATE=$(grep '^research_date:' "$DOSSIER" | awk '{print $2}')
TODAY=$(date +%Y-%m-%d)
AGE_DAYS=$(( ($(date -j -f %Y-%m-%d "$TODAY" +%s) - $(date -j -f %Y-%m-%d "$DOSSIER_DATE" +%s)) / 86400 ))

# For each source citation, find which TTL bucket it belongs to
# and apply the decay if AGE_DAYS > TTL.

# Composite confidence after decay = original confidence - sum-of-weighted-decays

# Decay weights (matches confidence-scoring.md weights):
#  - Multi-source corroboration (30) — decays as facts age (-1/30d after 90)
#  - Source verifiability (25) — decays slowly (-0.5/30d after 180)
#  - URL freshness (15) — decays fast (-2/30d after 60)
#  - Hallucination audit (15) — decays slowly (-0.5/30d after 365; audit is method, not data)
#  - Voice/format (15) — does NOT decay (formatting is timeless)
```

## Output template (insert as §23.X)

````markdown
### 23.X Freshness Decay & Refresh Recommendation

**Dossier dated**: <YYYY-MM-DD>
**Age**: <N> days
**As-of recompute**: <today YYYY-MM-DD>

#### Per-source freshness

| Source category | Last refresh | Age (d) | TTL (d) | Status |
|---|---|---:|---:|---|
| Funding | 2026-04-09 | 18 | 90 | ✅ fresh |
| Pricing | 2026-04-09 | 18 | 60 | ✅ fresh |
| Customer logos | 2026-04-09 | 18 | 90 | ✅ fresh |
| Trust certs (SOC 2 / ISO) | 2025-08-15 | 254 | 180 | ⚠️ aging (74d past TTL) |
| Press / news | 2026-04-09 | 18 | 90 | ✅ fresh |
| Reviews (G2/Capterra) | 2025-12-15 | 132 | 60 | ⚠️ aging (72d past TTL) |
| GitHub activity | 2026-04-09 | 18 | 30 | ✅ fresh |
| LinkedIn hiring | 2026-04-09 | 18 | 30 | ✅ fresh |
| Lawsuit / regulatory | 2026-04-09 | 18 | 30 | ✅ fresh |

#### Composite confidence decay

| Dimension | Original | Decay applied | Current |
|---|---:|---:|---:|
| Multi-source corroboration | 28/30 | -2 | 26/30 |
| Source verifiability | 22/25 | -1 | 21/25 |
| URL freshness | 13/15 | -3 | 10/15 |
| Hallucination audit | 13/15 | 0 | 13/15 |
| Voice/format | 14/15 | 0 | 14/15 |
| **Composite** | **90/100** | **-6** | **84/100** |

#### Recommendation

- **🟢 Still fresh** (decay <5pts): no action needed; revisit in <X> months
- **🟡 Soft refresh** (decay 5-15pts): re-pull pricing + reviews + press; ~10 minute task
- **🔴 Hard refresh** (decay >15pts): full /research-entity re-run recommended

**This dossier**: 🟡 Soft refresh recommended (decay -6). The Trust Page certifications (last refreshed 2025-08) and review platform counts (last refreshed 2025-12) are past TTL.

#### Auto-refresh

To set up periodic auto-refresh:

```
/schedule cron="0 9 1 * *" "/research-entity <entity> --year-over-year --convert=<this-dossier-path>"
```

This runs on the 1st of every month at 9am, doing a year-over-year diff if the prior version exists.
````

## Refresh strategies

When the user accepts the recommendation, three modes:

### Soft refresh
- Re-pull only the stale-tagged source categories
- Apply diffs to the existing dossier (no full rewrite)
- Re-render mermaid + re-validate URLs
- Re-compute composite confidence
- Output a "what changed since last refresh" delta in §0

### Hard refresh
- Full /research-entity re-run
- Save prior dossier as `<entity>-research-<YYYY-MM-DD>.md.archive`
- Generate new dossier
- Optionally auto-run comparison-mode to produce delta report

### Year-over-year refresh
- Same as hard refresh, but auto-detect the prior dossier in same directory
- Always produce comparison-mode delta in addition to new dossier
- Surface deltas in §0 prominently (the "what changed" pre-read)

## When to load this file

- Convert-only mode (always — to flag staleness before exporting an old dossier)
- After full Step 8 confidence-scoring write
- User asks "is this still accurate?" / "how old is this?" / "should I re-run?"
- Year-over-year comparison mode

## Anti-patterns

- ❌ Reporting old confidence score without decay (misleadingly fresh-looking)
- ❌ Auto-running full re-research without confirming with user (expensive)
- ❌ Computing decay without showing per-source breakdown (reader can't see what's stale)
- ❌ Recommending soft refresh for entity that recently rebranded (always hard refresh after rebrand)
- ❌ Decaying voice/format dimension (formatting never goes stale)
