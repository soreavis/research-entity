# Internal Consistency + Framing Discipline

Loaded by the `research-entity` skill at Step 5 (Validate) — pre-publication checks for internal-document consistency, framing-honesty, and dimension-separation. All techniques here are grounded in real validation findings from production runs where dossiers shipped with internal contradictions, false-precision numerics, generous tier-labeling, or composite scores that conflated independent dimensions.

This file is the home of **Category J anti-hallucination techniques (#50-89)** — sister category to Category I (`source-hierarchy.md` + public-source verification). Where Cat I targets external-source verification, Cat J targets internal-document discipline + claim-coverage discipline + SaaS-CXO claim discipline.

**Technique inventory by file:**
- **#50-72** — internal-consistency.md (this file): cross-section drift, version-label sweep, audit-completion-rate honesty, numeric-precision discipline, tier-generosity check, triangulation-independence, default-outcome probability, two-dimension confidence, count-vs-enumeration, terminology-rename residue, duplicate-paragraph scan, speaker-vs-founder identity, aggregator-data freshness, parent-network multiplier, comparison-directory probe, "not publicly disclosed" verification, single-feature → category-claim guard, negation-evidence rule, quasi-deterministic-claim guard, comparator-pricing source rule, subagent-audit blindspot, load-bearing claim N-source rule, round-number / methodology-not-disclosed labeling
- **#73, #83, #89** — `win-loss.md`: win-rate-without-denominator rule, win-driver-needs-3-corroborating-reviews, verbatim-quote discipline
- **#74, #75, #84** — `saas-economics.md`: NRR Bessemer-canonical-tier discipline, multi-method estimate band rule, cohort-benchmark citation
- **#76, #77, #78, #85, #86** — `moat-scoring.md`: Helmer 7-Powers no-aggregation, switching cost requires friction mechanism, network effect requires degree-N evidence, counter-positioning requires incumbent-paralysis evidence, process power requires 5+ years of evidence
- **#79, #80, #81, #82, #87, #88** — `roadmap-inference.md`: patent-filing ≠ product-shipping, job-posting → time-horizon labeling, conference-talk ≠ shipping-feature, GitHub-commit ≠ feature-direction, multi-channel convergence requirement, counter-evidence check

---

## §1 — Why this file exists

Twenty-three failure patterns surfaced across real production validation cycles, each with a measurable fix:

**v2.7 patterns (#50-57):**
1. Pricing line in §16 contradicted canonical pricing in §8 (real factual error)
2. Closing version-label artifact still said "v2.4" in a v2.6 document
3. Customer-logo audit headline said "50% verification rate" when only 30% had been empirically verified
4. ABSA sentiment scores reported as "+0.85", "+0.65" (two-decimal precision) when underlying data was qualitative review-text inference
5. SalesTechStar categorized as T2 "earned" — generous, should have been T3
6. ARR-proxy methods labeled as "triangulation" when they shared the same SaaS-at-this-scale assumption
7. Forecast on "branding-retention 18 months post-rebrand" set at 80% when most rebrands stick (default ≥90%)
8. Single composite confidence score conflated methodology rigor with factual confidence

**v2.9 patterns (#58-60):**
9. Within-section count-vs-list mismatch — prose summary said "2 light-evidence" while listing 3 names
10. Terminology-rename residue — "independently-triangulated" survived a "triangulation" → "multi-method estimation" rename
11. Duplicate-paragraph residue from re-edits — two consecutive `**Note:**` blocks with overlapping content

**v2.11 patterns (#61-72) — caught by reader-side validation on the AcmeCRM `--depth=quick` brief:**
12. Founder identity inferred from a press-release quote attribution (speaker ≠ founder) — Acme CRM brief said HoldCo Group was founded by the quoted executive alone; actual count is 4 co-founders
13. Aggregator citation >12 months old cited as if current — a 2024 podcast ARR figure cited in a 2026 dossier when the actual figure was materially higher
14. Headcount-velocity claim ran 5× across sections without acknowledging parent-network multiplier — "small-core-team ceiling" ignored the several-hundred-expert HoldCo Group network on the same about page
15. Comparison-directory probe missed in `--type=competitive` mode — the competitor's `/comparison/<employer>-vs-<competitor>/` page targeted the user's employer and went undetected
16. "Not publicly disclosed" claim without verification ladder — deal-close date IS public (the representing law firm + a secondary deal database both date it to the day)
17. Single-feature → category-claim extrapolation — "the AI email assistant is an OpenAI wrapper" → "Acme CRM has no AI strategy" (ignoring its other intelligence features + the parent's group-wide AI playbook)
18. Negation-claim without explicit negative-evidence — "no SOC 2" / "no proprietary data" need surface + date + searched-strings
19. Quasi-deterministic verb usage — "categorically beyond" / "cannot trivially" / "will never" disguised forecasts as facts
20. Competitor pricing cited inline without linking to competitor's /pricing page — Pipedrive / HubSpot prices unverified
21. Step 6 hallucination audit subagent shares writer's blindspots — audit caught 3 of 8 errors; reader-side validation caught all 8
22. Claim repeated 3+ times treated as multi-source-corroborated when underlying source-count is 1
23. Round-number / suspicious-precision vendor metric inherited as authoritative without "methodology not disclosed" label

Each pattern is reproducible across dossiers. This file codifies prevention.

---

## §2 — Internal-consistency cross-reference scan (technique #50)

### The failure mode

Two sections of the same dossier state different values for the same fact. Most common: a section that uses pricing as input (e.g., ARR-proxy estimation) lists a price that doesn't match the canonical pricing section. Other variants: customer count varying across sections, headcount range varying, founding year varying, ARR figure varying.

### The pre-publication scan

```bash
# Run after Step 4 Draft, before Step 6 Hallucination Audit
OUTPUT="<dossier path>"

# Pricing consistency — extract all € or $ + number patterns; flag drift
grep -nE '[€$][0-9]+(\.[0-9]+)?(/user|/seat|/mo|/month|/year|/yr|K|M|B)?' "$OUTPUT" | sort -t: -k2 -n > /tmp/pricing-extracts.txt

# Headcount consistency — extract all employee/headcount/headcount-range mentions
grep -inE '\b([0-9]+([-–][0-9]+)?\s*(employees|FTEs|headcount|people))' "$OUTPUT" > /tmp/headcount-extracts.txt

# Customer count consistency
grep -inE '\b([0-9]+(,[0-9]{3})?\s*(customers|clients|accounts|references|logos))' "$OUTPUT" > /tmp/customer-extracts.txt

# Revenue consistency
grep -inE '\$[0-9]+(\.[0-9]+)?\s*M\s*(ARR|revenue)' "$OUTPUT" > /tmp/revenue-extracts.txt

# Year consistency
grep -inE '\b(founded|incorporated|launched|established)\s+(in\s+)?[12][0-9]{3}' "$OUTPUT" > /tmp/year-extracts.txt
```

### Reading the output

For each extract list, the **same fact should produce the same value at every line** unless the dossier explicitly notes the discrepancy. Common patterns to flag:

- Pricing tier listed differently in §8.X (canonical) vs §16.X (input to ARR estimation)
- Headcount range varying across §0 Scorecard vs §3.4 Related Entities vs §16.7 Data Verifiability
- Customer count "1,200" in §1 vs "98 publicly named" vs "100+ on FeaturedCustomers" — these are different things and need separate labels
- Revenue figure cited as "$16M" in some sections, "~$15.6M" in others — pick one and explain the source

### Required action

If two sections disagree:
1. **Identify the canonical section** (usually §2 Company Fundamentals or §8 Pricing — the section that owns the fact)
2. **Restate downstream uses** to match canonical, OR explicitly note the discrepancy in §16.7 Data Verifiability
3. **Never silently pick one over the other** — the reader must see what was reconciled

---

## §3 — Version-label sweep (technique #51)

### The failure mode

Dossier header says "v2.6 methodology" but a closing footer says "v2.4 — full gold-standard methodology layer" — left over from an earlier revision. Reader confidence in the document's freshness is undermined by visible artifact-level drift.

### The pre-publication scan

```bash
# Extract every version reference
grep -nE 'v[0-9]+\.[0-9]+' "$OUTPUT" | sort -k2 -t: > /tmp/version-refs.txt

# All versions should match the header / front-matter version
# Manually inspect the list for outliers
```

### Required action

Pick a single version per dossier. If the dossier evolves across versions (v2.4 baseline + v2.5 corrections + v2.6 additions), the header should show the latest (v2.6) and the **revision-history section** in §23 should track per-version changes. Closing-footer / end-of-dossier label must match the header.

---

## §4 — Audit-completion-rate honesty (technique #52)

### The failure mode

A dossier samples 10 customers for verification, performs partial verification, then summarizes as "50% verification rate" — implying half were verified when only some fraction were actually completed and others were "uncertain" or "pending."

### The honest-framing rule

When sampling N items for any kind of audit (customer-logo, source-tier, pricing-consistency, etc.), report the result as:

```
N items sampled:
  - X verified (full Direction-A + Direction-B evidence)
  - Y light-evidence (Direction-A only, or partial Direction-B)
  - Z identification-uncertain (cannot pin down which entity is meant)
  - W pending (audit not completed)

Sample-audit-completion rate: X/N (where X = fully completed)
```

**Never synthesize a "verification rate" by combining partial-evidence categories.** A "50% verification rate" headline that bundles 3 verified + 2 light-evidence is misleading because the 2 light-evidence aren't actually verified.

### Pre-publication check

For any "X% verified" or "X out of N verified" headline in a dossier section, count the underlying status labels in the supporting table. The headline must match the count of FULLY verified items, not the sum of all partially-evidenced items.

---

## §5 — Numeric-precision discipline (technique #53)

### The failure mode

Aspect-Based Sentiment Analysis (ABSA) reports sentiment scores like "+0.85" or "-0.65" when the underlying analysis is pattern-based inference from review text — not a measured score from NLP tooling. Two-decimal precision creates false authority.

### The discipline

For any synthesized / inferred / estimated numeric:

| Underlying analysis | Allowed precision |
|---|---|
| **Measured (NLP run on actual corpus)** | 2 decimals + score citation |
| **Synthesized from text patterns** | 1 decimal + ordinal label (strongly positive / mixed / etc.) |
| **Inferred from indirect signals** | Range + ordinal label only (e.g., "high" / "medium" / "low") |
| **Speculative / directional** | Ordinal label only (no numeric) |

### Required action

Every numeric in §11 (sentiment), §16 (ARR estimation), §17 (probabilities), §0 (Scorecard) must be paired with **either** (a) a measurement source citation at appropriate precision, or (b) an explicit "synthesized estimates — directional only" disclaimer.

ABSA-specific: numeric sentiment should be 1 decimal + ordinal label by default; only use 2 decimals if the dossier ran actual NLP tooling against the review corpus.

---

## §6 — Tier-generosity check (technique #54)

### The failure mode

When categorizing sources / outlets / tiers / vendors, the LLM defaults to the more generous label. SalesTechStar (a press-release-republish trade outlet) was categorized as T2 "earned" when its actual behavior is closer to T4 wire-republish.

### The conservative-default rule

When in doubt about a tier assignment, **default to the lower (more conservative) tier**. Then the dossier reader's worst case is that something is undersold — not oversold. A T4-when-actually-T2 understatement understates Coverage; a T2-when-actually-T4 overstatement misleads about the actual signal value.

### Tier-defaults to apply (across categories)

| Category | If genuinely uncertain, default to |
|---|---|
| Press tier (T1-T5) | One tier lower than your first instinct |
| Source quality (Admiralty A1-F6) | One letter or one number worse |
| Customer-logo verification (verified / light / uncertain) | Light or uncertain unless full Direction-B evidence found |
| Triangulation method confidence (high / medium / low) | Medium becomes "medium-low" if methods aren't fully independent |
| Compliance certification weight | Lower-tier auditor over higher; Type I over Type II if not specified |
| Industry benchmark range | Wider range than narrower if data is across years |

---

## §7 — Triangulation-independence test (technique #55)

### The failure mode

Three estimation methods are labeled "triangulation" when they all share the same underlying assumption (e.g., "<entity> operates as a $X-scale SaaS"). Methods that share assumptions are not independent — they cannot truly triangulate.

### The independence test

Before calling N methods "triangulation":

1. **List the assumption stack** for each method
2. **Identify shared assumptions** across methods
3. **If methods share >50% of their assumption stack**, they are NOT independent — relabel as "multi-method estimation" or "plausibility-range bounds"
4. **True triangulation** requires methods that produce independent estimates of the same quantity from non-overlapping assumption stacks (e.g., headcount from LinkedIn + ARR from filings + customer count from regulatory disclosures)

### Required action

For ARR estimation specifically, the headcount × $/FTE method, AE-quota × attainment method, and customer × ACV method all share the assumption that the entity operates at SaaS-industry-typical metrics. Label as "multi-method estimation produces a plausibility-range band" — NOT "triangulated."

---

## §8 — Default-outcome probability check (technique #56)

### The failure mode

LLM forecasts about whether a status-quo state persists (a rebrand sticks, an exec stays, a customer logo remains) systematically under-estimate persistence. Most rebrands stick ~90%+ at 18 months; most executives stay 12 months ~95%+ unless visible departure signals; most customer relationships persist if no friction is observed.

### The status-quo prior

| Forecast type | Default base rate (in absence of contrary evidence) |
|---|---|
| Rebrand sticks 18 months | 90-95% |
| C-suite stays 12 months (no visible departure signals) | 90-95% |
| Customer logo remains 12 months | 70-85% (higher for enterprise, lower for SMB) |
| Pricing tier stays unchanged 12 months | 75-85% |
| Domain remains owned 12 months | 95%+ |
| Trust Center maintains current status (no certification change) | 80-90% |
| Funding round closes within announced timeframe | 70-85% |
| New product feature launches within stated quarter | 50-70% (notoriously slippy) |
| Vendor reaches stated ARR milestone within 12 months | 40-60% |

### Required action

For every forecast in §17 / §21 about status-quo persistence, **start from the base rate** and adjust for entity-specific signals. If the LLM-generated forecast is materially below the base rate without specific contrary evidence, flag as **forecast-too-low** and ask "what evidence justifies this lower-than-default probability?"

---

## §9 — Two-dimension confidence rule (technique #57)

### The failure mode

A single composite confidence score (e.g., "84/100") conflates two independent dimensions:
- **Methodology rigor** (how well-sourced, well-validated, well-disciplined is the analysis?)
- **Underlying factual confidence** (how trustworthy are the headline metrics themselves?)

These move independently. Methodology rigor improves with better techniques (Tetlock, ABSA, negative-space SAT, etc.). Factual confidence is bounded by source quality — it can only improve if NDA-stage access is obtained or new primary sources surface. **Conflating them inflates apparent confidence** in headline numbers that haven't actually been verified.

### The two-dimension rule

For `--type=competitive|due-diligence|investment` with **single-source / aggregator-derived / vendor-claimed** headline metrics, §23.1 must report **two separate scores**:

```markdown
### Two-Dimension Confidence

#### Dimension 1: Epistemic discipline (methodology rigor) — X/100
[Multi-source corroboration discipline / source verifiability discipline / URL freshness / hallucination audit / voice-format discipline / methodology-rigor bonus / external-verification penalty]

#### Dimension 2: Underlying factual confidence — Y/100
[Headline metric trustworthiness — driven by source quality, NOT improvable via methodology]

| Metric | Source quality | Factual confidence |
|---|---|---|
| Revenue | Single-source-Latka | Low-medium |
| Customer count | Single-source-aggregator | Low-medium |
| Employee count | Multi-aggregator-conflict | Low |
| Investor identity | Founder-stated, externally unverified | Very low |

**Honest summary:** v2.6 improved the discipline of how uncertainty is characterized. It did NOT reduce the underlying factual uncertainty. The two-dimensional framing avoids the misleading impression that methodology improvements increased trust in the headline numbers.
```

### Required action

Whenever methodology layer is added (v2.5 → v2.6 etc.), the methodology-rigor dimension increases. The factual-confidence dimension stays the same unless source quality changes. **Both must be reported** so the reader can distinguish "rigorous analysis of low-trust data" from "rigorous analysis of high-trust data."

---

## §10 — Count-vs-enumeration reconciliation (technique #58)

### The failure mode

Prose summary states a count that does not match its own adjacent enumeration. Most common: an audit summary like "**3 verified** (A / B / C), **2 light-evidence** (X / Y / Z), **5 identification-uncertain** (P / Q / R / S)" — the parenthesized name lists don't match the bolded counts. The numbers are read as authoritative; the names are skimmed; the inconsistency ships.

Distinct from technique #50 (cross-section drift between §8 and §16). #58 is **within a single sentence or paragraph** — a count and its enumeration disagree.

### The pre-publication scan

```bash
# Detect "**N <label>** (Name1 / Name2 / Name3 ...)" patterns and flag count mismatch
grep -nE '\*\*[0-9]+\s+[a-z-]+\*\*\s*\([^)]+\)' "$OUTPUT" | while read -r line; do
  num=$(echo "$line" | grep -oE '\*\*[0-9]+' | head -1 | tr -d '*')
  names=$(echo "$line" | grep -oE '\([^)]+\)' | head -1 | tr -d '()')
  count=$(echo "$names" | tr '/' '\n' | grep -cE '[A-Za-z]')
  if [ "$num" != "$count" ]; then echo "MISMATCH: claims $num, lists $count names: $line"; fi
done
```

The regex is heuristic — it covers the common pattern `**3 verified** (Tenaska / EMCS / Crestcom)`. Variants with em-dashes, commas, or "and" need manual review.

### Required action

When prose says "**N items** (name1 / name2 / ...)":
1. Count names in the parenthesized list (split on `/`, `,`, `and`, em-dash).
2. Reconcile against the bolded number.
3. If they disagree, the **enumeration is canonical** (the names are concrete; the number is a derived count). Update the number to match the enumeration.
4. Cross-check totals: if multiple buckets are enumerated as components of N (e.g., "3 verified + 2 light + 5 uncertain = 10 sampled"), the bucket counts must sum to N.

### Composability with #52

Technique #52 (audit-completion-rate honesty) requires reporting categories separately. #58 enforces the within-category arithmetic discipline so the categories themselves are self-consistent.

---

## §11 — Terminology-rename residue sweep (technique #59)

### The failure mode

A key term is deprecated mid-revision (e.g., "triangulation" → "multi-method estimation produces plausibility-range bands" per technique #55). The author runs find-and-replace on the canonical form but misses **inflected forms** ("triangulated", "triangulating", "triangulation-band", "independently-triangulated"). The deprecated term survives in derivative phrases, contradicting the rename.

Distinct from technique #51 (version-label artifacts — purely metadata). #59 is **terminology body-text residue** that contradicts the renamed framework.

### The pre-publication scan

For any term deprecated mid-revision, sweep every inflection — not just the canonical noun. Maintain a per-dossier deprecation log:

```bash
# Deprecation-log format (track in dossier or commit message)
DEPRECATED_TERMS=("triangulation" "triangulated" "triangulating" "triangulate")
REPLACEMENT="multi-method estimation"

for term in "${DEPRECATED_TERMS[@]}"; do
  hits=$(grep -nE "\\b${term}" "$OUTPUT" | grep -vE '<!--|^\s*#' | wc -l)
  if [ "$hits" -gt 0 ]; then
    echo "RESIDUE: ${hits} occurrence(s) of deprecated '${term}' (replace with '${REPLACEMENT}'):"
    grep -nE "\\b${term}" "$OUTPUT" | grep -vE '<!--|^\s*#'
  fi
done
```

### Required action

When deprecating a term mid-revision:

1. **Record the deprecation** in the dossier's revision-history block (`§23 — Methodology` revision notes).
2. **Sweep every inflection** of the deprecated term. Common inflection patterns:
   - Verb forms: `-ed`, `-ing`, `-es`, `-e`
   - Noun forms: `-tion`, `-er`, `-or`, `-ism`
   - Adjective forms: `-able`, `-ible`, `-ical`
   - Compound forms: `<term>-band`, `<term>-method`, `independently-<term>ed`
3. **Allowed exceptions** (must be flagged inline): when discussing the deprecated term itself ("we previously used 'triangulation' here, now renamed to..."). Mark with `<!-- intentional reference to deprecated term -->`.
4. **Re-run the sweep at Step 5** before publication; zero unflagged occurrences allowed.

### Composability with #55

Technique #55 prevents the **first** misuse of "triangulation" (e.g., labeling non-independent methods as triangulation). Technique #59 prevents **residual** misuse after a rename has been initiated — so a dossier that was correctly renamed in v2.6 doesn't ship with v2.5 terminology in §16.11.

---

## §12 — Duplicate-paragraph scan (technique #60)

### The failure mode

Iterative edits — especially when adding methodology disclosures or rationale paragraphs — leave **back-to-back paragraphs with overlapping content**. The editor adds a more complete version of an existing note but forgets to remove the prior one. The dossier ships with two adjacent `**Note:**` blocks that say substantially the same thing.

Real production case: §23.1 contained two consecutive paragraphs both starting with "**Note:** Mermaid diagram validation runs as a quality check during draft + export…" — one shorter, one longer; both true; both redundant.

### The pre-publication scan

```bash
# Flag adjacent paragraphs sharing the same lead-in marker
grep -nE '^\*\*(Note|Important|Caveat|Warning|Disclaimer|Methodology|Source):\*\*' "$OUTPUT" | awk -F: '
{
  if (prev_line && $1 - prev_line <= 3) {
    print "ADJACENT-NOTE-CLUSTER: lines " prev_line " and " $1 " — review for duplication"
  }
  prev_line = $1
}'

# Flag adjacent paragraphs with high lead-word overlap (first 8 words)
awk 'BEGIN{RS=""; FS="\n"} {
  curr = $0; gsub(/[*_`#]/, "", curr); split(curr, w, /[ \t]+/);
  curr_lead = w[1] " " w[2] " " w[3] " " w[4] " " w[5] " " w[6] " " w[7] " " w[8];
  if (NR > 1 && curr_lead == prev_lead && length(curr_lead) > 30) {
    print "DUP-LEAD-CANDIDATE: paragraph " NR " repeats lead-in of paragraph " NR-1 ": " curr_lead
  }
  prev_lead = curr_lead
}' "$OUTPUT"
```

### Required action

For every flagged adjacent paragraph cluster:
1. **Read both paragraphs in full.**
2. **If redundant** (same claim, same source, same rationale): delete the shorter / less complete version. Keep the one with the strongest rationale.
3. **If distinct but on related themes**: collapse into one paragraph or add a clear distinguishing lead-in (e.g., `**Note (separate concern):**`).
4. **If genuinely independent**: leave both, but inspect lead-in markers for clarity.

### Why this happens

Re-edit is the most common cause: an edit cycle replaces a `**Note:**` with a more complete version but appends instead of substituting. Other causes: (a) merge from a parallel revision branch, (b) two reviewers adding similar disclaimers in different passes, (c) automated insertion (e.g., methodology layer applying to multiple sections).

### Composability

Technique #60 is the **content-redundancy** sister to #51 (version-label) and #50 (cross-section drift). All three target post-edit residue, but at different scales: #51 is metadata, #50 is cross-section, #60 is adjacent-paragraph.

---

## §13 — Speaker-vs-founder identity discipline (technique #61)

### The failure mode

A press release / interview / podcast names a person speaking on behalf of a company. The dossier infers founder identity from that single source. **The press release names the speaker for the deal — not the founders.** Result: incomplete or wrong founder lists shipped as authoritative.

Real production case: an Acme CRM `--depth=quick` brief credited HoldCo Group's founding to a single person (because they were quoted in the strategy interview). Actual count: **four co-founders** — all discoverable on HoldCo Group's own /about page.

### The discipline

When citing entity leadership / founder identity:

1. **Source-of-record is the entity's own /about, /leadership, /team, or /founders page.** NOT the press release. NOT the podcast interview. NOT the third-party Wikipedia entry.
2. **Press releases name speakers, not founders.** A quote at the bottom of a press release is who-said-this, not who-founded-this.
3. **Triangulate against LinkedIn `/company/<entity>` "founders" surface** if available — this often surfaces co-founders not named in PR materials.
4. **For portfolio/parent companies**: load BOTH the entity's /about page AND the parent's /about page. Founder count for an entity acquired into a holding company can shift across the two sources.

### Required action

Pre-publication scan: every named "founder" in §3 / §4 must be backed by either (a) the entity's own /about or /leadership page, OR (b) a Wikipedia entry, OR (c) a primary press release explicitly naming the founding team. If the only source is a quote attribution, downgrade to "speaks on behalf" and flag founder-count as "not verified — see §16.X."

---

## §14 — Aggregator-data freshness sweep (technique #62)

### The failure mode

A T3 aggregator citation (founder-podcast interview, Latka profile, PitchBook deal record, Sacra teardown) is published in year N. The dossier cites it in year N+2 as if it were current. **In fast-moving categories (private SaaS, holding companies, AI vendors), 12+ month-old aggregator data is structurally stale.**

Real production case: an Acme CRM brief cited an aggregate-ARR figure across 25+ portfolio companies from a 2024 founder-podcast interview as HoldCo Group's parent scale. The actual current-year figures were materially higher on every dimension. The dossier was 2 years and ~25% behind.

### The freshness scan

```bash
# Detect citations with year-anchors (2020 / 2021 / ... / 2024) where current year is 2026+
OUTPUT="<dossier>"
CURRENT_YEAR=$(date +%Y)

# Extract all year-anchored citation phrases
grep -nE '(per|via|cited in|from|in)\s+(a\s+)?20[0-9]{2}\s+' "$OUTPUT" | while read -r line; do
  year=$(echo "$line" | grep -oE '20[0-9]{2}' | head -1)
  age=$((CURRENT_YEAR - year))
  if [ "$age" -ge 1 ]; then
    echo "FRESHNESS-CHECK [age=${age}y]: $line"
  fi
done
```

### Required action

For every citation with age ≥ 12 months in fast-moving categories:

1. **Search the entity's most recent press releases / blog / milestone announcements** for newer figures.
2. **Check the entity's annual letter / shareholder update / S-1 / 10-K** if public.
3. **For holding companies and serial acquirers**: ALWAYS check for newer aggregate-portfolio milestones (serial acquirers such as Tiny Capital and Constellation Software publish quarterly portfolio updates).
4. If newer data is found: **cite the newer figure** with the older as historical context ("up from $80M ARR in 2024").
5. If no newer data exists: tag the citation explicitly with `[as of <year>]` so the reader sees the staleness.

---

## §15 — Parent-network multiplier acknowledgement (technique #63)

### The failure mode

When entity is a portfolio company / subsidiary / division, the dossier cites entity-only headcount (e.g., "25-person core team") and runs analytical claims based on it ("low product-velocity ceiling", "cannot accelerate AI roadmap"). **The same source page often discloses parent-network resources that materially soften the headcount claim.**

Real production case: an Acme CRM brief anchored its product-velocity analysis on "~25-person team can't accelerate" repeatedly across §0 SWOT / §0 Strategic Playbook / §16 Risks / §17 Takeaways / §21 Final Assessment. The same About page that gave the core-team figure ALSO disclosed access to a several-hundred-expert global network, spanning dozens of countries, via HoldCo Group. The dossier never acknowledged the multiplier.

### The discipline

When entity is a portfolio company / subsidiary / division:

1. **Disambiguate** any headcount-velocity claim into three components:
   - (a) Entity-only direct headcount
   - (b) Parent-network access scope (people, geographies, capabilities)
   - (c) Practical applicability of the parent-network resources to the specific roadmap question
2. **Effective velocity formula** (qualitative or quantitative):
   ```
   effective_velocity_pool = entity_team + applicable_parent_resources
   ```
3. **Lead with the multiplier-aware framing** in any section that uses headcount as load-bearing analysis. Never just "X has a 25-person team." Always "X has a 25-person core team PLUS access to <parent>'s <N>-person network."
4. **For AI / category-creation claims specifically**: if parent has a portfolio-wide AI / strategic initiative, that is load-bearing context for the entity's category-creation potential.

### Required action

Pre-publication scan: any §0 / §16 / §17 / §21 claim that uses headcount-as-velocity must be checked against the entity's about page for parent-network disclosures. If parent-network is disclosed and not acknowledged, soften the velocity claim.

---

## §16 — Comprehensive comparison-directory probe (technique #64)

### The failure mode

For `--type=competitive` runs, the entity's own `/comparison/` directory is a goldmine of self-disclosed competitive-positioning artifacts. The dossier focuses on the entity's product surface and misses the directory entirely. **The single most actionable competitive intel for a user-at-competing-entity reader is the entity's named-targeting page for the user's employer.**

Common pattern: a vendor publishes a dedicated `/comparison/<employer>-vs-<competitor>/` page naming a rival directly and citing search-impression claims about that rival's traffic. Generic Step 2 source gathering does not probe for it.

### The discipline

For every `--type=competitive` run:

1. **Probe** `<entity-domain>/comparison/`, `<entity-domain>/vs/`, `<entity-domain>/alternatives/` directory-listing pages.
2. **Enumerate** every page in those directories. Each is a competitive-positioning artifact.
3. **For user-at-competing-entity context** (per CLAUDE.md user-employer memory): **explicitly probe** `<entity-domain>/comparison/<user-employer-slug>-vs-<entity-slug>/` AND the inverse slug ordering.
4. **For named Tier-A peers** (per §10 of the dossier): probe `<entity-domain>/comparison/<peer>-vs-<entity>/` for each. These pages reveal how the entity narrates its own competitive position.
5. **Each found page becomes a §10.X subsection** in the dossier (or at minimum a Watchlist row + a §10 named mention).

### Required action

Step 2 source gathering MUST include this probe (codified as Step 2 substep #14 in SKILL.md). Step 5 validation: confirm at least one comparison-directory entry was checked. If `--type=competitive` and zero comparison pages were probed → flag as scope-coverage gap.

---

## §17 — "Not publicly disclosed" verification rule (technique #65)

### The failure mode

The dossier treats absence-from-press-release as absence-from-public-record. Phrases like "deal-close date not publicly disclosed", "exact valuation not publicly known", "founder-departure date private" ship without checking secondary sources where these facts are routinely available.

Real production case: an Acme CRM brief flagged "exact deal-close date not publicly disclosed" for the HoldCo Group acquisition. The law firm that represented the acquirer and a secondary deal database both publicly date the close to a specific two-day window.

### The verification ladder

Before claiming any of these phrases:
- "not publicly disclosed"
- "not publicly known"
- "publicly unavailable"
- "exact <X> private"
- "details not released"

…run this verification ladder:

| Layer | Source category | What to check |
|---|---|---|
| 1 | Acquirer / target press release | The original announcement |
| 2 | **Legal-firm representation announcements** | Goodwin, Cooley, Wilson Sonsini, Morgan Lewis, Latham & Watkins, etc. — they publish deal closures with day-precision |
| 3 | **Secondary deal databases** | PrivSource, S&P Capital IQ, Pitchbook deal records, Mergermarket, Datasite Marketplace |
| 4 | Acquirer regulatory filings | 10-Q / 10-K footnotes (if public), 8-K material events |
| 5 | Trade-press deal-roundup columns | PE Hub, Axios Pro Rata, FT Lex, Bloomberg Deals, The Information |
| 6 | Domain WHOIS / state corporate filings | When ownership transfers, WHOIS records can date the change |

### Required action

If verification ladder yields the missing fact: cite the secondary source. If layer 6 still doesn't yield the fact: only THEN claim "not publicly disclosed", and explicitly list which sources were checked ("not publicly disclosed; not in PrivSource / Pitchbook / law firm announcements as of <date>").

---

## §18 — Single-feature → category claim guard (technique #66)

### The failure mode

The dossier observes a single feature (e.g., "the AI email assistant is an OpenAI wrapper") and extrapolates to a category claim (e.g., "Acme CRM has no AI strategy"). This is **slot-filling pressure**: the LLM fills "AI strategy" with "the one AI feature I've seen" without verifying that's the entity's full AI surface.

Real production case: an Acme CRM brief said "the AI email assistant is parity, not differentiation, and 25 people can't catch up" — extrapolating from one feature to a categorical statement, while ignoring (a) the entity's other intelligence and analytics features and (b) the parent-organization's group-wide AI-pivot playbook across sibling portfolio brands.

### The discipline

When making a category-level claim about a capability (e.g., "X has only basic AI", "X has no security strategy", "X has no enterprise pricing"):

1. **Enumerate the entity's full feature surface** for that capability category. Check: feature page, comparison pages, help-center categories, recent blog posts, integration partners, hiring posts.
2. **Check parent / sibling-portfolio-company context.** Is there a portfolio-wide initiative for the capability?
3. **Check trajectory signals.** Job postings for engineers in the capability area, recent feature additions, Wayback delta on the relevant landing page over the last 12 months.
4. **Soften categorical claims to bounded ones.** "Has no AI strategy" → "Current AI surface is limited to email-drafting; broader category answer requires multi-month investment but is roadmap-feasible via parent-network playbook."
5. **Avoid quasi-deterministic verbs:** never / categorically / cannot / impossible without explicit Tetlock probability + resolution criterion.

---

## §19 — Negation-evidence rule (technique #67)

### The failure mode

The dossier publishes claims of absence ("no SOC 2", "no proprietary data asset", "no marketplace presence") without explicit negative-evidence (the absence observed at a specific URL, captured at a specific time). Absence-claims are invisible to standard hallucination audits because they don't have a specific number to verify against.

### The discipline

For every "no X" / "X is missing" / "X is not disclosed" claim:

1. **Specify the surface where you looked.** "No SOC 2 disclosed on [Trust Center](https://trust.example.com/)" — not just "no SOC 2."
2. **Specify what you looked for.** "Searched for `SOC 2`, `Type II`, `attestation`, `compliance` strings on the page."
3. **Capture the snapshot date.** "As of 2026-04-27."
4. **Acknowledge the asymmetry.** Negative evidence is weaker than positive — the entity may have private SOC 2 audits, may have it under NDA, may publish it on a sales-only page. Never claim "X has never had SOC 2"; only "X does not currently disclose SOC 2 publicly."

### Required action

Pre-publication scan: every "no", "not", "absent", "missing", "without", "lacks" claim about an entity must be paired with (a) the URL where the absence was observed, (b) the snapshot date, (c) the strings that were searched.

---

## §20 — Quasi-deterministic-claim guard (technique #68)

### The failure mode

The dossier uses verbs like "categorically beyond", "cannot trivially", "will never", "must fail", "can't compete" — these are **forecasts disguised as facts**. They feel authoritative but make falsifiable predictions about uncertain futures without explicit probability or resolution criterion.

Real production case: an Acme CRM brief said agentic features were "categorically beyond Acme CRM's product velocity" — implying impossibility. The reality is that HoldCo Group has an industrialized AI-pivot playbook across sibling portfolio brands, making 12-18-month delivery realistic.

### The discipline

The following verbs / phrases trigger Tetlock-discipline review:

| Phrase | Required treatment |
|---|---|
| "categorically beyond" | Replace with point probability + resolution date OR specific time horizon ("12-18 months out") |
| "cannot trivially / cannot easily" | Replace with effort estimate ("requires multi-quarter investment") |
| "will never" | Replace with Tetlock probability ("≤10% in next 24 months") + resolution criterion |
| "must / always / inevitable" | Replace with conditional ("if X holds, Y follows") + the conditioning fact |
| "impossible / no path" | Replace with bounded-difficulty framing ("no public path; could emerge from <route>") |
| "guaranteed / certain to" | Replace with high-confidence Tetlock band (85-95%) + reasoning |

### Required action

Pre-publication scan: grep the dossier for these phrases and rewrite each instance with a Tetlock-compatible equivalent OR an explicit time horizon OR an effort estimate.

```bash
# Find absolute claims that need a horizon or a probability
grep -nE '\b(categorically|cannot trivially|will never|must (be|have|fail)|impossible|guaranteed|inevitable|never |always |only)\b' "$OUTPUT"
```

---

## §21 — Comparator-pricing source rule (technique #69)

### The failure mode

In a competitive analysis, the dossier cites competitor pricing ("Pipedrive $24-69", "HubSpot Sales Hub $20-50") inline without a citation link to that competitor's own pricing page. Competitor prices change frequently — these become stale fast and are also factually unverified by readers.

Real production case: an Acme CRM brief stated "parallel to Pipedrive Essential ($24)–Power ($69) and below HubSpot Sales Hub Starter ($20–$50)" — neither competitor price had a source citation.

### The discipline

For every competitor price cited in §8 or §10 of any dossier:

1. **The price must link to the competitor's own /pricing page** (not a third-party aggregator, not a comparison site).
2. **OR cite a Wayback snapshot** with the date of capture.
3. **OR explicitly mark as "directional bands only — verify at <competitor>/pricing"** rather than implying current-day precision.

### Required action

Pre-publication scan: any `$XX` or `€XX` figure in §8 or §10 attributed to a competitor must have an inline link to that competitor's /pricing or Wayback snapshot. Otherwise rewrite with the "directional only" disclaimer.

---

## §22 — Subagent-audit blindspot rule (technique #70)

### The failure mode

The Step 6 hallucination audit subagent has access to the same context as the writer. It can verify "is this claim cited?" but it cannot verify "is the cited source actually authoritative for this claim?" Audit subagents inherit the writer's blind spots about source coverage, source freshness, and category-claim extrapolation.

Real production case: the Step 6 subagent on the AcmeCRM brief flagged 3 issues (portfolio-count contradiction, deal-date precision, §23 audit-row honesty) but missed 5 material errors (HoldCo Group founder count, portfolio scale stale, headcount-narrative blind spot, AI-thesis blind spot, deal-close-date wrong). The reader's external validation caught all 5.

### The discipline

Step 6 hallucination audit subagent should be instructed to:

1. **Re-fetch a sample of cited URLs** rather than only checking that citations exist. Sample at least 3 high-priority citations (parent leadership, headline metrics, vendor-claimed scale).
2. **Specifically search for the absence patterns** that the writer's source-gathering missed:
   - Did the writer check `<entity-domain>/comparison/` for user-employer-targeted pages?
   - Did the writer check the entity's /about page for parent-network disclosures?
   - Did the writer cite any T3 aggregator data with age ≥ 12 months?
   - Did the writer say "not publicly disclosed" anywhere without verification-ladder evidence?
   - Did the writer make any single-feature → category-claim extrapolations?
3. **Flag categorical claims for Tetlock review** (per technique #68).
4. **Acknowledge audit-quality limits in the audit's output**: "I have the same source-context as the writer; reader-side validation against fresh sources may surface items I cannot."

### Required action

Update SKILL.md Step 6 hallucination audit prompt with subagent instructions covering technique #70's audit-discipline checks.

---

## §23 — Load-bearing claim N-source rule (technique #71)

### The failure mode

A single claim is repeated across N sections of the dossier (e.g., "25-person team caps velocity" appears in §0 SWOT / §0 Playbook / §16 / §17 / §21). Because the writer trusts their own source from one section, repetition feels like reinforcement — but the underlying source count remains 1.

Real production case: the "~25-person team caps velocity" claim was load-bearing in 5 sections; underlying source was a single about-page sentence. Adding 5× repetition didn't add 5× evidence.

### The discipline

For any claim that is referenced across **3 or more sections** of the dossier:

1. **Treat it as load-bearing.** A claim repeated 3+ times is structurally important to the analysis.
2. **Require ≥2 independent sources** for the underlying fact.
3. **Require ≥3 independent sources** if the claim is in §0 (Executive Briefing).
4. **Tag the load-bearing claim** with all sources at first use; downstream uses can reference back ("per §X").
5. **Avoid amplification illusion**: repeating a single-source claim 5 times does not increase its source count. The audit must check source count, not repetition count.

### Required action

Pre-publication scan: identify every claim used 3+ times. For each: confirm ≥2 independent sources cited at first use. If not, either (a) find a second source, (b) soften to "per <single source>", or (c) reduce repetition count to ≤2.

---

## §24 — Round-number / no-methodology vendor-metric labeling (technique #72)

### The failure mode

Vendor-stated headline metrics like "40,000+ users", "96.4% customer satisfaction", "3,400+ monthly impressions" are inherited as authoritative because they're specific. **Suspiciously round numbers AND uncommon precision both indicate methodology-not-disclosed.** A "96.4% satisfaction" without methodology is no more verified than "96% satisfaction" — both should be labeled "vendor-claimed: methodology not disclosed."

Real production case: a competitor dossier inherited a vendor-claimed user / satisfaction stat without noting that the methodology was undisclosed — as did a search-impressions claim lifted from an employer-targeted comparison page.

### The discipline

For every vendor-stated headline metric:

1. **Round numbers (10,000 / 50,000 / 100,000+ / 1M+):** likely marketing rounding. Label `vendor-claimed; rounded; methodology not disclosed`.
2. **Suspicious precision (96.4% / 99.4% / 23,847):** uncommon precision implies a methodology that should be disclosed. If it's not, label `vendor-claimed; methodology not disclosed`.
3. **Self-disclosed traffic / search-volume claims** (e.g., "X gets 3,400 monthly impressions for our brand"): label `vendor-self-disclosed; not externally audited; methodology not disclosed`.
4. **Customer-satisfaction percentages without N**: label `vendor-claimed; sample-size and methodology not disclosed`.

### Required action

Pre-publication scan: every metric of the form `[0-9,]+%`, `[0-9,]+\+ users/customers/accounts`, `[0-9,]+\+ <unit>` not in a citation block must have one of the labels above.

---

## §25 — Composability with existing skill features

| Concern | File |
|---|---|
| External-source verification (T1-T4 hierarchy, Wayback, customer-logo round-trip) | `source-hierarchy.md` (Cat I, v2.6) |
| Internal-document consistency (this file) | `internal-consistency.md` (Cat J, v2.11 — techniques #50-72) |
| Hallucination audit at Step 6 | `SKILL.md` Step 6 + this file's pre-checks at Step 5 |
| Confidence-scoring composition | `confidence-scoring.md` — must support two-dimension framing for single-source-headline-metric dossiers |
| Lessons #56-78 | `lessons.md` |

---

## §26 — When to load this file

- **Mandatory** at Step 5 (Validate) for `--type=competitive|due-diligence|investment`
- **Mandatory** at Step 5 for any dossier that has been edited across multiple revisions
- **Required** before composing §23.1 Confidence — must produce two-dimension framing if headline metrics are single-source
- **Required** when any term is deprecated mid-revision — terminology-rename sweep (#59) must run before publication
- **Required** at Step 2 (Source gathering) when entity is a portfolio company / subsidiary / division → load techniques #61, #62, #63
- **Required** at Step 2 when `--type=competitive` AND user-employer-domain is known → load technique #64
- **Required** at Step 4 (Draft) when writing competitor-pricing or comparator-pricing tables → load technique #69
- **Required** at Step 4 (Draft) when writing forward-looking claims or category-level capability claims → load techniques #66, #67, #68
- **Required** at Step 6 (Hallucination audit) — subagent instructions must include technique #70
- User asks "is this dossier internally consistent?" / "is the confidence score honest?" / "are these counts right?" / "have I missed anything?"

---

## §27 — Anti-patterns

- ❌ **Trusting the LLM's first instinct on tier labels** — LLMs are systematically generous
- ❌ **Reporting "verification rate %" without counting only fully-verified items** — bundles partial evidence into the rate
- ❌ **Using two-decimal precision on synthesized estimates** — false authority
- ❌ **Calling non-independent methods "triangulation"** — misuses the term and overstates rigor
- ❌ **Single composite confidence for single-source-headline dossiers** — conflates dimensions
- ❌ **Status-quo forecasts below the persistence base rate without contrary evidence** — under-estimates inertia
- ❌ **Trusting the count without auditing the enumeration** — the number is a derived summary; the names are the underlying facts (#58)
- ❌ **Sweeping only the canonical form when deprecating a term** — inflected forms survive the rename and contradict the new framework (#59)
- ❌ **Appending revised disclosures without removing the prior version** — produces back-to-back paragraphs (#60)
- ❌ **Inferring founder identity from a quote attribution in a press release** — speakers ≠ founders (#61)
- ❌ **Citing an aggregator >12 months old as if it's current data** in fast-moving categories (#62)
- ❌ **Running headcount-velocity analysis on a portfolio company without acknowledging parent-network resources** (#63)
- ❌ **Skipping the comparison-directory probe in `--type=competitive` mode** — misses the highest-leverage source (#64)
- ❌ **Claiming "not publicly disclosed" without running the verification ladder** (legal firms / deal databases / regulatory filings) (#65)
- ❌ **Extrapolating from a single feature observation to a category-level claim** — slot-filling pressure (#66)
- ❌ **Publishing absence-claims (no X) without specifying surface, snapshot date, and search strings** — invisible to audit (#67)
- ❌ **Using "categorically beyond / cannot trivially / will never" without Tetlock probability + resolution criterion** — forecast disguised as fact (#68)
- ❌ **Citing competitor prices in §8/§10 without linking to the competitor's own /pricing page** (#69)
- ❌ **Trusting Step 6 hallucination audit to catch what writer missed at source-gathering time** — audit shares writer's blind spots; require fresh-fetch sample (#70)
- ❌ **Treating claim-repetition as evidence-multiplication** — a 1-source claim repeated 5× is still a 1-source claim (#71)
- ❌ **Inheriting suspiciously precise vendor metrics without "methodology not disclosed" label** (#72)
