# Win/Loss Intelligence Framework

Loaded by the `research-entity` skill when `--win-loss` flag set OR `--type=competitive` AND `--audience=c-suite|operator|investor` (auto-suggest). Codifies the **single most-asked-for competitive-intelligence output**: where does the entity win, where does it lose, against whom, and why.

## §1 — Why this file exists

Per industry adoption data ([Klue](https://klue.com/blog/win-loss-analysis-guide), [Crayon G2 category](https://www.g2.com/categories/win-loss-analysis-services), [Monetizely](https://www.getmonetizely.com/articles/mastering-competitive-intelligence-how-to-track-winloss-rates-in-the-saas-landscape), [Development Corporate 2025 reality check](https://developmentcorporate.com/product-management/win-loss-rates-for-enterprise-saas-the-2025-reality-check/)):

- Companies with formalized win/loss programs achieve **15-30% higher win rates**
- Only **~20% of B2B SaaS** have robust win/loss tracking → 80% miss this leverage
- Enterprise SaaS competitive win-rate benchmarks:
  - 20-35% — average
  - 40-50% — high-growth
  - 50%+ — category-defining
- Companies using competitive insights to guide product development achieve **22% higher customer satisfaction**

For a CRO / CEO reading a competitive brief, "where do we win vs. them, and why" is the single most actionable question. This file codifies how to extract win/loss intelligence from public sources.

---

## §2 — Public-source inference rubric

For competitive analysis without access to your own deal data, win/loss patterns can be inferred from public review platforms:

### Method A — G2 / TrustRadius "switched from / switched to" mining

[G2](https://www.g2.com/) and [TrustRadius](https://www.trustradius.com/) reviews routinely contain verbatim "we switched from X to Y" / "we evaluated A, B, C" language.

**Mining query patterns:**
- `"switched from <competitor>" site:g2.com OR site:trustradius.com`
- `"we evaluated <entity>" site:g2.com OR site:trustradius.com`
- `"chose <entity> over" site:g2.com OR site:trustradius.com`
- `"replaced <competitor>" site:g2.com OR site:trustradius.com`

**Output:** verbatim quotes, attributed to reviewer name + role + company size + review date. **Never paraphrase**; quote directly to preserve source-discipline.

### Method B — Reddit / forum thread mining

`r/CRM`, `r/SaaS`, `r/sales`, `r/startups`, vertical-specific subreddits, [Hacker News](https://news.ycombinator.com/), and trade-press comment threads.

**Search patterns:**
- `"<entity> vs <competitor>" site:reddit.com`
- `"<entity> alternatives" site:reddit.com`
- `"why we picked <entity>" site:reddit.com OR site:news.ycombinator.com`

### Method C — Comparison-page narrative mining

The entity's own `/comparison/<peer>-vs-<entity>/` pages reveal **how the entity narrates its own wins**. Per `internal-consistency.md` technique #64 (comprehensive comparison-directory probe), every such page is mined for:

- **Claimed wins:** "Our customers tell us they pick us because…" verbatim claims
- **Acknowledged losses:** rare but visible — when the entity admits weakness ("if you need feature X, consider Y")
- **Pricing positioning:** how the entity frames its price advantage
- **Implementation positioning:** how the entity frames its time-to-value advantage

### Method D — Glassdoor sales-team commentary

Sales-team Glassdoor reviews often surface internal-narrative on competitive positioning. Mining for:
- "We struggle to compete against X on Y feature"
- "Our biggest losses are to <competitor>"
- "Buyers ask about <competitor> in every cycle"

This is internal-narrative leakage and counts as T2-T3 evidence (named-source but anonymized).

---

## §3 — With-input-data mode (`--win-loss=<csv>`)

When the user provides their own win/loss data via `--win-loss=<path-to-csv>`, the dossier integrates it as **ground-truth** alongside the public-source inference.

### Required CSV format

```csv
deal_id,outcome,competitor,deal_size,segment,vertical,close_date,primary_loss_reason,secondary_loss_reason
deal-001,won,<entity>,$50000,smb,construction,2026-01-15,,
deal-002,lost,<entity>,$120000,mid-market,manufacturing,2026-02-10,price,feature_gap
deal-003,lost,<entity>,$30000,smb,real_estate,2026-03-01,no_decision,
```

### Synthesis output

When ground-truth data is provided, the dossier produces:
- Win-rate vs. the entity (from user's data)
- Average deal size in won vs. lost deals
- Top-3 loss reasons by deal-count
- Top-3 loss reasons by deal-value
- Segments / verticals with highest win-rate and lowest win-rate

---

## §4 — Output template (§10.X Win/Loss Intelligence)

```markdown
## §10.X Win/Loss Intelligence

### §10.X.1 Public-source-inferred win drivers (entity wins because…)

[Top 3 with verbatim quotes from G2 / TrustRadius / Reddit]

| Win driver | Verbatim quote | Source | Date |
|---|---|---|---|
| <driver> | "<quote>" | [G2 review](url) | YYYY-MM |
| <driver> | "<quote>" | [TrustRadius](url) | YYYY-MM |
| <driver> | "<quote>" | [Reddit](url) | YYYY-MM |

### §10.X.2 Public-source-inferred loss drivers (entity loses because…)

[Top 3 with verbatim quotes]

### §10.X.3 Most-frequent named competitors in switching narratives

| Competitor | Switching direction | Frequency in mined corpus |
|---|---|---|
| <peer-A> | switched from peer-A to <entity> | High |
| <peer-B> | switched from <entity> to peer-B | Medium |
| <peer-C> | both directions cited | Medium |

### §10.X.4 With-data synthesis (if `--win-loss=<csv>` provided)

[User-data ground truth integration]

### §10.X.5 Strategic implications

- **Where to compete head-to-head**: <verticals/segments where entity's win-rate is below market>
- **Where to avoid**: <verticals/segments where entity has structural advantage>
- **Wedge opportunities**: <loss reasons that double-as your strengths>

### §10.X.6 Industry win-rate benchmarks (per Klue / Development Corporate)

- 20-35% — average enterprise SaaS competitive win rate
- 40-50% — high-growth SaaS leaders
- 50%+ — category-defining market leaders
```

---

## §5 — Anti-hallucination discipline (Cat J extensions)

- **#73 — Win-rate-without-denominator rule**: every win-rate claim must include the underlying N (sample size) AND the source (your own data / Klue / G2 sample). NEVER state "<entity> wins X% of deals against <competitor>" without N + source.
- **#83 — Win-driver-needs-3-corroborating-reviews**: a top-3 win driver claim must show ≥3 corroborating reviews. A single anecdote is not a "win driver" — it's an anecdote.
- **#89 — Verbatim-quote discipline**: when mining G2 / TrustRadius / Reddit, quote verbatim with attribution; never paraphrase. Paraphrase = synthesis = loss of source-discipline.
- **Avoid** publishing competitor-comparison win/loss claims that the entity itself disputes on its comparison page (acknowledge both directions).

---

## §6 — When to load this file

- **Auto-suggest** when `--type=competitive` + `--audience=c-suite|operator|investor`
- **Manual load** when `--win-loss` flag set
- **Mandatory** for `--export=battle-card` (Klue FIA format depends on win/loss inputs)
- User asks "where do they win?" / "what's their win rate?" / "why do we lose to them?" / "how do we beat them?"

---

## §7 — Composability

| Concern | File |
|---|---|
| Comparison-directory comprehensive probe | `internal-consistency.md` technique #64 |
| Reviews-platform sourcing (G2 / Capterra / TrustRadius) | `reviews-platforms.md` |
| Battle-card output format | `output-formats.md` |
| Klue FIA (Fact / Impact / Action) discipline | `output-formats.md` |
| Customer-reference call templates (for verifying public win/loss inference) | `expert-calls.md` |

---

## §8 — Anti-patterns

- ❌ Citing a single review as a "win driver" — anecdotes ≠ patterns
- ❌ Stating win-rate without N (sample size) and source
- ❌ Paraphrasing review quotes — always quote verbatim with attribution
- ❌ Ignoring the entity's own comparison-page narrative — they are the source-of-record for how they want to be perceived
- ❌ Confusing market-share with win-rate — different metrics, different methodologies
- ❌ Treating Glassdoor sales-team commentary as authoritative — it's directional, often biased by departing employees
