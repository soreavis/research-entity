# Press / Earned-Media + Conference + Trust-Center Auditor Verification

Loaded by the `research-entity` skill when the entity's media coverage is part of the dossier (always, but with deeper analysis for `--depth=deep`). Three layered analyses: **(1) earned-vs-paid press distinction** (PRovoke + AMEC methodology), **(2) conference / event presence** (marketing-budget proxy), **(3) trust-center auditor verification** (audit-rigor verification — Drata/Vanta-hosted vs. self-published, named auditor, audit period).

---

## §1 — Earned vs Paid press

### Why this matters

PR coverage in a dossier is often listed as flat "press timeline" entries. But there's a 10× signal difference between:
- **Paid press** (PR Newswire / GlobeNewswire / BusinessWire / EIN Presswire wire distribution; vendor pays $300-3,000 per release for distribution)
- **Earned press** (TechCrunch / Reuters / Bloomberg / FT / WSJ / The Information journalist reporting on their own initiative)

A dossier that conflates the two overstates the entity's actual market traction.

### Verified methodology citations

- **PRovoke Media Earned Media Index** → [provokemedia.com](https://www.provokemedia.com/) — annual earned-media measurement methodology
- **AMEC Barcelona Principles 3.0** (2020) → [amecorg.com/barcelona-principles](https://amecorg.com/barcelona-principles/) — industry standard for measuring earned vs paid PR
- **PR Council** professional standards → [prcouncil.net](https://prcouncil.net/)
- **The Drum / Holmes Report (PRovoke)** annual analysis distinguishing earned from paid
- **Burrelles** historical methodology (legacy) → [burrelles.com](https://burrelles.com/)
- **Cision** methodology for earned-media measurement → [cision.com](https://www.cision.com/)

### Distinguishing earned from paid

| Signal | Indicates | Verify by |
|---|---|---|
| **Named byline (real journalist)** | Earned | Author name + history of writing for outlet |
| **"Press release" or "Sponsored Content" tag** | Paid | URL pattern (e.g., `prnewswire.com/news-releases/` or `businesswire.com/news/home/`) |
| **Wire-distribution outlets** (PR Newswire / GlobeNewswire / BusinessWire / EIN / Newsfile / Cision PR / Markets Insider) | Paid | Outlet domain |
| **Tier-1 named outlet** (Reuters / Bloomberg / WSJ / FT / NYT / Forbes by-staff / TechCrunch by-staff) | Earned | Outlet's masthead + author history |
| **Sponsored content disclaimer** (e.g., "in partnership with X" / "promoted by Y") | Paid (native ad) | Disclosure label |
| **Republished content** (one outlet → others via syndication) | Counts as 1 earned | Track-back to original source |

### Press-tier classification

| Tier | Examples | Signal value |
|---|---|---|
| **Tier 1 — Earned, top journalist outlets** | Bloomberg, Reuters, WSJ, FT, NYT, The Information, TechCrunch (named-staff bylines) | 10× — high signal of real traction |
| **Tier 2 — Earned, trade press** | CRN, Forbes (staff bylines), CIO, Computerworld, ZDNet, VentureBeat | 5× — meaningful in segment |
| **Tier 3 — Forbes / Inc. contributor network** | Forbes contributor pieces (NOT staff), Inc. articles by guest authors | 1× — often pay-to-publish-adjacent |
| **Tier 4 — Wire / paid distribution** | PR Newswire, GlobeNewswire, BusinessWire, Newsfile, EIN Presswire | 0.5× — informational only, pure paid |
| **Tier 5 — Self-publishing** | Medium posts by founders, LinkedIn articles, company blog | 0.1× — primary-source-of-claims, not coverage |

### Press-tier table (added to §15)

```markdown
### 15.X Earned vs Paid Press Distribution (last 24 months)

| Outlet | Article | Date | Tier | Earned/Paid | URL |
|---|---|---|---|---|---|
| TechCrunch | "Acme raises $30M Series B" (Smith) | 2025-08-15 | T1 | **Earned** | [link] |
| GlobeNewswire | "Acme Launches AI Platform" | 2025-09-02 | T4 | Paid | [link] |
| Forbes (contributor) | "Why Acme is the Future" | 2025-10-10 | T3 | Earned (low-value) | [link] |
| ... | ... | ... | ... | ... | ... |

**Earned coverage rate (T1+T2 / total):** X / Y articles = Z%

**Verdict:** Real / Mixed / PR-driven (entity heavily reliant on wire distribution to manufacture coverage)
```

### Anti-patterns

- ❌ **Listing wire-distributed releases without flagging as paid** — overstates traction.
- ❌ **Counting Forbes contributor articles as Forbes coverage** — Forbes contributor network is pay-to-publish-adjacent.
- ❌ **Treating syndicated republishes as separate signals** — count once, note syndication breadth as secondary.

---

## §2 — Conference / event presence

### Why this matters

Conference speaking + sponsoring is a real marketing-budget signal:
- **Speaking slot at top conference** (SaaStr Annual, Dreamforce, RSA, Black Hat, AWS re:Invent, etc.) = significant industry visibility
- **Sponsorship tier** at conferences signals marketing spend (Diamond > Platinum > Gold > Silver > Bronze)
- **Conference presence trajectory** (more conferences = more aggressive GTM; fewer = budget-tightening)

### Verified methodology

- **EventMB / Skift Meetings** — event-industry benchmarks → [skift.com/meetings](https://skift.com/meetings/)
- **MPI (Meeting Professionals International)** — industry data → [mpi.org](https://www.mpi.org/)
- **IBTM World** annual reports
- **PCMA (Professional Convention Management Association)** — [pcma.org](https://www.pcma.org/)

### Public sources for conference presence

| Source | What it provides | URL pattern |
|---|---|---|
| **Conference sponsor/speaker pages** | Direct list of sponsors + speakers | conference's own website |
| **Lanyrd (legacy archive)** | Historical speaker data | [archive.org](https://web.archive.org/) |
| **Meetup.com (now Bending Spoons)** | Local meetup speakers | [meetup.com](https://www.meetup.com/) |
| **YouTube conference channels** | Recorded talks | [youtube.com](https://youtube.com/) (search by conference name) |
| **Twitter/X conference hashtags** | Real-time presence | search `#<event-hashtag>` |
| **LinkedIn event pages** | Public attendees + speakers | [linkedin.com/events/](https://linkedin.com/events/) |
| **Eventbrite** | Listings + organizer pages | [eventbrite.com](https://www.eventbrite.com/) |

### Major B2B SaaS conferences (verified with current websites)

| Conference | Vertical | URL |
|---|---|---|
| **Dreamforce** | Salesforce ecosystem | [salesforce.com/dreamforce](https://www.salesforce.com/dreamforce/) |
| **SaaStr Annual** | SaaS / GTM | [saastr.com](https://www.saastr.com/) |
| **AWS re:Invent** | Cloud / infrastructure | [reinvent.awsevents.com](https://reinvent.awsevents.com/) |
| **Microsoft Build / Ignite** | Microsoft ecosystem | [build.microsoft.com](https://build.microsoft.com/) / [ignite.microsoft.com](https://ignite.microsoft.com/) |
| **Google Cloud Next** | GCP | [cloud.withgoogle.com/next](https://cloud.withgoogle.com/next) |
| **HubSpot Inbound** | Marketing / sales | [inbound.com](https://www.inbound.com/) |
| **RSA Conference** | Cybersecurity | [rsaconference.com](https://www.rsaconference.com/) |
| **Black Hat / DEF CON** | Cybersecurity research | [blackhat.com](https://www.blackhat.com/) / [defcon.org](https://defcon.org/) |
| **Web Summit** | Tech (broad) | [websummit.com](https://websummit.com/) |
| **TechCrunch Disrupt** | Startup / venture | [techcrunch.com/events](https://techcrunch.com/events/) |
| **Money 20/20** | Fintech | [money2020.com](https://www.money2020.com/) |
| **HIMSS** | Healthcare IT | [himss.org](https://www.himss.org/) |
| **NRF (National Retail Federation)** | Retail | [nrf.com](https://nrf.com/) |
| **Reuters NEXT** | Business leaders | [reutersevents.com/events/next](https://events.reutersevents.com/next/hub) |

### Conference-presence table (added to §15)

```markdown
### 15.X Conference Presence (last 24 months)

| Event | Year | Role | Speaker(s) | Sponsorship tier | URL |
|---|---|---|---|---|---|
| SaaStr Annual | 2025 | Sponsor (Gold) | <Founder> "Scaling beyond $10M ARR" | Gold ($25-50K) | [link] |
| Dreamforce | 2025 | Sponsor (Silver) | none speaking | Silver ($15-30K) | [link] |
| RSA Conference | 2025 | Speaker only | <CISO> | none | [link] |
| ... | ... | ... | ... | ... | ... |

**Trajectory:** [growing presence / stable / declining]
**Estimated annual conference budget:** $X-Y based on observed sponsorships at standard tier rates
```

### Anti-patterns

- ❌ **Listing every meetup talk as "conference presence"** — meetups (50-200 attendees) are different signal class than RSA Conference (40,000+).
- ❌ **Estimating sponsorship $$ without disclosing rate source** — sponsorship rates vary widely; cite the conference's own published rate card.

---

## §3 — Trust-Center auditor verification

### Why this matters

Companies routinely list "SOC 2 Type II compliant" on Trust Centers without disclosing:
- **Who audited?** (Big 4 = high signal; lower-tier audit firm = weaker)
- **What audit period?** (continuous = high signal; one-time/lapsed = weaker)
- **What scope?** (entire product surface = high signal; "select systems" = weaker)
- **What service criteria?** (Security only? Or Security + Availability + Processing Integrity + Confidentiality + Privacy?)

### Verified methodology

- **AICPA SOC for Service Organizations** — methodology + reporting standards → [aicpa.org/topic/audit-assurance/audit-and-assurance-greater-than-soc-2](https://www.aicpa.org/topic/audit-assurance/audit-and-assurance-greater-than-soc-2)
- **SOC 2 audit firm lookup**: AICPA Peer Review program lookup → [peerreview.aicpa.org](https://peerreview.aicpa.org/) (validates audit firm credentials)
- **ISO certification body lookup**: IAF (International Accreditation Forum) → [iaf.nu](https://iaf.nu/) — validates accredited certification bodies

### Trust Center hosting platforms (signal differentiator)

| Platform | Signal | URL |
|---|---|---|
| **Drata Trust Center** | High-quality compliance automation; audits regularly | platform-hosted Trust Center URL contains "drata.com" or vendor's subdomain styled by Drata |
| **Vanta Trust Center** | Similar — comprehensive automation | URL contains "vanta.com" or hosted on Vanta |
| **Secureframe Trust Center** | Comprehensive | hosted on Secureframe |
| **SafeBase** | Customer-facing security review automation | URL contains "safebase.io" |
| **Tugboat Logic / OneTrust Compliance Cloud** | Big-platform Trust Center | hosted on OneTrust |
| **Self-published HTML page** | ⚠️ lower signal — self-attestation, no audit-trail visibility | vendor's own /security or /trust path with static content |

### Verification protocol

For any compliance certification claimed:

1. **Locate the audit report** (or summary):
   - Drata/Vanta/Secureframe: typically downloadable PDF after click-through agreement
   - Self-published: rarely have public PDF; ask via DPA path

2. **Verify the auditor**:
   - Big 4 (Deloitte, PwC, EY, KPMG) → highest signal
   - Top-50 audit firms (Schellman, A-LIGN, BDO, Grant Thornton, RSM, Coalfire) → strong signal
   - Smaller firms → verify via AICPA Peer Review lookup

3. **Verify the audit period**:
   - SOC 2 Type II = period of audit (typically 6-12 months); verify report dates
   - SOC 2 Type I = point-in-time only — much weaker signal
   - ISO 27001 = certification valid 3 years with annual surveillance audits

4. **Verify the scope**:
   - Should include ALL customer-facing products
   - "Carve-out" clauses (e.g., "excluding mobile") are red flags

### Trust-center verification subsection (added to §14 or §16.X)

```markdown
### 14.X Compliance Audit-Rigor Verification

| Certification | Vendor claims | Audit firm | Audit type | Audit period | Scope | Verification |
|---|---|---|---|---|---|---|
| SOC 2 Type II | ✅ on Trust Center | Schellman | Type II | 2024-Q4 to 2025-Q3 | Production + corp IT | ✅ Hosted on Drata; PDF downloadable |
| ISO 27001:2022 | ✅ claimed | TÜV SÜD | Cert | 2024-2027 (3yr) | Full product | ✅ Verified via IAF accreditation lookup |
| HIPAA | ✅ claimed | (no audit; self-attestation) | — | — | — | ⚠️ HIPAA is not a certification — only self-attestation possible |
| FedRAMP | ❌ not claimed | — | — | — | — | — |
```

### Anti-patterns

- ❌ **Treating "SOC 2 compliant" badge as equivalent to "SOC 2 Type II audited by Big 4"** — vast difference.
- ❌ **Trusting Trust Center claims without auditor name** — auditor identity changes the signal weight.
- ❌ **Skipping IAF-accreditation check for ISO claims** — there are unaccredited ISO "certifiers" issuing meaningless certificates.

---

## §4 — Workflow integration

**Step 2 — source gathering**: when fetching `/press`, `/about`, `/customers`, also fetch `/security`, `/trust`, `/compliance`, `/legal`. Run earned-vs-paid classification on press URLs.

**Step 4 — draft**: write the three subsections in §15 (press tier table + conference presence) and §14 (trust-center auditor verification).

**Step 5 — validate**: for each compliance certification claimed, verify auditor + period + scope before publishing.

---

## §5 — Anti-patterns (cross-cutting)

- ❌ **Aggregating press as "we have N press hits" without tier weighting** — misleads on real coverage quality.
- ❌ **Listing every conference appearance equally** — speaker at SaaStr ≠ panelist at local meetup.
- ❌ **Reporting "SOC 2 compliant" without auditor verification** — biggest ongoing skill anti-pattern.

---

## §6 — When to load this file

- Always for `--type=due-diligence|investment`
- Always for `--depth=deep`
- When user asks "is this real coverage or PR?"
- When user asks "is the SOC 2 claim verified?"

---

## §7 — Related

- `lessons.md` — lessons on press / Trust Center claims
- `data-sources-extended.md` — broader OSINT
- `frameworks.md` — PESTEL has overlap on regulatory + competitive landscape
