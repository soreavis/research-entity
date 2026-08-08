# ARR-Proxy Triangulation Math

Loaded by the `research-entity` skill when the entity is a private SaaS / subscription-revenue company that does not disclose audited ARR. Headcount + funding + Glassdoor band + marketplace install + traffic data → triangulated revenue estimate, with the math + assumptions explicit.

---

## §1 — Why this matters

Private companies routinely cite revenue figures that are **founder-self-reported single-source** (Latka interviews are the canonical example). External evaluators have no way to verify the figure unless they're under NDA. Triangulation math takes publicly-observable inputs and produces a defensible **range** that can either confirm the claimed number or flag a discrepancy.

This is how Big-4 commercial DD teams cross-validate vendor claims when audited financials aren't yet available — published in Bessemer's "Cloud 100" methodology, OpenView's "Expansion SaaS Benchmarks," and KeyBanc's "SaaS Survey."

---

## §2 — Methodology citations (verified, public)

| Source | What it provides | Free / paid | URL |
|---|---|---|---|
| **Bessemer Venture Partners "State of the Cloud"** | Annual report; ARR/FTE benchmarks, growth-rate cohorts, multiples | ✅ free PDF | [bvp.com/atlas](https://www.bvp.com/atlas) |
| **Bessemer Cloud Index (BVP Nasdaq Emerging Cloud)** | Real-time public-comp multiples | ✅ free | [cloudindex.bvp.com](https://cloudindex.bvp.com/) |
| **OpenView Expansion SaaS Benchmarks** | Headcount allocation, NRR, GRR by stage | ✅ free reports (legacy archive) | [openviewpartners.com/blog/saas-benchmarks](https://openviewpartners.com/blog/) |
| **KeyBanc Capital Markets SaaS Survey** | Annual survey; ARR/FTE, sales efficiency | ⚠️ summary free, full paywall | [keybanc.com](https://www.key.com/businesses-institutions/industry-expertise/keybanc-capital-markets.html) |
| **ICONIQ Growth quarterly reports** | Sales efficiency, magic number, cohort | ✅ free | [iconiq.com/growth/insights](https://www.iconiq.com/growth/insights) |
| **Sapphire Ventures benchmarks** | SaaS metrics by stage | ✅ free | [sapphireventures.com/blog](https://sapphireventures.com/blog) |
| **SaaS Capital benchmarks** | Annual private-SaaS benchmarks | ✅ free | [saas-capital.com](https://www.saas-capital.com/) |
| **Battery Ventures *State of the OpenCloud*** | OSS + cloud benchmarks | ✅ free | [battery.com/insights](https://www.battery.com/blog/category/research/) |

---

## §3 — The ARR-per-FTE method (primary triangulation)

### The formula

```
Estimated ARR = Headcount × Industry $/FTE benchmark
```

Adjusted by:
- Stage (seed = lower $/FTE, scale = higher)
- Sales-led vs PLG (sales-led has lower $/FTE due to sales-team weight)
- Vertical (vertical SaaS often higher; horizontal SaaS often lower)
- Geography (US headcount often higher $/FTE than global average)

### $/FTE benchmark ranges (industry — exact bands vary by report year/definition)

These ranges are synthesized from publicly-available industry benchmark reports (Bessemer State of the Cloud / OpenView Expansion SaaS Benchmarks / KeyBanc SaaS Survey / ICONIQ Growth / Sapphire / SaaS Capital). **Exact bands shift annually** as cohort medians evolve — always cite the source-year of any benchmark used. For this skill, these are **directional reference ranges** for triangulation:

| Stage / type | $/FTE directional range | Source-year reference |
|---|---|---|
| **Seed (pre-revenue / pre-product)** | < $80K | Earlier-stage benchmarks across reports |
| **Series A SaaS** | $80-180K / FTE | Cross-report range; verify with current-year Bessemer / OpenView |
| **Series B SaaS** | $130-250K / FTE | Cross-report range; verify with current-year benchmarks |
| **Series C+ SaaS (efficient)** | $180-300K / FTE | Cross-report range |
| **Top-quartile SaaS (scale)** | $250-450K / FTE | Bessemer Cloud 100-style benchmarks |
| **PLG-heavy (engineering-weighted)** | +10-25% premium vs same-stage sales-led | Cross-report observation |
| **Sales-led (sales-weighted)** | -10% to -20% vs PLG | Cross-report observation |
| **Vertical SaaS (specific verticals)** | +15-30% | Vertical-SaaS-specific reports vary widely |
| **Public SaaS median** | $200-400K / FTE | Bessemer Cloud Index public-comp data |

**Important caveat:** these are **directional industry benchmark ranges**, not exact published figures. Exact bands shift report-to-report and year-to-year. Always cite the **specific report-year** used (e.g., "Bessemer State of the Cloud 2024 cohort medians"). Use these for triangulation, not as authoritative single-source figures.

### Worked example

Vendor "Acme" claims:
- Founded 2018, Series B, raised $40M total
- LinkedIn shows ~85 employees
- Sales-led GTM
- Latka self-reports $14M ARR

Triangulation:
- Stage: Series B → $130-200K/FTE base
- Sales-led adjustment: -10% to -20% → $104-180K/FTE
- 85 employees × $104-180K = **$8.8M - $15.3M ARR estimated range**
- Latka claim ($14M) **survives validation** — falls within mid-to-upper of the range

If Latka claim were $30M instead → triangulation says max plausible is ~$15M → **flag in §16 Risks** as "claimed ARR ($30M) materially exceeds triangulated range ($8.8-15.3M)."

---

## §4 — Sales-rep-quota triangulation (sales-led specific)

### The formula

```
Estimated ARR = Number of quota-carrying reps × Average quota × Attainment rate

Where (industry directional ranges — verify with current Bridge Group / RepVue / Pavilion compensation surveys):
- Quota by tier:
  - SDR: $400-700K pipeline / year
  - AE (mid-market): $800K - $1.5M / year quota
  - AE (enterprise): $1.5M - $3M / year quota
  - AE (strategic / named accounts): $3M - $8M / year quota
- Attainment rate: 55-75% range (industry median historically ~67%, but varies by year + segment)
```

### Inputs (all from public sources)

- LinkedIn job board: count current open AE roles + currently-employed AEs (LinkedIn search "company:Acme title:AE")
- Job descriptions disclose quota: ~20% of public AE job postings include quota language; this gives at-tier evidence

### Quota benchmark sources (verify current-year data)

- **Bridge Group SaaS AE / Inside Sales Reports** — published industry-wide AE quota benchmarks → [bridgegroupinc.com](https://bridgegroupinc.com/) (subscription / report-purchase model)
- **RepVue compensation data** — AE quota + attainment by segment, real-time from anonymized rep-submitted data → [repvue.com](https://repvue.com/)
- **Pavilion (formerly Revenue Collective)** — peer-benchmark reports → [joinpavilion.com](https://www.joinpavilion.com/)
- **KeyBanc Capital Markets SaaS Survey** — annual; published attainment rates and quota distributions → [keybanc.com](https://www.key.com/businesses-institutions/industry-expertise/keybanc-capital-markets.html)
- **OpenView Benchmarks** (legacy archives, 2023 wind-down) — AE quota historical data → [openviewpartners.com](https://openviewpartners.com/)

**Caveat:** AE-quota and attainment are NOT primarily published by Bessemer (which focuses on top-line cohort metrics like ARR/FTE, NRR, magic-number, growth rate). Bridge Group / RepVue / Pavilion are the standard sources for quota-and-attainment specifics.

### Worked example

Vendor "Acme" has 12 mid-market AEs visible on LinkedIn:
- 12 × $1.0-1.2M (industry mid-market AE quota midpoint, per Bridge Group / RepVue ranges) × 60-70% attainment range = **~$7.2-10.1M ARR plausible**
- If founder claims $20M ARR → flag (claim is 2× upper bound of plausible range)

---

## §5 — Marketplace-install triangulation (PLG / marketplace-led)

For vendors with marketplace presence, see `marketplace-signals.md` §3 for the install-count → ARR conversion. Summary:

```
ARR (PLG) ≈ Active installations × Conversion-to-paid × ACV

Where conversion-to-paid:
- Atlassian Marketplace: ~10-15%
- Chrome Web Store freemium: ~2-5%
- HubSpot Marketplace: ~15-25%
- Mobile app freemium: ~2-5%
```

---

## §6 — Web-traffic-and-conversion triangulation

### The formula (rough; for top-of-funnel-driven SaaS)

```
ARR ≈ Monthly web visits × Lead-conversion-rate × Visitor-to-customer rate × ACV

Where:
- Lead conversion: 2-5% of visitors fill a form (industry median ~3%)
- Lead-to-customer: 5-15% of leads close
- ACV: depends on tier
```

### Free sources for web traffic

- **SimilarWeb free tier** — monthly visits estimate → [similarweb.com](https://www.similarweb.com/)
- **Semrush free tier** — organic + paid traffic → [semrush.com](https://www.semrush.com/)
- **Ahrefs free tier** — backlink + traffic → [ahrefs.com](https://ahrefs.com/)
- **Cloudflare Radar** — domain-level traffic data → [radar.cloudflare.com](https://radar.cloudflare.com/)

⚠️ **Caveat:** these tools estimate traffic; actual conversion rates vary 10× depending on funnel design. Use as sanity-check, not primary triangulation.

---

## §7 — Composite triangulation table (added to §1 Executive Summary or §16)

```markdown
### ARR triangulation (multi-method)

| Method | Estimated ARR | Method confidence |
|---|---|---|
| Headcount × $/FTE (Series B sales-led) | $8.8M - $15.3M | High |
| AE-quota × attainment | $9.6M | Medium |
| Marketplace install × conversion | $7M - $12M | Medium |
| Web-traffic × conversion | $5M - $20M | Low |
| **Triangulated band** | **$8M - $15M** | **High (multi-source)** |
| Founder-self-reported (Latka) | $14M | Single-source |
| **Verdict** | **Founder claim survives** | |
```

---

## §8 — Anti-patterns

- ❌ **Citing a single $/FTE figure as if it's law** — always cite the *range* (Series B = $130-200K/FTE, not "Series B = $164K/FTE").
- ❌ **Skipping stage / GTM adjustments** — sales-led vs. PLG materially changes $/FTE; failing to adjust biases the estimate.
- ❌ **Treating a triangulation match as proof of accuracy** — triangulation rules out implausible claims; it doesn't confirm exact numbers.
- ❌ **Producing a triangulation without disclosing inputs** — the value is in the input transparency. Always show the math.

---

## §9 — Workflow integration

**Step 4 — draft**: when entity has self-reported revenue figure (Latka, founder interview, etc.):
1. Pull public LinkedIn headcount → load into formula
2. Pull funding history → identify stage (Seed / A / B / C / Growth)
3. Pull GTM signal from job postings (sales-led if many AE roles; PLG if engineering-heavy)
4. Apply Bessemer/OpenView/KeyBanc benchmarks
5. Output the multi-method triangulation table in §1 or §16
6. Compare to founder-claimed figure
7. If founder claim is within ±50% of range → "survives validation"
8. If founder claim is >50% above max → flag in §16 Risks

---

## §10 — Related

- `marketplace-signals.md` — marketplace install counts
- `osint-public.md` — job-posting velocity
- `benchmarks.md` — broader industry benchmarks
- `lessons.md` — lesson on aggregator-derived headcount uncertainty
