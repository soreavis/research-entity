# Multi-Agent Parallel Strategy — `--agents=<level>`

Loaded by the `research-entity` skill at Step 1 (Plan) when `--agents=` is set OR auto-activated based on `--depth`. Defines which workstreams run as independent `Agent` subagents (parallel + isolated context windows) vs. inline within the main session (sequential + shared context).

Multi-agent execution offers three benefits:
1. **Speed** — parallel subagents finish in ~⅓-½ the wall-clock time vs. sequential
2. **Context hygiene** — each subagent has its own context window; main session doesn't burn context on raw research output
3. **Independent perspectives** — independent ACH / Devil's Advocate / hallucination-audit agents can't be biased by the main draft they're auditing

## 4 supported parallelism levels

| Level | Default for | # agents | Wall-clock vs. solo | API cost vs. solo |
|---|---|---:|---|---|
| `solo` | `--depth=quick` | 1 | 1.0× | 1.0× |
| `validation` | `--depth=standard` | 2-3 | 0.7× | 1.3× |
| `parallel` | `--depth=deep` | 5-7 | 0.5× | 1.8× |
| `max` | `--type=due-diligence\|investment` | 10-12 | 0.4× | 2.5× |

Cost/time numbers are directional based on production runs; actual results vary by entity complexity, source availability, and Tavily quota state.

## What runs in parallel at each level

### Level: `solo` (1 agent)
- Single Claude session executes all 8 steps sequentially
- Step 2 source gathering: batched WebSearch+WebFetch tool calls (parallel at the tool-call level, but single-agent reasoning)
- No subagent delegation
- **Best for**: quick scoping briefs, throwaway research, cost-constrained runs

### Level: `validation` (2-3 agents — CURRENT default for `--depth=deep`)
Subagents spawned at:
- **Step 3 — Cross-validation (2 agents)**:
  - Agent A: Business-register verification (load `registers.md`, verify each named legal entity in free public registers)
  - Agent B: Reviews + community + risk-scan (load `reviews-platforms.md` + `risk-scan.md`, multi-platform review counts + verbatim quotes + 8 red-flag patterns)
- **Step 6 — Hallucination audit (1 agent)**:
  - Agent C: Read the full draft; verify every §0 claim is body-supported; flag fabricated precision, single-source claims not labeled, founder-exit narratives not cross-checked, temporal "first mainstream X" claims not verified

### Level: `parallel` (5-7 agents)
Adds subagents at:
- **Step 2 — Source gathering (3 agents)**:
  - Agent D: Founder + funding + investor research
  - Agent E: Customer + case study + reviews scraping
  - Agent F: Competitor landscape + analyst coverage + market data
- **Step 4 — Audit modules (1-2 agents per `--audit=` scope)**:
  - When `--audit=pricing,tech-stack,customer-concentration,ai-maturity` is set, each module gets its own agent
- **Step 4 — Frameworks (1 agent per non-default `--framework=`)**:
  - PESTEL agent, Porter5 agent, VRIO agent run independently and merge into §10.X subsections

### Level: `max` (10-12 agents — for board / IC-grade DD)
Adds:
- **Step 4 — Independent analytic technique agents**:
  - Agent G: **ACH agent** (load `analytic-techniques.md`) — generates 3-5 competing hypotheses + evidence matrix WITHOUT seeing the main draft (true independent perspective; counters confirmation bias from inside the matrix)
  - Agent H: **Devil's Advocate agent** — for each major BLUF claim, generates the strongest counter-argument; runs ON the draft to stress-test
  - Agent I: **Pre-mortem agent** — "imagine this dossier is wrong in 18 months — why?"; generates 5 plausible failure modes
  - Agent J: **Key Assumptions Check agent** — extracts 5-7 load-bearing assumptions from the draft; rates stress-test status
- **Step 2 — Risk scan (1 agent per pattern; 8 patterns total)**:
  - Each `risk-scan.md` pattern (layoffs, exec departures, lawsuits, breaches, regulatory, Glassdoor, status-page, leadership-controversy) runs as its own agent with focused search
- **Step 5 — Independent fact-check agent**:
  - Agent K: Reads the draft; verifies every numeric claim has a citation; flags any number without inline source
- **Step 8 — Independent confidence-scoring agent** (optional):
  - Agent L: Reads the final draft and scores §23 confidence independently from the main session; if scores diverge by >5 points, the disagreement is investigated

## Agent specification template (used when delegating)

When the main session spawns a subagent, it provides a self-contained brief. The subagent has no access to the conversation history or the in-progress draft (unless explicitly handed the file path):

```
Agent({
  description: "Cross-validate competitor funding claims",
  subagent_type: "general-purpose",
  prompt: """
Verify the following 6 competitor funding claims against ≥2 independent public sources each.
For each, return: confirmed amount + lead investor + date + 2 source URLs, OR flag as unverifiable.

Competitors to verify:
1. Aurasell — claimed $30M seed, Aug 2025
2. Day.ai — claimed $24M total, including $20M Series A Feb 2026
3. Clarify — claimed $22.5M including $15M Series A June 2025
4. Lightfield — claimed $81M Tome-heritage including $43M Series B Feb 2023 at $300M
5. Monaco — claimed $35M total Founders Fund-led
6. Reevo — claimed $80M seed Nov 2025 at ~$500M valuation, Khosla + Kleiner Perkins

Sources to check: Crunchbase, PitchBook, Tracxn, BusinessWire, TechCrunch, The Information.
Report under 500 words. Use the `vendor-claimed`/`single-source`/`aggregator-derived` labels per the skill's voice rules.
"""
})
```

The subagent returns a structured report; the main session integrates findings.

## Composition rules

- `--agents=` composes with `--depth=`:
  - `--depth=quick --agents=parallel` is allowed but unusual (overkill for a quick brief)
  - `--depth=deep --agents=solo` is allowed but slow (skip cross-validation parallelism)
- `--agents=` composes with `--validation=`:
  - `--validation=max` REQUIRES `--agents=parallel` or higher
  - `--agents=max` IMPLIES `--validation=max`
- `--agents=max` is the only level that activates the **independent ACH agent** (G) — at lower levels, ACH runs inline within the main session

## Wizard integration (Q12 added)

When the wizard runs (per `SKILL.md` Step 1b), Question 12 surfaces the multi-agent option:

```
Q12: Multi-agent parallelism? Higher = faster wall-clock + higher API cost + better independent-perspective quality.
- 🤖 Solo (1 agent, sequential) — cheapest, slowest. Good for quick briefs.
  → ~$2-5 cost · 30-60min runtime
- 👥 Validation (2-3 agents) — recommended default for standard dossiers.
  → ~$10-20 cost · 20-35min runtime
- 🚀 Parallel (5-7 agents) — recommended for deep dossiers.
  → ~$25-50 cost · 25-45min runtime
- 🌟 Max (10-12 agents) — recommended for due-diligence / investment-committee outputs.
   Adds INDEPENDENT analytic-technique agents (ACH, Devil's Advocate, Pre-mortem, KAC, Risk Scan, Fact-Check)
   for true confirmation-bias resistance. The ACH agent doesn't see the main draft → genuinely independent.
  → ~$60-120 cost · 30-60min runtime (parallel speedup balances against more agent calls)
```

Default selection by `--depth`:
- `quick` → solo (auto)
- `standard` → validation (auto)
- `deep` → parallel (auto)
- `--type=due-diligence|investment` → max (auto)

User can override at any level via the wizard or `--agents=` flag.

## Anti-patterns

- ❌ `--agents=max` with `--depth=quick` — wastes parallelism on a thin source pool
- ❌ Spawning subagents and then waiting sequentially for each — defeats parallelism; always spawn ALL agents in a single message with multiple tool calls (per `SKILL.md` parallel-tool-call rule)
- ❌ Passing the main draft to the ACH subagent at `--agents=max` — defeats the "independent perspective" benefit; ACH agent should generate hypotheses BLIND to the main draft
- ❌ Using `--agents=max` for `--type=research|partnership` — these dossier types don't have the adversarial-rigor requirement that justifies the cost
- ❌ Failing to merge subagent findings back into the main draft — orphaned subagent outputs are wasted spend; the main session must integrate every subagent report

## Cost / runtime estimate per level

Numbers are approximate, based on production runs with Opus 4.7 + max effort:

| Level | Wall-clock | API cost (Opus 4.7) | Best for |
|---|---|---|---|
| `solo` | 30-60 min | $2-5 | Quick scoping; throwaway research; cost-constrained |
| `validation` | 20-35 min | $10-20 | Standard competitive dossiers; weekly portfolio updates |
| `parallel` | 25-45 min | $25-50 | Deep dossiers; quarterly competitive reviews; partnership eval |
| `max` | 30-60 min | $60-120 | Due-diligence; IC memos; board-grade outputs; PE-roll-up DD |

**Cost-quality frontier**: max-mode runs are ~10× the cost of solo-mode but produce dossiers that are independently-validated across 3-4 perspectives. For a $50K-500K human-DD-equivalent output, $120 of API spend is rounding error.

## When to load this file

- `--agents=` flag set
- Wizard reaches Q12 (multi-agent question)
- Auto-activation for `--depth=deep` or `--type=due-diligence|investment`
- User asks "can this run faster" / "use multiple agents" / "parallelize the audit"
- User asks "is this confirmation-biased" — recommend `--agents=max` for independent ACH

## Implementation note for the model

When `--agents=parallel` or higher is set, the main session must:
1. **Spawn all subagents in a single message** with multiple Agent tool calls (parallel execution)
2. **Wait for all subagent results** before integrating (don't block on one slow agent)
3. **Surface subagent findings in §23** under "Cross-validation pass: X of Y agents reported corroboration; Z disagreed on [item]"
4. **Document subagent count in §23 methodology** for reproducibility ("Composite confidence reflects N-agent parallel cross-validation")
5. **If a subagent fails** (e.g., quota exhausted, fetch error), log the failure but continue — don't halt the entire run
