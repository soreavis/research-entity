# Specialized Audit Modules — `--audit=<scope>`

Loaded by the `research-entity` skill at Step 4 (Draft) when `--audit=` is set. Adds a deep-dive section beyond the default 23-section structure. Each audit module produces a focused subsection with its own methodology, sources, and severity rating.

Four supported scopes (composable; `--audit=pricing,tech-stack`):

1. **`--audit=pricing`** — pricing teardown vs. 5 closest competitors
2. **`--audit=tech-stack`** — observable tech stack from public sources
3. **`--audit=customer-concentration`** — sample of customer base + concentration risk
4. **`--audit=ai-maturity`** — AI integration depth + safety posture

## 1. Pricing audit — `--audit=pricing`

**Section appended:** `§8.X Pricing Audit`

**Goal:** Surface what the entity *actually* costs vs. what the website implies, vs. competitors. Find hidden costs, packaging traps, discount opportunities.

**Methodology:**

1. **Public tier extraction** — capture all visible tiers from `/pricing` page. Note: published, not-published, "contact sales", overage rates, support tier add-ons.
2. **Wayback comparison** — compare current pricing to 12 months ago via Wayback (load `data-sources-extended.md`). Flag price changes ↑ / ↓ / restructured.
3. **Competitor pricing parity** — pull the same tier from 3–5 competitors. Show side-by-side at three personas: SMB / mid-market / enterprise.
4. **Hidden costs scan** — search for: "implementation fee", "professional services required", "premium support tier", "unlimited limits", "overage", "API call price", "per-seat with metered usage", "storage cost", "data egress", "custom domain", "SSO add-on", "audit logs add-on" (these are the standard "shrinkflation" levers).
5. **Customer-reported pricing** — search Reddit / G2 reviews for "I paid $X" / "we got quoted $Y" / "the upcharge was $Z" — gives reality check.
6. **Discount intel** — note negotiation patterns (e.g., "annual prepay 15% off" / "multi-year locks 25% off" / "if you mention competitor X they'll match").

**Output template:**

```markdown
### 8.X Pricing Audit

#### Public tier comparison

| Tier | <Entity> | Comp1 | Comp2 | Comp3 | Median |
|---|---|---|---|---|---|
| **Entry** | ... | ... | ... | ... | ... |
| **Mid** | ... | ... | ... | ... | ... |
| **Enterprise** | ... | ... | ... | ... | ... |

#### Hidden cost scan

| Lever | <Entity>'s position | Standard market position |
|---|---|---|
| **Implementation fee** | $X required / waived | typically $5–25K |
| **SSO** | included / add-on $X/mo | enterprise tier only at most |
| **Audit logs** | included / add-on $X/mo | enterprise tier add-on at most |
| **Support tier** | bundled / $X/mo | typically tiered |
| **Data egress** | not charged / $X/GB | usage-based |

#### Wayback price evolution
- 2024-Q1: <starting price>
- 2025-Q1: <change> (% delta)
- 2026-Q1: <change> (% delta)

#### Customer-reported pricing (verbatim, with attribution)
- "<quote>" — Reddit r/<sub>, 2025-08
- "<quote>" — G2 review by <reviewer>, 2026-01

#### Verdict
<2-3 sentences on whether pricing is competitive, transparent, escalating>
```

## 2. Tech-stack audit — `--audit=tech-stack`

**Section appended:** `§6.X Tech Stack`

**Goal:** Reverse-engineer the entity's tech stack from observable signals.

**Methodology:**

1. **BuiltWith / Wappalyzer** — hit the entity's main domain with these scanners:
   - https://builtwith.com/<domain>
   - https://wappalyzer.com/lookup/<domain>
   - Detect: framework (React, Next.js, Vue, Angular), CDN (Cloudflare, Fastly), analytics (GA, Segment, Amplitude, PostHog), CRM (HubSpot, Marketo, Salesforce form embeds), auth (Auth0, Okta, Clerk), CMS (WordPress, Contentful, Webflow), payment (Stripe, Braintree)
2. **Frontend inspection** — view-source the homepage; check `<meta name="generator">`, JS bundle filenames, asset URLs (often reveal framework + version)
3. **DNS records** — `dig <domain> MX` (email provider — Google Workspace / O365); `dig <domain> TXT` (SPF, DKIM, DMARC reveal SaaS dependencies)
4. **Subdomain enumeration** — `crt.sh?q=%.<domain>` reveals all SSL-cert-issuing subdomains; often reveals SaaS vendors used (e.g., `support.<domain>` → Zendesk; `status.<domain>` → Statuspage)
5. **GitHub** — load `data-sources-extended.md`; check public repos for SBOM (`package.json`, `requirements.txt`, `go.mod`, `Cargo.toml`)
6. **Job postings** — LinkedIn / job board postings reveal tech stack ("must have experience with: React, Next.js, Postgres, AWS, Datadog, Snowflake, Segment...")
7. **Status page** — what monitoring tool generates it (Statuspage.io / Incident.io / Cachet / Atlassian Statuspage / etc.)
8. **API responses** — call public API endpoints; `Server` header, `X-Powered-By` header reveal backend (Express, Rails, Django, FastAPI, Spring Boot)

**Output template:**

```markdown
### 6.X Tech Stack (observed from public signals)

| Layer | Detected | Source |
|---|---|---|
| **Frontend framework** | React + Next.js 14 | view-source, BuiltWith |
| **CDN** | Cloudflare | dig, response headers |
| **Hosting** | AWS us-east-1 | DNS, IP geolocation |
| **Analytics** | Segment + Amplitude + GA4 | network tab |
| **CRM/MAP** | HubSpot embed | form action URL |
| **Auth** | Auth0 | login redirect |
| **Payment** | Stripe | view-source, Stripe.js |
| **CMS** | Contentful | meta generator + asset URLs |
| **Database** | Postgres (inferred from job postings) | LinkedIn careers page |
| **Backend language** | Node.js (inferred from job postings) | LinkedIn careers page |
| **Monitoring** | Datadog (per job postings) | LinkedIn careers page |
| **Data warehouse** | Snowflake (per job postings) | LinkedIn careers page |
| **Email provider** | Google Workspace | dig MX |
| **Status page** | Statuspage.io (Atlassian) | status.<domain> domain |

#### Dependency notes
- Heavy reliance on AWS — single-cloud risk
- Auth0 dependency — vendor lock-in (consider whether a migration would be expensive)
- HubSpot CRM — predicts marketing motion (SMB-friendly inbound)

#### Sources
- [BuiltWith profile](url) (vendor-detected; not always accurate)
- [LinkedIn jobs page](url) (multiple postings analyzed for stack inference)
- [crt.sh subdomain dump](url) (SSL cert transparency log)
```

## 3. Customer-concentration audit — `--audit=customer-concentration`

**Section appended:** `§9.X Customer Concentration`

**Goal:** Identify single-customer dependency, vertical concentration, geographic concentration risk.

**Methodology:**

1. **Case study sample** — pull all named case studies from /customers + /case-studies + /resources/case-studies
2. **Logo wall enumeration** — extract every customer logo from the homepage / customers page
3. **G2 / Capterra named-customer list** — additional logos (some companies disclose logos there but not on /customers)
4. **Earnings-call mentions** (public co only) — top customers usually named in 10-K under "Customer Concentration" risk factor
5. **Vertical classification** — assign each named customer to a vertical (using their own /about page); compute distribution
6. **Geographic classification** — by HQ country
7. **Tier classification** — by employee count (SMB <100, Mid 100-1000, Enterprise 1000+, Fortune 500)

**Output template:**

```markdown
### 9.X Customer Concentration

#### Sample (N named customers)

| Customer | Logo | Vertical | Geography | Tier |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

#### Distribution

**By vertical** (% of named customers):
- SaaS: X%
- Healthcare: X%
- Fintech: X%
- ...

**By geography**:
- US: X%
- EU: X%
- APAC: X%
- ...

**By tier**:
- Fortune 500: X%
- Enterprise: X%
- Mid-market: X%
- SMB: X%

#### Concentration risk
- Largest single named customer (estimated revenue contribution): <X%>
- Top 5 customers (estimated): <X%>
- Top 10 customers (estimated): <X%>

#### For public companies (from 10-K)
[Customer concentration risk factor verbatim quote, with citation]

#### Verdict
<2-3 sentences on diversification, single-customer risk, vertical concentration, geo concentration>
```

## 4. AI-maturity audit — `--audit=ai-maturity`

**Section appended:** `§7.X AI Maturity`

**Goal:** For any entity claiming AI capabilities, audit how mature, defensible, and safe their AI integration is.

**Methodology:**

1. **Model identification** — what LLM does the product use? Look for:
   - Trust/AI-policy page disclosures (OpenAI / Anthropic / Cohere / open-weights / proprietary)
   - Model name version (gpt-4o vs. gpt-4-turbo matters)
   - Hosted-where (Azure OpenAI vs. OpenAI direct vs. self-hosted via Bedrock/Vertex)
2. **Fine-tuning signal** — is there a model trained on customer data? Is it customer-specific (BYOM) or shared?
3. **MCP / agent integration** — does the product expose an MCP server? Does it run agentic workflows? What guardrails?
4. **Eval framework** — is there a public statement on how they evaluate model output quality? Hallucination guards?
5. **Safety posture** — content moderation, prompt injection defense, jailbreak resistance, PII redaction, data residency for AI inputs
6. **Differentiation** — what's the actual AI moat? Proprietary data? Specialized models? RAG over private corpus? Multi-step workflow?
7. **Regression risk** — model deprecation policy (what happens when OpenAI deprecates the underlying model?)

**Output template:**

```markdown
### 7.X AI Maturity Audit

#### Model identification
- **Primary LLM**: <model name + version> (per [trust page](url))
- **Hosting**: <Azure OpenAI / Anthropic API / self-hosted Bedrock / etc.>
- **Fallback model**: <if disclosed>
- **Per-customer model selection**: <yes/no — BYOM or fixed>

#### Capability checklist
| Capability | Status | Source |
|---|---|---|
| Fine-tuning on customer data | yes/no/optional | trust page / docs |
| RAG over customer data | yes/no | docs |
| Agentic workflows (multi-step) | yes/no | product page |
| MCP server exposure | yes/no | mcp registry / docs |
| Embedded code interpreter | yes/no | docs |
| Multi-modal (image/audio/video) | yes/no | docs |
| Real-time / streaming responses | yes/no | demo |
| Conversation memory persistence | yes/no | docs |

#### Safety posture
| Vector | Posture | Source |
|---|---|---|
| Prompt injection defense | <described> | trust page |
| PII redaction | <yes/no/optional> | trust page |
| Hallucination guards | <eval framework / human-in-loop / none> | trust page |
| Content moderation | <Open AI moderation / custom / none> | trust page |
| Data residency (AI inputs) | <US-only / EU-only / global> | trust page |
| Customer data used for training | <yes/no/opt-in/opt-out> | trust page (gold-standard: explicit no) |
| Model deprecation policy | <documented / silent> | docs |

#### Defensibility
- **Proprietary data moat**: <strength>
- **Specialized fine-tunes**: <yes/no>
- **Workflow lock-in**: <strength>
- **Switch cost if model deprecates**: <high/med/low>

#### Verdict
<2-3 sentences on AI maturity vs. competitors, safety posture, regression risk>
```

## Composition with other flags

`--audit=` composes with `--depth`:
- `--depth=quick --audit=pricing` — minimal pricing-only deep-dive
- `--depth=deep --audit=pricing,tech-stack,ai-maturity` — full dossier + 3 audit modules

Each audit adds ~150-250 lines to the dossier. `--depth=deep --audit=all` (i.e., all 4 modules) adds ~800 lines.

## Anti-patterns

- ❌ Tech-stack audit relying solely on BuiltWith (often wrong; cross-check with job postings + view-source)
- ❌ Customer-concentration audit reporting "20% Fortune 500" when sample is 10 customers (insufficient sample size; flag the small-N caveat)
- ❌ AI-maturity audit reporting capabilities from a marketing page without confirming via docs/trust page (vendor claims often outpace reality)
- ❌ Pricing audit comparing US-published price to EU-quoted price (cross-currency / cross-tax distortion)
- ❌ All 4 audits without the user asking — adds 800 lines that may not be wanted; require explicit `--audit=` flag

## When to load this file

- `--audit=` flag set
- User asks "deep dive on pricing / tech stack / customer base / AI"
- `--vertical=devtools` (auto-suggest tech-stack audit)
- `--vertical=fintech|healthcare` (auto-suggest customer-concentration audit, since regulatory scrutiny matters)
- `--vertical=ai-native` or AI claim in /about page (auto-suggest ai-maturity audit)
