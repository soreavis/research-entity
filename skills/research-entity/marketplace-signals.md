# Marketplace / App-Store Signals

Loaded by the `research-entity` skill when the entity has any marketplace presence (B2B SaaS, dev tools, browser extensions, mobile apps, integration platforms). Marketplace listings are often the **only public usage signal** for private B2B companies that don't disclose ARR / customer count / revenue. Currently zero coverage in the skill — this file closes the gap.

---

## §1 — Why marketplaces matter

A vendor that claims "1,200 customers" is making an unverifiable assertion. A vendor whose Atlassian Marketplace listing shows **"4,200 active installations"** has produced a public, time-stamped, third-party-hosted figure. The marketplace operator (Salesforce, Atlassian, etc.) has its own incentive to publish accurate numbers because the count drives discovery ranking.

**Verified rationale:**
- Bain & BCG commercial-DD frameworks (general industry practice) treat marketplace install counts and app-store ratings as independent demand proxies — specific PE-DD playbook contents are typically client-confidential, but the practice is industry-standard
- Forrester Total Economic Impact (TEI) methodology — used to validate vendor-claimed ROI — references publicly observable usage signals as part of the impact-evidence chain → [forrester.com/research-and-services/total-economic-impact/](https://www.forrester.com/policies/tei)

---

## §2 — Marketplace catalog (verified public data)

For each marketplace, the table lists what's **publicly visible without login** and what's gated behind partner access.

### B2B SaaS marketplaces

| Marketplace | Public install/usage signal | Reviews | Public URL pattern | Notes |
|---|---|---|---|---|
| **Salesforce AppExchange** | Review count + average rating | ✅ public | [appexchange.salesforce.com/listingDetail?listingId=<ID>](https://appexchange.salesforce.com) | "Customers" tag (logos), but no install count |
| **HubSpot App Marketplace** | Install range ("100+", "1k+", "10k+") + review count | ✅ public | [ecosystem.hubspot.com/marketplace/apps/<slug>](https://ecosystem.hubspot.com/) | Install range is the most useful signal |
| **Microsoft AppSource** | Review count + rating | ✅ public | [appsource.microsoft.com/en-us/product/<category>/<vendor>.<product>](https://appsource.microsoft.com) | M365/Dynamics/Power Platform apps |
| **Microsoft Azure Marketplace** | Review count + rating | ✅ public | [azuremarketplace.microsoft.com/en-us/marketplace/apps/<slug>](https://azuremarketplace.microsoft.com) | Infrastructure + AI/ML apps |
| **Atlassian Marketplace** | **Exact install count** (gold standard) + review count | ✅ public | [marketplace.atlassian.com/apps/<id>/<slug>](https://marketplace.atlassian.com) | Install count is exact (e.g., "4,237 installations"); refreshed daily |
| **Slack App Directory** | Review count | ✅ public | [slack.com/apps/<id>-<slug>](https://slack.com/apps) | No install count public |
| **Microsoft Teams App Store** | Reviews + rating | ✅ public | [appsource.microsoft.com/en-us/product/office/<id>](https://appsource.microsoft.com) | Same backend as AppSource |
| **Zoom App Marketplace** | Review count + rating | ✅ public | [marketplace.zoom.us/apps/<id>](https://marketplace.zoom.us) | — |
| **GitHub Marketplace** | Install count visible on action listings; install button shows install context | ✅ public | [github.com/marketplace/<slug>](https://github.com/marketplace) | Open-source actions especially well-instrumented |
| **GitLab Marketplace / Catalog** | Reviews + rating | ✅ public | [gitlab.com/explore/catalog](https://gitlab.com/explore/catalog) | Smaller volume but enterprise-relevant |

### Browser extension stores

| Marketplace | Public install signal | Reviews | URL pattern |
|---|---|---|---|
| **Chrome Web Store** | **Exact user count** ("X users") | ✅ public | [chromewebstore.google.com/detail/<slug>/<id>](https://chromewebstore.google.com/) |
| **Firefox Add-ons (AMO)** | **Exact user count** ("X users") + total downloads | ✅ public | [addons.mozilla.org/en-US/firefox/addon/<slug>/](https://addons.mozilla.org) |
| **Edge Add-ons** | User count + reviews | ✅ public | [microsoftedge.microsoft.com/addons/detail/<id>](https://microsoftedge.microsoft.com/addons/) |
| **Safari Extensions Gallery** | Rating only | ✅ public | [apps.apple.com/us/app/<slug>/id<id>](https://apps.apple.com) (via Mac App Store) |

### Mobile app stores

| Store | Public install signal | Reviews | Notes |
|---|---|---|---|
| **Apple App Store** | Rating + review count (no install count) | ✅ public | iOS / Mac apps |
| **Google Play Store** | **Install range** ("100,000+", "1M+", "10M+") + review count | ✅ public | Range buckets: 5+, 10+, 50+, 100+, 500+, 1k+, 5k+, 10k+, 50k+, 100k+, 500k+, 1M+, 5M+, 10M+, 50M+, 100M+, 500M+, 1B+ |

### Cloud/infrastructure marketplaces

| Marketplace | Public signal | URL pattern |
|---|---|---|
| **AWS Marketplace** | Reviews + rating; no install count | [aws.amazon.com/marketplace/pp/prodview-<id>](https://aws.amazon.com/marketplace/) |
| **Google Cloud Marketplace** | Listing + reviews | [console.cloud.google.com/marketplace/product/<vendor>/<product>](https://console.cloud.google.com/marketplace) |
| **Azure Marketplace** | Reviews + rating | (covered above) |
| **DigitalOcean Marketplace** | Listings + tags | [marketplace.digitalocean.com/apps/<slug>](https://marketplace.digitalocean.com) |
| **Snowflake Marketplace** | Listing + provider info | [app.snowflake.com/marketplace](https://app.snowflake.com/marketplace) |
| **Databricks Marketplace** | Listings | [databricks.com/marketplace](https://marketplace.databricks.com/) |

### Integration / no-code platforms

| Platform | Public signal | URL pattern |
|---|---|---|
| **Zapier** | App listing presence + popularity ("popular," "premium") | [zapier.com/apps/<slug>/integrations](https://zapier.com/apps/) |
| **Make.com (formerly Integromat)** | App presence + review-equivalent | [make.com/en/integrations/<slug>](https://www.make.com/en/integrations) |
| **Workato** | App presence | [workato.com/integrations/<slug>](https://www.workato.com/integrations) |
| **n8n** | Node presence + popularity rank | [n8n.io/integrations/<slug>](https://n8n.io/integrations) |
| **Tray.io** | App listing | [tray.io/connectors](https://tray.io/connectors) |

### Developer tool registries

| Registry | Public signal | URL pattern |
|---|---|---|
| **npm** | **Exact weekly download count** + dependents | [npmjs.com/package/<name>](https://npmjs.com/) |
| **PyPI** | Download stats via [pypistats.org/packages/<name>](https://pypistats.org/) | [pypi.org/project/<name>/](https://pypi.org/) |
| **RubyGems** | **Exact download count** | [rubygems.org/gems/<name>](https://rubygems.org/gems/) |
| **NuGet** | Download count | [nuget.org/packages/<name>](https://www.nuget.org/packages/) |
| **Maven Central** | Indirect via libraries.io | [search.maven.org](https://search.maven.org/) |
| **Cargo (Rust)** | Download count | [crates.io/crates/<name>](https://crates.io/crates/) |
| **pkg.go.dev** | Importer count | [pkg.go.dev/<package>](https://pkg.go.dev/) |
| **Docker Hub** | Pull count + star count | [hub.docker.com/r/<owner>/<image>](https://hub.docker.com/) |

---

## §3 — Triangulation math (turning install counts into ARR proxies)

### The conversion problem

A "10,000 installations" Atlassian Marketplace count ≠ "10,000 paying customers." Conversion math:

```
Active installations × Conversion-to-paid × Average contract value = ARR proxy

Where:
- Conversion-to-paid: 5-15% for SaaS marketplace freemium (Atlassian discloses ~10-15% for paid apps)
- Average contract value: depends on tier; check pricing page
```

### Conversion benchmarks (industry estimates — these are NOT marketplace-disclosed exact rates)

| Marketplace | Free-to-paid conversion (industry estimate range) | Notes |
|---|---|---|
| Atlassian Marketplace (paid apps) | ~5-15% | Industry estimates from Atlassian partner blogs + community discussions; Atlassian itself does not publish a per-listing paid-conversion rate |
| Chrome Web Store (freemium) | ~2-5% | Generic SaaS-freemium conversion industry range; not Chrome-specific disclosure |
| Salesforce AppExchange | High (90%+ are paid-only) | Most AppExchange listings are paid-from-day-1, not freemium |
| Mobile app freemium | ~2-5% | Industry-broad benchmarks (data.ai / Sensor Tower / App Annie historical reports) |
| HubSpot Marketplace (paid apps) | ~10-20% | Industry estimates from HubSpot ecosystem partner discussions; not HubSpot-disclosed |

**Important caveat:** these conversion ranges are **industry estimates**, not marketplace-operator-disclosed figures. Use them to triangulate plausibility ranges, not as authoritative rates. When citing in a dossier, label as "industry-estimate conversion range, not marketplace-disclosed."

### Worked example

Vendor "Foo" claims "1,200 customers." Atlassian Marketplace shows 8,400 installations. Apply industry-estimate paid-conversion range 5-15% → 8,400 × 0.05 to 8,400 × 0.15 = **420 to 1,260 paying customers** (industry-estimate range). Vendor claim of 1,200 **survives validation at the upper end of plausible range** — flag in §16 as "vendor claim near upper bound of triangulated range."

If vendor claims "5,000 customers" but Atlassian shows 1,200 installations → **flag in §16 Risks** as customer-count discrepancy (range upper bound ~180 paying).

---

## §4 — App Store / Play Store install-range buckets (Google Play specifics)

Google Play uses a discrete install-range bucketing system. Knowing the bucket boundaries is essential for accurate triangulation:

| Bucket | Lower bound | Upper bound | Bucket midpoint (for ARR estimation) |
|---|---|---|---|
| 5+ | 5 | 9 | 7 |
| 10+ | 10 | 49 | 30 |
| 50+ | 50 | 99 | 75 |
| 100+ | 100 | 499 | 300 |
| 500+ | 500 | 999 | 750 |
| 1,000+ | 1,000 | 4,999 | 3,000 |
| 5,000+ | 5,000 | 9,999 | 7,500 |
| 10,000+ | 10,000 | 49,999 | 30,000 |
| 50,000+ | 50,000 | 99,999 | 75,000 |
| 100,000+ | 100,000 | 499,999 | 300,000 |
| 500,000+ | 500,000 | 999,999 | 750,000 |
| 1,000,000+ | 1M | 4.99M | 3M |
| 5,000,000+ | 5M | 9.99M | 7.5M |
| 10,000,000+ | 10M | 49.99M | 30M |
| 50,000,000+ | 50M | 99.99M | 75M |
| 100,000,000+ | 100M | 499.99M | 300M |
| 500,000,000+ | 500M | 999.99M | 750M |
| 1,000,000,000+ | 1B | — | — |

**Citation:** [Google Play Console install-bucket schema](https://support.google.com/googleplay/android-developer/answer/139628) — bucket boundaries are publicly disclosed by Google.

For dossier purposes, always cite **the bucket bound as published**, not a fabricated mid-point unless explicitly labeling the estimate.

---

## §5 — Anti-patterns

- ❌ **Treating "10,000+ installations" as "10,000 paying customers"** — this conflates the funnel.
- ❌ **Citing Chrome Web Store user count as "monthly active users"** — Chrome Web Store reports lifetime installs, not MAU.
- ❌ **Inventing install counts that aren't on the listing** — if Salesforce AppExchange doesn't show a number, the dossier doesn't either.
- ❌ **Assuming all marketplace listings are equally weighted** — Atlassian Marketplace install counts are gold (exact, daily-refreshed); Salesforce AppExchange is silver (review counts only); Slack App Directory is bronze (reviews-only, no install count).

---

## §6 — Workflow integration

**Step 2 — source gathering**: when the entity has any marketplace presence (auto-detected from the company's main domain or `/integrations` page), run a marketplace scan in parallel:

```python
# Marketplaces worth scanning when the entity has any listing presence
marketplaces_to_check = [
  "Salesforce AppExchange",
  "HubSpot App Marketplace",
  "Atlassian Marketplace",
  "Microsoft AppSource",
  "Slack App Directory",
  "Chrome Web Store",
  "Apple App Store + Google Play",
  "AWS Marketplace",
  "npm / PyPI / GitHub Marketplace (for dev tools)",
]
```

**Step 4 — draft**: surface findings in a new sub-table within §13 Integrations:

```markdown
### 13.X Marketplace Presence + Public Usage Signals

| Marketplace | Listing | Public install / usage | Review count | Avg rating | Listed since |
|---|---|---|---|---|---|
| Atlassian Marketplace | [foo-jira-app](url) | **4,237 installations** | 89 reviews | 4.2★ | 2022-03 |
| Chrome Web Store | [foo-extension](url) | 12,400 users | 156 reviews | 4.5★ | 2021-09 |
| ...
```

**Step 5 — validate**: cross-reference vendor "X customers" claim against marketplace install totals; flag discrepancies in §16 Risks.

---

## §7 — Related

- `arr-triangulation.md` — uses marketplace install counts as input to ARR-proxy math
- `data-sources-extended.md` — broader OSINT data sources
- `lessons.md` — lesson on marketplace-claim cross-validation
