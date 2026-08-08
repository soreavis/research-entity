# Strategic Frameworks — PESTEL, Porter's 5 Forces, VRIO, Value Chain

Loaded by the `research-entity` skill at Step 4 (Draft) when `--framework=` is set, OR auto-activated for `--type=due-diligence|investment` and certain verticals where regulatory/structural analysis is non-negotiable. Implements the four canonical strategic-analysis frameworks from McKinsey/BCG/Bain commercial DD work.

These frameworks are the "old guard" of strategic analysis — they predate competitive-intelligence software (Klue, Crayon) by decades and remain the structured-thinking backbone of every Big 4 CDD report.

## Supported frameworks

| Framework | Origin | When most relevant |
|---|---|---|
| **SWOT** | Stanford 1960s | Default; broad strategic snapshot (already in §0) |
| **PESTEL** | Aguilar 1967 (ETPS) → expanded 1980s | When regulatory/macro context is dominant (`--vertical=govtech\|healthcare\|fintech\|legaltech`) |
| **Porter's 5 Forces** | Porter, *Competitive Strategy* 1980 | Industry-structure analysis; competitive intensity |
| **VRIO** | Barney 1991 (resource-based view) | Identifying sustainable competitive advantage |
| **Value Chain Analysis** | Porter, *Competitive Advantage* 1985 | Operational deep-dive; cost vs differentiation |

## Activation

```
--framework=swot                        # default; SWOT only (in §0 as today)
--framework=pestel                      # PESTEL replaces or supplements SWOT
--framework=swot,pestel                 # both
--framework=swot,pestel,porter5         # SWOT + PESTEL in §0; Porter 5 Forces in §10
--framework=all                         # SWOT + PESTEL + Porter5 + VRIO + Value Chain
```

Auto-activated by `--vertical=`:

| Vertical | Auto-frameworks (in addition to SWOT) |
|---|---|
| healthcare | PESTEL (HIPAA + reimbursement + state regs dominate) |
| fintech | PESTEL (CFPB + OCC + state-MTL + GDPR dominate) |
| govtech | PESTEL (FedRAMP + GSA + state procurement dominate) |
| edtech | PESTEL (FERPA + COPPA + district procurement dominate) |
| legaltech | PESTEL (ABA Model Rules + state bar + e-discovery dominate) |
| consumer | Porter 5 Forces (App Store policy + competitive substitutes dominate) |
| devtools | VRIO (proprietary tech / docs / community as the moat question) |
| deeptech | VRIO + Value Chain (IP defensibility + manufacturing/scaling) |

## 1. PESTEL Framework

Insert as `§10.X PESTEL Analysis` (or replace §0 SWOT if `--framework=pestel-only`).

```markdown
### 10.X PESTEL Analysis

Per the PESTEL framework — six categories of macro/structural forces shaping the entity's environment over the next 18-36 months.

| Force | Specific factors affecting <entity> | Direction (next 18mo) | Impact magnitude |
|---|---|:-:|:-:|
| **Political** | <relevant administration / regulatory body / int'l-relations factors> | ↑ / ↓ / → | High / Med / Low |
| **Economic** | <interest rates / inflation / FX / capex cycles relevant to entity> | ↑ / ↓ / → | High / Med / Low |
| **Social** | <demographic / behavioral / cultural shifts affecting demand> | ↑ / ↓ / → | High / Med / Low |
| **Technological** | <relevant tech shifts: AI commoditization / cloud / new standards> | ↑ / ↓ / → | High / Med / Low |
| **Environmental** | <ESG / climate / sustainability factors; supply-chain exposure> | ↑ / ↓ / → | High / Med / Low |
| **Legal** | <upcoming legislation / case law / regulatory enforcement; standards> | ↑ / ↓ / → | High / Med / Low |

#### Worked example (CRM SaaS)

| Force | Factor | Direction | Impact |
|---|---|:-:|:-:|
| Political | EU AI Act phase-in (high-risk AI obligations); US state AI bills | ↑ | Med — adds compliance overhead |
| Economic | SaaS spending rationalization; "do-more-with-less" CFO posture | → | Med — favors consolidators (TCO claim relevant) |
| Social | Remote/hybrid sales norm; AI-augmented seller expectation | ↑ | High — favors AI-native CRMs |
| Technological | MCP standardization; agent frameworks; commodity LLMs | ↑ | High — table-stakes by 2027 |
| Environmental | Limited direct exposure (SaaS); customer ESG asks for vendor disclosures | → | Low |
| Legal | GDPR continuing enforcement; US state privacy laws (CA, CO, VA, etc.) proliferating | ↑ | Med — DPA/sub-processor lists become RFP-stage |

#### Strategic implications

The dominant PESTEL forces over the next 18 months are **Technological** (MCP/agent standardization) and **Social** (AI-augmented seller expectation). Both favor AI-native CRMs broadly; the question for any specific CRM is execution depth, not category positioning.
```

## 2. Porter's 5 Forces

Insert as `§10.X Porter's 5 Forces` in the Market Positioning section.

```markdown
### 10.X Porter's 5 Forces — Industry Structure

Per Michael Porter's 1980 framework — five competitive forces shaping industry profitability.

| Force | Strength (1-5) | Why |
|---|:-:|---|
| **1. Threat of New Entrants** | <1-5> | <How easy is it for new entrants? Capital required? Regulatory barriers? Brand-equity moats?> |
| **2. Bargaining Power of Suppliers** | <1-5> | <Who supplies the entity? AWS/cloud? OpenAI/Anthropic for LLMs? How concentrated?> |
| **3. Bargaining Power of Buyers** | <1-5> | <Who buys? How concentrated? Switching cost? Multi-vendor norm?> |
| **4. Threat of Substitute Products** | <1-5> | <What replaces the entity's product? Adjacent categories? Build-vs-buy? Spreadsheets?> |
| **5. Competitive Rivalry** | <1-5> | <How many competitors? How differentiated? Price-based or innovation-based?> |

**Composite industry attractiveness**: <1-5> (Average of forces; lower = more attractive industry to be in)

#### Worked example (CRM SaaS)

| Force | Strength | Why |
|---|:-:|---|
| 1. Threat of New Entrants | 4 (high) | Low capital barrier (SaaS open-source CRMs exist); AI-native peers raised $272.5M cumulatively; Bessemer benchmarks show Series A in 12-18 months from idea |
| 2. Bargaining Power of Suppliers | 3 (medium) | AWS / OpenAI / Anthropic are oligopolistic but not monopolistic; switching cost is moderate; some OSS alternatives |
| 3. Bargaining Power of Buyers | 4 (high) | CRM is shopped (G2/Capterra are decision points); switching cost is real but multi-vendor stack is normal; price-sensitive |
| 4. Threat of Substitutes | 3 (medium) | Spreadsheets + email + Slack still dominate sub-10-seat orgs; vertical-specific tools (real-estate, mortgage) substitute in niches |
| 5. Competitive Rivalry | 5 (very high) | Salesforce + HubSpot + Microsoft + Pipedrive + Zoho + monday + AI-native cohort = >100 funded competitors |

**Composite**: 3.8 — **structurally hard industry**. Profitability accrues to scaled players (Salesforce, HubSpot) and niche specialists (Veeva for healthcare, etc.); mid-market generalists struggle on sustained margin.
```

## 3. VRIO Framework

Insert as `§10.X VRIO Analysis` for `--vertical=devtools|deeptech` or `--type=investment`.

```markdown
### 10.X VRIO — Sustainable Competitive Advantage

Per Jay Barney's 1991 Resource-Based View — analyze each major resource/capability of the entity through 4 questions.

For each load-bearing asset, mark Yes/No across V (Valuable) → R (Rare) → I (Inimitable) → O (Organized to capture value):

| Resource / Capability | V | R | I | O | Verdict |
|---|:-:|:-:|:-:|:-:|---|
| <Asset 1> | Y/N | Y/N | Y/N | Y/N | Sustained competitive advantage / Temporary advantage / Competitive parity / Disadvantage |

#### Worked example (CRM SaaS)

| Resource | V | R | I | O | Verdict |
|---|:-:|:-:|:-:|:-:|---|
| ISO 27001 + ISO 9001 double-cert | Y | Y | N (other vendors can pursue) | Y | Temporary advantage (24-36mo until peers match) |
| Multi-year content / community franchise (sizable contributor base, large content library) | Y | Y | Y (multi-year build, network effect) | Y? (depends on whether monetized as standalone product) | Potential sustained advantage |
| Multi-year visual-product UX | Y | N (other vendors have visual UX) | N | Y | Competitive parity |
| <entity-AI-product> (built on third-party LLM) | Y | N (third-party-LLM access is commoditized) | N | Y | Competitive parity |
| MCP server (recent) | Y | N (large peers shipped 9-11mo earlier) | N | Y | Competitive parity (catching up) |
| Low-cost-region engineering structure | Y | Y (US/Western European peers may not have this) | Y (geography hard to replicate) | Y | Sustained advantage |

**Sustained advantages**: content-marketing asset + low-cost-region engineering structure. Both are foundational to a long-term thesis.
**Temporary advantages**: ISO double-cert (peers can match in 24-36mo).
**Parity**: visual UX + AI-product + MCP — these are table-stakes, not differentiators.
```

## 4. Value Chain Analysis

Insert as `§10.X Value Chain` for `--vertical=deeptech|consumer` or `--audit=tech-stack`.

```markdown
### 10.X Porter's Value Chain

Per Porter's 1985 framework — disaggregate the entity's operations into primary + support activities, identify cost drivers and differentiation sources.

#### Primary activities

| Activity | Description for <entity> | Cost driver | Differentiation source |
|---|---|---|---|
| **Inbound Logistics** | <how inputs reach the entity> | ... | ... |
| **Operations** | <how the product is built/delivered> | ... | ... |
| **Outbound Logistics** | <how the product reaches customers> | ... | ... |
| **Marketing & Sales** | <how the entity acquires customers> | ... | ... |
| **Service** | <post-sale support, success, renewal> | ... | ... |

#### Support activities

| Activity | Description | Notes |
|---|---|---|
| **Procurement** | <vendors / cloud / tools> | ... |
| **Technology Development** | <R&D, AI integration, platform> | ... |
| **HR Management** | <hiring, retention, comp structure> | ... |
| **Firm Infrastructure** | <legal, finance, governance> | ... |

#### Margin opportunities

The framework's purpose is to identify WHERE margin lives in the value chain. For a SaaS CRM:
- **Operations** (cloud cost / multi-tenant efficiency) — typically 15-25% of cost
- **Marketing & Sales** (CAC) — typically 30-50% of revenue → biggest lever
- **Service** (support + success) — typically 10-20% of cost; can be a differentiator (high-touch enterprise) or commodity (SMB self-serve)

For <entity>, the load-bearing margin opportunity is <X>; the load-bearing margin risk is <Y>.
```

## Composability with existing skill features

| Existing feature | Interaction |
|---|---|
| §0 SWOT | Stays as-is; PESTEL adds in §10.X (broader scope) |
| §10 Quadrant + tiered competitor list | Stays as-is; Porter 5 Forces adds STRUCTURAL view alongside |
| §10.6 Industry Benchmarks | Stays; benchmarks measure performance, frameworks measure structure |
| §16 Risks | PESTEL Legal + Political feeds into §16 risks |
| §17 Strategic Analysis | Frameworks inform the §17 decision tree's gate definitions |

## Output integration

If `--framework=` includes any framework beyond SWOT, add a §10.X subsection per framework. If `--framework=all`, expect ~150-300 added lines per framework × 4 frameworks = 600-1,200 added lines on a `--depth=deep` dossier.

## Anti-patterns

- ❌ Filling out PESTEL with generic platitudes ("regulation matters") — each cell must have entity-specific factors
- ❌ Porter's 5 Forces with all forces rated 3 (medium) — means the analysis didn't discriminate; revisit
- ❌ VRIO where every cell is "Y" — means no sustained advantage was actually identified; revisit
- ❌ Value Chain without quantification — at least % of cost / revenue per activity should be estimated
- ❌ Running all 4 frameworks for a 5-section quick brief — overhead; reserve for `--depth=deep` + `--type=due-diligence|investment`

## When to load this file

- `--framework=` flag set with anything beyond `swot`
- `--type=due-diligence|investment` (auto-activated, default `pestel,porter5`)
- `--vertical=` triggers per-vertical auto-activation (table above)
- User asks "do PESTEL" / "Porter 5 Forces" / "VRIO" / "value chain" / "industry structure"
- User is from McKinsey/BCG/Bain background and expects classic frameworks
