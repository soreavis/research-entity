# SaaS Economics — NRR / CAC / LTV / Payback Estimation

Loaded by the `research-entity` skill when `--unit-economics` flag is set OR `--audience=board|investor` OR `--type=investment|due-diligence` AND entity is private B2B SaaS without disclosed audited financials. Codifies multi-method estimation rubrics for Net Revenue Retention (NRR), Customer Acquisition Cost (CAC), Lifetime Value (LTV), and CAC Payback — the four metrics every SaaS board / IPO process / investor IC tracks.

## §1 — Why this file exists

Net Revenue Retention is **THE board metric for SaaS**. Per [ICONIQ State of Software 2025](https://www.iconiq.com/growth/reports/2025-state-of-software), [Bessemer State of the Cloud](https://www.bvp.com/atlas/state-of-the-cloud-2024), [Pavilion 2025 benchmarks](https://www.joinpavilion.com/resource/b2b-saas-performance-benchmarks), and [SaaS Capital](https://www.saas-capital.com/research/private-saas-company-growth-rate-benchmarks/), NRR is the single strongest predictor of growth velocity, IPO readiness, and acquisition multiple.

**Bessemer canonical tiers (the language SaaS boards actually speak):**

| NRR | Bessemer tier |
|---|---|
| 100% | **Good** |
| 110% | **Better** |
| 120%+ | **Best** |

**ICONIQ at-$10M-ARR portfolio benchmarks (per Bessemer Venture Partners):**
- Bottom quartile: <105% NRR
- Median: 140% NRR
- Top quartile: >145% NRR

**Growth-rate impact (per ICONIQ + Bessemer):**
- Increasing NRR from 90-100% to 100-110% improves growth rate by **5 percentage points**.
- Companies with the highest NRR report median growth **83% higher** than the population median.

For private SaaS without disclosed audited financials, NRR / CAC / LTV / Payback must be **estimated from public signals**, never fabricated. This file codifies the multi-method estimation rubrics.

---

## §2 — NRR estimation rubric (multi-method)

For private SaaS, NRR is rarely disclosed. Estimate via **≥2 independent methods** (per technique #55 — multi-method estimation produces plausibility-range bands, NOT triangulation):

### Method A — Expansion-team inference

Look at LinkedIn / job postings for these role titles:
- "Expansion AE" / "Account Manager" / "Customer Account Executive"
- "Renewals Manager" / "Renewals Specialist"
- "Customer Success Manager" / "CSM"
- "Strategic Account Manager"

**Heuristic** (Bessemer + Pavilion practice): a SaaS with NRR >120% typically has:
- ≥1 dedicated Expansion AE per ~$5M of ARR
- CSM-to-AE ratio ≥ 1:2
- Public role for "Renewals Manager" with named ownership

**A SaaS with NRR <100% typically has:**
- No dedicated expansion role
- CS team is "support" branded, not "success" branded
- No "renewals" role; renewals fall to original AE

### Method B — Case-study upgrade narrative density

Scan the entity's `/customers/` and case-study pages for **upgrade language**:
- "Started with X seats, now at Y" → strong expansion signal
- "Expanded from team A to enterprise" → strong expansion signal
- "Added module M / Y / Z over 18 months" → land-and-expand
- "Year over year ACV grew" → revenue-per-account expansion

**Heuristic:** ≥40% of public case studies showing upgrade narratives → NRR likely 110%+. <10% → NRR likely <105%.

### Method C — Investor-disclosure mining

Search [Sacra](https://sacra.com/), [Pitchbook public profiles](https://pitchbook.com/), [Crunchbase Pro](https://www.crunchbase.com/), [Bessemer State of the Cloud](https://www.bvp.com/atlas/state-of-the-cloud-2024), and [SaaS Capital](https://www.saas-capital.com/) for the entity's NRR if disclosed in a funding round or annual letter.

### Method D — Churn signal from review platforms

Inverse-correlate NRR with churn signals:
- High volume of [G2](https://www.g2.com/) / [TrustRadius](https://www.trustradius.com/) / [Capterra](https://www.capterra.com/) reviews mentioning "we switched away" or "we cancelled" = churn signal → likely NRR <100%
- High proportion of "we expanded our usage" mentions = expansion signal → likely NRR 110%+

### Required output format

```markdown
**NRR Estimation (per `saas-economics.md`):**

| Method | Inference | Estimate band |
|---|---|---|
| Method A (Expansion team) | <signal observed> | <band> |
| Method B (Case-study upgrades) | <signal observed> | <band> |
| Method C (Investor disclosure) | <signal observed> | <band> |
| Method D (Churn signals) | <signal observed> | <band> |

**Convergent estimate:** <band, e.g., "100-110%"> — Bessemer tier: <Good / Better / Best>

**Caveats:** Methods A-D share the assumption that public signals are unbiased; not independent measurements (per technique #55). Treat as plausibility-range band, not point estimate.
```

---

## §3 — CAC estimation rubric

CAC = (sales + marketing spend) / new customers acquired.

For private SaaS, neither numerator nor denominator is typically disclosed. Estimate via:

### Method A — Sales team × loaded cost / new logos

- Count AEs from LinkedIn (search `"Account Executive" "<entity>"`)
- Apply $200-300K/yr fully-loaded AE cost (Bessemer + Bridge Group benchmark)
- Estimate new logos / yr from press releases, customer-page additions (Wayback delta), case-study cadence
- CAC = AE_count × $250K / new_logos_per_yr

### Method B — Marketing spend × ad-tracking fraction

- Use [BuiltWith](https://builtwith.com/) or [Wappalyzer](https://www.wappalyzer.com/) to detect ad-tech stack
- Use [SimilarWeb](https://www.similarweb.com/) for paid-traffic-share estimation (paid % of total traffic)
- Cross-reference [SpyFu](https://www.spyfu.com/) for paid-keyword spend visibility (US market only)
- Backsolve marketing spend from these signals

### Method C — Public benchmark application

For B2B SaaS at the entity's stage, apply [OpenView](https://openviewpartners.com/) / [KeyBanc](https://www.key.com/saassurvey) / [ICONIQ](https://www.iconiq.com/growth/reports/2025-state-of-software) cohort medians:

| Stage | Median CAC ($) | Source |
|---|---|---|
| Seed / Series A SMB SaaS | $1,000–5,000 | Bessemer SOTC |
| Series B mid-market | $5,000–25,000 | KeyBanc SaaS Survey |
| Series C+ enterprise | $25,000–150,000+ | ICONIQ State of Software |

### Required output format

```markdown
**CAC Estimation:**

- Method A (Sales-team × loaded cost): $<X>K
- Method B (Ad-tracking inference): $<Y>K
- Method C (Cohort benchmark): $<Z>K
- **Convergent CAC band:** $<low>K – $<high>K
- **Confidence:** Low (private signals only) / Medium (multi-method aligned) / High (≥1 source disclosed)
```

---

## §4 — LTV estimation rubric

LTV = ACV × Gross-Margin × (1 / Annual-Churn-Rate)

### Method A — ACV × public gross-margin assumption

- Estimate ACV (per `arr-triangulation.md`)
- Apply 70-80% gross margin (typical SaaS — per [Bessemer](https://www.bvp.com/atlas/state-of-the-cloud-2024) and [SaaS Capital](https://www.saas-capital.com/))
- Apply 1/churn-rate as customer-lifetime estimator
- LTV = ACV × 0.75 × (1 / annual-churn)

### Method B — Public review-platform tenure analysis

- Sample [G2](https://www.g2.com/) reviewers; check their LinkedIn for company tenure
- Median customer tenure × ACV × gross-margin = LTV proxy

### Required output format

```markdown
**LTV Estimation:** $<low> – $<high>K
**Annual Churn estimate:** <X>% (inferred from <method>)
**Customer Lifetime estimate:** <Y> years
```

---

## §5 — CAC Payback estimation

CAC Payback (months) = CAC / (ACV × Gross-Margin / 12)

**Industry benchmarks (per Bessemer + Pavilion 2025):**

| CAC Payback | Tier |
|---|---|
| <12 months | Best-in-class (top quartile) |
| 12-18 months | Healthy |
| 18-24 months | Acceptable for enterprise |
| 24-36 months | Concerning unless NRR >130% |
| >36 months | Red flag |

The CAC Payback metric is the SaaS unit-economics rosetta stone — combines CAC + LTV + monetization velocity into one number. SaaS boards live and die by this.

---

## §6 — Output template (§X SaaS Economics)

```markdown
## §X — SaaS Economics

### §X.1 NRR estimate

[Multi-method NRR rubric output per §2 above]

**Bessemer tier (canonical):** <Good (100%) / Better (110%) / Best (120%+)>
**ICONIQ at-stage benchmark comparison:** <where this entity sits vs. portfolio quartiles>

### §X.2 CAC / LTV / Payback estimate

[Per §3, §4, §5 above]

### §X.3 Rule of 40 inference

Rule of 40 = Revenue Growth % + EBITDA Margin %.

**Bessemer canonical interpretation:**
- ≥40% = healthy
- 30-40% = acceptable
- <30% = concerning

[Estimate revenue growth from headcount-velocity / case-study cadence; estimate EBITDA margin from headcount × $/FTE vs. revenue band]

### §X.4 Honest framing of these estimates

These are **multi-method plausibility-range bands**, not triangulated point estimates (per `internal-consistency.md` technique #55). Methods share the assumption that public signals reflect underlying reality without bias — they don't fully. For investment / acquisition decisions, request audited financials.
```

---

## §7 — Anti-hallucination discipline (Cat J extensions)

When using this file, additional Cat J techniques apply:

- **#74 — Bessemer-canonical-tier discipline**: NRR claims must use Bessemer's 100/110/120 = Good/Better/Best terminology, not generic "low/medium/high." This is the language SaaS boards speak.
- **#75 — Multi-method estimate band rule**: every NRR / CAC / LTV / Payback estimate must show ≥2 independent inference methods; output is a band, not a point estimate.
- **#84 — Cohort-benchmark citation**: when applying $/CAC or $/FTE benchmarks, cite the specific source (Bessemer SOTC / OpenView / KeyBanc SaaS Survey / ICONIQ) — never "industry benchmark" without source.
- **Avoid:** publishing NRR / CAC / LTV / Payback as point estimates; using "industry standard" without source citation; bundling unverified ARR figure into LTV calc; treating multi-method estimates as triangulation.

---

## §8 — When to load this file

- **Auto-load** when `--audience=board|investor` set
- **Auto-load** when `--type=investment|due-diligence` AND entity is private B2B SaaS without disclosed audited financials
- **Manual load** when `--unit-economics` flag set
- **Mandatory** for `--export=vc-memo` (combines with `valuation.md`)
- User asks "what's their NRR?" / "estimate their unit economics" / "how does their CAC compare to benchmarks?"

---

## §9 — Composability

| Concern | File |
|---|---|
| ARR triangulation (revenue inference) | `arr-triangulation.md` (input to §X.1) |
| Multi-method estimation discipline | `internal-consistency.md` technique #55 |
| Bessemer / OpenView / KeyBanc benchmark sourcing | `benchmarks.md` |
| Investor-narrative mining | `press-analysis.md` |

---

## §10 — Anti-patterns

- ❌ Publishing a single point-estimate NRR (e.g., "NRR is 115%") without method or band
- ❌ Citing "industry benchmark" without naming Bessemer / ICONIQ / KeyBanc / OpenView / Pavilion explicitly
- ❌ Using non-Bessemer terminology ("strong NRR" instead of "Better tier per Bessemer")
- ❌ Bundling Latka revenue figure into LTV calc without flagging it as aggregator-derived
- ❌ Computing CAC from one signal only (e.g., AE count × cost) without cross-checking marketing-spend signals
- ❌ Treating multi-method estimates as "triangulation" (per technique #55 — they share assumption stack)
