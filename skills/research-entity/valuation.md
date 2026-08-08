# Valuation Methodologies — `--valuation=<method>`

Loaded by the `research-entity` skill at Step 4 (Draft) when `--valuation=` is set OR auto-activated for `--type=investment` with `--depth=deep`. Implements the four canonical valuation methodologies from investment banking + private equity practice: **DCF**, **Comparable Transactions**, **Public-Comp Multiples**, and **LBO modeling**.

For `--type=investment` dossiers (VC IC memos, PE LOI prep, M&A target screens), the valuation section is the load-bearing page. Without it, the dossier produces context but not a decision.

## When each method applies

| Method | Best for | Time horizon | Required disclosures |
|---|---|---|---|
| **DCF (Discounted Cash Flow)** | Mature SaaS with predictable cash flows | 5-10 year explicit + terminal | Revenue model, margin, capex |
| **Comparable Transactions** | M&A target with peer-deal precedents | Trailing 24-36 months | At least 5 comparable deal terms |
| **Public-Comp Multiples** | Companies with public comparables | Current market | EV/Revenue, EV/EBITDA, P/E if applicable |
| **LBO Model** | PE acquisition candidates | 5-7 year hold | Cash flow, debt capacity, exit multiple |

`--valuation=all` runs all 4 (recommended for `--type=investment` IC memos).

## 1. DCF (Discounted Cash Flow)

The "first principles" valuation: project the entity's free cash flows + discount to present value at the cost of capital.

### Output template (insert as §X DCF Valuation)

```markdown
### X. DCF Valuation

#### Assumptions
- **Revenue base year (2026)**: $X M (`single-source / founder-self-reported` per Latka — see §16.7)
- **Revenue growth (5-year explicit)**: Year 1: __% / Y2: __% / Y3: __% / Y4: __% / Y5: __%
- **Terminal growth rate**: 3% (long-term GDP-rate proxy for mature SaaS)
- **EBITDA margin (steady-state)**: __% (estimated from peer-comp Bessemer Cloud Index 2025 mid-quartile)
- **Tax rate**: 21% (US federal corp baseline; entity is Delaware-incorporated per §2)
- **Capex % of revenue**: __% (low for SaaS)
- **Working capital change**: ~5-10% of revenue change
- **WACC (discount rate)**: __% (estimated; see calculation below)

#### WACC calculation

| Component | Value | Source |
|---|---|---|
| Risk-free rate (10-yr Treasury) | __% | as of <date> |
| Equity risk premium | 5.5% | Damodaran 2026 estimate |
| Beta (private; estimated from public CRM peers) | ~1.2 | Inferred from Salesforce/HubSpot levered betas |
| Cost of equity | __% | Rf + β × ERP |
| Cost of debt (after-tax) | __% | Limited debt for bootstrap; assume 6% pre-tax |
| Capital structure (E/(D+E)) | ~95% | Bootstrap = mostly equity |
| **WACC** | **__%** | Weighted avg |

#### 5-year projection + terminal value

| Year | Revenue ($M) | EBITDA ($M) | Capex ($M) | Δ WC ($M) | FCF ($M) | Discount factor | PV ($M) |
|---|---|---|---|---|---|---|---|
| 2027 | __ | __ | __ | __ | __ | __ | __ |
| 2028 | __ | __ | __ | __ | __ | __ | __ |
| 2029 | __ | __ | __ | __ | __ | __ | __ |
| 2030 | __ | __ | __ | __ | __ | __ | __ |
| 2031 | __ | __ | __ | __ | __ | __ | __ |
| Terminal | __ | __ | — | — | TV = FCF<sub>2031</sub> × (1+g) / (WACC-g) | __ | __ |

**Sum of PV (Enterprise Value)**: $__ M
**Less: net debt** (cash − debt): $__ M
**Equity Value**: $__ M

#### Sensitivity analysis

| WACC \ Terminal Growth | 2% | 3% | 4% |
|---|---|---|---|
| 9% | $__ | $__ | $__ |
| 11% | $__ | $__ | $__ |
| 13% | $__ | $__ | $__ |

#### Caveats

- Revenue base year is `single-source / founder-self-reported` — DCF is only as good as the underlying number; a $5M revenue overstatement compounds to $50M+ EV overstatement
- Bootstrap entities have lumpy cash flows; "steady-state" assumptions may not hold
- WACC for private companies is highly subjective; sensitivity range matters more than point estimate
```

## 2. Comparable Transactions (M&A Comps)

Identify recent M&A transactions involving similar entities; derive valuation multiples from those deals.

### Output template

```markdown
### X. Comparable Transactions Analysis

Per IB practice — recent M&A transactions in the same vertical/stage; deal-multiples applied to target.

#### Comp universe (5+ comparable deals, last 36 months)

| Target | Acquirer | Date | Deal value ($M) | Target Revenue ($M) | EV/Revenue | Notes |
|---|---|---|---|---|---|---|
| Pipedrive | Vista Equity Partners | June 2020 | ~$1,500 | ~$90 | ~16.7× | PE roll-up; mid-market CRM |
| Insightly | Unbounce (merged) | July 2024 | not disclosed | ~$15-25M est. | n/a | Strategic merger not pure acquisition |
| Copper CRM | (still independent) | n/a | n/a | n/a | n/a | Comp not avail |
| <Comp 4> | <Acquirer> | <date> | $__ | $__ | __× | <notes> |
| <Comp 5> | <Acquirer> | <date> | $__ | $__ | __× | <notes> |

#### Applied multiples

| Multiple | Median | 25th-pctile | 75th-pctile |
|---|---|---|---|
| EV/Revenue | __× | __× | __× |
| EV/EBITDA | __× | __× | __× |

#### Implied valuation range for target

| Approach | Multiple | Target metric | Implied EV |
|---|---|---|---|
| EV/Rev (median) | __× | $X M revenue (`single-source`) | $__M |
| EV/Rev (25th-pctile) | __× | $X M revenue | $__M |
| EV/Rev (75th-pctile) | __× | $X M revenue | $__M |

**Implied EV range**: $__M – $__M (median: $__M)

#### Caveats

- Deal-multiples vary widely by buyer type (strategic vs. PE) and market conditions (2021 peak vs. 2024 trough)
- Private deals often don't disclose terms; comp set is necessarily incomplete
- Older comps (>24 months) get less weight as market conditions shift
```

## 3. Public-Comp Multiples

Public companies in the same vertical; trading multiples applied as a relative-valuation cross-check.

### Output template

```markdown
### X. Public-Comp Multiples Analysis

Per Bessemer Cloud Index methodology — public-SaaS comparables provide a market-based valuation cross-check.

#### Public comp set (CRM / mid-market SaaS)

| Company (Ticker) | Market Cap ($B) | Revenue (TTM, $M) | EV/Revenue | YoY Growth | NRR | Rule of 40 |
|---|---|---|---|---|---|---|
| Salesforce (CRM) | $__ | $__ | __× | __% | __% | __ |
| HubSpot (HUBS) | $__ | $__ | __× | __% | __% | __ |
| Microsoft (MSFT — Dynamics segment est.) | n/a | n/a | n/a | n/a | n/a | n/a |
| Freshworks (FRSH) | $__ | $__ | __× | __% | __% | __ |
| Zendesk (private) | n/a | n/a | n/a | n/a | n/a | n/a |

#### Multiples summary

| Multiple | Median | Mean | Range |
|---|---|---|---|
| EV/Revenue (current) | __× | __× | __ – __× |
| EV/Revenue (forward) | __× | __× | __ – __× |

#### Adjustments for private mid-market entity

Public-comps trade at a **liquidity premium**; private mid-market entities trade at a **discount of 25-40%**.

| Approach | Public median | Private discount | Implied private multiple |
|---|---|---|---|
| EV/Revenue | __× | -30% | __× |
| Implied EV | — | — | $__M |

#### Caveats

- Public-comps are large-cap; mid-market entity deserves substantial discount for size + liquidity
- Subscale operators trade at lower multiples even before the private-discount
- 2026 multiples are compressed vs. 2021 peak; cycle-adjustment matters
```

## 4. LBO Modeling

For PE buyers — solve for entry price + leverage that produces target IRR over 5-7 year hold.

### Output template

```markdown
### X. LBO Analysis (PE Sponsor Perspective)

Per PE practice — solve for the maximum entry price that produces a 20%+ IRR with a 5-7 year hold + 3-5x money multiple.

#### Assumptions

| Assumption | Value | Source |
|---|---|---|
| Entry year | 2026 | — |
| Hold period | 5 years (exit 2031) | Standard PE hold |
| Target IRR | 20% | Mid-market PE benchmark |
| Target money multiple | 3.0× | Mid-market PE benchmark |
| Exit EV/Revenue multiple | __× | Per public comps + discount |
| Debt capacity | ~5-7× EBITDA | Standard for stable SaaS |
| Leverage at close | __% of EV | Bank financing |
| Cost of debt | 8% | Mid-market term loan |
| Operational improvement (revenue CAGR) | __% | Modest under PE ownership |
| Operational improvement (EBITDA margin expansion) | +500 bps over 5yr | Standard PE thesis |

#### LBO output

| Year | Revenue ($M) | EBITDA ($M) | Debt ($M) | Cash ($M) | Equity Value ($M) |
|---|---|---|---|---|---|
| 2026 (entry) | __ | __ | __ | __ | __ |
| 2027 | __ | __ | __ | __ | __ |
| 2028 | __ | __ | __ | __ | __ |
| 2029 | __ | __ | __ | __ | __ |
| 2030 | __ | __ | __ | __ | __ |
| 2031 (exit) | __ | __ | __ | __ | __ |

**Exit equity value**: $__M
**MoM (Money on Money)**: __×
**IRR**: __%

#### Maximum bid price (solve for IRR=20%)

Working backwards from a 20% IRR target:
- Maximum entry EV: $__M
- Subtract net debt (none for bootstrap entity): $__M
- **Maximum equity check**: $__M

#### Caveats

- Bootstrap entities often lack the EBITDA margin to support standard PE leverage (5-7× EBITDA)
- Debt capacity for $X M revenue × Y% EBITDA margin = ~$Z M of debt — limits LBO economics
- Operational improvement assumptions are speculative without insider access
```

## Composite valuation summary

Insert at end of all valuation methods:

```markdown
### X.5 Valuation Composite

| Method | Implied EV ($M) | Confidence (ICD 203) |
|---|---|---|
| DCF | $__M – $__M | Low (depends on revenue base year + WACC) |
| Comparable transactions | $__M – $__M | Moderate (5+ comp deals) |
| Public-comp multiples | $__M – $__M | Moderate (public data is reliable; private discount is judgment) |
| LBO (max bid) | $__M – $__M | Low (depends on EBITDA + debt capacity) |
| **Composite range** | **$__M – $__M** | — |

**Football-field chart** (recommended): mermaid bar chart showing each method's range.

**Recommendation**: At entry of $X M ($Y M-$Z M range), the deal is [attractive / fair / unattractive] given target IRR of 20%+ over 5-year hold.
```

## When to load this file

- `--valuation=` flag set with any value (`dcf`, `comps`, `public-multiples`, `lbo`, `all`)
- `--type=investment` AND `--depth=deep` (auto-activated)
- `--export=vc-memo` (auto-includes a valuation section per VC IC memo convention)
- User asks "what's it worth?" / "valuation" / "DCF" / "comparable transactions" / "LBO"

## Anti-patterns

- ❌ DCF without sensitivity analysis — single-point output false precision
- ❌ Comp set with <3 deals — too thin to derive median/range
- ❌ Public comps without private discount — overstates value
- ❌ LBO with debt capacity exceeding EBITDA reality — math doesn't close
- ❌ Composite range that doesn't acknowledge the underlying revenue uncertainty (when revenue is `single-source`, the entire valuation cascades from that one number)
- ❌ Failing to surface the load-bearing assumption — every valuation rests on 1-2 critical assumptions; surface them explicitly
