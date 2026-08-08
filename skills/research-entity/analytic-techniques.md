# Structured Analytic Techniques (ACH + SATs + ICD 203)

Loaded by the `research-entity` skill at Step 4 (Draft) when `--type=due-diligence` OR `--type=investment` OR `--analytic-rigor=high` is set. Implements three intelligence-community standards: Analysis of Competing Hypotheses (Heuer/CIA), Structured Analytic Techniques (Devil's Advocate / Pre-mortem / Key Assumptions Check), and ICD 203 expressed-uncertainty discipline.

These techniques are the gold standard for high-stakes analytic products in the US Intelligence Community ([ICD 203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)) and have been adapted for private-sector M&A due-diligence by Big 4 consulting firms.

## Why this exists

A standard dossier risks **confirmation bias** — the analyst implicitly favors one narrative and selects evidence to support it. ACH and SATs counter this by:
1. Forcing enumeration of ALL plausible hypotheses (not just the favored one)
2. Evaluating each piece of evidence against EVERY hypothesis (matrix-style)
3. Aiming to **disprove** rather than confirm
4. Surfacing load-bearing assumptions explicitly so they can be stress-tested
5. Requiring per-claim uncertainty language, not just dossier-level confidence

## 1. Analysis of Competing Hypotheses (ACH)

Source: Heuer, *Psychology of Intelligence Analysis* (CIA, 1999, free PDF) — Chapter 8. Refined in Heuer & Pherson, *Structured Analytic Techniques for Intelligence Analysis* (2010 / 2014). Used by US Intelligence Community + cyber threat intelligence (SANS) + financial fraud investigations + private-sector strategic intelligence.

### Heuer's 8 ACH Steps (verbatim from Chapter 8 of *Psychology of Intelligence Analysis*)

The skill must execute all 8 steps when generating an ACH section — skipping steps degrades the technique to ad-hoc hypothesis generation:

1. **Hypothesis** — Identify the possible hypotheses to be considered. Use a group of analysts with different perspectives to brainstorm; this prevents the cognitive bias of locking in on one "likely" hypothesis early.

2. **Evidence** — List significant evidence and arguments for and against each hypothesis. Include assumptions, logical deductions, and absence-of-evidence (which is itself evidence in some hypotheses).

3. **Diagnostics (Matrix)** — Prepare a matrix with hypotheses across the top and evidence down the side. For each cell, mark Consistent (C) / Inconsistent (I) / Neutral (N). Some evidence has high "diagnosticity" (discriminates strongly between hypotheses); some has low diagnosticity (consistent with all hypotheses, doesn't help).

4. **Analysis** — Refine the matrix by considering one piece of evidence at a time and examining it AGAINST ALL HYPOTHESES (working ACROSS the matrix, row-by-row). This is the opposite of intuitive analysis (which works DOWN: one hypothesis at a time, all evidence). Working across is what counters confirmation bias.

5. **Refinement** — Identify gaps. Collect additional evidence needed to refute remaining hypotheses. Reconsider whether the evidence list is complete.

6. **Reevaluation** — Re-examine key assumptions and the few critical pieces of evidence that drive the analysis. Sensitivity analysis: how would the conclusion change if a single key piece of evidence were wrong?

7. **Conclusions** — Draw tentative conclusions about the **relative likelihood** of each hypothesis. Less consistency (more "I" marks) implies lower likelihood. Aim to ELIMINATE the least consistent hypotheses, not to prove the favored one. The conclusion is the SURVIVING hypothesis with the lowest disconfirmation count, NOT the hypothesis with the most "C" marks.

8. **Reporting** — Report all hypotheses with their relative likelihoods, the diagnostic evidence, and the milestones / indicators that would prompt re-evaluation. The transparency of the matrix is a key strength of ACH — the decision-maker can audit the analyst's logic.

### Why "disprove" beats "prove"

Heuer's central insight: human analysts (and LLMs) naturally seek confirming evidence for a favored hypothesis. ACH inverts this: the analyst's job is to FALSIFY hypotheses. The hypothesis that survives the most falsification attempts is the most defensible, regardless of how much "supporting" evidence exists for alternative hypotheses.

### Output template (insert as §17.X)

```markdown
### 17.X Analysis of Competing Hypotheses (ACH)

Per Heuer's ACH method — enumerate all plausible hypotheses about the entity's strategic state, then evaluate each piece of evidence against EVERY hypothesis. Aim to disprove (not confirm) hypotheses; the surviving hypothesis is the most-defensible interpretation.

#### Hypotheses (3-5, mutually exclusive where possible)

For an entity with claimed metrics (e.g. "$XM revenue, growth rate Y%, profitable"):

| H# | Hypothesis | Plain-English description |
|---|---|---|
| H1 | Founder claims accurate; entity is healthy | Revenue/growth/profitability roughly as claimed; aggregator data reflects reality |
| H2 | Founder claims inflated; entity is mediocre | Revenue 30-50% below claim; growth flat; profitable but at lower scale |
| H3 | Founder claims accurate; entity is contracting | Revenue at claim but YoY declining; previously larger; trending toward distress |
| H4 | Founder claims understated; entity is stronger than disclosed | Bootstrap entrepreneurs sometimes under-disclose to avoid attention; stronger position than aggregators show |
| H5 | Insufficient data for any of H1-H4 to be defensible | Public sources are too thin to choose between scenarios |

#### Evidence matrix

For each piece of evidence, mark whether it is **C** (consistent with), **I** (inconsistent with), **N** (neutral), or **NA** (not applicable) for each hypothesis. Aim to find evidence that DISPROVES hypotheses, not confirms them.

| Evidence | Source | H1 | H2 | H3 | H4 | H5 |
|---|---|:-:|:-:|:-:|:-:|:-:|
| 216 Capterra reviews @ 4.6/5 | Capterra | C | C | I | C | N |
| Single-source revenue ($16M Latka) | Latka | N | N | N | N | C |
| Aggregator employee count varies 85-500 | 5 aggregators | I | C | C | I | C |
| ISO 27001:2022 + ISO 9001:2015 | Trust page | C | C | I | C | N |
| No SOC 2 disclosed | Trust page | N | C | I | N | N |
| 15-year operating history | Press | C | C | I | C | N |
| 0 PACER court records | CourtListener | C | C | I | C | N |
| No layoffs found | layoffs.fyi | C | I | I | C | N |
| ... | ... | ... | ... | ... | ... | ... |

#### Disconfirmation count (the load-bearing metric)

| Hypothesis | "I" count (evidence inconsistent) | Surviving? |
|---|---:|---|
| H1: Healthy as claimed | 1 | ✅ Surviving (lowest disconfirm) |
| H2: Inflated; mediocre | 2 | ✅ Surviving |
| H3: Contracting | 6 | ❌ Largely disconfirmed |
| H4: Stronger than disclosed | 1 | ✅ Surviving |
| H5: Insufficient data | 0 (all neutral or consistent) | ✅ Always-surviving (cop-out) |

**Most-defensible interpretation**: Between H1, H2, and H4 (all with low disconfirmation count). H3 (contracting) is the least defensible given the evidence.

**Caveat**: H5 (insufficient data) always "survives" because evidence-based disconfirmation requires data; the absence of data cannot disprove the hypothesis "insufficient data." When H5 has the lowest disconfirm count, the dossier should explicitly recommend NDA-stage diligence rather than choosing among H1-H4.

#### What this technique surfaces

- **Confirmation bias resistance** — the analyst can no longer favor a single narrative; the matrix forces evaluation against alternatives
- **Evidence-disproportion** — evidence that "everyone agrees" doesn't help discriminate between hypotheses; the load-bearing evidence is the discriminating-evidence
- **Honest uncertainty** — when 3 hypotheses survive disconfirmation, the dossier should say so; pretending H1 "wins" by 1 vote is false precision
```

## 2. Structured Analytic Techniques (SATs)

Source: ICD 203 + CIA Tradecraft Primer (2009). Three techniques to apply per dossier:

### A. Devil's Advocate

For each major conclusion in §0 BLUF, generate the strongest counter-argument. The goal is not to refute the conclusion but to ensure the BLUF survives explicit challenge.

```markdown
#### Devil's Advocate — Counter-arguments to BLUF claims

| BLUF claim | Strongest counter-argument | Survives challenge? |
|---|---|---|
| "Financially-thin company" | "$2.25M raised + 15 years operating + claimed profitable = capital-efficient bootstrap; 'thin' framing is venture-bias" | ⚠️ Reframed to "capital-efficient bootstrap with funding-gap risk" |
| "<feature> is parity, not leadership" | "<entity> shipped <feature> 6-9 months after major peers — for a bootstrap, that is rapid; in <feature>-count terms <entity> is in top quartile of category" | ⚠️ Reframed to "fast-follower MCP, not first-mover" |
| "AI-native peers raised X× more" | "X× ratio assumes <entity> doesn't raise; if <entity> raises a $YM Series B in next 12mo, ratio collapses to Z× — and bootstrap entrepreneurs often raise late and well" | ✅ Stands; X× is current-state, not destiny |
```

### B. Pre-mortem

Imagine the dossier conclusion is wrong 18 months from now. Working backwards, what would have to be true?

```markdown
#### Pre-mortem — "Imagine this dossier is wrong in 18 months. Why?"

Generated: 2026-04-27
Pre-mortem date: 2027-10 (18 months forward)

Plausible failure modes:

1. **Single founder dependency materialized** — CEO health event, departure, or burnout in next 18mo. Today's dossier under-weighted the founder-concentration risk because the company is profitable. Watchlist signal: Glassdoor "CEO control" reviews tracked monthly.

2. **AI-native peer category-creation succeeded** — one of Aurasell/Day.ai/Reevo defined a new "AI-CRM" category that <entity> couldn't credibly enter. Watchlist: their Series B announcements + analyst-firm category coverage.

3. **MCP standard fragmented** — Anthropic, OpenAI, and Microsoft fork MCP into 3 incompatible variants; <entity>'s recent implementation becomes a stranded asset. Watchlist: MCP spec governance + Anthropic registry forks.

4. **the entity's content-platform audience plateaued** — the multi-million-view audience peaked and started declining; the content-moat thesis evaporated. Watchlist: monthly podcast download trends + new-contributor velocity.

5. **A SOC 2 exit-event** — a customer breach is publicly tied to absent SOC 2; US enterprise procurement freezes <entity>. Watchlist: §16.6 red-flag scan quarterly.

#### What we'd update in the dossier

Each failure mode maps to a §0 Watchlist signal — the pre-mortem isn't a prediction, it's an early-warning specification. Re-read this section quarterly.
```

### C. Key Assumptions Check

List 5-7 explicit load-bearing assumptions. For each, rate how stress-tested it is.

```markdown
#### Key Assumptions Check

| # | Assumption | Stress-test status | Confidence |
|---|---|---|---:|
| 1 | Founder ($16M) revenue claim is approximately correct (within ±30%) | Single-source; no audit | Low |
| 2 | "Profitable" claim is correct | Founder-stated only; no income statement | Low-Med |
| 3 | ISO 27001:2022 cert is current and valid | Trust-page-claimed; certificate not directly fetched | Med |
| 4 | The 98 FeaturedCustomers references are mostly current customers (not churned) | FeaturedCustomers maintains; could include past customers | Med |
| 5 | The named-investor-identity matter is benign (not fraud) | Could not be reconciled; could be data-entry error OR could be misrepresentation | Low-Med |
| 6 | <entity>'s MCP server is real (production, not press-release-only) | Press-release announcement; no customer case study | Med |
| 7 | AI-native peer cohort funding total (~$272.5M) is approximately correct | Multi-source aggregator data, internally cross-checked | High |

**Highest-risk assumption**: #1 (founder revenue claim). If it's off by >50%, the entire competitive picture changes. Recommended mitigation: customer-reference call to top-3 named customers to triangulate scale.
```

## 3. ICD 203 Expressed-Uncertainty Discipline

Source: [Intelligence Community Directive 203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf) (Analytic Standards), 2007 / revised 2015 / revised 2024.

### The 5 Analytic Standards (verbatim from ICD 203)

All IC analytic products must implement and exhibit:

1. **Objective**
2. **Independent of political consideration**
3. **Timely**
4. **Based on all available sources of intelligence information**
5. **Implements analytic tradecraft standards** (which itself contains 9 sub-standards, see below)

### The 9 Analytic Tradecraft sub-standards within Standard #5 (verbatim from ICD 203)

5(a). **Properly describes quality and credibility of underlying sources, data, and methodologies** — implemented in this skill via source-labeling taxonomy + Admiralty Code (`source-rating.md`)

5(b). **Properly expresses and explains uncertainties associated with major analytic judgments** — implemented in this skill via the WEP table below + Analytic Confidence levels

5(c). **Properly distinguishes between underlying intelligence information and analysts' assumptions and judgments** — implemented in this skill via §0 framework disclaimer + Key Assumptions Check

5(d). **Incorporates analysis of alternatives** — implemented in this skill via ACH (Section 1 above)

5(e). **Demonstrates customer relevance and addresses implications** — implemented in this skill via §0 Strategic Response Playbook + audience-mapping

5(f). **Uses clear and logical argumentation** — implemented in this skill via §17 Strategic Analysis decision-tree + scoring framework

5(g). **Explains change to or consistency of analytic judgments** — implemented in this skill via comparison-mode (`comparison-mode.md`) + freshness-decay (`stale-detection.md`)

5(h). **Makes accurate judgments and assessments** — implemented in this skill via hallucination audit + cross-validation pass + multi-source corroboration

5(i). **Incorporates effective visual information where appropriate** — implemented in this skill via portrait mermaid diagrams (`mermaid-validation.md`)

### Two distinct dimensions to express (per ICD 203)

ICD 203 mandates expressing TWO independent things, not one:

#### A. Words of Estimative Probability (WEP) — likelihood that the judgment is correct

Verbatim from ICD 203 Annex A:

| Term | Probability range | Notes |
|---|---|---|
| **almost no chance** / remote | **01–05%** | |
| **very unlikely** / highly improbable | **05–20%** | "high" sometimes substituted for "very" |
| **unlikely** / improbable | **20–45%** | |
| **roughly even chance** / roughly even odds | **45–55%** | |
| **likely** / probable / probably | **55–80%** | |
| **very likely** / highly probable | **80–95%** | "high" sometimes substituted for "very" |
| **almost certain(ly)** / nearly certain | **95–99%** | |

**Critical**: these ranges are NOT overlapping in the official ICD 203 table. The boundaries are exact (05%, 20%, 45%, 55%, 80%, 95%). Earlier versions of this file had incorrect ranges (40-55% / 20-40% / "highly likely") — corrected to the official ICD 203 specification.

#### B. Analytic Confidence — analyst's assessment of underlying source quality (separate dimension)

| Level | Definition (verbatim from ICD 203) |
|---|---|
| **High Confidence** | Judgments rely on "high-quality information from multiple sources, most or all of which are considered trustworthy, with minimal to no conflict among sources" |
| **Moderate Confidence** | Information is "credibly sourced and interpreted to be plausible but is not of sufficient quality or corroboration to warrant a higher level of confidence" |
| **Low Confidence** | Source credibility is "uncertain — that is, the source information is scant, questionable, fragmented, or poorly corroborated" |

**ICD 203 explicitly notes**: "high confidence does not imply that the assessment is a fact or a certainty; there is always a chance that an assessment might be wrong."

### Application — both dimensions together

Every major analytic judgment should express BOTH:

```
"<entity> will likely (55-80%) maintain its mid-market CRM position over the next 18 months
[low confidence — assessment relies on single-source revenue claims (Latka)
and aggregator-derived employee counts that vary 85–500]."
```

Replace vague analytic phrases with the standard set:

| ❌ Vague | ✅ ICD 203 |
|---|---|
| "<entity> will probably maintain its market position" | "<entity> will likely maintain its market position (likely = 55-80% probability)" |
| "Could go either way" | "Roughly even chance" |
| "Significant risk" | Specify: "very likely / likely / etc." + analytic confidence |
| "Some indication" | Always pair indicator with uncertainty: "Some indication suggests... [very unlikely / unlikely / likely]" |
| "It is possible that" | Replace with "very unlikely / unlikely / roughly even chance" |
| "We assess that" | Replace with "we assess [WEP-term] [analytic-confidence-level]" |
| "Highly likely" (informal use) | "Very likely" (canonical ICD 203) — note: "high" is an accepted substitute for "very" but the canonical form is "very" |

### Where to apply

- **§0 BLUF** — every forward-looking claim
- **§16 Risks** — every risk severity assessment
- **§17 Strategic Analysis** — every recommendation
- **§21 Final Assessment** — the closing 3-paragraph synthesis

### Where NOT to apply

- Verbatim quotes (preserve original wording)
- Factual claims with citations (the citation IS the confidence — adding "likely" is wrong)
- Numeric facts (a number is what it is; don't say "likely $16M" — say "$16M [`single-source`]")

## 4. Remaining CIA Structured Analytic Techniques (4)

The CIA *Tradecraft Primer* (2009) lists ~15 SATs. We've already implemented ACH (Section 1) and 3 SATs (Devil's Advocate / Pre-mortem / Key Assumptions Check, Section 2). The 4 remaining high-value SATs:

### 4A. Quality of Information Check (QIC)

A formal procedure for evaluating each cited source on 3 dimensions: accuracy, reliability, and completeness. More structured than our ad-hoc source labels (`single-source`/`vendor-claimed`); complements (does not replace) Admiralty Code (`source-rating.md`).

#### Procedure

For each source cited in the dossier, answer 3 yes/no questions:

1. **Accuracy** — Has this source been right in the past on similar topics?
2. **Reliability** — Is this source providing direct primary information, or interpreting other sources?
3. **Completeness** — Does this source have access to all the information it would need to be authoritative on this topic?

#### Output template (insert as §16.X for `--analytic-rigor=high`)

```markdown
### 16.X Quality of Information Check (QIC)

Per CIA Tradecraft Primer — formal QIC for the load-bearing sources.

| Source | Accuracy (track record) | Reliability (primary vs. interpretive) | Completeness (full access?) | Weighted assessment |
|---|---|---|---|---|
| Latka revenue claim | Mixed (founder-interview platform; founders self-report) | Interpretive (republishes founder claim) | Incomplete (no audit access) | LOW — single-dimension self-report |
| <entity> Trust page (ISO 27001 claim) | Generally reliable for vendor-controlled facts | Primary (vendor's own claim) | Complete on what they choose to disclose | MODERATE — primary but self-interested |
| Austrian Firmenbuch (FN 126157a) | High (legal register) | Primary (official source) | Complete on what's required to be filed | HIGH — register-grade |
| Reddit r/sales discussion | Variable | Interpretive | Incomplete (anonymous, fragmentary) | LOW |
| ... | ... | ... | ... | ... |

**Composite QIC for the dossier**: ~__% of citations rated MODERATE+; ~__% rated HIGH; ~__% rated LOW (mostly aggregator + founder-self-report).

**QIC vs. Admiralty Code**: QIC asks the analyst's QUALITATIVE judgment per source; Admiralty Code provides a STANDARDIZED rating. Both are useful; QIC catches things the Admiralty Code misses (e.g., a B-rated source with an outdated viewpoint).
```

### 4B. Indicators / Signposts (formal SAT)

The §0 Watchlist already identifies signals to monitor; the formal Indicators SAT goes deeper by:
1. Tying each indicator to a specific HYPOTHESIS or scenario
2. Specifying what observation would CONFIRM vs. DISCONFIRM the hypothesis
3. Setting an OBSERVATION CADENCE (how often to check)

#### Output template (insert as §0.X — extends Watchlist)

```markdown
### 0.X Indicators / Signposts (Formal SAT)

Per CIA Tradecraft Primer Indicators methodology — each indicator is tied to a specific hypothesis with confirm/disconfirm criteria.

| Hypothesis | Indicator | Confirm signal (within 12 mo) | Disconfirm signal | Observation cadence | Where to watch |
|---|---|---|---|---|---|
| H1: <entity> maintains mid-market position | Customer logo continuity | 95%+ of named customers still on /customers page in 12 mo | >10% logo turnover indicates churn | Monthly | <entity>/customers + Wayback Machine |
| H1 | G2 / Capterra rating stability | Rating stays 4.5-4.7 | Rating drops below 4.3 | Quarterly | G2 + Capterra |
| H2: <entity> gets acquired by 2027 | M&A rumor activity | Tier-1 press (TC / The Information) reports rumors | Founder publicly denies M&A | Continuous | TechCrunch, The Information, BizJournal |
| H3: AI-native peer category-creation succeeds | Analyst firm category coverage | Gartner / Forrester names "AI-CRM" as distinct category from "CRM" | Analyst firms collapse "AI-CRM" back into "CRM" Magic Quadrant | Annually (Gartner cadence) | Gartner.com + Forrester.com |
| H4: MCP standard fragments | Anthropic / OpenAI / Microsoft fork MCP | Public spec divergence (different schemas) | Convergence to single MCP-2.0 standard | Quarterly | mcp.so registry + GitHub MCP repos |

**Critical**: Indicators must be FALSIFIABLE and OBSERVABLE in advance — not retrospective hindsight markers.
```

### 4C. High Impact / Low Probability (HILP) Analysis

For tail risks and Black Swan events that point-estimate forecasting systematically misses. Particularly load-bearing for fintech, govtech, deeptech, and any entity with regulatory exposure.

#### Procedure

1. Brainstorm 3-7 events with **probability ≤ 10% but impact rated HIGH** (would materially change the strategic conclusion)
2. For each, articulate the chain of events that would lead to the outcome
3. Identify the EARLIEST observable indicator of that chain
4. Recommend a contingency action

#### Output template (insert as §16.X — supplements §16.6 Red-Flag Scan)

```markdown
### 16.X High Impact / Low Probability (HILP) Tail Risks

Per CIA Tradecraft Primer HILP — events with low probability + high impact that point-forecasts miss.

| HILP event | Probability (ICD 203) | Impact | Earliest indicator | Contingency action |
|---|---|---|---|---|
| Founder health event / sudden departure | very unlikely (5-20%) | Critical (single-founder dependency; succession planning unclear publicly) | Glassdoor reviews mentioning leadership-transition language; LinkedIn role-change events | Add to monthly watchlist; CXO-departure pattern in `risk-scan.md` |
| AI training-data class-action lawsuit implicates the entity's AI product by extension | unlikely (20-45%) | High (forces mid-flight model migration) | OpenAI lawsuit settlement terms; downstream-vendor disclosure requirements | Verify <entity>'s contractual indemnification with OpenAI |
| EU AI Act enforcement action at the GPAI-deployer level | very unlikely (5-20%) | High (compliance overhaul cost > <entity>'s annual cash flow) | Initial GPAI enforcement actions against larger vendors (Microsoft / Google) | Track Annex VIII compliance requirements |
| Choice Hotels Asia-Pac (anchor customer) churn | unlikely (20-45%) | Med-High (case-study removal cascade) | Wayback Machine: Choice Hotels logo removal from /customers | Monthly Wayback check on customers page |
| US trade restrictions on the entity's engineering region | almost no chance (1-5%) | High (operational disruption) | EU-US trade tensions; Slovakia-specific sanctions discussion | Geographic diversification of engineering |

**Why HILP matters**: most strategy work focuses on the 80% scenario; HILP forces the analyst to confront the 1-10% scenarios that would invalidate the central thesis. Per Taleb's *Black Swan*: tail-risk events drive most variance in long-run outcomes.
```

### 4D. What If? Analysis

Counterfactual reasoning — "what if assumption X were wrong?" Forces the analyst to confront the dossier's load-bearing assumptions directly.

#### Procedure

Pick 3-5 of the most load-bearing assumptions (from Key Assumptions Check, Section 2). For each, ask:
- "What if this assumption is FALSE?"
- "What would the dossier conclusion change to?"
- "What's the EARLIEST observable signal that this assumption is failing?"

#### Output template (insert as §17.Y — supplements §17 Strategic Analysis)

```markdown
### 17.Y What If? Analysis (Counterfactuals)

Per CIA Tradecraft Primer What If? Analysis — explicit counterfactual reasoning on the load-bearing assumptions.

| Load-bearing assumption | What if FALSE? | Conclusion changes to | Earliest signal |
|---|---|---|---|
| <entity>'s reported revenue claim is approximately accurate (±30%) | If actual revenue is $5-8M (50% overstatement) | Entire valuation cascades down; PE roll-up at $30-60M becomes overpriced; partnership preferred to acquisition | Customer-reference call sample sizes (per `expert-calls.md`) suggest much smaller scale than claimed |
| ISO 27001:2022 certification is current and valid | If certificate has lapsed or was misrepresented | Entire compliance posture collapses; US enterprise becomes inaccessible; SOC 2 absence becomes critical instead of just procurement-stage | Trust page certificate not visible; ISO registrar lookup fails |
| The 98 FeaturedCustomers references are current | If 30%+ are churned former customers | Customer base is much smaller than logo wall implies; churn rate is hidden | Wayback Machine: customers page churn rate >10%/yr |
| The named investor is a real institutional investor | If this is data-entry fraud or shell entity | Cap-table is not what it appears; corporate governance concerns escalate | Direct investor outreach fails; portfolio-page check returns null |
| AI-native peer category-creation succeeds (analyst firms recognize "AI-CRM") | If analyst firms keep "AI-CRM" inside the existing CRM Magic Quadrant | AI-native peer threat is overstated; <entity>'s mid-market position is more defensible than the dossier implies | Gartner 2027 SFA Magic Quadrant doesn't add AI-native peers |

**Counterfactual robustness check**: A dossier conclusion is ROBUST if the answer to most "what if false?" questions is "conclusion mostly stands". A FRAGILE conclusion is one where any single assumption-failure invalidates the recommendation.
```

## Composability with existing skill features

| Existing feature | Interaction with this file |
|---|---|
| §17 Decision-tree | ACH supplements (does not replace) the decision tree; both can coexist |
| §23 Confidence-scoring | ACH and SATs do NOT change the composite score; they add a "tradecraft rigor" qualitative note |
| Hallucination audit | Hallucination audit checks whether claims are supported; ACH/SATs check whether the SYNTHESIS is defensible — different layers |
| `--validation=max` | When set, the ACH section becomes mandatory (not just on `--type=due-diligence`) |

## When to load this file

- `--type=due-diligence` (always)
- `--type=investment` (always)
- `--analytic-rigor=high` flag is set
- User asks "what would make this dossier wrong?" / "have you considered alternatives?" / "how sure are you?"
- The dossier is destined for an audience trained in intelligence-community methods (former CIA / military / regulators / law-enforcement-adjacent)

## Anti-patterns

- ❌ ACH with only 1-2 hypotheses — defeats the purpose; need 3-5
- ❌ ACH where every cell is "C" (consistent) — means evidence isn't discriminating; revisit the hypotheses
- ❌ Pre-mortem that lists implausible failure modes — focus on plausible (5-15% probability) failures, not 1% tail risks
- ❌ Key Assumptions list with <5 entries — load-bearing assumptions are typically 5-7; less suggests under-examination
- ❌ Using ICD 203 expressed-uncertainty terms incorrectly — "almost certainly" is 95-99%, not "I'm pretty sure"; precision matters

---

## Section 5 — Tetlock superforecaster calibration (NEW v2.6)

### Why this matters

ICD 203's expressed-uncertainty is a 7-point qualitative scale (almost certainly / very likely / likely / roughly even chance / unlikely / very unlikely / almost no chance). It's verifiable in retrospect ("the analyst said 'likely' and the event happened") but not **calibrated** — there's no accountability for an analyst who says "likely" 100 times and is right 20% of the time.

Philip Tetlock and Barbara Mellers developed the calibration discipline in the **IARPA ACE program** (Aggregative Contingent Estimation, 2011-2015) and the subsequent **Good Judgment Project**. Their core finding: trained forecasters using explicit probabilities + Brier-score self-tracking outperform CIA analysts using qualitative language by ~30%.

### Verified methodology citations

- **Philip Tetlock & Dan Gardner**, *Superforecasting: The Art and Science of Prediction* (Crown, 2015) — book, paywalled but methodology is in public papers
- **Good Judgment Project (GJP) papers** — public, peer-reviewed → [goodjudgment.com/research](https://goodjudgment.com/research/)
- **Mellers, Stone, Atanasov et al.** "The psychology of intelligence analysis" — public IARPA papers
- **IARPA ACE program documentation** → [iarpa.gov/research-programs/ace](https://www.iarpa.gov/research-programs/ace)
- **Glenn Brier**, "Verification of Forecasts Expressed in Terms of Probability" (*Monthly Weather Review*, 1950) — origin of Brier score; public via AMS journals
- **Open Philanthropy calibration training** — [openphilanthropy.org](https://www.openphilanthropy.org/) — free, open-source

### The Brier score

For a forecast of probability `p` on an event that occurs (1) or doesn't (0):

```
Brier(p, outcome) = (p - outcome)^2

Examples:
- Forecast 0.9 on event that occurs: (0.9 - 1)^2 = 0.01 (excellent)
- Forecast 0.5 on event:               (0.5 - 1)^2 = 0.25 OR (0.5 - 0)^2 = 0.25 (no information)
- Forecast 0.1 on event that occurs:   (0.1 - 1)^2 = 0.81 (terrible)

Aggregate Brier = average across many forecasts.
- Random forecaster (always 0.5): ~0.25 (mathematical property)
- Tetlock superforecasters (top 2%): ~0.15-0.20 (per GJP papers, Mellers et al.)
- Uncalibrated qualitative forecasters (control group): ~0.25-0.30 (per GJP comparison data; not a single published "CIA Brier" figure)
```

### How to apply in dossiers

For every forward-looking judgment in §0 BLUF, §16 Risks, §17 Strategic Analysis, §21 Final Assessment:

1. **Pair the ICD 203 qualitative term** with an **explicit point probability** (or narrow range that falls within the term's defined range):
   ```
   "AI-native peer category creation will succeed by H2 2027" → very likely (78%)
   ```

2. **Sign off the prediction** with a forecast date so post-event scoring is possible:
   ```
   "Forecast as of 2026-04-27: 78% probability that competitor X reaches $50M ARR by H2 2027"
   ```

3. **Track aggregate Brier** in §23.X if the dossier is part of a series (e.g., quarterly refreshes).

### Calibration table template (added to §17.X for `--type=investment` or `--analytic-rigor=high`)

```markdown
### 17.X Quantitative Forecast Calibration (Tetlock-style)

| Forecast | ICD 203 term | Point probability | Resolution date | Resolution criterion | Status (next refresh) |
|---|---|---|---|---|---|
| AI-native peer reaches $50M ARR by Dec 2027 | very likely | 78% | 2027-12-31 | Public ARR disclosure ≥$50M | Pending |
| Entity raises Series C by Q3 2027 | roughly even chance | 45% | 2027-09-30 | Form D filing OR press release | Pending |
| Entity loses key customer (top-3) by H1 2027 | unlikely | 18% | 2027-06-30 | Public reference removal OR earnings call disclosure | Pending |

**Aggregate Brier (last 4 quarters):** [N/A — first cycle / 0.18 / etc.]
```

### Mapping ICD 203 ↔ Tetlock probability

| ICD 203 term | ICD 203 probability range | Tetlock-compatible point estimates |
|---|---|---|
| almost certainly | 95-99% | 95, 97, 99 |
| very likely | 75-85% | 75, 80, 85 |
| likely | 55-75% | 55, 60, 65, 70, 75 |
| roughly even chance | 45-55% | 45, 50, 55 |
| unlikely | 20-45% | 20, 25, 30, 35, 40, 45 |
| very unlikely | 5-20% | 5, 10, 15, 20 |
| almost no chance | 1-5% | 1, 3, 5 |

### Anti-patterns

- ❌ Using ICD 203 qualitative + point probability that contradicts (e.g., "very likely (35%)") — point must fall within range
- ❌ Failing to specify a resolution date — without a deadline, the forecast is unfalsifiable
- ❌ Forecasting on un-resolvable events ("entity will be successful") — must be falsifiable by an observable
- ❌ Treating Brier score in isolation — score must include the entire forecast portfolio, not cherry-picked successes

---

## Section 6 — Negative-space SAT — "the dog that didn't bark" (NEW v2.6)

### Why this matters

A dossier captures what an entity *does have*. The negative-space SAT asks: **what should be there but isn't?** Absence of expected signals is itself a signal — and one the LLM tends to miss because the model writes about what it found, not what it didn't find.

### Verified methodology citations

- **Richards Heuer**, *Psychology of Intelligence Analysis* (CIA, 1999, declassified) — Chapter 4 "Strategies for Analytical Judgment" → free PDF on [cia.gov](https://www.cia.gov/resources/csi/static/9a5f1162fd0932c29bfed1c030edf4ae/Pyschology-of-Intelligence-Analysis.pdf)
- **CIA Tradecraft Primer** (declassified 2009) — Section "Inconsistency Indicators" → free PDF on [cia.gov](https://www.cia.gov/resources/csi/static/955180a45afe3f5013772c313b16face/Tradecraft-Primer-apr09.pdf)
- **Pherson & Heuer**, *Structured Analytic Techniques for Intelligence Analysis* (CQ Press, 2014) — book, paywalled, but the SAT is in declassified Heuer above
- **Sherlock Holmes**, "The Adventure of Silver Blaze" (Conan Doyle, 1892) — origin of "the dog that didn't bark" as forensic technique

### Standard absence-checklist (added to §16.X Risk Scan)

For any entity, scan for missing signals that would normally be present in a healthy or reputable entity. Each missing signal is a soft flag; multiple missing signals together compound to a strong flag.

```markdown
### 16.X Negative-Space Scan ("the dog that didn't bark")

| Expected signal | Present? | Significance | Severity |
|---|---|---|---|
| Public engineering blog | ❌ | Suggests engineering team lacks public voice / talent-attraction motion | Soft flag |
| security.txt at /.well-known/ | ❌ | No standardized security-disclosure path; unusual for serious SaaS | Soft flag |
| Public status page | ❌ | No transparent uptime; unusual for paid SaaS | Soft flag |
| SOC 2 Type II disclosure | ❌ | Compliance gap for US-enterprise market | Hard flag (if US-enterprise targeted) |
| Public roadmap | ❌ | Customer-facing transparency missing | Soft flag |
| Trust Center (Drata/Vanta/SafeBase) | ❌ | Compliance posture is self-published only | Soft flag |
| Audited financials | ❌ | Expected for Series B+ / pre-IPO | Hard flag at later stages |
| RSS feed / press archive | ❌ | Press history is fragmented | Soft flag |
| Open API / developer docs | ❌ | No developer ecosystem | Domain-specific |
| GitHub presence | ❌ | No OSS contribution, no public engineering | Domain-specific |
| Conference speaker history | ❌ | No industry-thought-leadership | Soft flag for SaaS leaders |
| Glassdoor / Comparably presence | ❌ | Either too small to be reviewed OR actively suppressed | Soft flag |
| Customer references with case studies | ❌ | Logo wash risk (cf. `source-hierarchy.md` §3) | Hard flag if logos exist without studies |
| Wayback snapshots prior to 2023 | ❌ | Domain young; verify founding year claim | Soft flag |
| Founders' LinkedIn profiles complete | ❌ | Founders may be private OR profile-suppressing | Soft flag |
| Press release wire-distribution | ✅ but no earned coverage | PR-driven not market-driven | Soft flag (cf. `press-analysis.md` §1) |
| ... (vertical-specific entries) | ... | ... | ... |
```

### Vertical-specific absence checklists

| Vertical | Add these signals |
|---|---|
| `healthcare` | HIPAA-compliance disclosure, BAA template availability, HITRUST cert, patient-data DPA |
| `fintech` | PCI DSS disclosure, banking-regulator engagement (FDIC/OCC), AML/KYC disclosures, Form ADV (if RIA) |
| `govtech` | FedRAMP marketplace listing, StateRAMP, GSA Schedule, Cage Code |
| `edtech` | FERPA disclosure, COPPA compliance (if K-12), state DPA templates |
| `legaltech` | ABA Formal Opinion compliance, ABA TECHSHOW history, state bar association affiliations |
| `consumer` | Privacy Center, app-store ratings (vs. competitors), DMCA takedown handling |
| `devtools` | Open-source contributions, GitHub stars trajectory, Stack Overflow tag growth, RFC participation |

### Anti-patterns

- ❌ Cataloging every conceivable missing signal — focus on **expected** for the entity's type/stage/vertical
- ❌ Treating one missing signal as a verdict — multiple missing signals compound; one alone is at most "soft flag"
- ❌ Omitting the negative-space scan because the entity "looked clean" — the scan is precisely for entities that look clean

---

## Section 7 — ICD 206 — Sourcing Requirements (NEW v2.6)

### Why this matters

ICD 203 (Analytic Standards) governs *how* judgments are framed. **ICD 206 (Sourcing Requirements)** is the IC standard for *how sources are cited and characterized* — it's the source-discipline counterpart to the analytic-discipline of ICD 203.

Most professional intelligence products comply with both. Our skill has been ICD 203-compliant since v2.2 but only partially ICD 206-compliant. This section adds the missing source-citation requirements.

### Verified methodology citation

- **ICD 206: Sourcing Requirements for Disseminated Analytic Products** (Office of the Director of National Intelligence, 2007, updated periodically) — [dni.gov ICD index](https://www.dni.gov/index.php/what-we-do/ic-policies-reports/intelligence-community-directives) — public
- **Companion to ICD 203** → [ICD 203 PDF](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)

### Core ICD 206 requirements (mapped to skill features)

| ICD 206 requirement | Our skill's implementation |
|---|---|
| **Source descriptions sufficient to convey reliability + access** | Already partially via Admiralty Code (`source-rating.md`). v2.6 adds explicit T1-T4 tier labels (`source-hierarchy.md` §1) |
| **Origin and applicability of information** | Already done via inline citation + dateline labels |
| **Classification distinctions** | N/A for our public-source-only context (no classified material) |
| **Strengths and limitations of evidence** | Done via `single-source` / `vendor-claimed` / `founder-self-reported` labels (existing) |
| **Source-of-source disclosure** | NEW v2.6 — when citing an aggregator that cites a primary source, label both: e.g., `[T3] Sacra summary citing → [T2] Bloomberg breakdown` |
| **Continuous source-update tracking** | Partially done via `stale-detection.md`; v2.6 adds source-of-record date labels |

### ICD 206-compliant citation format

For high-rigor dossiers (`--type=due-diligence` AND `--analytic-rigor=high`), use ICD 206-compliant citation format:

```markdown
[T2] Bloomberg — "Reevo raises $80M from Khosla, Kleiner" (Smith, 2025-11-05) — `direct-named-byline` · [archive](https://web.archive.org/...)
```

Components:
- `[T2]` — source tier (this skill's hierarchy + Admiralty)
- Outlet name + article title
- `(Author, Date)` — author + publication date
- `direct-named-byline` — origin-and-access label
- `[archive]` — Wayback verification link (cf. `source-hierarchy.md` §2)

### Anti-patterns

- ❌ Citing aggregators without disclosing their downstream source ("per Crunchbase" without noting Crunchbase's own source)
- ❌ Treating multiple aggregators citing the same primary as multiple corroboration (it's all the same single source)
- ❌ Failing to tag source-of-record date (current page says X but Wayback shows X was added in 2025-Q4 means the claim's age is Q4-2025, not "current")
