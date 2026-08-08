# Primary-Source Hierarchy + Wayback Forensic Dating + Customer-Logo Verification

Loaded by the `research-entity` skill at Step 2 (source gathering) and Step 3 (cross-validation). Codifies the source-discipline lessons learned in the Aurasell/Reevo error pattern (lessons #41-45 in `lessons.md`): the model accepted secondary-outlet paraphrase as primary, missing facts that primary financial press had structured correctly.

This file enforces a **4-tier source hierarchy** (verified investigative-journalism standard) and adds two complementary verification disciplines: **Wayback forensic source-dating** (catch "the page edited history") and **customer-logo round-trip verification** (catch "logo wash" — vendors listing free-trial customers as references).

---

## §1 — Primary-source 4-tier hierarchy

### Methodology citation

The 4-tier hierarchy is grounded in three publicly-available standards:

- **Society of Professional Journalists (SPJ) Code of Ethics**: "Take responsibility for the accuracy of their work. Verify information before releasing it. Use original sources whenever possible." → [spj.org/ethicscode.asp](https://www.spj.org/ethicscode.asp)
- **AICPA AT-C 105: Concepts Common to All Attestation Engagements** — defines hierarchy of audit evidence, "obtained from sources independent of the responsible party" preferred. → [AICPA Attestation Standards](https://www.aicpa-cima.com/resources/download/aicpa-ssaes-currently-effective)
- **Reuters Handbook of Journalism**: "Wherever possible, we go directly to the primary source... Independent verification is the bedrock of accurate reporting." → [handbook.reuters.com](https://handbook.reuters.com/index.php?title=A_Brief_Guide_to_Standards,_Photoshop_and_Captions)
- **ICIJ Investigation Standards**: paragraphs on document-first, multi-source verification → [icij.org/about/our-impact](https://www.icij.org/about/)
- **Bellingcat Online Investigation Toolkit** — verification checklist → [bellingcat.com/resources/](https://www.bellingcat.com/resources/)

### The 4 tiers

```
TIER 1 — PRIMARY SOURCES (highest confidence)
  ├─ Filings / records / registers (legally compelled disclosure)
  ├─ Official press releases (with named dateline)
  ├─ Court records (PACER federal; CourtListener; UniCourt; state courts)
  └─ Direct disclosures (audited financials, S-1, 10-K, 10-Q, 8-K, DEF 14A)

TIER 2 — NAMED-BYLINE FINANCIAL PRESS (high confidence)
  ├─ Bloomberg (named reporter, fact-checked, primary-source-driven)
  ├─ Reuters / Reuters Wire (named bylines)
  ├─ Wall Street Journal / Dow Jones
  ├─ Financial Times
  ├─ TechCrunch / The Information / Axios Pro Rata (named bylines)
  └─ Trade press with named bylines (CNBC, CRN, etc.)

TIER 3 — STRUCTURED ANALYST DATABASES (medium confidence)
  ├─ Sacra (analyst-curated, methodology-disclosed)
  ├─ PitchBook (paid; structured investor / round records)
  ├─ Crunchbase (mostly user-submitted; verify vs. T1/T2)
  ├─ Tracxn (similar)
  ├─ Owler (mostly user-submitted)
  └─ Latka (founder-self-reported; never primary)

TIER 4 — AGGREGATOR / SECONDARY OUTLET PARAPHRASE (low confidence)
  ├─ Daily Company News-style aggregated digests
  ├─ "Top 10 X funded in Y" listicles
  ├─ Press-release-rewrite blogs (no named byline, paraphrasing wire)
  ├─ Founder-bio pages on aggregator sites
  └─ AI-summarized roundups
```

### Decision rules

| Situation | Rule |
|---|---|
| Source-tier conflict (T1 says X, T4 says Y) | **T1 wins** — record the conflict |
| Two T2 sources disagree | Find a T1 source to break the tie; if absent, label `single-source-T2` and quote both |
| Specific number cited only at T4 | **Soften to range or drop** — never publish from T4 alone |
| Lead investor stated only at T3+T4 | Require ≥1 T1/T2 source with named-partner attribution before publishing |
| HQ city stated only at T4 | **Press release dateline (T1) is canonical** — never publish HQ from a single T4 source |
| Bundled-announcement round structure ($Xm seed total) | **Search T2 for breakdown** before publishing — Bloomberg/TC typically have it |

### Tier-labeling discipline (Source-Tier Tag rule)

Every citation in §19 Sources must be tagged `[T1]` / `[T2]` / `[T3]` / `[T4]` (single uppercase T + tier number, in square brackets) so the reader sees the source-quality distribution at a glance:

```markdown
- [T1] [Acme Corp 10-K filing](https://sec.gov/...) — annual report
- [T2] [TechCrunch — Acme raises $30M Series B (Smith)](https://techcrunch.com/...)
- [T3] [Sacra Acme summary](https://sacra.com/...)
- [T4] [DailyCompanyNews — Acme funding roundup](https://...)  ← FORBIDDEN AS SOLE SOURCE
```

A **§23 dimension** (NEW v2.6) tracks source-tier composition: target ≥30% T1 + T2 for board-ready dossiers.

---

## §2 — Wayback Machine forensic source-dating

### Why this matters

When a dossier cites a current source ("per the company's `/about` page"), the underlying claim depends on what the page **says today**. But companies routinely edit their own history — tightening "founded 2011" to "founded 2010" to align with a funding-round narrative; removing customer logos who churned; rewriting product positioning. **A claim sourced to today's `/about` page may have been false 6 months ago.**

The Wayback Machine ([web.archive.org](https://web.archive.org/)) operated by the Internet Archive captures snapshots of public pages. Independent verification of "what the source said when the claim was made" is a verified investigative practice (Bellingcat handbook, ICIJ Panama Papers methodology, ProPublica's standard verification chain).

### Methodology citation

- **Internet Archive Wayback Machine** — [web.archive.org](https://web.archive.org/) — free, public, no API key
- **Wayback Availability API** — `https://archive.org/wayback/available?url=<URL>&timestamp=<YYYYMMDD>` — free, public
- **Wayback CDX Server API** — `https://web.archive.org/cdx/search/cdx?url=<URL>&output=json` — free, public
- **Bellingcat Online Investigations Toolkit** — Wayback verification chapter → [bellingcat.com/resources/](https://www.bellingcat.com/resources/)

### Forensic-dating protocol

For any claim that is **time-sensitive** — i.e., could plausibly have changed since the source was written — perform a Wayback check:

1. **Capture a current snapshot** (when sourcing the claim):
   ```bash
   # Submit current page to Wayback
   curl -s "https://web.archive.org/save/<URL>"
   ```

2. **Compare against historical snapshots** (when claim is challenged or aged):
   ```bash
   # Fetch list of snapshots
   curl -s "https://web.archive.org/cdx/search/cdx?url=<URL>&output=json&limit=20" | jq

   # Fetch a specific snapshot
   curl -s "https://web.archive.org/web/<TIMESTAMP>/<URL>"
   ```

3. **Document drift**:
   - If the page **today** says "founded 2010" but the **2024 snapshot** says "founded 2011," cite both: `[Company about page (current)](https://example.com/about) · [Wayback 2024-Q1 snapshot](https://web.archive.org/web/20240101000000*/example.com/about)`
   - In §16 Risks: flag the rewrite as a **history-edit pattern** — neutral signal but worth surfacing

### When to apply

| Claim type | Wayback verify? |
|---|---|
| Founding year (when claimed by entity) | ✅ always |
| Customer logo (especially churned-looking) | ✅ when customer is challenged |
| Pricing tier ("plan X costs $Y") | ✅ when historical pricing matters |
| Founder bio claims (career history) | ✅ when narrative is load-bearing |
| Headcount range ("X employees") | ✅ if claim is >12 months old |
| Product feature list | ✅ when first-mover claim made |
| Trust/security page (SOC 2 status) | ✅ when compliance is load-bearing |
| Press release content | ❌ press releases are stable (change = correction notice) |

### Anti-pattern

❌ **Citing a current page for a 5-year-old claim without Wayback validation.** The page today is not authoritative for what was true 5 years ago.

---

## §3 — Customer-logo round-trip verification

### Why this matters

Vendors routinely list logos on `/customers` pages that include:
- **Free-trial-only users** (technically a "customer" but never paid)
- **Pilot-only customers** that didn't convert
- **Logo-permission-only relationships** (vendor allowed to use logo for a brief period)
- **Acquisition-orphan customers** (the customer was acquired and the relationship died but logo remains)
- **Marketing-relationship-only customers** (one webinar appearance ≠ paying customer)

This is "logo wash" — a well-documented vendor practice flagged in Bain & BCG commercial-DD frameworks (industry general practice) and BCG's PE-DD frameworks. The diligence question: **is this customer publicly using or endorsing the product?** If yes, the relationship is real. If no, the logo is decorative.

### Round-trip verification protocol

For each customer logo on the entity's `/customers` page (or any logo cited in §9 Customer Base), perform **two-direction verification**:

**Direction A — entity → customer:**
- Entity's own page lists the customer ✅ (1 point)
- Entity has a published case study with the customer name ✅ (2 points)
- Entity has a recorded video / podcast with the customer's named executive ✅ (3 points)

**Direction B — customer → entity (the load-bearing direction):**
- Customer's own site mentions entity by name ✅ (3 points)
- Customer has a press release mentioning entity ✅ (3 points)
- Customer's executive(s) have publicly endorsed entity (LinkedIn / conference talks) ✅ (2 points)
- Customer's job postings mention the entity's product as required experience ✅ (2 points)
- Customer is publicly listed in a paid-tier marketplace (Salesforce AppExchange "Approved customer") ✅ (1 point)
- No mention found anywhere on customer's own digital footprint ❌ (-2 points)

**Composite scoring:**

| Total | Verdict | Action in dossier |
|---|---|---|
| ≥4 | **Verified customer** | Standard inclusion |
| 1-3 | **Light evidence** | Include but label `vendor-listed only` |
| 0 | **Logo only** | Include but label `logo-only — no public reciprocal evidence` |
| ≤-1 | **Logo wash flag** | Move to §16 Risks subsection "Customer-base verification gaps" |

### Search batch (Step 2 — source gathering)

For an entity with ≤30 named customers, run this in parallel during source gathering:

```bash
# For each customer, check both directions
for customer in "${customers[@]}"; do
  # Direction A: entity case study about customer
  tavily_search "<entity> <customer> case study"

  # Direction B: customer mentioning entity on its own site
  tavily_search "site:<customer-domain> <entity>"

  # Direction B (broader): customer's executive endorsements
  tavily_search "<customer-CEO/CTO-name> <entity>"
done
```

For an entity with ≥30 named customers, sample 10-15 customers across the size distribution (mix of small, mid-market, and named-large) and apply the protocol to that sample.

### Anti-patterns

- ❌ **Treating the customer's logo on the entity's site as evidence of an active relationship** — that is what's being verified, not the verification itself.
- ❌ **Counting one Reddit comment from a "former employee" as customer endorsement** — too noisy, not a corroborating signal.
- ❌ **Skipping verification when customer is "obviously real" (e.g., Coca-Cola)** — large-cap companies have many vendor relationships; logo-wash specifically targets named brands because they confer credibility regardless of contract size.

---

## §4 — Composability with existing competitor-verification.md

This file complements `competitor-verification.md` (v2.5) but applies broadly across the dossier — not just §10 competitor rows.

| Concern | File |
|---|---|
| Lead investor / HQ / round-structure for **competitor rows** in §10 | `competitor-verification.md` |
| **All claims** in dossier — primary-source hierarchy, Wayback dating | `source-hierarchy.md` (this file) |
| Customer logos — logo-wash detection across §9 | `source-hierarchy.md` (this file) §3 |
| Confidence-score impact | `confidence-scoring.md` — adds Source-Tier Composition dimension |

---

## §5 — When to load this file

Load `source-hierarchy.md` when:

- **Mandatory** at Step 2 (source gathering) for `--type=competitive|due-diligence|investment`
- **Mandatory** at Step 3 (cross-validation) for any claim with single-source attribution
- **Optional** for `--type=research|partnership` when sources are sparse
- When user asks "is this still accurate?" or "how recent is this?" (Wayback verification path)
- When user pushes back on a customer logo or testimonial (logo-wash verification path)

---

## §6 — Anti-patterns

- ❌ **Treating T3 (Crunchbase / Tracxn) as primary** — these are user-submitted aggregators with known accuracy gaps.
- ❌ **Bypassing T1 because it's "harder to find"** — SEC EDGAR, business registers, and court records are search-indexed and free.
- ❌ **Trusting a current page for historical claims** — Wayback is the only way to verify what a page said in the past.
- ❌ **Relying on entity-side customer-page logos as evidence** — verification requires customer-side reciprocal evidence.

---

## §7 — Related files

- `lessons.md` — lessons #41-45 codify the failure patterns this file prevents
- `competitor-verification.md` — narrower v2.5 protocol for §10 competitor rows
- `analytic-techniques.md` — Quality of Information Check (QIC) layer; this file feeds the QIC
- `source-rating.md` — Admiralty Code formal source-quality notation; this file's tier system maps to A1-F6
