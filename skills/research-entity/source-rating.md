# Admiralty Code Source Rating — `--source-rating=admiralty`

Loaded by the `research-entity` skill at Step 4 (Draft) when `--source-rating=admiralty` is set OR when `--type=due-diligence|investment` is set with `--validation=max`. Applies the formal NATO / Five Eyes 2-character source rating to every cited source, alongside or in place of the existing ad-hoc labels (`single-source` / `vendor-claimed` / etc.).

The Admiralty Code is the gold-standard source-provenance notation in intelligence work. Used by NATO ([AJP-2.1](https://www.researchgate.net/figure/NATO-AJP-21-Source-Reliability-and-Information-Credibility-Scales_tbl1_328858953)), Five Eyes (US/UK/CA/AU/NZ), and adopted by cyber threat intelligence ([SANS Institute guidance](https://www.sans.org/blog/enhance-your-cyber-threat-intelligence-with-the-admiralty-system)).

Reference: [Wikipedia — Admiralty code](https://en.wikipedia.org/wiki/Admiralty_code), [Intelligence source and information reliability](https://en.wikipedia.org/wiki/Intelligence_source_and_information_reliability).

## The 2-character notation

Every source gets a **letter-number** code: letter = source reliability (A-F), number = information credibility (1-6).

### Source reliability (letter)

| Code | Meaning | Examples in research-entity context |
|---|---|---|
| **A** | Completely reliable — no doubt of authenticity, trustworthiness, or competency; history of complete reliability | Official business register (Firmenbuch FN, Companies House, SEC EDGAR); certified compliance docs (ISO certificate); 10-K filing |
| **B** | Usually reliable — minor doubt about authenticity, trustworthiness, or competency; mostly valid information in past | Major analyst firms (Gartner, Forrester); mainstream business press (WSJ, FT, Reuters); audited financial statements from non-Big-4 |
| **C** | Fairly reliable — doubt of authenticity, trustworthiness, or competency, but has provided valid information in the past | Aggregators (Crunchbase, PitchBook, Tracxn) when the underlying source is named; vendor-published case studies |
| **D** | Not usually reliable — significant doubt; has provided valid information in past | Single-source aggregators (Latka, RocketReach) when underlying source is unverified; founder interviews retold by 3rd parties |
| **E** | Unreliable — lacks authenticity, trustworthiness, and competency; history of invalid information | Anonymous Reddit/forum posts; uncorroborated competitor claims; SEO-spam comparison pages |
| **F** | Reliability cannot be judged — no basis exists for evaluating reliability | New aggregator with no track record; anonymous tip; first-time-cited source |

### Information credibility (number)

| Code | Meaning | Examples |
|---|---|---|
| **1** | Confirmed — confirmed by other independent sources; logical in itself; consistent with other information on the subject | Multi-source-corroborated funding round (BusinessWire + Crunchbase + TechCrunch agree on amount + lead investor + date) |
| **2** | Probably true — not confirmed; logical in itself; consistent with other information on the subject | Funding round per single press release that aligns with company's growth-stage profile |
| **3** | Possibly true — not confirmed; reasonably logical in itself; agrees with some other information on the subject | Founder-claimed metric (revenue, customer count) that aligns with order-of-magnitude expectations |
| **4** | Doubtful — not confirmed; possible but not logical; no other information on the subject | Aggregator-only data with no corroboration; unusual claim that doesn't fit other evidence |
| **5** | Improbable — not confirmed; not logical in itself; contradicted by other information on the subject | Founder claim that contradicts business-register filings or audited statements |
| **6** | Truth cannot be judged — no basis exists for evaluating the validity of the information | Information from a source with no track record; first-time claim with no comparators |

## Worked examples

| Source | Original ad-hoc label | Admiralty Code | Reason |
|---|---|---|---|
| <Entity legal-name> business-register entry (e.g. Austrian Firmenbuch FN 12345a / German HRB 12345 / etc.) | (none) | **A1** | Official register, multi-source confirmable |
| ISO 27001:2022 cert claim on entity Trust page | `vendor-claimed` | **C2** | Vendor-source, plausible but not certificate-fetched |
| Latka revenue figure (founder interview) | `single-source / founder-self-reported` | **D3** | Aggregator with weak track record, founder-claimed but plausible |
| RocketReach revenue figure (likely re-published from Latka) | `aggregator-derived` | **D4** | Aggregator with weak track record, single-source-derived, doesn't add corroboration |
| Tracxn-only investor identity that doesn't reconcile to that investor's known portfolio | `unverified` | **E5** | Aggregator with credibility gap; contradicts disclosed portfolio of similarly-named firm |
| Capterra review count + rating (Capterra direct page, bot-blocked but cross-referenced) | (none) | **B2** | Established platform, plausible but not directly fetched |
| BusinessWire press release for an AI-product launch announcement | (none) | **B1** | Mainstream wire service; multi-source confirmable from PRNewswire mirror + entity press |
| Anonymous Reddit comment claiming "<entity> lost 2 customers in YYYY" | (none) | **E5** or **F6** | Anonymous + unconfirmed + unusual claim |

## When to apply

### Always apply (mandatory):
- `--type=due-diligence` (regulated buyer expectation)
- `--type=investment` (LP-readable IC memo expectation)
- `--validation=max` (highest-rigor pipeline)

### Apply on request (`--source-rating=admiralty`):
- `--type=competitive` for adversarial / litigation-adjacent dossiers
- Audience includes intel-community / military / regulator / law-enforcement-trained readers

### Skip (default):
- `--type=research|partnership` (overhead exceeds benefit for friendly audiences)
- `--depth=quick` (the source-rating cost outweighs the brief's value)

## How to integrate into the dossier

### Option 1: Inline next to source citations (most rigorous)

```markdown
The company was founded in **YYYY** ([<Entity> About page](https://www.<entity-domain>/about/) — **C2**).
Revenue is reported as $XM per [Latka, MMM-YYYY](https://getlatka.com/companies/...) — **D3** `single-source / founder-self-reported`.
```

### Option 2: Source-list-only ratings (cleaner body, ratings in §19)

```markdown
The company was founded in **YYYY** [^about].
Revenue is reported as $XM [^latka].

...

[^about]: [<Entity> About page](https://www.<entity-domain>/about/) — Admiralty: **C2**
[^latka]: [Latka, MMM-YYYY](https://getlatka.com/companies/...) — Admiralty: **D3** (`single-source / founder-self-reported`)
```

### Option 3: Per-section composite rating (executive summary)

```markdown
### §0 Source-rating composite
- **A1-B2 sources**: 23 (register + audited + multi-source press)
- **C1-D2 sources**: 89 (analyst + aggregator + vendor-claimed but plausible)
- **D3-E5 sources**: 14 (single-source-aggregator + founder-self-claim + unverified)
- **F6 sources**: 0 (no truly-unevaluable sources)

**Composite source quality**: Strong (76% in B2-or-better band)
```

## Composability with existing labels

The Admiralty Code does NOT replace our existing labels (`single-source`, `vendor-claimed`, `founder-self-claim`, `aggregator-derived`). It adds a formal cross-comparable rating ON TOP. Our labels describe WHY a source is weak; the Admiralty Code rates HOW weak.

| Our label | Typical Admiralty range | Why |
|---|---|---|
| (no label — register / audited) | A1-B2 | Strongest tier |
| `vendor-claimed` | B2-C3 | Reliable source (the vendor itself), but inherent self-interest |
| `single-source` | C3-D4 | Source may be reliable but lack of corroboration limits credibility |
| `aggregator-derived` | C2-D4 | Aggregator track record varies; depends on which aggregator |
| `founder-self-claim` | D3-E4 | Self-interested + un-auditable + sometimes contradicts other sources |
| `unverified` | E5-F6 | Active credibility gap |

A single source can carry both labels: e.g., Latka revenue figure = **D3** AND `single-source / founder-self-reported`. The Admiralty rating gives intel-trained readers a quick credibility signal; the ad-hoc label gives general-business readers a plain-English explanation.

## Quality assurance: the source-rating audit

When `--source-rating=admiralty` is set, run this scan in Step 5 (Validate):

```bash
# Count sources by Admiralty code distribution
grep -oE '\b[A-F][1-6]\b' "$DOSSIER" | sort | uniq -c | sort -rn

# Flag concerning concentrations:
# - >50% in D3-F6 band → low source quality, dossier credibility limited
# - Any cited fact in §0 BLUF rated D4 or worse → re-evaluate the BLUF claim
# - 0 sources in A1-B1 band → no anchor sources, all claims rest on aggregators
```

Surface the distribution in §23 Confidence (alongside the 5-dimension framework).

## Anti-patterns

- ❌ Rating sources without inspecting them — Admiralty Code is meaningless if applied superficially
- ❌ Defaulting every aggregator to "C3" — different aggregators have different track records (Crunchbase ≠ Tracxn ≠ Latka)
- ❌ Rating an information-piece higher than its source — the source rating caps the information rating (a D-source can't produce 1-information)
- ❌ Confusing source reliability (A-F) with information credibility (1-6) — they're independent dimensions
- ❌ Adding F6 to every uncertain source — F6 means "no basis for evaluation"; if you have ANY basis, use a real letter+number
- ❌ Replacing our ad-hoc labels rather than supplementing them — both serve different audiences; keep both

## When to load this file

- `--source-rating=admiralty` flag set
- `--type=due-diligence|investment` (auto-activated)
- `--validation=max` (auto-activated)
- User asks "rate the sources" / "how reliable is this?" / audience is intel-trained
