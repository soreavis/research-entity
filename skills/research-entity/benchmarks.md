# Industry Benchmarks — `--benchmark[=cohort]`

Loaded by the `research-entity` skill at Step 4 (Draft) when `--benchmark` is set, OR auto-activated for `--stage=series-b`+, `--stage=growth`, `--stage=pe`, `--stage=public`. Inserts a new section **§X Industry Benchmarks** comparing the entity's metrics to public benchmark medians.

## Public benchmark sources

| Source | What it covers | Free public report URL |
|---|---|---|
| **Bessemer Cloud Index** | Public SaaS multiples, R40, NRR, growth rates by ARR band | https://www.bvp.com/atlas/state-of-the-cloud-2024 |
| **SaaS Benchmarks Report — High Alpha (formerly OpenView)** | Pricing, packaging, sales efficiency, GTM motions, by ARR band | https://www.highalpha.com/saas-benchmarks |
| **KeyBanc SaaS Survey** | Annual private SaaS survey (subscription-based but high-level summary public) | https://www.key.com/saassurvey |
| **ICONIQ Growth Benchmarks** | Private growth-stage benchmarks, NRR, gross retention, payback | https://www.iconiq.com/growth/insights |
| **Sapphire Ventures** | "Best of breed" benchmarks for cloud / data / AI | https://sapphireventures.com/perspectives/ |
| **Battery Ventures Cloud Software Index** | Public multiples, growth, profitability tradeoff curves | https://www.battery.com/blog/opencloud-2024/ |
| **Gartner Cool Vendors** | Annual vendor identification across categories | (paid; cite if user has subscription) |

Note: each year's report supersedes the prior year. Always cite the most recent public report and the as-of date.

## Cohort selection

`--benchmark=<cohort>` lets the user specify which benchmark cohort to compare against:

- `--benchmark=public-saas` (default) — Bessemer / Battery for public SaaS comps
- `--benchmark=growth-stage` — ICONIQ for $25M-$200M ARR private SaaS
- `--benchmark=early-stage` — OpenView for sub-$25M ARR private SaaS
- `--benchmark=ai-native` — Bessemer / a16z AI infrastructure benchmarks
- `--benchmark=vertical-saas` — vertical-specific from public 10-Ks
- `--benchmark=devtools` — devtools-specific (open-source-distributed) from a16z / OpenAI fund

If `--vertical=` is also set, prefer vertical-specific where available.

## Metrics compared

| Metric | Definition | Why it matters |
|---|---|---|
| **ARR** | Annual Recurring Revenue | Stage classifier |
| **YoY growth %** | (ARR_now / ARR_year_ago) - 1 | Top-line acceleration |
| **NRR** | Net Revenue Retention (excl. new logos) | Expansion strength |
| **GRR** | Gross Revenue Retention (incl. churn only) | Stickiness |
| **Magic Number** | Net new ARR / S&M spend (4Q lookback) | Sales efficiency; >0.7 = healthy |
| **R40** | Growth rate + EBITDA margin | Bessemer's go-to scoring |
| **CAC payback (months)** | New ARR generated per $1 of S&M, expressed in months | Deal economics |
| **Burn multiple** | Net burn / Net new ARR | Capital efficiency |
| **Rule of X** | Custom; e.g., growth × NRR | Segment-specific comp |
| **Gross margin %** | (Rev - COGS) / Rev | Software vs. services purity |
| **Sales cycle (days)** | Median lead-to-close | Velocity |
| **ACV** | Average Contract Value | Tier classification |

## §X Industry Benchmarks template

```markdown
## §X. Industry Benchmarks

Comparison to public benchmark medians for **<cohort name>** as of **<benchmark report date>**. Source: <report URL>. Entity metrics are <observed | estimated from public sources | vendor-claimed>.

| Metric | <Entity> | Cohort median | Top quartile | Verdict |
|---|---:|---:|---:|---|
| ARR | $XXM | $XXM | $XXM | ✅ above / 🟡 at / ⚠️ below |
| YoY growth | XX% | XX% | XX% | ... |
| NRR | XXX% | 110% | 130% | ... |
| GRR | XX% | 90% | 95% | ... |
| Magic Number | X.X | 0.7 | 1.5 | ... |
| R40 | XX | 40 | 70 | ... |
| CAC payback | XX mo | 18 mo | 9 mo | ... |
| Burn multiple | X.X | 1.5 | 0.5 | ... |
| Gross margin | XX% | 75% | 85% | ... |

**Composite assessment**: 

- 🟢 **Top-quartile** on: <list>
- 🟡 **At-median** on: <list>
- 🔴 **Below-median** on: <list>

**Stage-adjusted note**: at <stage>, the cohort medians shift toward <growth | profitability | balance>. The entity's <metric> may reflect <reason>, not necessarily a weakness.

**Sources**:
- [<Benchmark report 1>](url) — as of <date>
- [<Benchmark report 2>](url) — as of <date>
- [<Entity 10-K / press release>](url) — for entity metrics

---
```

## Estimation rules

When the entity is private and metrics aren't disclosed, you must label estimates:

- **NRR / GRR** — typically not disclosed by private companies; show "Not disclosed" rather than estimate
- **ARR** — if Latka or similar reports it, label `single-source / founder-self-reported`
- **R40** — only computable if both growth and margin disclosed; otherwise "Insufficient public data"
- **Magic Number** — typically not estimable for private; show "Not disclosed"
- **Gross margin** — if 10-K or S-1 → disclosed; else "Not disclosed"

**Hard rule**: do not show a calculated benchmark comparison row if the underlying metric is fabricated/unsourced. Better to show "Not disclosed → cannot benchmark" than to invent a number.

## Vertical-specific benchmarks

If `--vertical=` is set, use the most relevant cohort:

| Vertical | Best benchmark cohort | Notable adjustment |
|---|---|---|
| healthcare | Vertical SaaS public comps (Veeva, Phreesia, Doximity) | Lower growth, higher gross margin, higher NRR |
| fintech | Public neobanks + payment processors | Variable — depends on lending vs. SaaS subset |
| govtech | Tyler Tech, Granicus comps | Slow growth, very high retention, long sales cycle |
| edtech | Powerschool, Renaissance, Instructure comps | Seasonal (academic year) revenue lumpiness |
| legaltech | Clio, MyCase comps (private); Litify (private) | Mid-tier growth, very high stickiness |
| devtools | GitHub, GitLab, JetBrains, Vercel comps | Very high gross margin (90%+), bottom-up adoption metrics matter more |
| consumer | Public DTC + subscription comps (Roblox, Match, Hinge) | High customer acquisition cost; LTV/CAC matters more than NRR |
| deeptech | OpenAI / Anthropic / Hugging Face comps where possible | Fewer public; cite peer cohort qualitatively |

## Comparison-mode interaction

When `--compare=A.md,B.md` is set, the benchmarks section becomes a 3-column comparison: Entity A | Entity B | Cohort median. Enables "which one is closer to median? which one is closer to top quartile?" verdicts.

## Anti-patterns

- ❌ Citing a benchmark report from 3+ years ago (cohort medians shift; stale benchmarks mislead)
- ❌ Comparing a $5M ARR seed company to a $500M ARR public-cloud cohort (wrong cohort)
- ❌ Estimating NRR / Magic Number without underlying disclosure (these aren't observable from outside)
- ❌ Citing Gartner Magic Quadrant placement as a benchmark (it's a vendor-positioning, not a metric)
- ❌ Reporting a single-data-point comparison with no error bar / variance disclosure ("110% NRR" is meaningless without "vs. cohort median 105% with σ=20%")

## When to load this file

- `--benchmark` flag set
- `--stage=series-b` / `growth` / `pe` / `public` (auto-activated)
- User asks "how do they compare to industry?"
- User mentions Bessemer / OpenView / R40 / Magic Number / NRR
