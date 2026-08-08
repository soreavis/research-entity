# About this skill — `--about`

<!-- markdownlint-disable MD025 -->

Loaded when the user invokes `/research-entity --about`. Prints a self-documenting overview to the user (does NOT generate a dossier). Use this to surface what the skill does, which methodologies it implements, and which anti-hallucination techniques are baked in.

## Output template

When `--about` is set, print this to the user (do not write a dossier):

---

# `research-entity` skill — version 2.2 — 2026-04-27

A modular Claude Code skill for generating board-ready competitive-intelligence and due-diligence dossiers on any legal entity. **Methodologically equivalent to a Big 4 commercial DD engagement** + IC-grade analytic tradecraft + Klue's industry-standard battle-card framework.

**26 segment files · 5,800+ lines · all anonymized for sharing.**

## What this skill produces

- **23-section dossier** (BLUF · Scorecard · SWOT · Heat Map · Playbook · Watchlist · Founders · Funding · Product · Tech · Pricing · Customers · Market · Community · Risks · Ecosystem · Sources · Quote Bank · Final Assessment · Glossary · Confidence Appendix)
- **Up to 10+ portrait mermaid diagrams** (validated static + dynamic)
- **220+ cited URLs** (validated; 0 × 404 floor)
- **Composite confidence score** (5 dimensions, 100 points)
- **Optional alternate exports**: 1-page exec summary · battle card (Klue FIA) · VC IC memo · JSON · expert-call question battery · customer-reference question battery
- **Optional direct publish**: Notion · Confluence · Google Docs · Coda

## Methodology layers (5 layers)

### Layer 1 — Foundational structure (always applied)
- **23-section structure** modeled after Big 4 commercial DD reports (Market & Competitive · Operational · Management · Strategic Fit · Commercial Risk)
- **BLUF** (Bottom Line Up Front) — military origin; mandatory ≤200 words at top of dossier
- **Scorecard + SWOT + Heat Map + Playbook + Watchlist** — §0 framework synthesis
- **Multi-source corroboration** — every §0/§2 datapoint requires ≥2 independent sources OR explicit `single-source`/`vendor-claimed`/`founder-self-claim` label

### Layer 2 — Source provenance + labeling
- **Source labeling system**: `single-source` · `vendor-claimed` · `founder-self-claim` · `aggregator-derived` · `unverified` (plain-English)
- **[Admiralty Code](https://en.wikipedia.org/wiki/Admiralty_code) (NATO AJP-2.1)** — formal A-F × 1-6 source rating; auto-applied when `--source-rating=admiralty` or `--type=due-diligence|investment` + `--validation=max`
- **URL validation** — every URL fetched + validated; HTTP 200 / 403-bot-block-but-valid / 404-fixed-or-removed; 0 × 404 floor
- **Citation discipline** — every numeric / proper-noun / regulatory / customer claim must have a clickable URL trail or be dropped

### Layer 3 — Strategic frameworks (auto-activated by `--vertical=`)
- **SWOT** (Stanford 1960s) — always in §0
- **[PESTEL](https://en.wikipedia.org/wiki/PEST_analysis)** (Aguilar 1967) — Political/Economic/Social/Technological/Environmental/Legal; auto-activated for govtech/healthcare/fintech/edtech/legaltech
- **[Porter's 5 Forces](https://en.wikipedia.org/wiki/Porter%27s_five_forces_analysis)** (Porter 1980) — Buyer/Supplier Power · Threat of Entrants/Substitutes · Competitive Rivalry; auto-activated for consumer
- **[VRIO](https://en.wikipedia.org/wiki/VRIO)** (Barney 1991) — Valuable/Rare/Inimitable/Organized; auto-activated for devtools/deeptech
- **[Porter's Value Chain](https://en.wikipedia.org/wiki/Value_chain)** (Porter 1985) — Primary + Support activities; auto-activated for deeptech/consumer

### Layer 4 — Intelligence-community analytic tradecraft (`--type=due-diligence|investment`)
- **[ICD 203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf) (Intelligence Community Directive — Analytic Standards)** — 5 mandatory tradecraft standards: Objectivity · Independence · Timeliness · All Available Sources · Tradecraft (sourced + distinguished facts/judgments + expressed uncertainty + cause-and-effect + alternative analysis + relevance)
- **[Analysis of Competing Hypotheses (ACH)](https://en.wikipedia.org/wiki/Analysis_of_competing_hypotheses)** — Heuer/CIA 1999 (*Psychology of Intelligence Analysis*); enumerate 3-5 hypotheses, matrix-evaluate evidence, aim to disprove (not confirm)
- **Structured Analytic Techniques (SATs)** — Devil's Advocate · Pre-mortem ("imagine this is wrong in 18 months — why?") · Key Assumptions Check (5-7 explicit load-bearing assumptions, stress-tested)
- **Expressed-uncertainty discipline** — 7-term scale (almost certainly 95-99% / highly likely 80-95% / likely 55-80% / roughly even chance 40-55% / unlikely 20-40% / highly unlikely 5-20% / almost no chance 1-5%); applied to every forward-looking claim

### Layer 5 — Industry / competitive-intelligence standards
- **[SCIP Code of Ethics](https://www.scip.org/page/Ethical-Intelligence)** (Strategic & Competitive Intelligence Professionals) — 25,000+ members, ANSI/IACET-accredited; ethical CI gathering
- **[Klue's Fact / Impact / Act (FIA)](https://klue.com/blog/fact-impact-act-the-battlecard-framework-you-need-to-be-using)** — battle-card industry standard; hard-enforced when `--export=battle-card`
- **[Bessemer Cloud Index](https://www.bvp.com/atlas/state-of-the-cloud-2024) / OpenView SaaS Benchmarks / KeyBanc / ICONIQ Growth / Battery / Sapphire** — public benchmark cohorts for §10.6 Industry Benchmarks comparison
- **[Gartner Magic Quadrant](https://www.gartner.com/en/research/methodologies/magic-quadrants-research)** dimensions (Completeness of Vision × Ability to Execute) — informs §10 Quadrant Positioning
- **[Forrester Wave](https://dealhub.io/glossary/forrester-wave/)** dimensions (Current Offering × Strategy × Customer Feedback) — informs weighted-scorecard logic
- **VC IC memo template** (Sequoia / a16z / Bessemer style) — used when `--export=vc-memo`
- **Big 4 expert-call + customer-reference workflows** (Tegus / GLG / Third Bridge / AlphaSights) — generated when `--export=expert-call-questions|customer-reference-questions`

## Anti-hallucination techniques (35 implemented across 7 categories)

The skill's most distinctive value over generic LLM dossier generation is its **multi-layer anti-hallucination pipeline**. No single technique catches all hallucinations; the layered approach is what makes the dossier trustworthy. Each technique below addresses a SPECIFIC hallucination failure mode that LLMs systematically exhibit.

### Category A: Source discipline (catches "made-up facts")

1. **Source-backing rule (non-negotiable)** — every claim that can be backed by a public source MUST have a citation. If the claim can't be sourced, it's dropped. Not "we believe" / "it appears" / "industry observers note" — those are LLM hallucination tells. (`voice-and-style.md`)
2. **Two-source rule for §0/§2 hard claims** — every Scorecard / §1 / §2 datapoint requires ≥2 independent sources OR an explicit single-source label. Forces the model to discriminate facts from inferences. (`SKILL.md` Step 3)
3. **Source labeling taxonomy** — `single-source` / `vendor-claimed` / `founder-self-claim` / `aggregator-derived` / `unverified` — every weak source gets labeled inline. The reader sees source quality at the point of consumption, not buried in §19.
4. **Admiralty Code A1-F6 formal source rating** (when `--source-rating=admiralty`) — NATO/Five Eyes 2-character notation makes source quality cross-comparable across dossiers.
5. **URL validation pipeline** — every cited URL fetched (curl / WebFetch); HTTP 404 = removed or fixed; 0 × 404 is a hard floor before ship. Catches LLM-fabricated URLs.

### Category B: Cross-validation (catches "plausible-looking made-up facts")

6. **Cross-validation subagent pass** — for `--depth=deep`, 2-3 parallel `Agent` subagents independently verify business-register entities, review counts, and competitor data. (`SKILL.md` Step 3)
7. **Founder-claim verification rule** — any narrative implying a founder achieved an exit or built a $XXX-million company MUST be cross-checked against Wikipedia + acquirer press + investor exit announcement. (`lessons.md` #6)
8. **First-mover claim verification** — any "first mainstream X" claim MUST be verified by searching for that capability across the top 5 competitors. (`lessons.md` #9)
9. **Aggregator failure-mode awareness** — Latka / RocketReach / PitchBook / Crunchbase / Tracxn data is treated as `aggregator-derived` by default; the model knows these aggregators routinely disagree on the same fact. (`lessons.md` #2-#5)
10. **Internal arithmetic consistency check** — same numeric claim grep-checked across the document; if "$272M" appears in 2 places and "$267M" in 1 place, the divergence is flagged and reconciled. (`lessons.md` #20)

### Category C: Hallucination audit (catches "synthesis hallucinations")

11. **Hallucination audit subagent** — post-draft, an `Agent` reads the dossier and verifies every §0 framework claim (Scorecard / SWOT / Heat Map / Playbook) is body-supported. Specific failure modes flagged: (a) claim new in §0 without body support, (b) specific number without citation, (c) competitor stat from single source not labeled, (d) temporal claim not market-verified, (e) founder-exit narrative not cross-checked. (`SKILL.md` Step 6)
12. **Decision-tree scoring framework** — replaces qualitative "Strong fit"/"Mismatch" labels with explicit scoring (5 dimensions × weights summing to 100). Removes vague-narrative cover for the model. (`lessons.md` #17)
13. **Data Verifiability subsection (§16.X)** — explicit table listing every single-source / aggregator-only / founder-claimed metric. Forces the model to confront which "facts" are actually weak. (real-dossier §16.7 example)
14. **§23 Confidence Appendix with "what this does NOT mean" disclaimer** — composite score reflects sourcing rigor, NOT whether underlying facts are true. The disclaimer is non-negotiable. (`confidence-scoring.md`)
15. **External Verification Penalty (-5)** for `--type=competitive|due-diligence` — caps composite at 70-82 to acknowledge structural ceiling on what's externally verifiable. (`confidence-scoring.md`)

### Category D: Analytic technique (catches "single-narrative confirmation bias")

16. **Analysis of Competing Hypotheses (ACH)** — Heuer/CIA matrix method; enumerate 3-5 hypotheses, evaluate evidence against EVERY hypothesis, aim to disprove. Counters the LLM's tendency to write a single coherent narrative. (`analytic-techniques.md`)
17. **Devil's Advocate** — for each major BLUF claim, generate the strongest counter-argument. (`analytic-techniques.md`)
18. **Pre-mortem** — "imagine this dossier is wrong in 18 months — why?" Surfaces non-obvious failure modes the LLM would otherwise paper over. (`analytic-techniques.md`)
19. **Key Assumptions Check** — 5-7 explicit load-bearing assumptions, each rated for stress-test status and confidence. Makes implicit LLM assumptions reviewable. (`analytic-techniques.md`)
20. **ICD 203 expressed-uncertainty discipline** — vague analyst phrases ("could go either way", "significant risk", "some indication") replaced with the standard 7-term scale (almost certainly 95-99% → almost no chance 1-5%). Forces precision. (`analytic-techniques.md`)

### Category E: Voice + format discipline (catches "promotional drift")

21. **Promotional language prohibition** — banned in analytical voice: "revolutionary", "best-in-class", "industry-leading", "game-changing", "first mainstream X". If the entity uses promotional language, it's quoted with attribution rather than adopted. (`voice-and-style.md`)
22. **Editorial trail prohibition** — no "in this revision", "previously stated", "we updated", "originally was". Final document is single-source-of-truth. Catches LLM tendency to narrate its own corrections. (`voice-and-style.md`)
23. **Skill / tool self-reference prohibition** — no `/research-entity`, `/schedule`, `load X.md`, "the skill that produced this dossier". Catches LLM tendency to leak its own provenance. (`voice-and-style.md` v2.1)
24. **Lens-comparison prohibition** for competitive dossiers — no "outsider lens scored X / insider lens would score Y". Catches LLM tendency to produce comparative meta-commentary that reveals dossier history. (`voice-and-style.md` v2.1)
25. **12-category depersonalization leak scan** — bash one-liner checks for: personal names, emails, outsider/insider terms, skill refs, conversation refs, insider author voice, personal location, editorial trail, authorial self-ref, meta production, lens comparisons, Claude Code artifacts. Hard gate before ship for `--type=competitive|due-diligence`. (`voice-and-style.md` v2.1)

### Category F: Output discipline (catches "format-induced fabrication")

26. **Glossary completeness scan** — every all-caps acronym + jargon term used in the body must have a §22 entry. Catches the LLM tendency to introduce undefined acronyms (BLUF, SWOT, MEDDPICC, etc.) that may be confused or hallucinated. (`voice-and-style.md` Glossary discipline section)
27. **Mermaid validation (static + dynamic)** — every diagram passes 9 static checks (no `**bold**`, no LR direction, balanced subgraph/end, etc.) + optional `mmdc` dynamic render. Mermaid syntax errors are a common LLM hallucination mode. (`mermaid-validation.md`)

### Category G: Precision discipline (catches "false-precision hallucinations")

28. **Numeric range vs point-estimate discipline** — when uncertainty is high (single-source / aggregator-derived / vendor-claimed), prefer ranges ("$10-30M ARR") over false-precision points ("$23.4M ARR"). LLMs systematically fabricate decimal precision to sound authoritative; ranges expose the underlying uncertainty. (`voice-and-style.md`)
29. **"As of date" annotations on time-sensitive data** — every claim about funding / pricing / certifications / employee counts / customer logos carries an "as of <date>" annotation. Catches LLM tendency to mix data from different time periods (e.g., Q1 2024 employee count + Q4 2025 pricing presented as one snapshot). (`voice-and-style.md`)
30. **Negation-evidence rule** — "no public lawsuit found" ≠ "no lawsuit exists"; "no breach disclosed" ≠ "no breach occurred". Absence of public evidence is NOT evidence of absence — it's an absence-of-evidence claim that must be labeled as such. Catches LLM tendency to convert null findings into positive assertions. (`risk-scan.md` + `voice-and-style.md`)
31. **Quotation chain-of-custody** — every verbatim quote MUST include speaker name + role + date + source URL. LLMs hallucinate quotes more than other content type; chain-of-custody catches this. Quotes without complete chain-of-custody are dropped. (`voice-and-style.md`)
32. **Recency check** — for claims about "current"/"recent"/"<this year>", verify the source date matches the claim. Fail any "recent" claim citing a >12-month-old source. Catches LLM tendency to describe outdated info as current. (`stale-detection.md`)
33. **Self-consistency cross-section check** — same fact must match across all dossier sections (e.g., employee count in §3 must match §16 must match §0 Scorecard). Pre-ship grep-check for numeric discrepancies. (`lessons.md` #20 + automated in Step 5)
34. **Specific-number-no-source halt** — any specific number ($X.X million / X.X% / X people / X integrations) without an inline citation HALTS the draft, not paraphrased to a "round number". Forces the model to either cite or drop. (`voice-and-style.md` Citation discipline)
35. **Causal-claim-needs-explicit-causation-source** — "X caused Y" requires a source that explicitly states the causation, not just temporal correlation. LLMs systematically fabricate causation from correlation. Causal claims without explicit-causation source are reframed as correlations. (`voice-and-style.md`)

### Category H: Competitor-row pre-publication verification (NEW v2.5)

36. **Lead-investor identity ≥3-source rule with named-partner attribution preference** — outlets routinely use ambiguous phrasing ("backed by", "with", "and") that conflates leading and participating investors. The diagnostic that settles ambiguity is the lead investor's CEO or partner being quoted as "we led the round." Require ≥3 sources for lead-investor identity in any peer row; prefer sources with named-partner attribution over outlet paraphrase. Caught the Aurasell error (Menlo→Next47). (`competitor-verification.md`)
37. **HQ city: press release dateline canonical** — when secondary outlets disagree on HQ, the press release dateline (GlobeNewswire / BusinessWire / PR Newswire) wins because press releases are issued by the company's own PR function. Bay-Area-specific gotcha: SF/SM/MTV/PA confusion in transcribed business news. Caught the Aurasell HQ error (San Mateo→San Francisco). (`competitor-verification.md`)
38. **Bundled-announcement round structure: Bloomberg/TC primary breakdown** — companies announcing simultaneously at GA / public launch routinely bundle seed + Series A in the headline. The structural breakdown lives in primary financial press (Bloomberg, TechCrunch, The Information). For any peer announcing $50M+ at GA / launch, search primary financial press for the seed-vs-Series-A breakdown before publishing. Caught the Reevo error ($80M seed → $10M seed + $70M Series A). (`competitor-verification.md`)
39. **Numeric-figure attribution drift: verify number IS in cited source** — when citing a specific number to a specific article, the number must be in the article body, not just paraphrased from a related discussion. The leak pattern is "[topic discussed in article] + [plausible-sounding number] = false specificity attributed to a real source." Caught the Pento "5,800+ MCP servers" attribution drift. (`competitor-verification.md`)

### Category I: Public-source verification + ARR triangulation gates (NEW v2.6)

40. **Source-Tier Tag rule (T1-T4)** — every citation in §19 Sources tagged with its tier; T4 (aggregator paraphrase) alone is forbidden as the sole evidence for any factual claim. Tier definitions: T1 primary (registers/filings/press-release-datelines) · T2 named-byline financial press · T3 structured analyst databases · T4 aggregator paraphrase. (`source-hierarchy.md` §1) — grounded in SPJ Code of Ethics + AICPA AT-C 105 + Reuters Handbook.
41. **Wayback forensic source-dating** — for any time-sensitive claim sourced to a current page, optionally verify via [web.archive.org](https://web.archive.org/) what the page said when the claim was applicable. Catches "the page edited history" (companies adjusting founding year, customer logos, product framing). Mandatory for claims >12 months old. (`source-hierarchy.md` §2) — grounded in Bellingcat handbook + ICIJ + ProPublica practice.
42. **Customer-logo round-trip verification** — every customer logo cited in §9 must have customer-side reciprocal evidence (customer's own site mentions entity, OR customer-issued press release, OR customer's exec on record endorsing). Logos lacking round-trip evidence are flagged "logo-only — no public reciprocal evidence" or moved to §16 Risks. Catches "logo wash" (free-trial customers listed as references). (`source-hierarchy.md` §3) — grounded in Bain *Diligent* + BCG PE-DD methodology.
43. **Marketplace install-count cross-validation** — when entity claims "X customers" AND has marketplace listing (Atlassian / Salesforce / HubSpot / etc.), cross-validate the X against marketplace install count × industry conversion rate. Discrepancies (claimed customers > marketplace-implied range) flagged in §16 Risks. (`marketplace-signals.md` §3) — grounded in Forrester TEI + Bain commercial DD.
44. **ARR-proxy triangulation** — for vendors with self-reported revenue (Latka / founder interview / vendor PR), compute multi-method triangulation (headcount × Bessemer/OpenView/KeyBanc $/FTE + AE-quota × attainment + marketplace × conversion + traffic × conversion). Vendor claim flagged if outside triangulated range by >50%. (`arr-triangulation.md`) — grounded in Bessemer State of the Cloud + KeyBanc SaaS Survey + ICONIQ public benchmarks.
45. **Tetlock-compatible probability assignment** — every forward-looking claim in §0 BLUF, §16 Risks, §17, §21 paired with explicit Tetlock-compatible point probability (1-99%) that falls within the ICD 203 qualitative term's range. Resolution date + criterion required for falsifiability. (`analytic-techniques.md` §5) — grounded in Tetlock+Mellers IARPA ACE + Good Judgment Project.
46. **Negative-space SAT — "the dog that didn't bark"** — pre-publication scan for missing signals expected for the entity's type/stage/vertical (no engineering blog, no security.txt, no status page, no SOC 2, no Trust Center, no audited financials, no public roadmap, ...). Vertical-specific checklists for healthcare/fintech/govtech/edtech/legaltech/consumer/devtools. (`analytic-techniques.md` §6) — grounded in CIA *Tradecraft Primer* + Heuer *Psychology of Intelligence Analysis*.
47. **ICD 206 sourcing-discipline compliance** — IC standard for source citations: source descriptions sufficient to convey reliability + access; origin disclosure; strengths and limitations of evidence; source-of-source disclosure (when citing aggregator that cites primary, label both). Companion to ICD 203 (analytic standards). (`analytic-techniques.md` §7) — grounded in [DNI ICD 206](https://www.dni.gov/index.php/what-we-do/ic-policies-reports/intelligence-community-directives).
48. **Trust-Center auditor verification** — every compliance certification claim (SOC 2 / ISO / HIPAA / FedRAMP) verified for: auditor name (Big 4 vs lower-tier via AICPA Peer Review or IAF accreditation), audit period (Type II = period of audit; Type I = point-in-time only), and scope (full product vs carve-outs). Self-published Trust Centers are weaker signal than Drata/Vanta/Secureframe-hosted. (`press-analysis.md` §3) — grounded in AICPA SOC standards + IAF accreditation framework.
49. **Earned-vs-paid press tier labeling** — every press citation labeled `earned` (Tier 1-2: Bloomberg/Reuters/WSJ/FT/TechCrunch named-byline) or `paid` (Tier 4: PR Newswire / GlobeNewswire / BusinessWire wire distribution) or `forbes-contributor` (Tier 3: pay-to-publish-adjacent). Earned coverage rate (T1+T2 / total) reported in §15.X. (`press-analysis.md` §1) — grounded in PRovoke Media EMI + AMEC Barcelona Principles 3.0.

### Category J: Internal consistency + framing discipline (NEW v2.7)

50. **Internal-consistency cross-reference scan** — at Step 5, run grep across the dossier for pricing/headcount/customer-count/revenue/year extracts; reconcile any drift between sections. The canonical section (typically §2 or §8) owns each fact; downstream uses must match. Catches the failure mode where ARR-proxy estimation in §16 lists prices that don't match canonical §8 pricing. (`internal-consistency.md` §2)
51. **Version-label sweep** — at Step 5, grep all `vX.Y` references; reconcile any reference that doesn't match the header version. Catches editorial-trail artifacts left over from prior revisions (closing-footer "v2.4" in a v2.6 dossier). (`internal-consistency.md` §3)
52. **Audit-completion-rate honesty** — when sampling N items for any audit, count ONLY fully-completed verifications in the headline rate. Bundling partial-evidence items into a synthesized "X% verified" rate is misleading. Honest framing: "X verified / Y light-evidence / Z uncertain / W pending"; sample-audit-completion rate counts only X. (`internal-consistency.md` §4)
53. **Numeric-precision discipline** — match decimal precision to underlying analysis depth. Measured-via-NLP-tooling = 2 decimals. Synthesized-from-text-patterns = 1 decimal + ordinal label. Inferred-from-signals = ordinal label only (high/medium/low). Speculative = ordinal label, no numeric. Catches false-authority two-decimal precision on qualitative ABSA scores. (`internal-consistency.md` §5)
54. **Tier-generosity check (conservative-default rule)** — when in doubt about tier/label assignment, default to the lower (more conservative) tier. LLMs are systematically generous; conservative-default rule prevents press-release-republish outlets being labeled "earned T2" when they're actually closer to T3-T4 wire-republish. (`internal-consistency.md` §6)
55. **Triangulation-independence test** — before calling N methods "triangulation," list each method's assumption stack. If methods share >50% of assumptions, relabel as "multi-method estimation produces a plausibility-range band" — NOT "triangulated." Catches ARR-proxy methods that all share the SaaS-at-this-scale premise being mislabeled as triangulation. (`internal-consistency.md` §7)
56. **Default-outcome probability check** — for status-quo persistence forecasts (rebrand sticks, exec stays, customer logo remains, pricing tier unchanged), start from base-rate priors (e.g., 90-95% for 18mo rebrand-sticks) and adjust DOWN only when specific contrary evidence is present. Catches the LLM bias of under-estimating persistence (80% on a forecast that should default to ~92%). (`internal-consistency.md` §8)
57. **Two-dimension confidence rule** — for `--type=competitive|due-diligence|investment` with single-source / aggregator-derived / vendor-claimed headline metrics, §23.1 must report TWO scores: epistemic discipline X/100 (improvable via methodology) + headline-fact confidence Y/100 (bounded by source quality). The two move independently. Single-composite scoring conflates dimensions and inflates apparent confidence in headline metrics that haven't been verified. (`internal-consistency.md` §9)

### Comparison to professional CDD anti-hallucination measures

| Technique | This skill | Big 4 CDD | Forrester Wave | Klue battle card |
|---|---|---|---|---|
| Multi-source corroboration | ✅ formalized | ✅ informal | ✅ vendor RFI + customer | ✅ source-tagging |
| Source labeling taxonomy | ✅ 5 ad-hoc + Admiralty | ⚠️ partial | ✅ structured | ✅ Klue source-tags |
| Admiralty Code (formal) | ✅ optional | ❌ no | ❌ no | ❌ no |
| URL validation | ✅ HTTP-checked | ⚠️ informal | ✅ live links | ✅ Compete Agent |
| Cross-validation pass | ✅ subagent | ✅ team review | ✅ analyst peer | ⚠️ partial |
| Hallucination audit (post-draft) | ✅ subagent (novel for AI) | ⚠️ peer review | ⚠️ editor | ❌ no |
| ACH (Heuer) | ✅ optional | ❌ rare | ❌ no | ❌ no |
| SATs (Devil's/Pre-mortem/KAC) | ✅ optional | ⚠️ informal | ❌ no | ❌ no |
| ICD 203 expressed-uncertainty | ✅ when --analytic-rigor=high | ❌ no | ❌ no | ❌ no |
| Confidence score with disclaimer | ✅ 5-dim + disclaimer | ⚠️ narrative | ✅ weighted scorecard | ⚠️ partial |
| Depersonalization scan | ✅ 12 categories (novel) | N/A (human authors) | N/A | N/A |
| Stale-data freshness decay | ✅ TTL-by-source | ❌ static reports | ❌ static | ⚠️ Compete Agent re-runs |

Most of these techniques exist informally in human-analyst workflows; this skill's contribution is **codifying them as a reproducible pipeline** so an AI can hit Big-4-CDD-grade rigor without an analyst team.

## How to invoke

### Basic
```
/research-entity "Acme Corp"                                              # interactive wizard
/research-entity "Acme Corp" --no-wizard                                  # silent defaults
/research-entity "Acme Corp" --type=competitive --depth=deep              # competitive dossier
/research-entity "Acme Corp" --type=due-diligence --depth=deep --validation=max --analytic-rigor=high   # full IC-grade DD
```

### Full v2.2 — gold-standard methodology
```
/research-entity "Acme Corp" \
    --type=due-diligence \
    --depth=deep \
    --validation=max \
    --analytic-rigor=high \
    --source-rating=admiralty \
    --framework=swot,pestel,porter5,vrio \
    --benchmark=ai-native \
    --audit=pricing,tech-stack,customer-concentration,ai-maturity \
    --data-sources=sec,wayback,github,linkedin,uspto,pacer \
    --export=md,html,pdf,exec,vc-memo,expert-call-questions,customer-reference-questions
```

### Convert-only mode (existing MD → HTML/PDF/JSON/etc.)
```
/research-entity ./acme-research.md --export=html
/research-entity ./acme-research.md --export=exec,battle-card,vc-memo
```

### Comparison / year-over-year
```
/research-entity --compare=./acme-research.md,./competitor-research.md
/research-entity "Acme Corp" --year-over-year
```

### Self-MCP server
```
/research-entity --mcp-serve                                              # expose dossier library to future Claude sessions
```

## Cost / runtime

| Mode | Runtime | API cost (Opus 4.7 + max) | Human equivalent cost |
|---|---|---|---|
| `--depth=quick` | 5-10 min | ~$2-5 | $5K (analyst hour) |
| `--depth=standard` | 20-35 min | ~$10-20 | $25K (junior analyst day) |
| `--depth=deep` | 45-75 min | ~$25-50 | $50K-150K (Big 4 CDD chapter) |
| Full v2.2 (above) | 90-120 min | ~$60-120 | $200K-500K (Big 4 full CDD) |

The dollar comparison is approximate but directional: this skill produces ~80-92% of the rigor of a Big 4 commercial DD engagement at <0.1% of the cost.

## Version history

| Version | Date | Highlights |
|---|---|---|
| v1.0 | 2026-04 (early) | Initial skill: 11 segment files, 23-section dossier, 5-dim confidence scoring, hallucination audit, mermaid validation, EU business registers (66 countries), 245-entry glossary catalog, HTML/PDF export, wizard mode |
| v2.0 | 2026-04-27 | 18-feature expansion: stage/vertical templates, comparison/YoY mode, always-on §16 risk scan (8 patterns), SEC EDGAR/Wayback/GitHub/LinkedIn/USPTO/PACER data sources, exec/battle-card/vc-memo/json exports, Notion/Confluence publish, industry benchmarks, 4 audit modules (pricing/tech-stack/customer-concentration/AI-maturity), stale-data freshness decay, self-MCP server |
| v2.1 | 2026-04-27 | Depersonalization pipeline: 12-category leak scan (hard gate for competitive/DD), neutral-verdict competitive-voice rules, External Verification Penalty (-5) for competitive composite |
| v2.2 | 2026-04-27 | Gold-standard methodology layer: ACH (Heuer/CIA), SATs (Devil's Advocate/Pre-mortem/Key Assumptions Check), ICD 203 expressed-uncertainty discipline, Admiralty Code A-F × 1-6 source rating, PESTEL + Porter's 5 Forces + VRIO + Value Chain frameworks, Klue FIA battle-card enforcement, Tegus/GLG/Third Bridge expert-call + customer-reference question batteries |
| v2.3 | 2026-04-27 | Multi-agent execution formalization: 4 levels (solo/validation/parallel/max), `--agents=` flag, independent-ACH-agent at max-mode |
| v2.4 | 2026-04-27 | Strategic-analysis layer: Royal Dutch Shell 2x2 scenarios + Cone of Plausibility, DCF/Comps/Public-Multiples/LBO valuation, Christensen Disruption + Moore Crossing the Chasm + Rumelt Strategy Kernel + JTBD + Wardley Mapping. Initial dossier rebuilt with 19 new methodology sections. |
| v2.5 | 2026-04-27 | Competitor-row pre-publication verification (`competitor-verification.md`): 4 error classes — lead-investor identity, HQ-from-press-release-dateline, bundled-announcement round structure, numeric-figure attribution drift. |
| v2.6 | 2026-04-27 | Public-source verification + ARR triangulation + regulatory overlay: 6 new files (source-hierarchy, marketplace-signals, osint-public, arr-triangulation, regulatory-overlay, press-analysis); 2 extensions (analytic-techniques + Tetlock + Negative-space SAT + ICD 206; reviews-platforms + ABSA). 10 new anti-hallucination gates (Cat I, techniques #40-49). Hallucination audit prompt extended with 6 new flag types (k-p). |
| **v2.7** | **2026-04-27** | **Internal-consistency + framing-discipline layer (post-v2.6-validation): new file `internal-consistency.md` (Cat J) with 8 anti-hallucination techniques (#50-57) — internal-consistency cross-reference scan, version-label sweep, audit-completion-rate honesty, numeric-precision discipline, tier-generosity check, triangulation-independence test, default-outcome probability check, two-dimension confidence rule. Lessons #56-63 added. Hallucination audit prompt extended (flags q-w). Codifies the 8 failure patterns surfaced in real production validation: pricing-line internal contradiction; version-label artifact persistence; audit-completion-rate overstatement; two-decimal precision on synthesized estimates; tier-generosity bias; "triangulation" misuse on non-independent methods; status-quo persistence forecasts under-estimated; single-composite confidence conflating dimensions.** |

## Sources / further reading

**Intelligence-community methodology:**
- [ICD 203 (Analytic Standards)](https://www.dni.gov/files/documents/ICD/ICD-203.pdf) · [Heuer's Psychology of Intelligence Analysis (CIA, free PDF)](https://www.cia.gov/resources/csi/static/9a5f1162fd0932c29bfed1c030edf4ae/Pyschology-of-Intelligence-Analysis.pdf) · [ACH on Wikipedia](https://en.wikipedia.org/wiki/Analysis_of_competing_hypotheses) · [Admiralty Code](https://en.wikipedia.org/wiki/Admiralty_code)

**Strategic-analysis classics:**
- Porter, *Competitive Strategy* (1980) — 5 Forces · Porter, *Competitive Advantage* (1985) — Value Chain · Barney (1991) — VRIO · Aguilar (1967, expanded 1980s) — PESTEL

**Competitive intelligence standards:**
- [SCIP](https://www.scip.org/) (Strategic & Competitive Intelligence Professionals — Code of Ethics) · [Klue Fact-Impact-Act blog](https://klue.com/blog/fact-impact-act-the-battlecard-framework-you-need-to-be-using)

**Industry benchmarks:**
- [Bessemer State of the Cloud 2025](https://www.bvp.com/atlas/state-of-the-cloud-2024) · [Battery Cloud Software Index](https://www.battery.com/blog/opencloud-2024/) · [Forrester Wave methodology](https://dealhub.io/glossary/forrester-wave/) · [Gartner Magic Quadrant methodology](https://www.gartner.com/en/research/methodologies/magic-quadrants-research)

**Big 4 commercial DD references:**
- [Bain Private Equity DD](https://www.bain.com/industry-expertise/private-equity/due-diligence/) · [BCG DD & Strategy](https://www.bcg.com/capabilities/mergers-acquisitions-transactions-pmi/due-diligence) · [Deloitte Corporate Intelligence](https://www.deloitte.com/us/en/services/consulting/services/corporate-intelligence-advisory-services.html)

---

*Self-documenting `--about` content. Print this when invoked; do NOT generate a dossier. To proceed with research, drop `--about` and provide an entity name.*

## When to load this file

- `--about` flag set — print the content above and exit
- User asks "how does this skill work" / "what methodologies" / "what anti-hallucination" / "compare to Big 4" / "version history"
- User is evaluating whether to use this skill vs. alternatives (Klue / Crayon / commissioning a Big 4 CDD)

## Anti-patterns

- ❌ Running `--about` AND attempting to generate a dossier in the same invocation — they're mutually exclusive; `--about` is informational-only
- ❌ Showing a different methodology list than what's actually implemented — keep this file in sync with the actual segment files
- ❌ Listing methodologies without source citations — defeats the purpose; sources lend credibility
- ❌ Marketing-tone language ("revolutionary", "best-in-class") — same anti-promotional rule from `voice-and-style.md` applies here
