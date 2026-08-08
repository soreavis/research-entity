# Glossary Catalog — Canonical Term Bank

Loaded by the `research-entity` skill during Step 4 (Draft) when writing §22 Glossary. This catalog contains canonical pre-written definitions for terms commonly used in vendor-research dossiers. The skill's workflow:

1. **Scan the draft body** for which catalog terms appear
2. **Include those terms** in §22 Glossary, copy/adapt the canonical definition
3. **Add entity-specific terms** (e.g., a vendor-specific AI product or module name) per the writing rules in `voice-and-style.md`
4. **Run the glossary-completeness scan** (per `voice-and-style.md`) to catch anything missed

**Rule:** if a term from this catalog appears in the body, it MUST appear in the glossary. Don't skip the obvious ones — readers from non-domain backgrounds rely on the glossary.

The catalog is alphabetized within each category. Categories are NOT preserved in the dossier glossary — flatten alphabetically when writing §22.

---

## Document framework terms (almost always applicable)

| Term | Canonical definition |
|---|---|
| **BLUF** | Bottom Line Up Front — opening paragraph of §0 Executive Briefing summarizing the dossier in ≤200 words. Standard analyst-briefing format. |
| **Heat Map** | §0 framework — stakeholder/force × pressure-level × time-horizon table; identifies where strategic threats sit and on what time horizon. |
| **Playbook** | §0 framework — strategic recommendations grouped by reader persona ("if you are X, do Y"). |
| **Scorecard** | §0 framework — ~15-row metrics table where each row is a single fact + source citation + a labelled signal (`🟢 Strong` / `🟡 Unverified` / `🔴 Absent` / `⚪ N/A` — dot plus a one-or-two-word verdict, never a bare dot). The dossier's quick-reference summary; the Signal column must read as a coherent summary on its own. |
| **SWOT** | Strengths / Weaknesses / Opportunities / Threats — 2×2 strategic-analysis framework. Standard §0 framework component. |
| **Watchlist** | §0 framework — 10–12 specific monitoring signals with "where to watch" URLs and red-flag triggers. Tracks the highest-leverage indicators of the entity's trajectory. |

## Funding & financial terms

| Term | Canonical definition |
|---|---|
| **ARR** | Annual Recurring Revenue — the normalized annual value of subscription contracts. |
| **ARPU** | Average Revenue Per User — total revenue ÷ number of users; SaaS unit economic. |
| **CAC** | Customer Acquisition Cost — sales+marketing spend ÷ new customers acquired. |
| **CAGR** | Compound Annual Growth Rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — operating profit measure. |
| **GMV** | Gross Merchandise Value — transaction-marketplace top-line metric. |
| **LTV** | Lifetime Value — total expected revenue from a customer over their tenure. |
| **MRR** | Monthly Recurring Revenue — ARR ÷ 12 for pure-subscription businesses. |
| **NRR** | Net Revenue Retention — % of starting ARR retained from existing customers, including expansion and contraction. |
| **OTE** | On-Target Earnings — sales-rep total compensation including bonus at 100% quota. |
| **PE** | Private Equity — investment firms acquiring private companies. |
| **Seed / Series A / B / C** | Sequential rounds of venture-capital funding. Seed = first institutional round (typically $0.5M–$5M). Series A → B → C indicate growing rounds at higher valuations. |
| **SAM** | Serviceable Addressable Market — the realistic subset of TAM. |
| **SOM** | Serviceable Obtainable Market — the share of SAM the vendor can capture in a given period. |
| **TAM** | Total Addressable Market. |
| **VC** | Venture Capital — investment firms providing equity capital to early-stage companies. |

## Standards / certifications / compliance

| Term | Canonical definition |
|---|---|
| **BCDR** | Business Continuity / Disaster Recovery — operational planning for system failures. |
| **CCPA** | California Consumer Privacy Act — California state law analogous to GDPR. |
| **DPA** | Data Processing Addendum — contractual document defining how a vendor processes customer data. Required under GDPR. |
| **DPO** | Data Protection Officer — role mandated by GDPR for organizations processing personal data at scale. |
| **FedRAMP** | Federal Risk and Authorization Management Program — US federal government cloud security certification. |
| **GDPR** | General Data Protection Regulation — EU privacy law; mandates consent, breach notification, data subject rights. |
| **HIPAA** | Health Insurance Portability and Accountability Act — US healthcare data privacy regulation. |
| **ISO 9001:2015** | International quality management standard (process discipline, customer focus, continuous improvement). |
| **ISO/IEC 27001:2022** | International information security management standard. The 2022 revision is the latest. |
| **PCI DSS** | Payment Card Industry Data Security Standard — required for entities handling credit-card data. |
| **PIPEDA** | Personal Information Protection and Electronic Documents Act — Canadian federal privacy law. |
| **Schrems II** | EU Court of Justice 2020 ruling restricting EU-to-US data transfers; sets the bar for cross-border DPA terms. |
| **SOC 2** | American Institute of CPAs audit framework for service organizations; a common US enterprise procurement requirement. |

## Security / infrastructure

| Term | Canonical definition |
|---|---|
| **AES-256** | Advanced Encryption Standard with 256-bit key length — symmetric encryption used at rest. |
| **BYOK** | Bring Your Own Key — security model where customers manage their own encryption keys rather than the vendor. |
| **CSP** | Content Security Policy — HTTP header policy mitigating XSS / clickjacking. |
| **MFA / 2FA** | Multi-Factor Authentication / Two-Factor Authentication. |
| **OWASP** | Open Web Application Security Project — security testing methodology. |
| **PIA** | Privacy Impact Assessment — required documentation under GDPR for high-risk processing. |
| **PII** | Personally Identifiable Information. |
| **RBAC** | Role-Based Access Control. |
| **RPO / RTO** | Recovery Point Objective / Recovery Time Objective — disaster-recovery metrics. |
| **SAML** | Security Assertion Markup Language — enterprise SSO standard. |
| **SCIM** | System for Cross-domain Identity Management — provisioning/deprovisioning protocol. |
| **SLA / SLO** | Service Level Agreement / Service Level Objective — uptime / response-time commitments. |
| **SSO** | Single Sign-On. |
| **TLS** | Transport Layer Security — successor to SSL; encrypts in-transit traffic. |
| **WAF** | Web Application Firewall. |

## AI / modern tech

| Term | Canonical definition |
|---|---|
| **AI / AI assistant / AI agent** | Generic terms for LLM-powered software (Claude, ChatGPT, Microsoft Copilot, etc.). "Agent" / "agentic" specifically refers to systems that take autonomous multi-step actions rather than just responding to single prompts. |
| **AI-native** | Software architected around large-language-model agents from inception, rather than retrofitted with AI features over an existing data model. |
| **API** | Application Programming Interface — the contract for software-to-software communication. |
| **Generative AI** | AI that produces new content (text, images, code, etc.) rather than classifying / predicting. |
| **iPaaS** | Integration Platform as a Service — Zapier, Make, Workato, n8n, Tray.io. |
| **LLM** | Large Language Model — transformer-based models like GPT-4, Claude Sonnet/Opus, Llama. |
| **MCP** | Model Context Protocol — open standard introduced by Anthropic in late 2024 for connecting AI assistants to external data sources via standardized servers. |
| **MCP Server** | A specific implementation of MCP deployed as a server — exposes a vendor's data to AI assistants under user-level permissions. |
| **NLU** | Natural Language Understanding — AI ability to interpret human language. |
| **REST** | Representational State Transfer — predominant web API architecture. |
| **RLHF** | Reinforcement Learning from Human Feedback — training method for instruction-tuned LLMs. |
| **SDK** | Software Development Kit — language-specific client library for an API. |
| **TTS / STT** | Text-to-Speech / Speech-to-Text — voice AI capabilities. |

## Sales / CRM / GTM

| Term | Canonical definition |
|---|---|
| **AE** | Account Executive — sales rep responsible for closing deals. |
| **BANT** | Budget / Authority / Need / Timeline — qualification framework. |
| **BDR** | Business Development Representative — outbound prospecting sales role. |
| **CHAMP** | Challenges / Authority / Money / Prioritization — qualification framework. |
| **CPQ** | Configure-Price-Quote — software for generating sales quotes. |
| **CRM** | Customer Relationship Management — software for tracking sales pipelines, customer interactions, and account data. |
| **CSM** | Customer Success Manager — post-sale account-management role. |
| **GTM** | Go-to-Market — the strategy and motion for reaching customers (sales, marketing, partnerships, pricing). |
| **ICP** | Ideal Customer Profile — definition of which buyer / firmographic segment a vendor targets. |
| **MEDDPICC** | Metrics / Economic buyer / Decision criteria / Decision process / Paper process / Identified pain / Champion / Competition — enterprise-sales qualification framework. |
| **MQL** | Marketing Qualified Lead. |
| **SDR** | Sales Development Representative — inbound-lead-qualifying sales role. |
| **SFA** | Sales Force Automation — historic Gartner Magic Quadrant category for sales-rep-facing CRM. |
| **SI / VAR** | Systems Integrator / Value-Added Reseller — channel partners that resell and customize software. |
| **SPIFF** | Sales Performance Incentive Fund — short-term bonus for specific deals. |
| **SPIN Selling** | Consultative sales methodology — Situation / Problem / Implication / Need-payoff. |
| **SQL** | Sales Qualified Lead (NOT Structured Query Language in this context). |

## Procurement / legal / corporate

| Term | Canonical definition |
|---|---|
| **GA** | General Availability — the launch state when software is broadly purchasable, post-beta. |
| **KPI** | Key Performance Indicator — quantitative metric used to track progress toward an objective. |
| **NDA** | Non-Disclosure Agreement — confidentiality contract; required for procurement-stage data exchanges. |
| **OKR** | Objectives and Key Results — goal-setting framework. |
| **PoC / POC** | Proof of Concept — pre-purchase technical evaluation. |
| **PR** | Public Relations / Press Release — context-dependent. |
| **PRD** | Product Requirements Document. |
| **RFP** | Request for Proposal — formal procurement document soliciting vendor bids. |
| **SaaS** | Software as a Service. |
| **TCO** | Total Cost of Ownership. |

## Business-register codes (per jurisdiction)

When the dossier mentions any non-US legal entity, define the relevant register codes:

| Term | Canonical definition |
|---|---|
| **ABN** | Australian Business Number (11-digit). |
| **ACN** | Australian Company Number (9-digit). |
| **CIN** | Corporate Identification Number — India MCA21 (21-digit). |
| **CIPC** | Companies and Intellectual Property Commission — South Africa registrar. |
| **CNPJ** | Cadastro Nacional da Pessoa Jurídica — Brazilian corporate tax ID (14-digit). |
| **CRO** | Companies Registration Office — Ireland registrar. |
| **CVR** | Det Centrale Virksomhedsregister — Danish business register (8-digit). |
| **DUNS** | Dun & Bradstreet Universal Numbering System — global business identifier. |
| **EIN** | Employer Identification Number — US federal tax ID. |
| **FN** | Firmenbuchnummer — Austrian commercial register entry number (e.g., FN 12345a). |
| **HRB** | Handelsregister-B — German commercial register entry for limited liability companies. |
| **ICO** | Identifikačné Číslo Organizácie — Slovak national entity ID. (Note: in other contexts, ICO = Information Commissioner's Office UK or Initial Coin Offering — disambiguated by context.) |
| **KRS** | Krajowy Rejestr Sądowy — Polish National Court Register (10-digit). |
| **KvK** | Kamer van Koophandel — Dutch chamber of commerce register (8-digit). |
| **NIF** | Número de Identificación Fiscal — Spanish/Portuguese tax ID. |
| **NIPC** | Número de Identificação de Pessoa Coletiva — Portuguese corporate ID. |
| **NIT** | Número de Identificación Tributaria — Colombian tax ID. |
| **NZBN** | New Zealand Business Number (13-digit). |
| **REGON** | Polish statistics register (9 or 14-digit). |
| **RFC** | Registro Federal de Contribuyentes — Mexican tax ID. |
| **RUC** | Registro Único de Contribuyentes — Peruvian tax ID. |
| **RUT** | Rol Único Tributario — Chilean / Uruguayan tax ID. |
| **SIREN / SIRET** | French national company identifier (9-digit) and establishment-level identifier (14-digit). |
| **UEN** | Unique Entity Number — Singapore ACRA register. |
| **UID** | Unternehmens-Identifikationsnummer — Swiss company identifier. |
| **USCC** | Unified Social Credit Code — Chinese 18-digit corporate ID. |
| **VAT** | Value Added Tax — EU and UK consumption tax; VAT number format varies per country. |
| **Y-tunnus** | Finnish business ID. |

## Reading-time / format terms

| Term | Canonical definition |
|---|---|
| **AWS Marketplace / GCP Marketplace / Azure Marketplace / Salesforce AppExchange** | Cloud-vendor catalogs for purchasing software through the cloud-vendor's billing relationship. |
| **Magic Quadrant** | Gartner's 2×2 vendor positioning framework (Leaders / Challengers / Visionaries / Niche Players). |
| **Wave (Forrester Wave)** | Forrester's analyst evaluation report — analogous to Gartner Magic Quadrant. |

## Product & growth metrics

| Term | Canonical definition |
|---|---|
| **AARRR / Pirate Metrics** | Acquisition / Activation / Retention / Revenue / Referral — Dave McClure's startup-funnel framework. |
| **Activation** | The point where a new user reaches first meaningful value (the "aha moment"). Not the same as signup. |
| **Churn** | % of customers who cancel in a period. Logo churn = customer count; gross dollar churn = revenue lost; net churn = factoring expansion. |
| **CES** | Customer Effort Score — single-question survey ("how easy was it to resolve your issue?"). Customer-success metric. |
| **Cohort analysis** | Tracking metrics for groups of users by signup date / behavior cohort. |
| **CSAT** | Customer Satisfaction Score — typical 1–5 or 1–10 scale survey. |
| **DAU / MAU / WAU** | Daily / Monthly / Weekly Active Users — engagement metrics. DAU/MAU ratio = stickiness. |
| **K-factor / Viral coefficient** | Average new-users-invited-per-existing-user × invite-conversion-rate. K > 1 = viral growth. |
| **MAU** | Monthly Active Users — see DAU/MAU/WAU. |
| **North-star metric** | Single metric a company optimizes for; aligns the whole org. Often a leading indicator of long-term value. |
| **NPS** | Net Promoter Score — % promoters minus % detractors on a 0–10 "would you recommend" scale. |
| **PMF** | Product-Market Fit — qualitative state where users genuinely need the product (e.g., 40%+ "very disappointed if it disappeared" per Sean Ellis). |
| **Retention curve** | % of users still active after N days/weeks/months. Flat curve = sticky product. |
| **Stickiness** | DAU ÷ MAU; how often users come back. |
| **TTV** | Time-to-Value — duration from signup to first meaningful outcome. |

## Pricing & business models

| Term | Canonical definition |
|---|---|
| **Consumption / usage-based pricing** | Charge by units consumed (API calls, tokens, GB stored). Common in DevOps tools (Snowflake, Datadog) + AI APIs. |
| **Flat-rate pricing** | Single price per seat/account regardless of usage. Common at SMB tier. |
| **Free trial** | Time-limited full-feature access with no payment up front. Common in B2B SaaS. |
| **Freemium** | Free tier with limited features + paid tiers. Drives top-of-funnel acquisition (Slack, Notion, Figma, Zoom). |
| **Hybrid pricing** | Combination of flat-rate base + consumption-based usage. Common in enterprise tools. |
| **Land-and-expand** | Sales motion — start small, expand seats/usage over time. Standard for enterprise SaaS. |
| **Per-seat pricing** | Charge per user/seat. Standard for collaboration tools (Slack, Salesforce, GitHub). |
| **PLG** | Product-Led Growth — distribution model where the product itself drives acquisition (free tier + viral mechanics + self-serve onboarding). Slack, Notion, Figma archetypes. |
| **Tiered pricing** | Fixed packages (Basic / Pro / Enterprise) at increasing price points + features. Most common B2B SaaS model. |

## Engineering / DevOps

| Term | Canonical definition |
|---|---|
| **CI/CD** | Continuous Integration / Continuous Deployment — automated build + test + deploy pipeline. |
| **CDN** | Content Delivery Network — geographically distributed cache (Cloudflare, Fastly, Akamai). |
| **Edge / edge function** | Compute that runs at CDN edge nodes vs centralized servers. Lower latency. |
| **FaaS** | Function as a Service — event-driven compute (AWS Lambda, Cloudflare Workers, Vercel Functions). |
| **IaaS** | Infrastructure as a Service — raw VMs / storage / network (AWS EC2, GCP Compute, Azure VMs). |
| **IaC** | Infrastructure as Code — declarative infra management (Terraform, CloudFormation, Pulumi, CDK). |
| **K8s / Kubernetes** | Container orchestration platform; de facto standard for managing containerized apps. |
| **MLOps** | Machine Learning Operations — DevOps practices for ML model lifecycle. |
| **Microservices vs monolith** | Architectural styles. Monolith = single deployable; microservices = independently deployable services. |
| **MTBF / MTTR** | Mean Time Between Failures / Mean Time To Recovery — reliability metrics. |
| **Multi-tenant vs single-tenant** | Multi-tenant = one infra instance serving many customers (data segregated); single-tenant = isolated infra per customer. |
| **Observability** | Ability to understand system behavior from external outputs (logs, metrics, traces). Tools: Datadog, New Relic, Grafana, OpenTelemetry. |
| **OpenTelemetry** | CNCF open standard for observability data (logs, metrics, traces). |
| **PaaS** | Platform as a Service — managed runtime (Heroku, Vercel, Railway, Render). |
| **Serverless** | Compute model with no server management; FaaS or managed runtime; pay per execution. |
| **SRE** | Site Reliability Engineering — Google-originated discipline merging SWE + ops; defines SLIs/SLOs/SLAs. |

## Data / analytics

| Term | Canonical definition |
|---|---|
| **Data lake** | Storage for raw / unstructured data at scale (S3, GCS, Azure Data Lake). |
| **Data lakehouse** | Hybrid of data lake + warehouse; query unstructured data with warehouse semantics (Databricks, Snowflake Iceberg). |
| **Data mesh** | Decentralized data architecture; each domain team owns its data products. |
| **Data warehouse** | Analytics-optimized columnar database (Snowflake, BigQuery, Redshift). |
| **dbt** | Data build tool — open-source SQL-based transformation framework; transformed-layer of modern data stack. |
| **ELT vs ETL** | Extract-Load-Transform vs Extract-Transform-Load. ELT = transform inside warehouse (modern); ETL = transform before loading (legacy). |
| **Reverse ETL** | Sync data FROM warehouse back into operational tools (Hightouch, Census). |

## Modern AI terms

| Term | Canonical definition |
|---|---|
| **Agentic AI** | AI systems that take autonomous multi-step actions, reason about goals, and use tools — vs single-prompt response. |
| **Embedding** | Numeric vector representation of content (text, image, audio); enables similarity search and retrieval. |
| **Fine-tuning** | Adapting a pre-trained model to a specific dataset / task. Producing a domain-specific model. |
| **Function calling / Tool use** | LLM capability to invoke external tools / APIs based on user prompts. Foundation for agentic systems. |
| **GPT wrapper / AI wrapper** | Slang (often pejorative) for products that primarily wrap an underlying LLM (OpenAI, Anthropic) without proprietary value. Common Reddit critique of micro-SaaS AI tools. |
| **Hallucination** | LLM confidently producing factually wrong output. Mitigated by RAG + citations + grounding. |
| **Jailbreak** | Prompt-engineering technique to bypass an LLM's safety guardrails. |
| **LoRA / QLoRA** | Low-Rank Adaptation — parameter-efficient fine-tuning method; fine-tunes small adapter weights instead of full model. |
| **Prompt engineering** | Crafting inputs to LLMs to elicit better outputs. |
| **RAG** | Retrieval-Augmented Generation — pattern where LLM queries an external knowledge base (vector DB) before generating. Mitigates hallucination. |
| **System prompt** | High-level instructions / persona / constraints injected at the start of an LLM context window. |
| **Vector database / Vector DB** | Database optimized for storing + querying embeddings (Pinecone, Weaviate, Qdrant, Chroma, pgvector). |

## Marketing / growth / sales ops

| Term | Canonical definition |
|---|---|
| **ABM** | Account-Based Marketing — targeting specific named accounts vs broad demand-gen. |
| **Cold outreach / cold email** | Unsolicited contact to prospects; backbone of outbound sales. |
| **Deal velocity** | Avg time from opportunity created → closed/won. Lower = better. |
| **Drip campaign** | Automated sequence of emails / messages over time. |
| **GEO** | Generative Engine Optimization — optimizing content to surface in LLM-generated answers (vs SEO for search engines). |
| **Growth hacking** | Term coined by Sean Ellis; data-driven, rapid-experimentation approach to growth. Now a generic / cliché term. |
| **Growth loops** | Self-reinforcing user-acquisition loops (referral loops, content loops, viral loops). Distinct from one-shot funnels. |
| **Logo retention** | % of customer logos retained year-over-year (independent of expansion / contraction revenue). |
| **Outbound vs inbound** | Outbound = vendor reaches out (cold email, SDR motion). Inbound = customer comes to vendor (SEO, content, referral). |
| **Pipeline coverage** | Pipeline value ÷ quota; healthy SaaS sees 3-4× coverage. |
| **PLG vs SLG** | Product-Led Growth vs Sales-Led Growth — distribution-strategy archetypes. |
| **Quota attainment** | % of sales reps hitting their quota. Industry healthy = 50–60%. |
| **Ramp time** | Months for a new sales rep to reach full productivity. Typical SaaS: 3–6 mo. |
| **SEM** | Search Engine Marketing — paid search ads (Google Ads). |
| **SEO** | Search Engine Optimization — organic search visibility. |
| **TOFU / MOFU / BOFU** | Top / Middle / Bottom of Funnel — content / lead-gen funnel stages. |

## Equity / compensation / corporate events

| Term | Canonical definition |
|---|---|
| **Cap table** | List of who owns what % of a company; tracks shares outstanding by class. |
| **Cliff** | Initial period before stock vesting begins (typical 1-year cliff on 4-year vest). |
| **Down-round** | Funding round at lower valuation than prior round. Generally negative signal. |
| **ESPP** | Employee Stock Purchase Plan — public-company perk; employees buy stock at discount. |
| **Exit** | Liquidity event — IPO, acquisition, or buyout. |
| **Fully diluted** | Cap-table view including all options/warrants/convertibles as if exercised. |
| **IPO** | Initial Public Offering — listing on a public stock exchange. |
| **ISO / NSO** | Incentive Stock Options / Non-Qualified Stock Options — US tax treatments for stock options. |
| **M&A** | Mergers & Acquisitions. |
| **MBO** | Management Buyout — existing leadership purchases the company. |
| **Post-money / Pre-money valuation** | Valuation after / before a funding round. Post-money = pre-money + round size. |
| **Recap (recapitalization)** | Restructuring of capital structure; sometimes signals distress. |
| **RSU** | Restricted Stock Unit — promise of stock; common at later-stage / public companies. |
| **Secondary** | Sale of existing shares (vs new "primary" shares). Provides liquidity to founders/early employees pre-IPO. |
| **SPAC** | Special Purpose Acquisition Company — "blank check" listing vehicle; alternative to traditional IPO. Boom 2020–21, faded since. |
| **Spinoff** | Separating a business unit into an independent entity. |
| **Vesting** | Schedule by which stock/options become owned by the recipient. Standard: 4 years with 1-year cliff. |

## Modern startup vocab (Reddit / Twitter / Indie Hackers)

| Term | Canonical definition |
|---|---|
| **Bootstrapped** | Self-funded company; no institutional VC. Common framing on r/SaaS, r/Entrepreneur, IndieHackers. |
| **Build-in-public** | Sharing development progress / metrics publicly (Twitter, Reddit, IndieHackers). Marketing strategy common in indie SaaS. |
| **Indie hacker / IndieHackers** | Solo or small-team founder building SaaS products without external funding. Community: indiehackers.com. |
| **Lifestyle business** | Profitable small business optimized for founder quality-of-life rather than venture-scale growth. |
| **Low-code / no-code** | Build software with minimal / no traditional programming (Zapier, Bubble, Webflow, Airtable). |
| **Micro-SaaS** | Small (often 1-person) SaaS targeting a narrow vertical. Typically $10K–$100K MRR ceiling. |
| **Moat** | Competitive advantage that's structurally hard to replicate (network effects, switching costs, brand, data). Buffett-originated. |
| **Network effect** | Value increases with each new user (Metcalfe's Law). Marketplaces, social networks, comms tools. |
| **Sticky** | High retention; low churn. Subjective term. |
| **Solopreneur** | Solo founder running a self-funded business. |
| **SaaS arbitrage** | Reselling existing SaaS as a packaged service (often pejorative; Reddit critique). |
| **Vibe coding** | Coding by feel / iteration with AI assistance, accepting LLM-generated code without deep review. Coined ~2024–25; popular and polarizing on Reddit / X. |

## Customer success / support

| Term | Canonical definition |
|---|---|
| **AHT** | Average Handle Time — duration of a support interaction. |
| **Deflection rate** | % of support requests resolved without human intervention (self-serve docs, AI chatbot). |
| **FCR** | First Contact Resolution — % of issues resolved on first interaction. |
| **GRR** | Gross Revenue Retention — retention without expansion (compares to NRR). |
| **NDR** | Net Dollar Retention — same as NRR; some firms use this term. |
| **Onboarding** | Process of getting a new customer to first value (TTV) and adoption. |
| **QBR** | Quarterly Business Review — recurring meeting between vendor + enterprise customer. |

## Privacy / data residency / sovereignty

| Term | Canonical definition |
|---|---|
| **Data residency** | Where customer data is physically stored (specific country / region). |
| **Data sovereignty** | Legal jurisdiction governing data, often more restrictive than residency. |
| **DSAR** | Data Subject Access Request — GDPR-mandated right to receive a copy of one's personal data. |
| **Right to be forgotten** | GDPR Article 17 — right to erasure of personal data. |

## Open source / licensing

| Term | Canonical definition |
|---|---|
| **AGPL** | GNU Affero General Public License — strong copyleft; triggers source-share even on network/SaaS deployment. |
| **Apache 2.0** | Permissive license; allows commercial use; requires preserving notices. |
| **BSL / Business Source License** | Source-available; converts to open source after time delay. Used by HashiCorp Terraform, MariaDB, CockroachDB. |
| **Copyleft** | License class requiring derivative works to use the same license (GPL, AGPL). |
| **Fork** | Independent copy of an open-source project; can diverge from upstream. |
| **GPL** | GNU General Public License — strong copyleft. |
| **MIT** | Permissive license; minimal restrictions; widely used for libraries. |
| **Permissive** | License class allowing relicensing of derivative works (MIT, Apache, BSD). |
| **SPDX** | Software Package Data Exchange — standard for license / dependency identification. |

## When to load this file

Load `glossary-catalog.md` when:
- Writing §22 Glossary (Step 4 Draft, near end)
- After running the glossary-completeness scan in Step 5 to identify which catalog entries to add for missed terms
- When asked to "expand the glossary" or "review what's missing"

## How to use this file

The catalog is a **menu, not a recipe.**

- ✅ Pull entries that match terms ACTUALLY USED in the body
- ✅ Adapt definitions to be specific to the entity (e.g., for an entity's MCP Server entry, mention when they shipped vs. when competitors did)
- ❌ Don't dump the entire catalog into §22 — clutter; readers don't need definitions for terms not in the body
- ❌ Don't define terms generically when entity-specific framing is more useful (e.g., for entity X, "API rate limits" is more useful than just "API")

## Anti-patterns

- ❌ Glossary with <30 entries on a `--depth=deep` dossier — likely missing terms; rerun the scan
- ❌ Using the catalog literal-copy when the entity has specific framing — adapt
- ❌ Defining terms that don't appear in the body — clutter
- ❌ Letting the model decide which terms to include from memory alone — relies on attention, misses obvious ones; **always run the scan**
