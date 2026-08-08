# Risk / Red-Flag Scan — Always-On §16.X

Loaded by the `research-entity` skill at Step 2 (parallel source gathering) — NOT optional. Every dossier gets a Risk Scan section. Time-sensitive risk findings are the highest-ROI part of any due-diligence dossier; missing one is the difference between catching the failure mode and walking into it.

This file defines the 8 scan patterns that run in parallel as part of Step 2.

## What this section produces

A new subsection in §16 Risks & Weaknesses titled **§16.X Red-Flag Scan**, which presents:

- A severity-ranked table of any signals found (Critical / High / Medium / Low / None)
- Verbatim source quotes for each finding (with date)
- A "no-finding" row for any pattern that searched cleanly (so the reader knows the scan ran, not just got skipped)
- A "next monitoring action" recommendation per finding

## The 8 scan patterns

### 1. Layoffs

```
search: "<entity> layoff" OR "<entity> headcount reduction" OR "<entity> RIF"
sources: layoffs.fyi, news, LinkedIn employee-departure spike
date-window: last 18 months
severity:
  - 0 layoffs found → None
  - 1 layoff < 5% headcount → Low
  - 1 layoff 5–15% headcount → Medium
  - layoff > 15% headcount → High
  - multiple layoffs in 12 months → Critical
```

Specific URLs:
- `https://layoffs.fyi/?company=<entity-slug>`
- Site-scoped: `site:thelayoff.com "<entity>"`
- LinkedIn search: `"left <entity>" past month`

### 2. Executive departures

```
search: "former <entity> CEO" OR "former <entity> CTO" OR "<entity> executive departure" OR "<exec name> joined"
sources: LinkedIn role-change posts, news, company press releases
date-window: last 12 months
severity:
  - No CXO turnover → None
  - 1 non-CEO/CTO/CFO departure → Low
  - 1 CEO/CTO/CFO departure with planned succession → Medium
  - 1 CEO/CTO/CFO sudden departure (no successor named) → High
  - Multiple CXO departures in 6 months → Critical
```

### 3. Lawsuits

```
search: "<entity> lawsuit" OR "<entity> sued" OR "<entity> settlement" OR "<entity> class action"
sources:
  - PACER (US federal): https://pacer.uscourts.gov/ — load `data-sources-extended.md`
  - CourtListener: https://www.courtlistener.com/?type=r&q=<entity>
  - state court records (varies by state)
  - news
date-window: last 5 years (older if material)
severity:
  - 0 lawsuits → None
  - Small contractor / vendor disputes → Low
  - Customer disputes / data-related disputes → Medium
  - Class action / patent infringement / regulatory action → High
  - Securities fraud / criminal charges → Critical
```

### 4. Data breaches

```
search: "<entity> breach" OR "<entity> data leak" OR "<entity> incident" OR "<entity> ransomware"
sources:
  - https://haveibeenpwned.com/PwnedWebsites
  - https://www.databreaches.net/?s=<entity>
  - https://news.ycombinator.com/from?site=&q=<entity>+breach
  - state AG breach-notification disclosures (CA AG, NY AG, etc.)
date-window: last 5 years
severity:
  - 0 breaches → None
  - Phishing / credential-stuffing-only → Low
  - PII exposure < 10K records → Medium
  - PII exposure 10K–1M records → High
  - PII exposure > 1M records OR PHI/PCI exposure → Critical
```

### 5. Regulatory actions

```
search: "<entity> SEC enforcement" OR "<entity> FTC consent order" OR "<entity> CFPB" OR "<entity> NYDFS" OR "<entity> EU GDPR fine" OR "<entity> ICO fine"
sources:
  - SEC litigation: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany
  - FTC press releases: https://www.ftc.gov/news-events/news/press-releases
  - CFPB enforcement: https://www.consumerfinance.gov/enforcement/actions/
  - GDPR enforcement tracker: https://www.enforcementtracker.com/
  - ICO action database: https://ico.org.uk/action-weve-taken/
date-window: last 5 years
severity:
  - 0 actions → None
  - Compliance warning / consent order without fine → Medium
  - Fine < $1M → High
  - Fine ≥ $1M OR criminal referral → Critical
```

### 6. Glassdoor rating plummet

```
search: site:glassdoor.com <entity> reviews
extract: current overall rating, CEO approval rating, "would recommend to a friend" %
compare: rating 12 months ago (via Wayback Machine — load `data-sources-extended.md`)
severity:
  - Rating ≥ 4.0 stable or improving → None
  - Rating 3.5–4.0 stable → Low
  - Rating dropped > 0.5 stars in 12 months → Medium
  - Rating dropped > 1.0 stars in 12 months → High
  - Rating < 3.0 OR "would recommend" < 50% → Critical
```

### 7. Status-page outage history

```
search: <entity>'s status page (typically status.<domain> or trust.<domain>/status)
extract: incident count past 90 days, mean time to resolution, severity distribution
sources:
  - <entity>.statuspage.io
  - status.<entity>.com
  - https://status.io/<entity>
  - https://www.uptime.com/status (third-party validators)
date-window: last 90 days
severity:
  - 0–2 incidents, all minor → None
  - 3–5 incidents OR 1 major → Low
  - 6–10 incidents OR 2 majors → Medium
  - > 10 incidents OR 1 critical OR 1 multi-hour outage → High
  - Status page itself missing / not public → Medium (transparency red flag)
```

### 8. CEO / leadership controversy

```
search: "<CEO name> controversy" OR "<CEO name> investigation" OR "<CEO name> resigned" OR "<entity> founder dispute"
sources: news (especially TechCrunch, The Information, Forbes, NYT, WSJ)
date-window: last 5 years (older if material)
severity:
  - 0 controversy → None
  - Minor PR mishap (apology issued, moved on) → Low
  - HR allegation / harassment claim → High
  - Founder lawsuit / cofounder ouster → High
  - Criminal investigation / SEC investigation → Critical
```

## Output template (insert as §16.X)

```markdown
### 16.X Red-Flag Scan

Automated scan of 8 risk-signal patterns as of <date>. Cleanly-searched patterns reported as "✓ none found"; positive findings include source + severity + recommendation.

| Pattern | Result | Severity | Source(s) | Recommendation |
|---|---|---|---|---|
| **Layoffs (18mo)** | ... | ... | ... | ... |
| **Executive departures (12mo)** | ... | ... | ... | ... |
| **Lawsuits (5yr)** | ... | ... | ... | ... |
| **Data breaches (5yr)** | ... | ... | ... | ... |
| **Regulatory actions (5yr)** | ... | ... | ... | ... |
| **Glassdoor rating delta (12mo)** | ... | ... | ... | ... |
| **Status-page outage rate (90d)** | ... | ... | ... | ... |
| **Leadership controversy (5yr)** | ... | ... | ... | ... |

**Composite risk severity**: None / Low / Medium / High / Critical (the highest of the 8 patterns).

**Detail per finding** (only include rows with severity > None):

#### Finding 1: <Pattern name> — Severity: <Critical|High|Medium|Low>
- **What**: <1-sentence description>
- **When**: <date or date range>
- **Source**: [<title>](<url>) (verbatim quote: "...")
- **Why it matters**: <1–2 sentences>
- **Monitoring action**: <add to §0 Watchlist with specific URL or trigger>
```

## Workflow

Step 2 (Parallel source gathering) runs all 8 patterns in parallel via WebSearch + WebFetch (Tavily fallback if available).

For high-severity findings, spawn an `Agent` subagent to deep-dive: "Pull every news article on this layoff event and produce a 200-word timeline."

Append findings to §16 as a new subsection. Surface composite severity in §0 Heat Map (e.g., row "Operational risk: High — recent layoff + 1 CXO departure").

## Anti-patterns

- ❌ Skipping the scan when no obvious risk is mentioned in /about page (the absence of mention is exactly when the scan adds value)
- ❌ Reporting "no findings" without showing which patterns ran (reader can't distinguish "scan was clean" from "scan was skipped")
- ❌ Citing aggregator-only data on lawsuits (always go to PACER / CourtListener / state court for primary source)
- ❌ Reporting a 2018 layoff as "Critical" when there have been 2 funding rounds and headcount tripling since (severity must reflect recency)
- ❌ Glassdoor data without comparison to 12 months ago (a 3.2 rating could be stable improvement from 2.8, or could be a slide from 4.1 — the delta matters more than the absolute)

## Suggested follow-up

After running this scan, offer to /schedule a recurring re-run. Layoff and exec-departure signals are highly time-sensitive:

> "Risk scan completed. Highest severity: <severity>. Want me to /schedule a monthly re-scan that emails you when severity changes? Recommend cron: `0 9 1 * *` (first of every month, 9am)."

## When to load this file

- Always loaded at Step 2 (Risk scan is mandatory, not opt-in)
- User asks "are there any red flags?" or "what could go wrong?"
- Pre-renewal vendor review
- Pre-investment due-diligence
