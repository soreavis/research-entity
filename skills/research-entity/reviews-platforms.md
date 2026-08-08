# Review & Community Platforms

Loaded by the `research-entity` skill during Step 2 (Source gathering) and Step 4 (Draft) for §11 Community Reception. Always quote ≥2 negative reviews verbatim with dates and ≥2 positive reviews verbatim with dates. Flag platform absence ("no Reddit signal") explicitly — absence is itself information.

## B2B SaaS reviews (primary)

- **[G2](https://www.g2.com/)** — review count + rating + badges (Leader / High Performer / Easiest Setup / Best Support / Users Love Us / season + year). Bot-blocked direct fetch is common (HTTP 403); count corroborated via aggregator mirrors (e.g., AWS Marketplace syndication of G2 reviews) or [prospeo.io](https://prospeo.io/) syndication.
- **[Capterra](https://www.capterra.com/)** — review count + sub-ratings (Ease, Features, Value, Customer Support). Ownership: Gartner Digital Markets.
- **[Software Advice](https://www.softwareadvice.com/)** — Capterra-affiliated; often shares the same review database.
- **[GetApp](https://www.getapp.com/)** — Capterra-affiliated; often shares the same data; check for distinct ratings distribution per stars (5★ / 4★ / 3★ / 2★ / 1★).
- **[Gartner Peer Insights](https://www.gartner.com/reviews/)** — often missed; valuable since enterprise procurement reads it. Required login but public count visible.
- **[TrustRadius](https://www.trustradius.com/)** — long-form reviews, business-context-focused. Bot-blocked direct fetch common.
- **[SourceForge](https://sourceforge.net/)** — open-source / SMB tool reviews.

## B2C / general reputation

- **[Trustpilot](https://www.trustpilot.com/)** — TrustScore + review count + breakdown by stars. Note: Trustpilot reviews skew negative (people review when they have a complaint); a 1.5/5 with 70+ reviews is a structural reputation signal, not anecdotal. Quote 2–3 negative reviews verbatim with reviewer pseudonym + date + URL.
- **[Sitejabber](https://www.sitejabber.com/)** — alternative B2C review aggregator.
- **[BBB (Better Business Bureau)](https://www.bbb.org/)** — US-only; complaints + ratings. Useful for billing-dispute patterns.
- **[ResellerRatings](https://www.resellerratings.com/)** — e-commerce reseller reputation.

## Employer / talent platforms

- **[Glassdoor](https://www.glassdoor.com/)** — employee reviews; CEO approval %; culture / WLB / management ratings; recommendation %. **Watch for:** layoff threads, leadership-departure clusters, "trust issues" or "strategy-of-the-week" patterns. No 2024–2026 layoff signals = healthy; presence of those signals = material risk for §16.
- **[Indeed reviews](https://www.indeed.com/)** — overall + Work-life / Culture / Management ratings. Often fewer reviews than Glassdoor but useful cross-check.
- **[Comparably](https://www.comparably.com/)** — comparative employer ratings.
- **[Built In](https://builtin.com/)** — employer profile + tech stack disclosure (in some cases).
- **[Levels.fyi](https://www.levels.fyi/)** — compensation data (anonymous self-reports). Useful for "is this a recruit-from / recruit-to target?" persona.
- **[teamblind.com](https://www.teamblind.com/)** — anonymous employee discussion (login-walled, but news often surfaces here first).

## Community / developer

- **[Reddit](https://www.reddit.com/)** — search across r/<industry>, r/<role>, r/SaaS, r/sales, r/Entrepreneur, r/AskMarketing. Absence is itself a signal (operations-heavy mid-market buyers don't congregate on Reddit). Direct API often bot-blocked; use Google site-search: `site:reddit.com <entity>`.
- **[Hacker News](https://hn.algolia.com/)** — search via Algolia. Absence = low developer mindshare. For developer-tooling vendors, presence is required; for non-developer mid-market vendors, absence is expected and not negative.
- **[Quora](https://www.quora.com/)** — buyer-question presence. Useful for "what do early-stage founders ask about X?"
- **[Product Hunt](https://www.producthunt.com/)** — launch + community votes; useful for early-stage tool-evaluator signal.
- **[Stack Overflow](https://stackoverflow.com/)** — for developer tools, search for the entity / SDK; question count + answer quality.
- **[GitHub](https://github.com/)** — public org repos, last-update cadence, license, star count, SDK languages.

## Marketplace presence

- **[AWS Marketplace](https://aws.amazon.com/marketplace/)** — review count (native + syndicated), pricing terms, SaaS / AMI / container offerings. **Cold-start signal**: if listed for >12 months with 0 native reviews, that's a co-sell motion that hasn't generated engagement.
- **[Google Cloud Marketplace](https://cloud.google.com/marketplace)** — equivalent for GCP customers.
- **[Microsoft Azure Marketplace](https://azuremarketplace.microsoft.com/)** — Microsoft ecosystem.
- **[Salesforce AppExchange](https://appexchange.salesforce.com/)** — for Salesforce-ecosystem ISVs.
- **[HubSpot App Marketplace](https://ecosystem.hubspot.com/marketplace/apps)** — HubSpot ecosystem.
- **[Atlassian Marketplace](https://marketplace.atlassian.com/)** — Atlassian ecosystem.
- **[Zapier App Directory](https://zapier.com/apps)** — Zapier ecosystem; popularity signal.
- **[Make (formerly Integromat) App Library](https://www.make.com/en/integrations)** — Make ecosystem.

## Customer reference databases

- **[FeaturedCustomers](https://www.featuredcustomers.com/)** — case study + testimonial reference count + vendor self-rating (~4.7/5 typical, treat with skepticism); useful for "how many public customer logos exist?"
- **[Enlyft](https://enlyft.com/)** — tracks tool deployment via tech-stack scraping; gives "X companies use this product" estimates (vendor-claimed customer count vs. Enlyft-tracked deployments is a useful sanity-check).
- **[BuiltWith](https://builtwith.com/)** — site technology profiler; useful for "which sites use this tool?"

## Industry analyst sources

- **[Sacra](https://sacra.com/)** — SaaS company analyst reports; valuation models; key metrics. Free for some companies, paywalled for others.
- **[Forrester reports](https://www.forrester.com/)** — Wave reports; Forrester search.
- **[Gartner reports](https://www.gartner.com/)** — Magic Quadrant placement; Hype Cycle.
- **[IDC](https://www.idc.com/)** — market share / forecasts.
- **[CB Insights](https://www.cbinsights.com/)** — startup analytics; basic data free.
- **[PitchBook](https://pitchbook.com/)** — VC tracking; basic free.
- **[Crunchbase](https://www.crunchbase.com/)** — funding tracking; basic free.
- **[Tracxn](https://tracxn.com/)** — startup database.

## Press / news

- **Trade press** by industry: e.g., for CRM → DestinationCRM, KMWorld, SalesTechStar, MarTech Cube, CRM Buyer; for cybersecurity → CSO Online, Dark Reading; for DevOps → InfoQ, The New Stack.
- **General business** — TechCrunch, Forbes, Bloomberg, WSJ, FT, Reuters, AP.
- **Wires** — PRNewswire, BusinessWire, GlobeNewswire (where the entity issues its own press releases).
- **Aggregators** — Morningstar (often mirrors PRNewswire), Yahoo Finance.

## Searches to always run

For lawsuits / breaches / layoffs / regulatory action, search:
- `<entity> lawsuit`
- `<entity> data breach`
- `<entity> layoff`
- `<entity> SEC complaint`
- `<entity> class action`
- `<entity> regulatory action`
- `<entity> CFPB / FTC / DOJ / EU Commission` (depending on jurisdiction)

If found, document with verbatim excerpts + dates + URL in §16 Risks.

## When to load this file

Load `reviews-platforms.md` when:
- Drafting §11 Community Reception
- Pricing discussion needs market-positioning corroboration
- §16 Risks & Weaknesses needs negative-review evidence
- Persona-specific Playbook needs employer or community context (talent persona, customer-renewal persona, press persona)

## Rules

- Always cite ≥10 platforms in §11's quantitative table (even if the value is "0 reviews / not present" — absence is data).
- Always quote ≥2 negative + ≥2 positive reviews verbatim with dates and URLs.
- Always run lawsuit / breach / layoff searches; document outcome (positive or negative) in §16.
- Direct-fetch failures (HTTP 403 from G2, Glassdoor, Trustpilot) are not "no data" — corroborate via aggregator mirrors (prospeo.io, AWS Marketplace syndication, Google site-search snippets).

---

## Aspect-Based Sentiment Analysis (NEW v2.6)

### Why this matters

Aggregate ratings (4.6/5 stars across 216 reviews) hide the **structure** of the rating: which features customers love vs. which they hate. Two products with identical aggregate scores can have completely different competitive postures.

**Aspect-Based Sentiment Analysis (ABSA)** decomposes review text into feature-level sentiment scores: pricing, support, ease-of-use, integrations, performance, etc. Real Voice-of-Customer methodology used by Forrester / Gartner / IDC since the early 2000s.

### Verified methodology citations

- **Minqing Hu & Bing Liu**, "Mining and Summarizing Customer Reviews" (KDD 2004) — foundational paper for **aspect-based** sentiment analysis (introduced the aspect-extraction + opinion-mining framework specifically) → public via [ACM Digital Library / Bing Liu's UIC page](https://www.cs.uic.edu/~liub/publications/kdd04-revSummary.pdf)
- **Bo Pang & Lillian Lee**, *Opinion Mining and Sentiment Analysis* (Foundations and Trends in Information Retrieval, 2008) — comprehensive survey of the sentiment-analysis field including ABSA → [public PDF on cs.cornell.edu](https://www.cs.cornell.edu/home/llee/omsa/omsa.pdf)
- **SemEval ABSA shared task** (2014, 2015, 2016) — academic benchmark that standardized the ABSA evaluation methodology → [alt.qcri.org/semeval2014/task4](https://alt.qcri.org/semeval2014/task4/)
- **Forrester Voice of the Customer** — methodology summary → [forrester.com](https://www.forrester.com/)
- **Qualtrics Text iQ** — commercial implementation → [qualtrics.com/experience-management/research/text-iq](https://www.qualtrics.com/support/survey-platform/data-and-analysis-module/text-iq/text-iq-functionality/)
- **MonkeyLearn / Hugging Face ABSA models** — open-source implementations available on Hugging Face Hub

### How to apply (manual / LLM-assisted)

For dossiers with ≥30 publicly accessible reviews (G2, Capterra, Trustpilot, app stores), categorize each review's content into 6-12 aspects:

```
Default aspect taxonomy for B2B SaaS:
1. Pricing / value-for-money
2. Customer support quality
3. Ease of use / onboarding
4. Performance / reliability
5. Integration breadth + quality
6. Feature completeness
7. Documentation / training
8. Reporting / analytics
9. Mobile / cross-platform
10. Security / compliance
11. Account management / CSM
12. Product roadmap responsiveness
```

For each aspect, score sentiment as +1 / 0 / -1 per review mentioning it.

### Output table (added to §11.X for `--depth=deep` OR `--audit=customer-concentration`)

```markdown
### 11.X Aspect-Based Sentiment Analysis (last 24 months, n=N reviews)

| Aspect | Mention rate | Avg sentiment | Trend (vs. prior 12mo) |
|---|---:|---:|---|
| Pricing / value-for-money | 68% | +0.32 | ⬇ from +0.51 |
| Ease of use | 54% | +0.78 | ⬆ from +0.65 |
| Customer support | 47% | -0.21 | ⬇ from +0.10 (red flag) |
| Integrations | 42% | +0.62 | flat |
| Performance | 31% | -0.05 | ⬇ from +0.30 (yellow flag) |
| Feature completeness | 28% | +0.41 | flat |
| Mobile experience | 12% | -0.45 | (low n; directional) |
| ... | ... | ... | ... |

**Verdict:** Strengths — ease of use + integrations. Weaknesses — declining support quality, declining performance scores. **Watchlist signal**: support sentiment declined from +0.10 to -0.21 in last 12 months — verify against churn / G2 review velocity.
```

### Anti-patterns

- ❌ Reporting aggregate ratings without aspect decomposition — masks the structure
- ❌ Treating low-sample-size aspects as definitive (n<10) — label as "directional"
- ❌ Using ABSA scores from one platform alone — corroborate across G2 + Capterra + Trustpilot
- ❌ Hallucinating aspect scores from a small sample — only score aspects mentioned in ≥10% of reviews

### When to load this section

- `--depth=deep` AND entity has ≥30 reviews on G2/Capterra/Trustpilot
- `--audit=customer-concentration` (auto)
- User asks "what do customers actually like / dislike?"
- User asks "where is the entity at risk of churn?"
