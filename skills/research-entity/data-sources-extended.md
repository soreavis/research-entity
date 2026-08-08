# Extended Data Sources

Loaded by the `research-entity` skill at Step 2 (parallel source gathering) when the entity matches the relevant trigger conditions, OR explicitly via `--data-sources=<list>`. These sources are NOT in the default Step 2 search wave because they require domain-specific knowledge to query well — but they substantially raise dossier quality when applicable.

Six source families:

1. **SEC EDGAR** — for any US-incorporated entity (private companies often file too: Form D, S-1, etc.)
2. **Wayback Machine** — for site evolution, deleted pages, claim recovery
3. **GitHub** — for devtools, OSS-distributed products, technical credibility
4. **LinkedIn hiring velocity** — for growth signal, layoff signal, geographic expansion
5. **USPTO + EPO** — for patents and trademarks (deeptech, hardware, regulated)
6. **PACER + CourtListener** — for federal court records (lawsuits, IP disputes, regulatory)

## 1. SEC EDGAR

**When to query:** US-incorporated entity (Delaware C-Corp common). Public companies — always. Private companies — if any of:
- Raised institutional capital (Form D required for most rounds)
- Recently filed S-1 (pre-IPO)
- Acquired a public company (8-K)
- Filed 10-K / 10-Q (post-IPO or via acquisition)

**Free public access:** https://www.sec.gov/cgi-bin/browse-edgar

**Key search:**
```
https://efts.sec.gov/LATEST/search-index?q=%22<entity>%22&dateRange=custom&startdt=2020-01-01&enddt=<today>
```

**Forms to look for:**

| Form | What it reveals |
|---|---|
| **10-K** | Annual report — Risk Factors, segment revenue, customer concentration, exec comp, liquidity |
| **10-Q** | Quarterly report — current-quarter performance, guidance changes |
| **8-K** | Material event — acquisitions, exec changes, restructuring, breach disclosures |
| **DEF 14A** | Proxy statement — exec comp, board composition, shareholder proposals |
| **S-1 / S-3** | IPO / secondary offering — full company profile, risk factors, historical financials |
| **Form D** | Private placement filing — round size, investor count, principals |
| **D/A** | Amendment to Form D — round increase or modification |
| **13D / 13G** | Beneficial ownership > 5% — strategic investor positioning |
| **SC 13E3** | Going-private transaction — PE buyout terms |

**Specific extraction rules:**

- Risk Factors section in 10-K is gold — verbatim quotes for §16 Risks (especially competitive risks, regulatory exposure, customer concentration, supplier dependency)
- Segment reporting in 10-K — split revenue by geography, product line, customer tier
- Management Discussion (MD&A) — narrative explanation of YoY change
- Auditor's report — note any going-concern language (RED FLAG)
- Litigation section — both currently-pending and historical

**Sample query:**
```bash
# Get most recent 10-K filing URL
curl -s "https://efts.sec.gov/LATEST/search-index?q=%22<entity>%22&forms=10-K" | jq '.hits.hits[0]'
```

For non-US entities: equivalent registers per country — load `registers.md`.

## 2. Wayback Machine

**When to query:** Always (1 cheap query). Specifically valuable when:
- Site recently redesigned (compare claims pre/post)
- Pricing page changed (track price evolution)
- Customer logos appeared/disappeared (churn signal)
- Trust page certifications changed (compliance regression)
- Founder bio changed (narrative pivot)

**Free public access:** https://web.archive.org/web/*/

**Key queries:**

```
# All snapshots of pricing page
https://web.archive.org/web/*/https://<entity>.com/pricing

# Specific date snapshot
https://web.archive.org/web/2024*/https://<entity>.com/customers

# Compare two snapshots
https://web.archive.org/web/2025*/https://<entity>.com/pricing
https://web.archive.org/web/2026*/https://<entity>.com/pricing
```

**Specific patterns to detect:**

- **Customer logo removal** — logo present in 2024 snapshot, absent in 2026 → likely churned. Surface in §16 Risks.
- **Pricing tier removal** — free tier present in 2024, gone in 2026 → freemium → freemium-paid transition (signal of GTM maturation)
- **Trust badge removal** — SOC 2 badge present in 2024 snapshot, absent in 2026 → certification expired or lost
- **Team page shrinkage** — exec team page lists 8 people in 2024, 5 in 2026 → 3 exec departures (cross-check with LinkedIn)
- **Founder bio change** — Wikipedia-style fact change ("founded 2011" → "founded 2009") suggests narrative revision

**Sample CLI**:
```bash
# Wayback CDX API — list all snapshots
curl "https://web.archive.org/cdx/search/cdx?url=<entity>.com/pricing&output=json&limit=20"
```

## 3. GitHub

**When to query:** Devtools, AI tools, OSS-distributed products, dev-focused SaaS. Skip for traditional B2B SaaS, consumer apps, fintech with closed source.

**Free public access:** https://github.com/<entity-slug>

**Metrics to extract:**

| Signal | What it indicates |
|---|---|
| **Star count** | Developer interest; > 10K = significant; trend matters more than absolute |
| **Star velocity** (stars/month) | Hype curve; >500/mo sustained = breakout |
| **Contributor count** | Community health; >50 = vibrant; <10 = inner-source-only |
| **Last commit date** | Project health; >6 months idle = at-risk |
| **Issue resolution time** | Maintainer responsiveness; median <14 days = healthy |
| **Dependents graph size** | Real-world usage; >1K dependents = ecosystem-significant |
| **Contributors over time** | Org health; declining contributor count = concerning |
| **Sponsors / Funding** | OSS sustainability model |

**API queries (no auth needed for public repos):**
```bash
# Repo metadata
curl https://api.github.com/repos/<owner>/<repo>

# Star history
curl "https://api.github.com/repos/<owner>/<repo>/stargazers?per_page=100"

# Contributors
curl https://api.github.com/repos/<owner>/<repo>/contributors

# Dependents (HTML scrape — no API endpoint)
# https://github.com/<owner>/<repo>/network/dependents
```

**Star-history.com:** https://star-history.com/#<owner>/<repo>&Date — for visual chart

**Tools to detect tech stack from GitHub:**
- `https://github.com/<owner>/<repo>/blob/main/package.json` — Node deps
- `https://github.com/<owner>/<repo>/blob/main/requirements.txt` — Python deps
- `https://github.com/<owner>/<repo>/blob/main/Cargo.toml` — Rust deps
- `https://github.com/<owner>/<repo>/network/dependencies` — full SBOM

## 4. LinkedIn hiring velocity

**When to query:** Always (free signal of growth, contraction, geographic expansion). LinkedIn Insights requires Premium login — fall back to Google site-scoped search.

**Public-friendly access patterns:**

```
# Site-scoped Google: count "open roles" mentions
"<entity>" "we're hiring" site:linkedin.com

# LinkedIn job count (signed-in only):
https://www.linkedin.com/jobs/search/?keywords=&location=&distance=25&f_C=<company-id>

# Indeed (no auth):
https://www.indeed.com/cmp/<entity>/jobs

# AngelList / Wellfound:
https://wellfound.com/company/<entity>/jobs

# YC Work at a Startup (if YC alum):
https://www.workatastartup.com/companies/<entity>
```

**Metrics:**

| Signal | Interpretation |
|---|---|
| **Open roles count, current** | Snapshot of hiring intent |
| **Open roles count, 3-month trend** | Hiring acceleration / deceleration |
| **Geographic distribution** | Expansion signal (e.g., 30% of roles in EU = EU push) |
| **Function distribution** | Investment area (60% of roles in Sales = GTM scale-up) |
| **Senior role concentration** | Org build-out (5+ Director / VP roles open = leadership thinning) |
| **Engineering vs. GTM ratio** | Stage signal (early = engineering-heavy; late = GTM-heavy) |

**Layoff signal:** If open roles dropped > 50% over 6 months without a corresponding hiring announcement = stealth headcount cut. Cross-check with `risk-scan.md` Pattern 1.

## 5. USPTO + EPO patents and trademarks

**When to query:** Deeptech, hardware, AI/ML model companies, biotech, fintech with proprietary algorithms, anyone making "patented" or "patent-pending" claims.

**Free public access:**
- USPTO patent search: https://ppubs.uspto.gov/pubwebapp/external.html?db=USPAT
- USPTO assignee search: https://ppubs.uspto.gov/pubwebapp/
- USPTO trademark search (TESS): https://tmsearch.uspto.gov/
- EPO Espacenet (worldwide patents): https://worldwide.espacenet.com/
- Google Patents (cross-jurisdiction): https://patents.google.com/?assignee=<entity>

**Search syntax:**
```
# Google Patents by assignee
https://patents.google.com/?assignee=%22<entity>%22

# USPTO assignee search
https://assignmentcenter.uspto.gov/search/patent<entity>

# Trademarks (active vs. abandoned)
https://tmsearch.uspto.gov/<entity>
```

**Metrics:**

| Signal | Interpretation |
|---|---|
| **Granted patents (count)** | Defensive moat (especially in hardware) |
| **Pending applications (count)** | Innovation pipeline |
| **Patent classification (CPC codes)** | Technology area focus |
| **Citation count (forward)** | Patent quality — patents cited by others = valuable |
| **Patent age distribution** | Old patents = legacy moat; new patents = active innovation |
| **Trademark portfolio** | Brand investment; abandoned trademarks = product retirement |

**Red flags:**
- Claim "patented technology" but no granted patents found = marketing fluff
- All patents are continuation-in-part = thin moat
- Recent trademark abandonments = product line discontinued

## 6. PACER + CourtListener (US federal courts)

**When to query:** Always (cheap), especially for fintech, healthcare, AI companies (regulatory + IP exposure).

**Free public access:**
- CourtListener (recap-scraped PACER): https://www.courtlistener.com/?type=r&q=<entity>
- PACER (paid for full docs, free index): https://pacer.uscourts.gov/

**Search:**
```
https://www.courtlistener.com/?type=r&q=%22<entity>%22&order_by=score+desc
```

**Specific patterns:**

| Case type | Severity for §16 |
|---|---|
| Trademark dispute (lost) | Medium — may force rebrand |
| Patent infringement (pending against entity) | High — financial liability + product injunction risk |
| Class action (consumer protection / antitrust) | High — financial liability + reputational damage |
| Employment lawsuit (discrimination / harassment) | Medium — reputational damage + payout |
| SEC enforcement (active) | Critical — existential risk |
| Bankruptcy (Ch 11) | Critical — vendor extinction risk |
| Contract dispute (between $5K vendors) | Low — noise |

**For state court records:** state-by-state, no unified system. Most populous states with usable systems:
- CA: https://www.courts.ca.gov/courts.htm (case-search varies by county)
- NY: https://iapps.courts.state.ny.us/webcivil/ecourtsMain
- TX: https://search.txcourts.gov/

## How to use these in the dossier

When applicable findings exist, integrate as:

- **SEC EDGAR findings** → §2 Company Fundamentals (filings table) + §16 Risks (verbatim Risk Factors quotes)
- **Wayback findings** → §0 Watchlist (deltas detected) + §16 Risks (lost SOC 2 badge, customer churn)
- **GitHub findings** → §6 Tech Architecture + §11 Community + §16 Risks (project decline)
- **LinkedIn hiring** → §3 Senior Leadership (recent senior hires) + §16 Risks (hiring slowdown)
- **Patents/trademarks** → §6 Tech Architecture (IP portfolio) + §10 Competition (patent moat)
- **Court records** → §16 Risks (litigation table) + §0 Heat Map (legal-risk row)

## Activation flag

```
--data-sources=sec,wayback,github,linkedin,uspto,pacer
```

Or auto-activated by:
- US-incorporated → SEC EDGAR
- Devtool / OSS → GitHub
- Always → Wayback + LinkedIn + PACER (cheap to query)
- Deeptech / hardware / regulated → USPTO

## When to load this file

- `--data-sources=` flag set
- Auto-activation conditions met
- Stage is `series-c+` / `pe` / `public` (mature companies have more public data)
- User asks about IP / patents / hiring / outage / SEC filings
