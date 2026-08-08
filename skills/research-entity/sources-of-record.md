# Sources of Record — Skill-Cited External Sources Registry

**Single source of truth for every load-bearing external source cited by the research-entity skill.** When a source migrates, deprecates, or shuts down, update the entry here. Skill segment files reference this registry; updating one row propagates correct guidance.

**Maintenance command:** `/research-entity --validate-skill-sources` runs URL validation across all skill files + cross-references this registry's `last-verified` dates + flags shutdown-risk + outputs a remediation plan. Recommended cadence: **monthly** (via `/schedule`).

---

## §1 — How to read this registry

Each source row contains:

| Field | Meaning |
|---|---|
| **Source** | Canonical name (e.g., "ICD 203 — Analytic Standards") |
| **Primary URL** | Authoritative source URL |
| **Backup/Mirror** | Fallback URL if primary fails (Wayback / mirror / academic copy) |
| **Last verified** | Date a maintainer confirmed URL resolves + content matches citation (YYYY-MM-DD) |
| **Cadence** | How often the source itself updates: `frozen` / `annual` / `continuous` / `irregular` |
| **Risk** | Decay risk: `STABLE` / `ANNUAL` / `CONTINUOUS` / `URL-PRONE` / `SHUTDOWN-RISK` |
| **Cited in** | Which skill files reference this source |
| **Notes** | Migration history, known-issues, special-handling guidance |

## §2 — Decay-rate categories

| Category | Decay rate | Example | Maintenance |
|---|---|---|---|
| **STABLE** | Decade-scale | Heuer, CIA Tradecraft Primer, Pang & Lee 2008, Ghemawat HBR 2001, ICD 203 declassified | Validate URLs annually; content frozen — no skill refresh needed for content |
| **ANNUAL** | 12 months | Bessemer State of the Cloud, KeyBanc SaaS Survey, ICONIQ quarterly | Update report-year citation when new edition publishes; pin year in skill text |
| **CONTINUOUS** | Real-time | MITRE ATT&CK (~quarterly), CISA KEV, NVD CVE, marketplace install counts | URL stable; data is live → no skill refresh needed |
| **URL-PRONE** | Months-years | AICPA org migration to aicpa-cima.com; USPTO TESS retired Nov 2023 | Validate URLs quarterly |
| **REGULATORY** | 6-24 months | EU AI Act enforcement timeline; new state privacy laws cascading | Quarterly regulatory-overlay refresh |
| **SHUTDOWN-RISK** | Years | OpenView (closed 2023), Lanyrd (closed 2014), MonkeyLearn | Annual check; flag when source goes dark |

---

## §3 — Sources by category

### Category A: Stable foundational (academic / government / declassified — content frozen, URLs stable)

| # | Source | Primary URL | Backup | Last verified | Cadence | Risk | Cited in | Notes |
|---|---|---|---|---|---|---|---|---|
| A1 | **ICD 203 — Analytic Standards** (DNI) | https://www.dni.gov/files/documents/ICD/ICD-203.pdf | dni.gov ICD index | 2026-04-27 | frozen (last update 2015) | STABLE | analytic-techniques.md, source-rating.md, about.md | Foundational IC analytic standard |
| A2 | **ICD 206 — Sourcing Requirements** (DNI) | https://www.dni.gov/index.php/what-we-do/ic-policies-reports/intelligence-community-directives | — | 2026-04-27 | frozen | STABLE | analytic-techniques.md (Section 7) | Companion to ICD 203 |
| A3 | **CIA Tradecraft Primer (2009, declassified)** | https://www.cia.gov/resources/csi/static/955180a45afe3f5013772c313b16face/Tradecraft-Primer-apr09.pdf | Internet Archive | 2026-08-07 | frozen (declassified) | STABLE | analytic-techniques.md (Section 6) | CIA static-asset paths can change; verify quarterly |
| A4 | **Heuer — Psychology of Intelligence Analysis (1999, declassified)** | https://www.cia.gov/resources/csi/static/9a5f1162fd0932c29bfed1c030edf4ae/Pyschology-of-Intelligence-Analysis.pdf | Internet Archive | 2026-08-07 | frozen | STABLE | analytic-techniques.md | Note: CIA URL uses misspelling "Pyschology" — this is the real CIA URL |
| A5 | **SPJ Code of Ethics** | https://www.spj.org/ethicscode.asp | Internet Archive | 2026-04-27 | rare-revisions | STABLE | source-hierarchy.md | Verify URL still resolves; SPJ has hyphenated alternative paths |
| A6 | **AICPA AT-C 105 — Concepts Common to All Attestation Engagements** | https://www.aicpa-cima.com/resources/download/aicpa-ssaes-currently-effective | https://www.aicpa-cima.com/ | 2026-08-07 | rare-revisions | URL-PRONE | source-hierarchy.md | AICPA migrated to AICPA & CIMA in 2022; backup URL preferred |
| A7 | **AICPA SOC for Service Organizations** | https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2 | aicpa.org legacy | 2026-04-27 | annual | STABLE | press-analysis.md | "greater-than" in URL slug is real (encoded `>`) |
| A8 | **AICPA Peer Review program** | https://peerreview.aicpa.org/ | — | 2026-04-27 | continuous | CONTINUOUS | press-analysis.md | Used to verify SOC 2 audit firm credentials |
| A9 | **IAF (International Accreditation Forum)** | https://iaf.nu/ | — | 2026-04-27 | continuous | CONTINUOUS | press-analysis.md | ISO certification body lookup |
| A10 | **Reuters Handbook of Journalism** | https://handbook.reuters.com/ | — | 2026-04-27 | rare-revisions | STABLE | source-hierarchy.md | Reuters editorial standards |
| A11 | **Bellingcat Online Investigations Toolkit** | https://www.bellingcat.com/resources/ | — | 2026-04-27 | irregular | STABLE | source-hierarchy.md, internal-consistency.md | OSINT verification handbook |
| A12 | **ICIJ (Investigative reporting standards)** | https://www.icij.org/about/ | — | 2026-04-27 | irregular | STABLE | source-hierarchy.md | Multi-source verification methodology |
| A13 | **Hu & Liu 2004 — Mining and Summarizing Customer Reviews (KDD)** | https://www.cs.uic.edu/~liub/publications/kdd04-revSummary.pdf | ACM Digital Library | 2026-04-27 | frozen | STABLE | reviews-platforms.md | Foundational ABSA paper |
| A14 | **Pang & Lee 2008 — Opinion Mining and Sentiment Analysis** | https://www.cs.cornell.edu/home/llee/omsa/omsa.pdf | — | 2026-04-27 | frozen | STABLE | reviews-platforms.md | Field survey of sentiment analysis |
| A15 | **SemEval 2014 Task 4 — ABSA shared task** | https://alt.qcri.org/semeval2014/task4/ | — | 2026-04-27 | frozen | STABLE | reviews-platforms.md | Academic benchmark |
| A16 | **Tetlock & Mellers — Good Judgment Project research** | https://goodjudgment.com/research/ | — | 2026-04-27 | irregular | STABLE | analytic-techniques.md | GJP papers |
| A17 | **IARPA ACE program** | https://www.iarpa.gov/research-programs/ace | — | 2026-04-27 | frozen (program ended 2015) | STABLE | analytic-techniques.md | Aggregative Contingent Estimation |
| A18 | **Brier 1950 — Verification of Forecasts Expressed in Terms of Probability** | AMS Journals | — | 2026-04-27 | frozen | STABLE | analytic-techniques.md | Origin of Brier score |
| A19 | **Ghemawat — Distance Still Matters (HBR Sept 2001)** | https://hbr.org/2001/09/distance-still-matters-the-hard-reality-of-global-expansion | — | 2026-04-27 | frozen | STABLE | regulatory-overlay.md | CAGE Distance Framework |
| A20 | **Pherson & Heuer — Structured Analytic Techniques (CQ Press 2014)** | (book — paywalled) | declassified Heuer 1999 covers same content | 2026-04-27 | frozen | STABLE | analytic-techniques.md | Book content via declassified Heuer 1999 |
| A21 | **AMEC Barcelona Principles 3.0 (2020)** | https://amecorg.com/barcelona-principles/ | — | 2026-04-27 | revised every 5-10yr | STABLE | press-analysis.md | PR measurement industry standard |
| A22 | **Forrester Total Economic Impact (TEI) methodology** | https://www.forrester.com/policies/tei | — | 2026-08-07 | annual-summaries | STABLE | marketplace-signals.md, about.md | URL was wrong in early v2.6; corrected |

### Category B: Annual benchmarks (year-pin required when citing)

| # | Source | Primary URL | Last verified | Latest year cited in skill | Risk | Notes |
|---|---|---|---|---|---|---|
| B1 | **Bessemer State of the Cloud** | https://www.bvp.com/atlas | 2026-04-27 | "current-year" referenced (year-pin required) | ANNUAL | Annual report; skill cites $/FTE bands as directional |
| B2 | **Bessemer Cloud Index (BVP Nasdaq Emerging Cloud)** | https://cloudindex.bvp.com/ | 2026-04-27 | continuous (real-time) | CONTINUOUS | Public-comp multiples |
| B3 | **OpenView Expansion SaaS Benchmarks** | https://openviewpartners.com/blog/ | 2026-04-27 | legacy archives only — OpenView wound down 2023 | SHUTDOWN-RISK | Reports archived; no new editions |
| B4 | **KeyBanc Capital Markets SaaS Survey** | https://www.key.com/businesses-institutions/industry-expertise/keybanc-capital-markets.html | 2026-04-27 | summary-public, full-paywall | ANNUAL | Annual survey |
| B5 | **ICONIQ Growth quarterly reports** | https://www.iconiq.com/ | 2026-04-27 | quarterly | ANNUAL (quarterly) | Sales efficiency, magic number, NRR cohorts |
| B6 | **Sapphire Ventures benchmarks** | https://sapphireventures.com/blog | 2026-04-27 | irregular | ANNUAL | SaaS metrics by stage |
| B7 | **SaaS Capital benchmarks** | https://www.saas-capital.com/ | 2026-04-27 | annual | ANNUAL | Private SaaS benchmarks |
| B8 | **Battery Ventures State of the OpenCloud** | https://www.battery.com/blog/category/research/ | 2026-08-07 | annual | ANNUAL | OSS + cloud benchmarks |
| B9 | **Bridge Group SaaS AE / Inside Sales Reports** | https://bridgegroupinc.com/ | 2026-04-27 | subscription/report-purchase | ANNUAL | AE quota benchmarks |
| B10 | **RepVue compensation data** | https://repvue.com/ | 2026-04-27 | continuous | CONTINUOUS | Real-time AE quota + attainment |
| B11 | **Pavilion (formerly Revenue Collective)** | https://www.joinpavilion.com/ | 2026-04-27 | annual | ANNUAL | Peer-benchmark reports |
| B12 | **PRovoke Media Earned Media Index** | https://www.provokemedia.com/ | 2026-04-27 | annual | ANNUAL | Earned-vs-paid PR measurement |

### Category C: Continuously updated registries (URL stable, content live)

| # | Source | Primary URL | Last verified | Cadence | Notes |
|---|---|---|---|---|---|
| C1 | **MITRE ATT&CK Framework** | https://attack.mitre.org/ | 2026-04-27 | quarterly | Adversary-behavior framework |
| C2 | **MITRE D3FEND** | https://d3fend.mitre.org/ | 2026-04-27 | irregular | Defensive techniques |
| C3 | **CISA Known Exploited Vulnerabilities (KEV)** | https://www.cisa.gov/known-exploited-vulnerabilities-catalog | 2026-04-27 | continuous (CSV/JSON download) | Real-time KEV catalog |
| C4 | **NVD CVE Database** | https://nvd.nist.gov/ | 2026-04-27 | continuous (REST API) | National Vulnerability Database |
| C5 | **CVE.org (MITRE)** | https://www.cve.org/ | 2026-04-27 | continuous | CVE source-of-record |
| C6 | **EPSS (Exploit Prediction Scoring System)** | https://www.first.org/epss/ | 2026-04-27 | continuous | FIRST.org |
| C7 | **ENISA Threat Landscape** | https://www.enisa.europa.eu/ | 2026-04-27 | annual report | EU cyber agency |
| C8 | **NCSC UK guidance** | https://www.ncsc.gov.uk/ | 2026-04-27 | continuous | UK National Cyber Security Centre |
| C9 | **USPTO TM Search (formerly TESS, retired Nov 2023)** | https://tmsearch.uspto.gov/ | 2026-08-07 | continuous | TM Search replaced TESS |
| C10 | **EUIPO eSearch plus** | https://euipo.europa.eu/eSearch/ | 2026-04-27 | continuous | EU trademarks |
| C11 | **WIPO Madrid Monitor** | https://www3.wipo.int/madrid/monitor/ | 2026-04-27 | continuous | International trademarks (verify URL — `madrid.wipo.int` is alternative subdomain) |
| C12 | **Internet Archive Wayback Machine** | https://web.archive.org/ | 2026-04-27 | continuous | Free, no API key needed |
| C13 | **crt.sh (Certificate Transparency)** | https://crt.sh/ | 2026-04-27 | continuous | SSL cert transparency search |
| C14 | **ICANN whois lookup** | https://lookup.icann.org/ | 2026-04-27 | continuous | Current whois |
| C15 | **DNSdumpster** | https://dnsdumpster.com/ | 2026-04-27 | continuous | DNS map + subdomains |

### Category D: Marketplaces + integrations (continuously updated, listing-stable)

| # | Source | Primary URL | Last verified | Notes |
|---|---|---|---|---|
| D1 | **Salesforce AppExchange** | https://appexchange.salesforce.com/ | 2026-04-27 | Reviews + ratings public; no install count |
| D2 | **HubSpot App Marketplace** | https://ecosystem.hubspot.com/ | 2026-04-27 | Install range + reviews public |
| D3 | **Microsoft AppSource** | https://appsource.microsoft.com/ | 2026-04-27 | Reviews + ratings public |
| D4 | **Microsoft Azure Marketplace** | https://azuremarketplace.microsoft.com/ | 2026-04-27 | Reviews + ratings public |
| D5 | **Atlassian Marketplace** | https://marketplace.atlassian.com/ | 2026-04-27 | **Exact install count** (gold standard) |
| D6 | **Slack App Directory** | https://slack.com/apps | 2026-04-27 | Reviews public; no install count |
| D7 | **Zoom App Marketplace** | https://marketplace.zoom.us/ | 2026-04-27 | Reviews + ratings |
| D8 | **GitHub Marketplace** | https://github.com/marketplace | 2026-04-27 | Install context visible |
| D9 | **Chrome Web Store** | https://chromewebstore.google.com/ | 2026-04-27 | Exact user count |
| D10 | **Firefox Add-ons (AMO)** | https://addons.mozilla.org/ | 2026-04-27 | Exact user count + total downloads |
| D11 | **Edge Add-ons** | https://microsoftedge.microsoft.com/addons/ | 2026-04-27 | User count + reviews |
| D12 | **AWS Marketplace** | https://aws.amazon.com/marketplace/ | 2026-04-27 | Reviews + rating; no install count |
| D13 | **Google Cloud Marketplace** | https://console.cloud.google.com/marketplace | 2026-04-27 | Listings + reviews |
| D14 | **Snowflake Marketplace** | https://app.snowflake.com/marketplace | 2026-04-27 | Listings |
| D15 | **Zapier integrations** | https://zapier.com/apps/ | 2026-04-27 | Popularity rank |
| D16 | **Make.com (formerly Integromat)** | https://www.make.com/en/integrations | 2026-04-27 | App presence |
| D17 | **n8n integrations** | https://n8n.io/integrations | 2026-04-27 | Popularity rank |
| D18 | **npm registry** | https://npmjs.com/ | 2026-04-27 | Exact weekly download count |
| D19 | **PyPI** | https://pypi.org/ | 2026-04-27 | Download stats via pypistats.org |
| D20 | **RubyGems** | https://rubygems.org/ | 2026-04-27 | Exact download count |
| D21 | **Cargo (Rust crates)** | https://crates.io/ | 2026-04-27 | Download count |
| D22 | **pkg.go.dev** | https://pkg.go.dev/ | 2026-04-27 | Importer count |
| D23 | **Docker Hub** | https://hub.docker.com/ | 2026-04-27 | Pull count + stars |

### Category E: Regulatory regimes (verify quarterly for enforcement updates)

| # | Source | Primary URL | Last verified | Cadence | Notes |
|---|---|---|---|---|---|
| E1 | **GDPR (EU/UK) — EDPB** | https://www.edpb.europa.eu/ | 2026-04-27 | continuous | European Data Protection Board |
| E2 | **EU AI Act** | https://artificialintelligenceact.eu/ | 2026-04-27 | enforcement-evolving 2026-2027 | REGULATORY — enforcement timeline shifts |
| E3 | **EU AI Act (official)** | https://eur-lex.europa.eu/ | 2026-04-27 | regulatory updates | EUR-Lex |
| E4 | **OFAC SDN list** | https://sanctionslist.ofac.treas.gov/Home/SdnList | 2026-08-07 | continuous | Backup: home.treasury.gov/policy-issues/financial-sanctions; legacy URL deprecated |
| E5 | **CFIUS (US foreign investment)** | https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius | 2026-04-27 | irregular | US Treasury |
| E6 | **HIPAA (US health) — HHS OCR** | https://www.hhs.gov/hipaa/ | 2026-04-27 | irregular | Health regulatory |
| E7 | **GLBA (US finance) — FTC** | https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act | 2026-04-27 | irregular | Financial regulatory |
| E8 | **CCPA / CPRA (California)** | https://oag.ca.gov/privacy/ccpa | 2026-04-27 | annual updates | CA AG |
| E9 | **State privacy laws (IAPP comparator)** | https://iapp.org/resources/article/us-state-privacy-legislation-tracker | 2026-08-07 | quarterly | IAPP — quarterly cascade tracking |
| E10 | **DPDP Act (India) — MeitY** | https://www.meity.gov.in/ | 2026-04-27 | enforcement-evolving | Indian regulatory |
| E11 | **PIPL (China) — CAC** | http://www.cac.gov.cn/ | 2026-04-27 | irregular | English summaries via NYU Asia Society |
| E12 | **LGPD (Brazil) — ANPD** | https://www.gov.br/anpd/ | 2026-04-27 | irregular | Brazilian regulatory |
| E13 | **POPIA (South Africa)** | https://inforegulator.org.za/ | 2026-04-27 | irregular | SA Information Regulator |
| E14 | **PIPEDA (Canada) — OPC** | https://www.priv.gc.ca/ | 2026-04-27 | irregular | Canadian Privacy Commissioner |
| E15 | **Privacy Act (Australia) — OAIC** | https://www.oaic.gov.au/ | 2026-04-27 | irregular | Australian Privacy |
| E16 | **PDPO (Hong Kong) — PCPD** | https://www.pcpd.org.hk/ | 2026-04-27 | irregular | HK Privacy |
| E17 | **PDPA (Singapore) — PDPC** | https://www.pdpc.gov.sg/ | 2026-04-27 | irregular | Singapore Privacy |
| E18 | **PCI Security Standards Council** | https://www.pcisecuritystandards.org/ | 2026-04-27 | annual | PCI DSS |
| E19 | **FedRAMP (US gov cloud) — GSA** | https://www.fedramp.gov/ | 2026-04-27 | continuous (marketplace) | US gov cloud certification |
| E20 | **StateRAMP** | https://www.stateramp.org/ | 2026-04-27 | continuous | US state-level cloud cert |
| E21 | **C5 (Germany cloud) — BSI** | https://www.bsi.bund.de/EN/ | 2026-04-27 | irregular | German cloud cert |
| E22 | **TISAX (German automotive) — ENX** | https://enx.com/tisax/ | 2026-04-27 | annual | Auto industry security |
| E23 | **NIST CSF / 800-53** | https://www.nist.gov/cyberframework | 2026-04-27 | major-updates | NIST cybersecurity framework |
| E24 | **HITRUST Alliance** | https://hitrustalliance.net/ | 2026-04-27 | annual | Healthcare security |
| E25 | **NCSC Cyber Essentials (UK)** | https://www.ncsc.gov.uk/cyberessentials/overview | 2026-04-27 | annual | UK basic-cyber cert |

### Category F: Job boards / OSINT data sources (continuously updated)

| # | Source | Primary URL | Last verified | Notes |
|---|---|---|---|---|
| F1 | **Greenhouse Job Boards** | https://boards.greenhouse.io/ | 2026-04-27 | Companies-using-Greenhouse-ATS pattern |
| F2 | **Lever** | https://jobs.lever.co/ | 2026-04-27 | Companies-using-Lever-ATS pattern |
| F3 | **Ashby** | https://jobs.ashbyhq.com/ | 2026-04-27 | Modern startup ATS |
| F4 | **Workable** | https://apply.workable.com/ | 2026-04-27 | — |
| F5 | **LinkedIn Jobs** | https://linkedin.com/jobs/ | 2026-04-27 | Largest aggregator |
| F6 | **Indeed** | https://indeed.com/ | 2026-04-27 | US largest aggregator |
| F7 | **AngelList / Wellfound** | https://wellfound.com/ | 2026-04-27 | Startup-focused |
| F8 | **Built In** | https://builtin.com/ | 2026-04-27 | Startup-focused |

### Category G: Press/aggregator/specialty (URL-prone, verify quarterly)

| # | Source | Primary URL | Last verified | Risk | Notes |
|---|---|---|---|---|---|
| G1 | **Wappalyzer** (free tier) | https://www.wappalyzer.com/ | 2026-04-27 | URL-PRONE | Tech-stack from headers |
| G2 | **BuiltWith** (free tier) | https://builtwith.com/ | 2026-04-27 | URL-PRONE | Tech-stack |
| G3 | **SecurityTrails** (free tier 50/mo) | https://securitytrails.com/ | 2026-04-27 | URL-PRONE | Subdomain history |
| G4 | **DomainTools whois history** (paid for full) | https://whois.domaintools.com/ | 2026-04-27 | URL-PRONE | Whois changes over time |
| G5 | **SimilarWeb** (free tier) | https://www.similarweb.com/ | 2026-04-27 | URL-PRONE | Web traffic estimate |
| G6 | **Semrush** (free tier) | https://www.semrush.com/ | 2026-04-27 | URL-PRONE | Organic + paid traffic |
| G7 | **Ahrefs** (free tier) | https://ahrefs.com/ | 2026-04-27 | URL-PRONE | Backlink + traffic |
| G8 | **Cloudflare Radar** | https://radar.cloudflare.com/ | 2026-04-27 | URL-PRONE | Domain-level traffic |
| G9 | **Justia trademarks** (US mirror) | https://trademarks.justia.com/ | 2026-04-27 | URL-PRONE | US TM mirror |

### Category H: Conferences (irregular updates, mostly stable)

| # | Source | Primary URL | Last verified | Notes |
|---|---|---|---|---|
| H1 | **Dreamforce** | https://www.salesforce.com/dreamforce/ | 2026-04-27 | Salesforce ecosystem |
| H2 | **SaaStr Annual** | https://www.saastr.com/ | 2026-04-27 | SaaS / GTM |
| H3 | **AWS re:Invent** | https://reinvent.awsevents.com/ | 2026-04-27 | Cloud / infrastructure |
| H4 | **Microsoft Build / Ignite** | https://build.microsoft.com/ | 2026-04-27 | Microsoft ecosystem |
| H5 | **Google Cloud Next** | https://cloud.withgoogle.com/next | 2026-04-27 | GCP |
| H6 | **HubSpot Inbound** | https://www.inbound.com/ | 2026-04-27 | Marketing / sales |
| H7 | **RSA Conference** | https://www.rsaconference.com/ | 2026-04-27 | Cybersecurity |
| H8 | **Black Hat / DEF CON** | https://www.blackhat.com/ | 2026-04-27 | Cyber research |
| H9 | **Web Summit** | https://websummit.com/ | 2026-04-27 | Tech (broad) |
| H10 | **TechCrunch Disrupt** | https://techcrunch.com/events/ | 2026-04-27 | Startup / venture |
| H11 | **Money 20/20** | https://www.money2020.com/ | 2026-04-27 | Fintech |
| H12 | **HIMSS** | https://www.himss.org/ | 2026-04-27 | Healthcare IT |
| H13 | **NRF (National Retail Federation)** | https://nrf.com/ | 2026-04-27 | Retail |
| H14 | **Reuters NEXT** | https://events.reutersevents.com/next/hub | 2026-08-07 | Business leaders |

### Category I: Shutdown-risk / sustainability flags

These sources have known sustainability concerns. Annual review: confirm still operating; if shutdown, update skill citations to backup sources.

| # | Source | Primary URL | Status | Last verified | Action if shutdown |
|---|---|---|---|---|---|
| I1 | **SaaS Benchmarks Report — High Alpha (formerly OpenView)** | https://www.highalpha.com/saas-benchmarks | OpenView **WOUND DOWN 2023**; report continued by High Alpha since 2024 | 2026-08-07 | Cite current editions as "High Alpha SaaS Benchmarks"; pre-2024 editions as "OpenView (legacy)" |
| I2 | **MonkeyLearn** | (defunct) | **DEFUNCT** | 2026-04-27 | Already noted — replaced with Hugging Face ABSA models |
| I3 | **Lanyrd** | https://web.archive.org/ (archived) | **CLOSED 2014** | 2026-04-27 | Already noted — pointed to archive.org |
| I4 | **Burrelles** | https://burrelles.com/ | Operating but legacy methodology | 2026-04-27 | Replace with Cision/PRovoke if shutdown |
| I5 | **DomainTools whois history** | https://whois.domaintools.com/ | Paid model — free tier shrinking | 2026-04-27 | Backup: ICANN whois + Wayback |
| I6 | **SecurityTrails** | https://securitytrails.com/ | Free tier capped at 50/mo | 2026-04-27 | Backup: crt.sh + dig manual |

### Category J: Specific articles cited (check periodically — articles can be deleted/moved)

| # | Source | Primary URL | Last verified | Notes |
|---|---|---|---|---|
| J1 | **Pento "A Year of MCP" (2025 review)** | https://www.pento.ai/blog/a-year-of-mcp-2025-review | 2026-04-27 | Specific article — verify still accessible; backup via Wayback |
| J2 | **DNI ICD index (master list)** | https://www.dni.gov/index.php/what-we-do/ic-policies-reports/intelligence-community-directives | 2026-04-27 | Hosts ICD 203 + ICD 206 PDFs |

### Category K: GitHub / OSS metadata APIs (continuous, stable)

| # | Source | Primary URL | Last verified | Notes |
|---|---|---|---|---|
| K1 | **GitHub REST API** | https://api.github.com/ | 2026-04-27 | repos, contributors, stargazers, etc. |
| K2 | **pypistats.org** | https://pypistats.org/ | 2026-04-27 | PyPI download stats |
| K3 | **libraries.io** | https://libraries.io/ | 2026-04-27 | OSS dependency tracking |

---

## §4 — Maintenance protocol

### Monthly (automated via `/schedule`)
1. Run `/research-entity --validate-skill-sources` — produces URL-validation + last-verified report
2. For any URL returning HTTP 404 / 5xx persistent: open issue / fix
3. For any source >12 months last-verified: schedule manual review

### Quarterly (manual)
1. Review **Category B (Annual benchmarks)** — has a new Bessemer / KeyBanc / OpenView edition published?
2. Review **Category E (Regulatory)** — has EU AI Act enforcement evolved? New state privacy laws?
3. Review **Category I (Shutdown-risk)** — confirm sources still operating
4. Update `last-verified` date for all rows touched

### Annually (deep refresh)
1. **Foundational frameworks check** — has ICD 203 been updated? NIST CSF revision? AICPA new attestation standard?
2. **URL migration sweep** — government sites reorganize; AICPA migrated to aicpa-cima.com; USPTO retired TESS
3. **New sources added during the year** — incorporate any new standards, frameworks, or registries cited
4. **Bump skill version** if methodology shifts materially

### When a source migrates or shuts down
1. Update **this file** first (the registry)
2. Run grep across skill files for the old URL — replace with new URL or backup
3. Add note in `Notes` column documenting the migration
4. Update relevant `lessons.md` entry if the migration teaches a generalizable pattern

---

## §5 — When to load this file

- **Always** during `--validate-skill-sources` mode
- **Manual reference** when a maintainer is updating skill citations
- **Onboarding** when a new maintainer needs to understand source dependencies

---

## §6 — Anti-patterns

- ❌ Search-and-replacing URLs across skill files without updating this registry — creates drift
- ❌ Updating skill citations to a new source without adding row here — loses the maintenance trail
- ❌ Skipping `last-verified` update when validating — defeats the registry's purpose
- ❌ Adding sources to skill files without registering them here — they fall out of the maintenance scope
