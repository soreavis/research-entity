# OSINT Public-Source Extensions

Loaded when the dossier needs additional verification depth beyond the core 23 sections. This file consolidates five OSINT verification techniques, all using free public sources: **(1) job-posting velocity** (hiring pace + tech stack); **(2) MITRE ATT&CK / KEV / CVE** (security entities); **(3) DNS / passive DNS** (infrastructure / tech archaeology); **(4) trademark portfolio** (USPTO / EUIPO — product roadmap signals); **(5) founder LinkedIn velocity** (engagement signals).

---

## §1 — Job-posting velocity analysis

### Why this matters

A vendor that claims "we're growing 200% YoY" can be cross-checked against actual hiring pace. Public job boards expose the entity's hiring velocity, role distribution, tech stack, and location strategy — all without inside access.

### Verified methodology

- **Battery Ventures** *State of the OpenCloud* — publishes hiring-velocity benchmarks across SaaS verticals → [battery.com/insights](https://www.battery.com/blog/category/research/)
- **Datapeople** hiring-pace research → public reports
- **Gem** recruiting benchmarks → public

### Free public sources for job postings

| Source | Coverage | URL pattern |
|---|---|---|
| **Greenhouse Job Boards** | Companies using Greenhouse ATS (broad SaaS coverage) | [boards.greenhouse.io/<company-slug>](https://boards.greenhouse.io/) |
| **Lever** | Companies using Lever ATS | [jobs.lever.co/<company-slug>](https://jobs.lever.co/) |
| **Ashby** | Companies using Ashby ATS (modern startup standard) | [jobs.ashbyhq.com/<company-slug>](https://jobs.ashbyhq.com/) |
| **Workable** | Companies using Workable | [apply.workable.com/<company-slug>](https://apply.workable.com/) |
| **LinkedIn Jobs** | Largest aggregator | [linkedin.com/jobs/<company>-jobs](https://linkedin.com/jobs/) |
| **Indeed** | Largest US aggregator | [indeed.com/cmp/<company-slug>/jobs](https://indeed.com/) |
| **AngelList / Wellfound** | Startup-focused | [wellfound.com/company/<company-slug>](https://wellfound.com/) |
| **Built In** | Startup-focused | [builtin.com/company/<company-slug>](https://builtin.com/) |

### Velocity signals to extract

| Signal | What it means | Source |
|---|---|---|
| Total open positions | Total hiring breadth | Direct count from board |
| Engineering : sales ratio | Product- vs sales-led | Categorize roles |
| New roles vs renewals | Growth vs replacement | Job age tag |
| Geographic distribution | Remote / hybrid / location-concentrated | Location field |
| Tech-stack-in-JD | Required experience reveals stack | Required-skills section |
| Manager-level vs IC ratio | Org maturity (pyramid shape) | Title parsing |
| Hiring pace YoY | Compare to prior 12 months via Wayback | Wayback historical snapshots |

### Anti-patterns

- ❌ **Assuming "X open roles = growth"** — could be replacement hiring (high churn).
- ❌ **Treating recruiter-posted LinkedIn jobs as definitive** — recruiters post on speculation; ATS-direct postings are more reliable.
- ❌ **Skipping Wayback comparison** — current hiring pace alone misses the trend.

---

## §2 — MITRE ATT&CK / CISA KEV / NVD CVE for security entities

### Why this matters

For cybersecurity / SaaS-with-security-claims vendors, MITRE ATT&CK is the industry-standard adversary-behavior framework. Vendors claiming "we cover 80% of MITRE ATT&CK techniques" need that mapped against the actual ATT&CK matrix. CISA's Known Exploited Vulnerabilities (KEV) catalog and NVD's CVE database provide the verified vulnerability surface.

### Verified methodology + sources

| Source | Free / public | URL |
|---|---|---|
| **MITRE ATT&CK Framework** | ✅ free, public | [attack.mitre.org](https://attack.mitre.org/) |
| **MITRE D3FEND** (defensive techniques) | ✅ free, public | [d3fend.mitre.org](https://d3fend.mitre.org/) |
| **CISA Known Exploited Vulnerabilities (KEV)** | ✅ free, public, CSV/JSON download | [cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) |
| **NVD CVE Database** | ✅ free, public, REST API | [nvd.nist.gov](https://nvd.nist.gov/) |
| **CVE.org (MITRE)** | ✅ free, public | [cve.org](https://www.cve.org/) |
| **EPSS (Exploit Prediction Scoring System)** | ✅ free, public | [first.org/epss](https://www.first.org/epss/) |
| **ENISA Threat Landscape** | ✅ free, public, annual report | [enisa.europa.eu](https://www.enisa.europa.eu/) |
| **NCSC UK guidance** | ✅ free, public | [ncsc.gov.uk](https://www.ncsc.gov.uk/) |

### Apply when

- `--vertical=security` OR
- entity claims a security feature (DLP, SIEM, SOAR, EDR, XDR, IAM, ZTNA, WAF, CASB, CSPM, ASPM, vuln management) OR
- entity has had a public breach (CVE assigned)

### Verification subsection (added to §14 Security & Trust)

```markdown
### 14.X MITRE ATT&CK + CVE Coverage Audit

#### ATT&CK technique coverage (vendor-claimed vs. evidence)

| Technique ID | Technique name | Vendor claim | Evidence | Verdict |
|---|---|---|---|---|
| T1078 | Valid Accounts | ✅ "covered" | datasheet ref | confirmed |
| T1486 | Data Encrypted for Impact | ✅ "ransomware coverage" | feature listing | confirmed |
| T1190 | Exploit Public-Facing Application | ❌ | (not mentioned) | gap |
| ... | ... | ... | ... | ... |

**Coverage rate:** X / 188 enterprise techniques (per current MITRE matrix). [vendor-claim: Y%; verified: X%]

#### CVE history (entity's own software)

| CVE | Year | CVSS | KEV-listed | Patch issued | Note |
|---|---|---|---|---|---|
| CVE-YYYY-NNNNN | YYYY | 9.8 | ✅ | YYYY-MM-DD | Critical RCE |
| ... | ... | ... | ... | ... | ... |
```

### Anti-patterns

- ❌ **Claiming MITRE ATT&CK coverage % without method disclosure** — the MITRE matrix is 188+ enterprise techniques; coverage % only meaningful with explicit denominator.
- ❌ **Citing "vendor claims SOC 2" as security verification** — SOC 2 is operational; ATT&CK is technical. Different question.
- ❌ **Treating zero CVEs as zero risk** — small / private companies often have unreported security debt; flag with `coverage-gap` rather than declare clean.

---

## §3 — DNS / passive DNS / SSL-cert transparency

### Why this matters

Public DNS records and SSL certificate transparency logs reveal: which cloud provider the entity uses (Cloudflare CDN, AWS, Azure, GCP), which SaaS products they integrate (subdomains often expose vendors — `support.<entity>.com` → Zendesk; `status.<entity>.com` → Statuspage), and the historical infrastructure trajectory.

### Verified free public sources

| Source | What it provides | URL |
|---|---|---|
| **crt.sh (Certificate Transparency search)** | All public SSL certs issued for `*.<domain>` — reveals all subdomains historically certified | [crt.sh/?q=%25.<domain>](https://crt.sh/) |
| **DNSdumpster** | DNS map + subdomains + MX/SPF | [dnsdumpster.com](https://dnsdumpster.com/) |
| **SecurityTrails** (free tier 50/mo) | Subdomain history + DNS history | [securitytrails.com](https://securitytrails.com/) |
| **DomainTools whois history** (paid for full) | Whois changes over time | [whois.domaintools.com](https://whois.domaintools.com/) |
| **ICANN whois lookup** | Current whois | [lookup.icann.org](https://lookup.icann.org/) |
| **`dig`** (CLI tool) | All DNS records | `dig <domain> ANY +short` |
| **Wappalyzer** (free tier) | Tech stack from headers + JS | [wappalyzer.com](https://www.wappalyzer.com/) |
| **BuiltWith** (free tier) | Tech stack | [builtwith.com](https://builtwith.com/) |

### What to extract

| DNS record | Signal |
|---|---|
| **MX records** | Email vendor — Google Workspace (`aspmx.l.google.com`) vs O365 (`<tenant>.mail.protection.outlook.com`) vs Zoho vs Fastmail |
| **SPF / DKIM / DMARC** | Reveals SaaS vendors authorized to send mail (`include:_spf.salesforce.com` = uses Salesforce; `include:mailgun.org` = uses Mailgun; etc.) |
| **NS records** | DNS provider — Cloudflare (`*.ns.cloudflare.com`) vs Route53 vs Azure DNS |
| **CNAME / A records** | CDN — Cloudflare, Fastly, CloudFront, Akamai |
| **Subdomain inventory** (via crt.sh) | Hosted services: `support.x → Zendesk`, `status.x → Statuspage`, `help.x → Helpscout`, `community.x → Discourse`, `docs.x → ReadMe / Mintlify`, `app.x → product`, `api.x → API gateway` |

### Worked example (added to §6.X Tech Stack subsection)

```markdown
### 6.X Inferred Infrastructure (from public DNS + SSL transparency)

| Layer | Vendor (inferred) | Evidence |
|---|---|---|
| CDN | Cloudflare | NS records → ns.cloudflare.com; CT logs |
| Email | Google Workspace | MX → aspmx.l.google.com |
| Marketing | HubSpot | SPF → include:_spf.hubspot.com |
| Customer support | Zendesk | subdomain support.<entity>.com → CNAME zendesk.com |
| Status page | Statuspage (Atlassian) | subdomain status.<entity>.com → CNAME statuspage.io |
| Documentation | Mintlify | subdomain docs.<entity>.com → CNAME mintlify.app |
```

### Anti-patterns

- ❌ **Assuming subdomain SaaS = the only vendor used** — some vendors run multi-vendor on the same surface (Zendesk + Helpscout, etc.)
- ❌ **Reporting "uses AWS" without IP / NS evidence** — many companies front AWS via Cloudflare; the visible hop is Cloudflare.

---

## §4 — Trademark portfolio (USPTO / EUIPO / WIPO)

### Why this matters

Trademark filings are forward-looking signals: companies file marks 12-18 months **before** product launch. A pending trademark for "Acme Pulse" or "Acme Vision" reveals product roadmap that PR hasn't surfaced yet. Defensive filings (filing similar marks to block competitors) reveal strategic positioning.

### Verified free public sources

| Office | URL | Coverage |
|---|---|---|
| **USPTO TM Search** (formerly TESS) | [tmsearch.uspto.gov](https://tmsearch.uspto.gov/) | US |
| **EUIPO eSearch plus** | [euipo.europa.eu/eSearch](https://euipo.europa.eu/eSearch/) | EU |
| **UK IPO trademark search** | [trademarks.ipo.gov.uk](https://trademarks.ipo.gov.uk/ipo/tm/) | UK |
| **CIPO (Canada)** | [ic.gc.ca/app/opic-cipo/trdmrks/srch](https://ised-isde.canada.ca/cipo/trademarks-search/srch) | Canada |
| **IP Australia** | [search.ipaustralia.gov.au/trademarks](https://search.ipaustralia.gov.au/trademarks/) | Australia |
| **WIPO Madrid Monitor** | [www3.wipo.int/madrid/monitor](https://www3.wipo.int/madrid/monitor/) | International |
| **Justia trademarks** (US) | [trademarks.justia.com](https://trademarks.justia.com/) | US (mirror, easier search) |

### What to extract

| Trademark field | Signal |
|---|---|
| Filing date | Earliest evidence of intent |
| Status (live / abandoned / registered) | Did the product actually launch under this mark? |
| Goods/services class (Nice Classification) | Product category — class 9 (software), class 35 (advertising/biz services), class 42 (SaaS) |
| Description ("computer software for...") | Specific positioning |
| Owner of record | Verifies entity, may reveal subsidiaries |
| Office actions | Disputes, refusals, opposition |

### Anti-patterns

- ❌ **Citing pending trademarks as live products** — "intent to use" filings often abandon.
- ❌ **Treating one EU filing as equivalent to global protection** — Madrid System filings are tracked separately.

---

## §5 — Founder / Executive LinkedIn velocity

### Why this matters

Public LinkedIn activity from founders / C-suite is a real engagement signal: posting velocity correlates with fundraise prep (visibility push); silence often precedes departures; profile changes (title shifts, new bullet points) reveal reorgs before they hit the press. **No private API needed** — LinkedIn's public profiles are crawlable.

### Verified methodology

- **SignalHire / Apollo** publish time-series LinkedIn analyses for sales-prospecting (commercial — limited free tiers)
- **LinkedIn Talent Insights** (commercial) — corporate-signal aggregation
- **Academic research on social-media-as-leading-indicator** has been published across multiple business schools and information-systems journals (general body of literature; cite specific papers when needed)

### Public LinkedIn signals (no auth required)

| Signal | What to extract |
|---|---|
| Profile change frequency | Title changes, new bullets — visible on profile |
| Post velocity | Posts per month — visible on activity tab |
| Engagement on posts | Like / comment counts — public |
| Connection growth | Trend visible via WayBack of profile page |
| Mention frequency on others' posts | Search `linkedin.com "<name>"` |
| Conference speaker slots | Profile experience entries |

### Verification subsection (added to §3.X Founder activity)

```markdown
### 3.X Founder Public Engagement Signals (last 12 months)

| Founder/Exec | LinkedIn URL | Posts (12mo) | Avg engagement | Conference talks | Title changes |
|---|---|---|---|---|---|
| <Name> (CEO) | [linkedin.com/in/...](url) | 24 | 89 reactions | 3 | none |
| <Name> (CTO) | [linkedin.com/in/...](url) | 4 | 23 reactions | 0 | added "Co-founder" 2025-Q3 |
```

### Anti-patterns

- ❌ **Assuming silent founders = trouble** — many technical founders post rarely; not a signal alone.
- ❌ **Using LinkedIn-paid-tools data without disclosure** — paid tools (RocketReach, Apollo) extrapolate; cite them as `aggregator-derived`.
- ❌ **Treating "open to work" badges as departure signal** — sometimes legitimately recruiting; verify via other sources.

---

## §6 — Anti-patterns (cross-cutting)

- ❌ **Treating any single OSINT signal as definitive** — these are all triangulation inputs, not facts.
- ❌ **Skipping the Wayback dating layer** — current state ≠ historical state.
- ❌ **Citing OSINT as if it's primary** — these are enriching public-source layers; SEC filings, court records, and press release datelines remain the primary.

---

## §7 — When to load this file

- `--depth=deep` AND any of: `--vertical=security|fintech|govtech` (auto-load MITRE/KEV/CVE section)
- `--audit=customer-concentration` (auto-load job-velocity + LinkedIn-velocity)
- `--data-sources` includes any of: `dns`, `trademark`, `mitre`, `linkedin-velocity`, `job-velocity`
- User asks "what other public signals exist?" / "how can we verify this independently?"

---

## §8 — Related

- `data-sources-extended.md` — broader catalog (SEC EDGAR, GitHub, USPTO, PACER)
- `marketplace-signals.md` — marketplace install counts (complementary signal)
- `arr-triangulation.md` — uses these signals as inputs to ARR-proxy math
