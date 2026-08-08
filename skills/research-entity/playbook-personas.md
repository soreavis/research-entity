# Strategic Response Playbook — 12 Personas

Loaded during Step 4 (Draft) when writing §0 Strategic Response Playbook. Always include personas 1–4 (universal). Add 5–12 selectively per `--audience` (mapping below).

## Always-include (universal)

### 1. Investor / acquirer
- Diligence priorities (cap table, ARR/NRR, audit-quality of self-reported metrics)
- Valuation reality-check (aggregator-derived vs. last-round-implied vs. market-comparables)
- Exit scenarios (acquisition fit, IPO readiness, strategic-buyer overhang)
- What's missing publicly that needs disclosure under NDA

### 2. Enterprise buyer
- Fit / gap vs. their requirements
- Security / compliance asks (SOC 2 / ISO 27001 / HIPAA / FedRAMP)
- Demo questions to ask the vendor (not the marketing pitch)
- Alternatives to weigh (top 3 by use case)

### 3. Internal operator (board / leadership / founder)
- Execution priorities (next 90 days, next 6 months)
- KPIs that matter (and the gap between vanity and operational)
- Fixable trust gaps (compliance disclosure, public metrics, customer references)
- Cultural / org-design risks (founder-control patterns, leadership churn)

### 4. Competitor
- Where to attack (price, integration depth, vertical fit, content moat absence)
- Where NOT to attack (the entity's structural advantage)
- Displacement vectors (refund-friction customers, low-engagement customers, AI-feature-gap customers)

## Audience-triggered

### 5. Channel partner / SI / VAR / reseller
- Margin structure + recurring vs. one-time
- Training overhead (certification depth, time-to-productive)
- Lead-flow expectation (vendor-driven vs. partner-driven)
- Implementation skill demand (consulting revenue per deal)
- Co-marketing materials availability

### 6. Integration / tech partner
- Integration surface (REST API + webhooks + native connectors + iPaaS support)
- Public API stability + SDK languages + breaking-change cadence
- Native vs. third-party connector landscape
- MCP / AI-agent integration surface
- Revenue share model (where disclosed)

### 7. Talent / recruiter
- Recruit-from signals: layoffs, glassdoor churn, leadership exits, anti-pattern reviews
- Recruit-to signals: funding, growth, mission, founder reputation, equity terms
- Compensation band (Levels.fyi if available)
- Cultural fit indicators
- Key talent magnets (research network, content platform, mission-driven leadership)

### 8. Procurement / vendor-risk
- Concentration risk (single vendor, single founder, lightly-funded)
- Lock-in vectors (data-format proprietary, custom workflows, vendor-specific keys)
- Exit cost (data export window, cooperation in migration, contract-end fees)
- Sub-processor list + DPA terms
- Refund / cancellation policy (negotiable terms)

### 9. Legal / compliance (DPO, privacy, security)
- Data residency (which regions, which AWS/GCP/Azure regions)
- Certifications status (publicly claimed vs. on-request, SOC 2 Type II timeline)
- Encryption posture (at-rest, in-transit, BYOK availability)
- AI training opt-out (explicit clause vs. "not stated")
- Breach notification SLA + sub-processor change-notification policy

### 10. Existing customer (renewal team)
- Renewal vs. expansion vs. exit decision
- New value at renewal (recently shipped features, free upgrades, content access)
- Pricing trajectory (frozen / increasing / decreasing in last 12 months)
- Tier-threshold check (have you crossed into a higher tier without realizing?)
- Risk of being targeted by AI-native peer outreach (low premium-tier-equivalent usage)

### 11. Press / industry analyst
- Publishable angle (rebrand narrative, founder milestone, customer logo, layoff)
- Publishable data (annual research report, headcount disclosure, customer-count milestone)
- Quote-worthy executives (CEO, founder, key product VP)
- Avoid the unverifiable angle (vendor-claimed first-mover, vendor-claimed market size)
- Strongest contrarian frame the entity itself doesn't market

### 12. Open-source / API consumer / developer
- Public GitHub org state (active vs. archived repos)
- Modern language SDKs available (TypeScript, Python, Go, Rust)
- API rate limits + tier mapping
- Webhook + REST + GraphQL availability
- MCP server / AI-agent integration availability and source disclosure
- Help center quality + developer docs URL

## `--audience` → Persona mapping

When the user specifies `--audience=<X>`, include this subset:

| Audience | Personas to include |
|---|---|
| `c-suite` (default) | 1, 2, 3, 4 |
| `investor` | 1, 3, 5, 7, 10, 11 |
| `operator` (board / leadership) | 3, 5, 6, 7, 8 |
| `technical` | 6, 9, 12 |
| `board` | 1, 3, 8, 9, 11 |

Always include 1–4. Add 5–12 per the audience flag. Maximum 8 personas per Playbook (filter to most relevant if more are triggered).

## Format for each persona

Each persona is a sub-block in §0 Strategic Response Playbook formatted as:

```markdown
**If you are an investor / acquirer evaluating <entity>:**
- Concrete recommendation 1 (with link to relevant §)
- Concrete recommendation 2
- Concrete recommendation 3
- Watchlist signal (with where-to-watch URL)
```

3–6 bullets per persona. Each bullet:
- Specific to the entity (not generic)
- Action-oriented ("ask for X", "verify Y", "stress-test Z")
- Cites the relevant body section if it depends on a §-specific fact

## Anti-patterns

- ❌ Generic boilerplate ("evaluate fit / consider price / ask about security") — every bullet must be specific to the entity
- ❌ Personas that don't apply (e.g., open-source persona for a closed-source enterprise vendor)
- ❌ More than 8 personas — prune to the most relevant
- ❌ Recommendations that contradict the §-body sourced facts
- ❌ Recommendations the user can't act on ("become a partner of NVIDIA" if irrelevant)

## When to load this file

Load `playbook-personas.md` when:
- Writing §0 Strategic Response Playbook (always)
- Audience flag is set (to confirm persona mapping)
- User asks to "expand the playbook" / "add more personas"
- Reviewing a draft where the playbook feels generic
