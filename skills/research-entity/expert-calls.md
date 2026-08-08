# Expert Call & Customer Reference Workflow — `--export=expert-call-questions|customer-reference-questions`

Loaded by the `research-entity` skill at Step 7 (Export) when one of these flags is set, OR auto-activated for `--type=due-diligence|investment` and `--depth=deep`. Generates structured question batteries for expert-network calls (Tegus, GLG, Third Bridge, AlphaSights) and customer-reference calls — the workflows that define Big 4 commercial DD.

A typical Big 4 commercial DD engagement includes **5-15 expert calls** + **15-25 customer-reference calls** as primary research. Without this workflow output, our skill produces public-sources-only intelligence with no equivalent to the primary-research layer that distinguishes professional CDD work.

## Two distinct workflows

| Workflow | Audience | Purpose | Typical N |
|---|---|---|---|
| **Expert calls** | Industry experts, ex-execs at the entity, ex-execs at competitors, channel partners, integration partners | Triangulate market dynamics, vendor reputation, technology assessment, competitive intelligence | 5-15 calls per dossier |
| **Customer reference calls** | Current customers (named or backchannel), former customers (especially churned), prospective customers who evaluated and didn't buy | Validate vendor claims (NRR, satisfaction, deployment ease), surface deal-economics intel, win/loss analysis | 15-25 calls per dossier |

## 1. Expert call questions (`--export=expert-call-questions`)

### Output: `<dossier-base>-expert-questions.md`

Produces a structured question battery for ~30-45 minute expert calls via Tegus / GLG / Third Bridge / AlphaSights / Tegus.

```markdown
# Expert Call Question Battery — <entity>
For Tegus / GLG / Third Bridge expert-network calls.
Target persona: <e.g. "Former VP Sales at competitor X" / "Industry analyst covering <category>" / "Channel partner with 50+ <entity> deployments">
Estimated duration: 30-45 minutes
Generated: <date>

## Pre-call preparation (analyst's prep, not for asking)

- **Expert background to confirm**: <role / years of relevance / departure date if ex-employee>
- **Compliance**: confirm NDA scope; clarify expert is not bound by current-employer confidentiality on topics being discussed
- **Recording**: per platform policy (Tegus auto-records; GLG opt-in; Third Bridge platform-dependent)

## Section A: Expert background (3-5 min)

1. Briefly walk me through your background relevant to <entity / competitive set / vertical>.
2. What's your current relationship to the company / vertical?
3. Are there any topics today where you would not be comfortable speaking?

## Section B: Vendor evaluation (10-15 min)

4. When buyers in <vertical> shortlist vendors, what's the typical 3-5 vendor cohort that comes up alongside <entity>?
5. What does <entity> do better than the alternatives? What does <entity> do worse?
6. If you were advising a $X mid-market buyer in <vertical>, when would you recommend <entity>? When would you steer away?
7. Have you seen <entity> win or lose deals in the last 12 months? What were the deciding factors?

## Section C: Pricing & deal economics (5-10 min)

8. What's your view on <entity>'s pricing relative to alternatives — published vs. real?
9. Have you seen <entity> discount aggressively? What's the typical "real" ACV vs. published list?
10. Are there hidden costs (implementation, premium support, AI add-ons) buyers should expect?
11. How does <entity>'s renewal / cancellation friction compare to <Pipedrive / HubSpot / Salesforce>?

## Section D: Vendor reputation & risk signals (5-10 min)

12. Have you heard of any breaches / outages / lawsuits / regulatory issues at <entity> in the last 24 months?
13. What's the team-stability picture? Recent CXO churn? Engineering team retention?
14. How financially stable do you assess <entity> to be? Any signals of distress?
15. Are there signals about a potential acquisition, IPO, or major round?

## Section E: Forward-looking (5-10 min)

16. Where do you see <entity> in 18-24 months? Strongest plausible bull case? Bear case?
17. What's the single biggest risk to <entity>'s competitive position?
18. What's the single biggest opportunity <entity> isn't pursuing aggressively enough?
19. If you were running <entity>, what would you change immediately?

## Section F: Backchannel & sourcing (3-5 min)

20. Are there other experts you'd recommend we speak with on this topic?
21. Are there primary documents / databases we should be looking at that we likely aren't?
22. Anything we haven't asked that we should have?

## Post-call processing checklist

- [ ] Update §0 Scorecard with any expert-confirmed metrics
- [ ] Update §11 Community with verbatim expert quotes (with attribution disclosure)
- [ ] Update §16 Risks with any non-public risks surfaced
- [ ] Update §17 Strategic Analysis with expert verdicts
- [ ] Cross-check expert claims against §16.6 Red-Flag Scan (do they corroborate or contradict?)
- [ ] If expert is at a competitor — apply higher skepticism to their assessment of <entity>
- [ ] If expert is an ex-employee with negative-departure pattern — apply higher skepticism
- [ ] Add to §22 Glossary: any vertical-specific jargon used by the expert
```

## 2. Customer reference questions (`--export=customer-reference-questions`)

### Output: `<dossier-base>-customer-reference-questions.md`

Produces a structured battery for ~30-45 minute customer reference calls. Two variants based on customer status:

### Variant A: Current customer (vendor-supplied reference)

```markdown
# Customer Reference Call — Current Customer of <entity>
Target: <named customer> (or "anonymous current customer in <vertical>")
Vendor-supplied: yes (means responses lean positive; calibrate accordingly)
Generated: <date>

## Section A: Customer profile (3 min)

1. Briefly walk me through your role + your team's use of <entity>.
2. How long have you been a customer? Original buying-team composition?
3. Approximate seat count + tier you're on?

## Section B: Buying decision (5-10 min)

4. What problem were you solving when you brought in <entity>?
5. Who else did you evaluate? What was the deciding factor?
6. What was the typical sales cycle length? Anyone you worked with at <entity>?
7. Did you negotiate pricing? What were typical discounts?

## Section C: Deployment & adoption (10 min)

8. How long was implementation? Smooth / rocky? Where did it stick?
9. What % of your team uses it weekly today? Daily?
10. What features do you actually use? Which features do you ignore?
11. How do you feel about <entity>'s AI capabilities (e.g. <entity-AI-product> / MCP server / etc.)?

## Section D: Realized value (5-10 min)

12. What outcomes have you measured? Pipeline velocity? Win rate? Rep productivity?
13. Did <entity> deliver on its TCO / consolidation claims for your stack?
14. Net-net, would you renew today at the same price?

## Section E: Friction & risk (5-10 min)

15. What's the single biggest annoyance you have with <entity>?
16. Any incidents / outages / data issues in the last 12 months?
17. How responsive is support / customer success?
18. Have you considered switching? To whom? Why didn't you?

## Section F: Reference value & expansion (3-5 min)

19. Have you upgraded tiers or added seats in the last 12 months? Plans to expand?
20. Would you recommend <entity> to a peer in your vertical? With what caveats?
21. Are there other reference customers in your network we should speak with?
```

### Variant B: Churned / former customer (the gold-standard reference)

```markdown
# Customer Reference Call — FORMER Customer of <entity>
Target: <former customer> (often most-valuable reference)
Vendor-supplied: NO (means responses are unfiltered; this is the gold-standard reference)
Generated: <date>

## Section A: Customer profile (3 min)
[Same as Variant A]

## Section B: Why you left (10-15 min) — THE LOAD-BEARING SECTION

5. When did you stop using <entity>? Replaced or just stopped?
6. What replaced it? Why was the replacement better?
7. Was the decision precipitated by a specific event? Pricing? Outage? Feature gap? Acquisition? Team change?
8. What did <entity> do (or not do) to retain you? Were they aware you were leaving?
9. With hindsight, what would have kept you?

## Section C: Operational realities (5-10 min)

10. What did you actually use vs. what you had been sold on?
11. What was the realized TCO vs. the pitched TCO?
12. Were there hidden costs that surfaced post-deployment?
13. How did the support / success motion perform under stress?

## Section D: Migration & lock-in (5-10 min)

14. How hard was the data migration off <entity>?
15. Were there contractual / cancellation issues?
16. How long did the migration take? Any data loss?

## Section E: Net assessment (3-5 min)

17. Would you ever consider <entity> again? Under what conditions?
18. What specific advice would you give a peer evaluating <entity> today?
19. Are there other former customers we should speak with?
```

### Variant C: Lost-deal prospect (Klue/Crayon win-loss style)

```markdown
# Customer Reference Call — LOST DEAL Prospect (evaluated <entity>, chose alternative)
Target: <prospect> (most-valuable for understanding why <entity> loses deals)
Generated: <date>

## Section A: Buyer profile + buying process (5 min)

1. Walk me through your evaluation process — when, who, what was the trigger event?
2. What was the long-list / short-list? Where did <entity> sit?

## Section B: Why you didn't choose <entity> (15-20 min) — THE LOAD-BEARING SECTION

3. Walk me through the decision criteria. How did <entity> score on each?
4. What was the single biggest reason <entity> didn't make the final cut?
5. Was there a deal-breaker, or was it a sum-of-margins decision?
6. Did <entity> handle the loss professionally? Did they understand why they lost?
7. What did the winning vendor do better in the sales process?
8. If <entity> had done one thing differently, would they have won?

## Section C: Post-decision (5-10 min)

9. How is the chosen vendor performing today, 6-12-18 months in?
10. Looking back, would you make the same choice?
11. Have you seen <entity>'s positioning / pricing / product change since?

## Section D: Forward look (3-5 min)

12. Would <entity> be in your shortlist for a future evaluation? Why or why not?
13. Are there peers in your network who recently evaluated <entity>?
```

## Aggregation — `--export=expert-call-questions,customer-reference-questions`

When both flags are set, generate a combined `*-primary-research.md` deliverable that includes:
- 1 expert-call template (generic; customize per persona)
- 1 each of customer-reference Variants A, B, C
- A **call-tracking spreadsheet outline** (CSV) — call ID, persona, date scheduled, date completed, status, key findings (3 bullets), follow-up needed

This becomes the primary-research playbook for the dossier.

## Integration with main dossier

After the calls are completed, manually update:
- **§9 Customer Base** — add Section "Reference Call Findings" with anonymized aggregate findings
- **§11 Community Reception** — add expert verbatim quotes with attribution disclosure
- **§16 Risks** — add Section "Risks Surfaced via Primary Research"
- **§17 Strategic Analysis** — refresh decision tree with primary-research-confirmed gates
- **§23 Confidence** — primary-research can lift composite by 5-10 points (moves dossier from "public-source-only" to "NDA-stage access" band per `confidence-scoring.md` comparison table)

## Cost & timing

- **Expert calls** via Tegus / GLG / Third Bridge / AlphaSights: ~$1,000-1,500 per 30-min call (analyst pricing); ~$300-500 per 30-min call (Tegus subscription model)
- **Customer reference calls**: typically free if vendor-supplied (Variant A); harder to source for Variants B and C (requires backchannel via shared LinkedIn networks, ex-colleagues, or industry events)
- **Time**: 1 call = ~30-45 min on call + 30 min prep + 30 min write-up = ~1.5-2 hrs analyst time
- **Total for full DD with 10 expert + 20 customer calls**: ~50-60 hours analyst time + ~$10K-15K direct platform cost

## Anti-patterns

- ❌ Asking leading questions ("don't you think <entity> is great?") — kills reference value
- ❌ Asking yes/no questions — extract narrative responses
- ❌ Skipping Variant B (former customers) — current customers are vendor-curated and biased positive
- ❌ Treating vendor-supplied references as independent — they're not; weight responses accordingly
- ❌ Failing to record and transcribe — most platforms record; transcripts enable later searchability
- ❌ Not asking "who else should we speak with?" — every call should snowball to 1-2 next calls

## Compliance & ethics

Per [SCIP Code of Ethics](https://www.scip.org/page/Ethical-Intelligence):
- Do not misrepresent yourself or your purpose
- Do not solicit confidential information from current employees of <entity>
- Do not pay for confidential information
- Honor expert NDAs with their current employer
- Disclose recording (most platforms do this automatically; confirm)

## When to load this file

- `--export=expert-call-questions` flag set
- `--export=customer-reference-questions` flag set
- `--type=due-diligence|investment` AND `--depth=deep` (auto-activated)
- User asks "expert call questions" / "reference call questions" / "primary research" / "Tegus / GLG / Third Bridge"
