# Moat Scoring — Hamilton Helmer 7 Powers Framework

Loaded by the `research-entity` skill when `--moat=helmer` flag set OR `--audience=board|investor` (auto-load) OR user asks "what's their moat?" / "how defensible is this?". Implements [Hamilton Helmer's 7 Powers framework](https://7powers.com/) — the SaaS-investor-class moat lexicon validated by Helmer's 22-year **41.5% CAGR vs 14.9% S&P 500** as an active equity investor.

## §1 — Why this file exists

SWOT is the operational lens. Helmer's 7 Powers is the **strategic moat lens** — the framework SaaS boards, growth-stage investors, and IPO underwriters actually use to assess durable competitive advantage.

Helmer's framework systematizes seven sources of persistent power. **Each one alone is sufficient** to sustain a business — they don't sum into a "total moat score." A business with strong Switching Costs but no Network Economies can still be category-leading.

**Validation:**
- [7powers.com](https://7powers.com/) (Helmer's own site)
- [Acquired podcast — Helmer episode](https://www.acquired.fm/episodes/7-powers-with-hamilton-helmer)
- [Lenny's Newsletter — Business strategy with Hamilton Helmer](https://www.lennysnewsletter.com/p/business-strategy-with-hamilton-helmer)
- [7 Powers book](https://www.amazon.com/7-Powers-Foundations-Business-Strategy/dp/0998116319) (referenced extensively in SaaS-investor circles since 2016)

**Helmer's definition of Power:** a business has Power when its position is simultaneously (a) **superior** (improves free cash flow), (b) **significant** (cash-flow improvement is material), and (c) **sustainable** (improvement is largely immune to competitive arbitrage).

---

## §2 — The 7 Powers

| # | Power | Definition | SaaS-applicable? |
|---|---|---|---|
| 1 | **Scale Economies** | Per-unit cost decreases with size | High — infrastructure, support, sales |
| 2 | **Network Economies** | Value to user increases with user count | Limited to SaaS with collaboration / marketplace / data-graph |
| 3 | **Counter-Positioning** | New player adopts model the incumbent can't copy without harming itself | Frequent for AI-native vs. legacy CRM |
| 4 | **Switching Costs** | Customer faces real cost / friction to leave | **Highest-value SaaS power** (data lock, integration depth, training) |
| 5 | **Branding** | Customers pay premium for brand alone | Rare for B2B SaaS (more common for consumer) |
| 6 | **Cornered Resource** | Privileged access to a coveted asset | Rare unless regulated industry / proprietary data / exclusive partnership |
| 7 | **Process Power** | Operational excellence built over time, hard to replicate | Rare for tech (typically too young); 5+ years of continuous improvement required |

**Helmer's observation about tech companies (per Acquired podcast):** *"The first 3 sources of power [Scale, Network, Counter-Positioning] are rare for tech companies. The company is usually too young to have built sufficient brand love or uniquely efficient processes, and cornered resources are uncommon unless operating in a highly regulated industry."*

For SaaS specifically, the realistically-attainable powers are: **Switching Costs** (#4), **Network Economies** (#2 if applicable), **Counter-Positioning** (#3 if disrupting incumbent).

---

## §3 — Scoring rubric (each power independently, 0–3 scale)

Each power scored on a **0-3 integer scale** (NEVER decimals — would imply false precision). Score must be paired with **explicit public-source evidence**.

### Score definitions

| Score | Interpretation | Required evidence |
|---|---|---|
| **0** | Not present / no signal | (no evidence required) |
| **1** | Weak signal — directional but not load-bearing | At least 1 public-source observation |
| **2** | Strong signal — meaningful moat contribution | ≥2 independent public-source observations |
| **3** | Category-defining power — the moat | ≥3 independent observations + measurable competitive impact |

### Power-specific scoring criteria

**1. Scale Economies (cost decreases with size)**
- 0: Cost-per-customer is flat or growing
- 1: Cloud-infra cost-per-customer declining (commodity scale)
- 2: Sales / support cost-per-customer declining as ARR grows
- 3: Multiple cost-curves (infra + sales + R&D allocation) compounding; competitor cost structure visibly worse

**2. Network Economies (value increases with users)**
- 0: No network signal; product is single-tenant utility
- 1: Some collaboration features (shared workspaces, share-by-link)
- 2: Cross-tenant features (shared data, marketplaces, integrations directory)
- 3: Demonstrable network effect: more users measurably make product better for all users (per Reed's Law / Metcalfe's Law)

**3. Counter-Positioning (incumbent can't respond)**
- 0: No counter-positioning; entity is a direct copy of incumbent
- 1: Different pricing model (PLG vs. sales-led, freemium vs. enterprise) but no incumbent-can't-copy claim
- 2: New architecture incumbent can't adopt without cannibalizing (e.g., AI-native zero-input data graph)
- 3: Demonstrable incumbent paralysis: incumbent has tried to respond and visibly failed (e.g., explicit M&A capitulation, internal-product cancellation)

**4. Switching Costs (friction to leave)** — **the highest-value SaaS power**
- 0: Customer can leave with one CSV export and zero friction
- 1: Light switching cost (some UI training, but data exports cleanly)
- 2: Real switching cost (proprietary data formats, integrations require re-architecture, contract early-termination fees)
- 3: Mission-critical lock-in (system of record, regulatory audit trail, multi-year integrations across entire workflow)

**5. Branding (premium for brand alone)**
- 0: No premium pricing power; price-competitive only
- 1: Minor brand premium (~10% over commodity)
- 2: Real brand premium (20-50% over comparable feature set)
- 3: Category-defining brand (Salesforce-tier; "no one ever got fired for buying X")

**6. Cornered Resource (privileged access to asset)**
- 0: No exclusive resource; commoditized inputs
- 1: One semi-exclusive partnership / data feed / talent cluster
- 2: Multi-year exclusive contract / regulated license / proprietary dataset
- 3: Government-granted monopoly / patent thicket / exclusive licenses to scarce inputs

**7. Process Power (operational excellence built over time)**
- 0: Standard operating model
- 1: Some operational discipline visible (above-average efficiency metrics)
- 2: Demonstrable 3-5 year operational improvement curve
- 3: 5+ years of compounding operational advantage; competitor benchmarking shows 2x+ efficiency gap

---

## §4 — Output template (§17.X Moat Scoring — Helmer 7 Powers)

```markdown
## §17.X Moat Scoring (Helmer 7 Powers)

> **Framework:** Hamilton Helmer's 7 Powers ([7powers.com](https://7powers.com/)). Each power scored independently 0-3 with public-source evidence. **Powers don't sum** — any single power of 3+ can sustain a business.

| Power | Score | Evidence |
|---|---:|---|
| **1. Scale Economies** | <0-3> | <evidence> |
| **2. Network Economies** | <0-3> | <evidence> |
| **3. Counter-Positioning** | <0-3> | <evidence> |
| **4. Switching Costs** | <0-3> | <evidence> |
| **5. Branding** | <0-3> | <evidence> |
| **6. Cornered Resource** | <0-3> | <evidence> |
| **7. Process Power** | <0-3> | <evidence> |

### Power summary

**Highest power:** <name> at <score>. <One-sentence interpretation>.

**Powers absent (0):** <list>. Not load-bearing for the entity's moat.

**Strategic implication:** <If primary power is Switching Costs: defensibility comes from data lock; competitor displacement requires migration tooling. If Network Economies: defensibility is self-reinforcing with scale. If Counter-Positioning: incumbent capitulation visible — opportunity to compound. Etc.>

### Honest framing

Helmer's framework is a **moat assessment lens**, not a competitive forecast. A high power score means the moat is durable today; it does NOT mean the entity will outperform competitors over a specific time horizon. Power scores must be re-assessed annually as competitive landscape shifts.
```

---

## §5 — Anti-hallucination discipline (Cat J extensions)

- **#76 — Each power scored independently; no aggregation**: never sum or average the 7 scores. Helmer's framework specifically holds that any single power can sustain a business; aggregation misrepresents the model.
- **#77 — Switching cost claim requires friction mechanism**: a 2 or 3 score on Switching Costs requires citing the specific friction (data lock, API limits, contract terms, integration depth) — never just "high switching cost" without mechanism.
- **#78 — Network effect claim requires degree-N evidence**: a 2 or 3 score on Network Economies requires demonstrating that more users measurably make the product better. "Has a marketplace" alone is not Network Economies — many marketplaces have no network effect.
- **#85 — Counter-positioning requires incumbent-paralysis evidence**: a 3 score on Counter-Positioning requires citing visible incumbent failure (M&A capitulation, internal product cancellation, public investor commentary acknowledging the threat).
- **#86 — Process power requires 5+ years of evidence**: a 3 score on Process Power requires demonstrable continuous improvement over 5+ years. Tech companies <5 years old cannot have a 3 on Process Power per Helmer's own framework.
- **Score range is integer 0-3**: never decimals. Decimal precision implies measurement that isn't there.

---

## §6 — When to load this file

- **Auto-load** when `--audience=board|investor` set
- **Auto-load** when `--type=due-diligence|investment` AND `--depth=deep`
- **Manual load** when `--moat=helmer` flag set
- **Composes with** `frameworks.md` SWOT — Helmer is the strategic-moat lens; SWOT is the operational lens. Use both for `--audience=board|investor`.
- User asks "what's their moat?" / "how defensible is this?" / "is this a category-defining business?"

---

## §7 — Composability with existing strategy frameworks

| Lens | When to use |
|---|---|
| **SWOT** (`frameworks.md`) | Operational competitive analysis — strengths, weaknesses, opportunities, threats |
| **Porter's 5 Forces** (`frameworks.md`) | Industry-structure analysis — buyer power, supplier power, rivalry, etc. |
| **VRIO** (`frameworks.md`) | Resource-based-view — Valuable / Rare / Inimitable / Organized |
| **Helmer 7 Powers** (this file) | Strategic moat / durable power assessment — what makes this business persistently valuable |
| **Rumelt Strategy Kernel** (`strategy-classics.md`) | Diagnosis / guiding policy / coherent action — what the entity should DO |
| **Christensen Disruption** (`strategy-classics.md`) | Sustaining vs. disruptive innovation classification |

Helmer is the most widely-cited modern moat framework in SaaS-investor-class analysis. SWOT is required for any audience; Helmer is required for board/investor audience.

---

## §8 — Anti-patterns

- ❌ Aggregating the 7 scores into a single "moat score" or "Helmer index" — misrepresents the framework
- ❌ Using decimal scores (2.5, 1.7) — false precision; Helmer's framework is integer-based
- ❌ Scoring Switching Costs as 3 without naming the specific friction mechanism
- ❌ Claiming Network Economies for any product with multi-user features (network effect requires degree-N value scaling)
- ❌ Claiming Process Power for a sub-5-year company
- ❌ Claiming Branding power for B2B SaaS without measurable price-premium evidence
- ❌ Treating absence of one power as a weakness — Helmer holds that **any single power can sustain a business**

---

## §9 — Bonus: SaaS-specific 7-Powers playbook (analyst opinion)

From the [Acquired podcast](https://www.acquired.fm/episodes/7-powers-with-hamilton-helmer) Helmer interview, the SaaS-applicable powers in priority order:

1. **Switching Costs** — most achievable; data lock + integration depth is the reliable path
2. **Network Economies** — only if product structurally scales with users (collaboration / marketplace / data-graph)
3. **Counter-Positioning** — common for AI-native vs. incumbent-CRM but requires sustained incumbent paralysis
4. **Scale Economies** — accessible at maturity; commodity infra plus consolidating R&D
5. **Branding** — rare; requires consumer-grade brand investment (Salesforce, HubSpot, Shopify level)
6. **Cornered Resource** — rare; usually regulated-industry play
7. **Process Power** — rarest; requires 5+ years of continuous-improvement evidence

For a typical Series-B SaaS, scoring 2+ on Switching Costs + 1 or 2 on one other power is a healthy moat. Scoring 0 on all 7 = no moat = competitive position is purely speed-of-execution-dependent.
