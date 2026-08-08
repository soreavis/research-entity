# Stage Templates — `--stage=<stage>`

Loaded by the `research-entity` skill at Step 1 (Plan) when `--stage=` is set OR auto-detected from `/about` + funding rows. Tunes which sections get emphasis, which metrics matter, and which red flags to surface.

A SaaS company at seed needs different scrutiny than a public company. The default 23-section template is stage-neutral; this file maps stage to section weight.

## Supported stages

| Stage | Auto-detect heuristics | Section emphasis | Skip / de-emphasize |
|---|---|---|---|
| `seed` | Founders ≤3 yrs since incorporation; <$5M raised; team <15 | §3 Founders, §11 Community, §12 Data Asset, §16 Risks | §10 Heat Map (too early), §15 Press cadence, §8 ARR signals |
| `series-a` | $5–20M raised; 10–50 employees; named lead VC | §4 Funding (lead-investor thesis), §7 Features (PMF signal), §9 Customer Base (early logos), §17 Decision Tree | Cost-consolidation math, multi-region expansion |
| `series-b` | $20–60M raised; 50–200 employees; ≥1 follow-on | §0 Scorecard (R40, NRR, magic number), §8 Pricing (packaging maturity), §10 Competition, §16 Risks (sales efficiency) | Brand/press depth |
| `series-c+` | $60M+ raised; 200+ employees; late-stage / pre-IPO | §0 + §4 + §8 + §16 + Industry Benchmarks (load `benchmarks.md`); add R40, gross margin, burn multiple | Founder-bio depth |
| `growth` | Bootstrap with $20M+ ARR (no equity rounds); profitable | §8 Pricing, §9 Customer Base (retention), §16 Risks (single-founder dependency) | §4 Funding (sparse) |
| `pe` | PE-owned; $50M+ ARR; mature operating model | Cash flow, margin, NRR cohorts, multiple-on-money potential | §11 Community (less salient) |
| `public` | Has ticker symbol on a major exchange | 10-K mining, segment reporting, guidance-vs-actuals, analyst day | §11 Reddit (replaced by 10-Q reading) |

## Per-stage template overrides

### `--stage=seed`

**Goal:** Is the team capable, is there an early signal, is the round priced sanely?

Add these sections:
- **§3.5 Team-Market Fit** — prior exits / domain expertise / hiring quality
- **§7.5 Wedge** — single use case the founders are obsessed with
- **§16.X Founder-Risk** — single technical-founder dependency, co-founder breakup risk

Skip / de-emphasize:
- §0 Heat Map (too early; replace with "what would prove this works in 12 months")
- §15 Press cadence (typically empty; skip the timeline diagram)
- Cost-consolidation math (no large customer base yet)

Confidence-score adjustment: cap at 75/100 — too little public information at seed for higher.

### `--stage=series-a`

**Goal:** Has the company found PMF, are the early customers expanding, is the GTM repeatable?

Add:
- **§9.X Repeatability Test** — same-segment logos? same buyer persona? same use case?
- **§4.X Round Dynamics** — speed (oversubscribed in 2 weeks?), valuation step-up vs seed, what the lead VC's portfolio thesis is

De-emphasize:
- Multi-region expansion (likely premature)
- Brand depth (typically thin)

### `--stage=series-b` and `--stage=series-c+`

**Goal:** Are the unit economics defensible, is the company running ahead of or behind benchmarks, what's the path to next milestone?

Required:
- **Industry benchmarks comparison** — load `benchmarks.md`; add §X Benchmarks comparing R40, NRR, magic number, payback period to median
- **§16.X Sales Efficiency** — magic number from disclosed metrics (or estimate from sales hire count + announced revenue)
- **§16.X Customer-Concentration** — load `audits.md` audit-customer-concentration if any single logo > 10% revenue

### `--stage=public`

**Goal:** What does the 10-K reveal that the website doesn't?

Required pulls:
- Latest 10-K + most recent 10-Q via SEC EDGAR (load `data-sources-extended.md`)
- Last 4 quarterly earnings transcripts (Seeking Alpha or company IR page)
- Risk Factors section verbatim (often reveals litigation, competitive risks, regulatory exposure)
- Segment reporting (revenue mix; geo mix; customer concentration if disclosed)

De-emphasize Reddit / G2; replace with analyst notes (Gartner/Forrester/Sacra), sell-side analyst targets, options-implied volatility (signal on uncertainty).

## Stage auto-detection logic

When `--stage` is not set, auto-detect by walking these checks in order. Use the first match:

```bash
# 1. Public ticker → public
if grep -qiE '\b(NYSE|NASDAQ|LSE|FTSE|TSX):\s*[A-Z]{1,5}\b' "$ABOUT_PAGE"; then STAGE=public

# 2. PE owner mentioned in /about or recent press → pe
elif grep -qiE 'acquired by|portfolio company of|backed by [A-Z][a-z]+ Partners|Vista Equity|Thoma Bravo|KKR|Blackstone' "$ABOUT_PAGE $RECENT_PRESS"; then STAGE=pe

# 3. Funding rows in §4 (parsed) → infer from latest round
elif [ -n "$LATEST_ROUND" ]; then
  case "$LATEST_ROUND" in
    Seed|Pre-seed) STAGE=seed ;;
    "Series A") STAGE=series-a ;;
    "Series B") STAGE=series-b ;;
    "Series C"|"Series D"|"Series E"|"Series F"|"Series G") STAGE=series-c ;;
  esac

# 4. No funding rows but ARR claims → growth (bootstrap)
elif grep -qiE 'bootstrapped|profitable|self-funded' "$ABOUT_PAGE"; then STAGE=growth

# 5. Default → unknown; use neutral 23-section template
else STAGE=unknown
fi
```

If auto-detection runs, surface the inference: "Detected `--stage=series-b` from `$2M Series A 2013 + ~$16M ARR`. Use `--stage=` to override."

## Stage and audience interplay

Stage modifies content emphasis; audience modifies tone + ordering. The two flags compose:

| Stage \ Audience | c-suite | investor | board | operator | technical |
|---|---|---|---|---|---|
| seed | Lead with team, dilute risk content | Lead with team + lead-VC thesis | Lead with single-founder dependency | Lead with use case + wedge | Lead with tech debt risk |
| series-b | Standard | Lead with R40/NRR/magic number | Lead with sales efficiency | Lead with packaging maturity | Lead with architecture scalability |
| public | Standard + analyst notes | Lead with valuation + 10-K Risk Factors | Lead with quarterly miss/beat history | Lead with competitive pricing pressure | Lead with security disclosures |

## When to load this file

- `--stage=` flag is set explicitly
- Auto-detection chooses a stage
- User asks "what's stage-appropriate for X?"
- Wizard Question 8 (stage selection, when added)
