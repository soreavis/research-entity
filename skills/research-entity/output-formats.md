# Output Formats — `--export=exec|battle-card|vc-memo|json`

Loaded by the `research-entity` skill at Step 7 (Export) when one of the alternate output formats is set. These are condensed/repurposed views of the full 23-section dossier; they do NOT replace the canonical MD — they're additional artifacts derived from it.

## Four supported alternate formats

| Format | Length | Audience | Source dossier needed |
|---|---|---|---|
| `exec` | 1 page (PDF/HTML) | C-suite, board pre-read | Full dossier OR Scorecard + BLUF |
| `battle-card` | 1 page (PDF/HTML) | Sales reps, AEs, SDRs | Full dossier (esp. §10 Competition + §16 Risks) |
| `vc-memo` | 4–6 pages (PDF) | VCs, investment committee | Full dossier (esp. §3 Founders + §4 Funding + §10 + §16) |
| `json` | Structured data file | Downstream tooling, data pipelines | Full dossier |

## 1. Executive Summary — `--export=exec`

**Purpose:** A 1-page artifact for an executive who has 60 seconds. Pure top-of-funnel; no deep analysis.

**Content:**
1. **BLUF** (4–5 sentences from §0)
2. **Scorecard** (top 8 rows; cap at 1/3 of page)
3. **3 strengths · 3 risks** (from §0 SWOT, condensed)
4. **Verdict** (1 sentence — recommend / pass / monitor)
5. **As of** date + composite confidence + active model

**Layout:** 8.5×11 portrait, 1-inch margins, sans-serif, no mermaid diagrams (too dense for 1 page).

**Generation pipeline:**
```bash
# Extract sections from full MD
sed -n '/^## §0/,/^## §1/p' "$FULL_MD" > /tmp/section0.md  # BLUF + Scorecard + SWOT
sed -n '/^## 21\. Final Assessment/,/^## 22/p' "$FULL_MD" > /tmp/verdict.md

# Compose 1-page MD
cat > "$EXEC_MD" <<EOF
# Executive Summary — <entity>
<as-of date> · <composite confidence>/100 · <model + effort>

## What it is
<BLUF — 4 sentences>

## Scorecard (top 8)
<table extract — 8 most important rows>

## 3 strengths · 3 risks
**Strengths:** ... · ... · ...
**Risks:** ... · ... · ...

## Verdict
<1 sentence>

EOF

# Convert to PDF (single page)
pandoc "$EXEC_MD" -o "$EXEC_PDF" --pdf-engine=xelatex \
  -V geometry:margin=1in -V papersize:letter \
  --variable fontsize=10pt
```

**HTML variant:** Same content, single landing-page-style HTML; print stylesheet enforces 1-page break.

## 2. Battle Card — `--export=battle-card` (Klue FIA framework)

**Purpose:** Sales-team aid. Walk-and-talk format. "Why we win, why we lose, talk track, traps to avoid."

**Required structural framework: Klue's Fact, Impact, Act (FIA)** — each row of intel must follow Fact → Impact → Act, the dominant industry standard ([Klue blog](https://klue.com/blog/fact-impact-act-the-battlecard-framework-you-need-to-be-using)).

| Column | Definition | Bad example | Good example |
|---|---|---|---|
| **Fact** | The competitive intel itself — neutral, sourced | "They're better than us" | "<entity> ships ISO 27001:2022 certification (per Trust page)" |
| **Impact** | Why this fact matters to field teams — translates intel into deal-stage relevance | "It's important" | "Removes EU enterprise compliance objection in mid-market deals; matters most for Schrems II–sensitive prospects" |
| **Act** | Recommended action — talk track, follow-up, escalation, or qualifier | "Be aware of it" | "If prospect mentions GDPR/Schrems II, ask: 'Is your data processor's ISO 27001 cert recent — 2022 standard or older?' Steers toward our newer cert." |

### Battle card structure (FIA-enforced)

```markdown
# Battle Card: <our-product> vs <entity>
As of <date>. For <our> Sales / Sales Engineering / Solutions Consulting.

## At a glance
- **Vendor**: <entity name + founded year + last-known team band>
- **Funding**: <total raised + last round>
- **Primary product**: <one line>
- **Where they show up**: <buyer-signal categories — RFP slot, integration listing, etc.>

## Why we win (FIA, 3 rows)

| Fact | Impact | Act |
|---|---|---|
| <fact 1, sourced> | <impact for field> | <talk track> |
| <fact 2, sourced> | ... | ... |
| <fact 3, sourced> | ... | ... |

## Why they win (FIA, 3 rows — preserve credibility, don't fabricate)

| Fact | Impact | Act |
|---|---|---|
| <fact 1, sourced> | <impact — when this is decisive> | <how to neutralize / when to walk> |
| ... | ... | ... |
| ... | ... | ... |

## Their objections to handle (FIA, 3 rows)

| Fact (their pitch) | Impact (why prospects buy it) | Act (our reframe) |
|---|---|---|
| ... | ... | ... |

## Trap questions to ask the prospect

5 questions that surface answers favorable to us:
1. <question> → if answered <X>, lean into <our advantage>
2. ...

## Pricing intel
- Published tiers: <list>
- Range estimate: <range>
- Hidden costs: <list>

## Reference customers (overlap)
3 named logos where prospect may know someone:
- <Customer 1> (industry / size)
- <Customer 2> ...

## Risk signals to mention (carefully — disclosure not weaponization)

| Risk | Severity | When to mention |
|---|---|---|
| <e.g., absent SOC 2> | High for US enterprise | Only if prospect raised compliance topic |
| <e.g., recent layoff if any> | Medium | Only if prospect raised vendor-stability concerns |

## What NOT to say
- Don't claim <X> if it isn't sourced
- Don't disparage their team / product personally
- Don't quote competitor pricing as fact (it changes; cite ranges)
```

**Layout:** 8.5×11 landscape, 2-column, color-coded sections (Fact = blue, Impact = orange, Act = green to mirror Klue's color scheme).

**Critical anti-patterns**:
- ❌ FIA where Fact is unsourced → Klue calls this "battle card erosion"; the rep loses credibility on first prospect challenge
- ❌ FIA where Impact is generic ("it's important") → useless for field teams; must be deal-stage-specific
- ❌ FIA where Act is missing → defeats the purpose of the framework; every row must end in an action
- ❌ "Why we lose" rows where the fact is fabricated → sales reps lose deals when they parrot fake competitive points
- ❌ Battle card without sourcing → 50%+ of Klue's customer-reported battle-card failures stem from un-sourced intel

**Generation requires:** the user's own employer/product context. If unknown, prompt: "Battle card needs your own company's positioning. Provide product name + your 3 differentiators, OR I'll output a generic competitive intel one-pager instead."

## 3. VC Memo — `--export=vc-memo`

**Purpose:** Investment committee pre-read. Standard VC memo template (typically followed by Sequoia/a16z/Bessemer/etc.).

**Content (in order):**
1. **Recommendation** (1 paragraph: invest at $X / pass / pursue at $Y)
2. **Company** — what it does, founded when, where based, founders + key team
3. **Market** — TAM size, growth rate, competitive landscape, why now
4. **Product** — what's been built, demo highlights, technical differentiation
5. **Traction** — revenue, growth rate, NRR, customer list, key wins
6. **Team** — founder backgrounds, key hires, gaps
7. **Round dynamics** — round size, pre/post valuation, lead/participation, use of funds
8. **Risks** — 3 most material (technical, market, team, regulatory)
9. **References** — customer references called, founder references called
10. **Decision matrix** — if X happens within Y, then we...

**Length:** 4–6 pages. Heavy on traction + team + risks (the three things ICs actually debate).

**Layout:** Portrait, 11pt body, 1-inch margins, footer with page X of Y.

**Required inputs from full dossier:**
- §3 Founders & Senior Leadership — for Team section
- §4 Funding & Investors — for Round Dynamics
- §7-8 Product + Pricing — for Product
- §9 Customer Base + §11 Community — for Traction
- §10 Market Positioning — for Market
- §16 Risks — for Risks (top 3 chosen)

**For VC-grade rigor**: Pair `--export=vc-memo` with `--depth=deep` and `--validation=max`. A VC memo with single-source-only claims is a credibility risk.

## 4. JSON Export — `--export=json`

**Purpose:** Structured data feed for downstream tooling (CRM enrichment, BI dashboards, data warehouse, MCP server).

**Schema (canonical):**

```json
{
  "schema_version": "1.0",
  "research_date": "2026-04-27",
  "researcher": "research-entity skill v<x.y>",
  "model": "claude-opus-4-7",
  "effort": "max",
  "validation": "max",
  "depth": "deep",
  "composite_confidence": 87,
  "entity": {
    "name": "Acme Corp",
    "trade_name": "Acme",
    "legal_name": "Acme Corporation, Inc.",
    "domain": "https://acme.example",
    "linkedin": "https://www.linkedin.com/company/acme",
    "founded": "2018-03-15",
    "hq": {"city": "San Francisco", "state": "CA", "country": "US"},
    "incorporation": {"jurisdiction": "Delaware", "type": "C-Corp"},
    "registers": [
      {"register": "CA SOS", "id": "C1234567", "url": "https://bizfileonline.sos.ca.gov/..."}
    ]
  },
  "founders": [
    {"name": "Jane Doe", "linkedin": "...", "role": "CEO", "prior": "Stripe (Eng)"}
  ],
  "funding": {
    "total_raised_usd": 50000000,
    "latest_round": {"series": "B", "amount_usd": 35000000, "date": "2025-09-12", "lead": "Sequoia", "post_money_usd": 250000000},
    "rounds": [...]
  },
  "scorecard": [
    {"row": "Founded", "value": "2018", "source": "[Crunchbase](...)", "signal": "..."}
  ],
  "swot": {
    "strengths": [...], "weaknesses": [...], "opportunities": [...], "threats": [...]
  },
  "competitors": [
    {"name": "Aurasell", "tier": "ai-native-peer", "url": "...", "funding_usd": 30000000}
  ],
  "customers": [
    {"name": "BigCo Inc", "logo_url": "...", "case_study_url": "...", "vertical": "fintech"}
  ],
  "risk_scan": {
    "composite": "Medium",
    "findings": [
      {"pattern": "layoffs", "severity": "Medium", "date": "2025-11", "source": "..."}
    ]
  },
  "compliance": {
    "soc2": {"type": "II", "as_of": "2024-Q4", "url": "..."},
    "iso27001": {"version": "2022", "url": "..."},
    "gdpr": true, "hipaa_on_request": true
  },
  "sources": {
    "primary": [...], "press": [...], "aggregators": [...], "community": [...]
  },
  "glossary": [
    {"term": "ARR", "definition": "Annual Recurring Revenue"}
  ]
}
```

**Generation:** Parse the full MD; populate the JSON object section by section. Validate with `jq` before saving.

**Output path:** `<dossier-base>.json` next to the MD.

**Use cases:**
- Feed to CRM (Salesforce/HubSpot custom objects)
- Power BI / Looker dashboards
- Vector-DB embedding for RAG queries
- Skill self-MCP server (load `mcp-server.md`)

## Format composition

`--export=` accepts a comma-separated list:
```
--export=md,html,exec,json
```

Generates all listed formats from the same source. JSON is always derived from the full MD; exec/battle-card/vc-memo are derived condensations.

## Anti-patterns

- ❌ Generating exec without source dossier (no place to validate from)
- ❌ Generating battle card without user's own product context (becomes generic)
- ❌ Generating VC memo without `--validation=max` for due-diligence claims
- ❌ Generating JSON with stale schema version (always declare `schema_version`)
- ❌ Including PHI / financial data in JSON without explicit user consent (data-pipeline downstream may not have right permissions)

## When to load this file

- `--export=` includes `exec`, `battle-card`, `vc-memo`, or `json`
- User asks for "1-page summary" / "battle card" / "investment memo" / "JSON export"
- Convert-only mode where the user wants a derived format from existing dossier
