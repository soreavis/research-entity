# Roadmap Inference — Job Postings + GitHub + Patents + Conference Talks

Loaded by the `research-entity` skill when `--depth=deep` AND `--type=competitive|due-diligence|investment` (auto-load) OR `--roadmap` flag set OR user asks "what are they building next?". Codifies the multi-channel inference for **what the entity is building 6-36 months out**.

## §1 — Why this file exists

Per [Rathvane patent CI analysis](https://rathvane.ai/blog/patent-analysis-competitive-intelligence.html) and [Aqute Intelligence patent search](https://www.aqute.com/blog/patent-search-tools-for-competitor-analysis):

> *"Competitors can hide their product roadmap and cannot hide their patent filings, which require public disclosure of innovations including technical details and application areas, often years before products reach market."*

Per [Visualping CI guide](https://visualping.io/blog/what-is-competitive-intelligence) and [FieldReport CI automation analysis](https://www.fieldreport.ai/insights/competitive-intelligence-automation):

> *"A B2B software company monitoring competitor job postings may notice a surge in AI/ML engineering hires, which signals a pivot toward AI-powered features before any public announcement."*

The CI-automation market grew **450% in 2024** with companies reporting **340% ROI** — direction-of-travel intelligence is now table stakes for B2B SaaS strategic decisions.

This file codifies the five public channels for inferring an entity's roadmap.

---

## §2 — Channel A: Job postings (3-9 month horizon)

**Sources:**
- [Greenhouse](https://www.greenhouse.io/) — `boards.greenhouse.io/<entity-slug>`
- [Lever](https://www.lever.co/) — `jobs.lever.co/<entity-slug>`
- [Ashby](https://www.ashbyhq.com/) — `jobs.ashbyhq.com/<entity-slug>`
- [Workable](https://www.workable.com/), [Recruitee](https://recruitee.com/) — entity-hosted equivalents
- [LinkedIn Jobs](https://www.linkedin.com/jobs/) — entity company page → "Jobs"

**Inference rubric (role-keyword density):**

| Role-keyword surge | Inferred roadmap direction |
|---|---|
| "AI / ML / GenAI Engineer" / "Applied Scientist" | AI feature investment 6-12mo |
| "Platform Engineer" / "SRE" / "Infrastructure" | Scaling / multi-tenant rearchitecture |
| "Compliance" / "Security Engineer" | SOC 2 / ISO / FedRAMP track |
| "Solutions Architect" / "Implementation" | Enterprise / mid-market expansion |
| "Channel" / "Partner" / "Alliances" | Partnership / OEM motion |
| "International" / "Localization" / "Multi-region" | Geographic expansion |
| "Vertical-specific PM" (e.g., "Healthcare PM") | Vertical-product edition |
| "Renewals Manager" / "Expansion AE" | Land-and-expand investment |
| "Developer Relations" / "DevRel" | Developer-platform / API motion |
| "Mobile Engineer" (iOS/Android) | Native mobile investment |
| "Field Sales" / "Outside Sales" | Mid-market / enterprise expansion |

**Volume thresholds:**
- 1-2 postings = noise
- 3-5 postings in same area = signal
- 6+ postings in same area = directional confirmation
- 10+ postings in same area = explicit strategic priority

**Time horizon:** 3-9 months from posting to feature shipping (typical for engineering hires).

---

## §3 — Channel B: GitHub public repos (1-3 month horizon)

**Sources:**
- `github.com/<entity-org-slug>` — main org page
- Contributor LinkedIn cross-reference (engineers' public GitHub)
- [GitHub Activity API](https://docs.github.com/en/rest/activity/events) for commit-pattern analysis

**Inference rubric:**

| Signal | Inferred direction |
|---|---|
| New public repo created | New product / SDK / dev-tool launch (3-6mo) |
| Spike in commits to existing repo | Active development on that surface |
| New language adoption (e.g., Rust appearing) | Performance / infra rewrite |
| New dependencies on AI libraries (langchain, OpenAI SDK) | AI feature in development |
| API documentation changes | Public API surface area shifting |
| Commits to security / compliance configs | Compliance investment |
| OSS-license open-sourcing of core component | Developer-marketing motion |

**Caveats:**
- Most production code is in **private repos** — public GitHub shows the developer-relations / OSS / dev-tool surface only
- Commit count ≠ feature direction (much commit activity is refactoring / dependency updates / CI tweaks)
- A single contributor's GitHub may not represent the company's roadmap

**Time horizon:** 1-3 months for changes already in commit-history; 3-6 months for new-repo-creation signal.

---

## §4 — Channel C: Patent filings (12-36 month horizon)

**Sources:**
- [USPTO Patent Search](https://ppubs.uspto.gov/pubwebapp/) (post-November 2023 successor to PatFT)
- [USPTO Trademark Search](https://tmsearch.uspto.gov/)
- [EUIPO eSearch Plus](https://euipo.europa.eu/eSearch/) (EU patents + trademarks)
- [WIPO PatentScope](https://patentscope.wipo.int/) (international PCT filings)
- [Google Patents](https://patents.google.com/) (free, well-indexed)

**Inference rubric:**

| Signal | Inferred direction |
|---|---|
| Patent filing in new technical area | New product line in development (12-36mo) |
| Continuation patent (refining prior filing) | Existing product getting deeper investment |
| Trademark filing for new product name | Product launch within 6-12 months |
| Provisional patent (1-year window) | Early-stage technology exploration |
| PCT international filing | Geographic expansion intent for the underlying tech |

**Critical anti-hallucination caveat:**
- **Patent filing ≠ product shipping.** Industry abandonment rate for filed patents is **40-60%** depending on industry. Filing a patent is a defensive / signal investment, not a commitment to ship.
- **Patent filings have 12-36 month lag** between filing and product. By the time a patent surfaces publicly, the entity has been working on the underlying tech for years.

**Time horizon:** 12-36 months between patent filing and product shipping (industry average); 50%+ of filings never ship.

---

## §5 — Channel D: Conference talks + public technical content (6-18 month horizon)

**Sources:**
- Engineering blog post velocity (entity's `/blog/` page Wayback delta)
- Conference speaker databases ([SaaStr Annual](https://www.saastr.com/), [Web Summit](https://websummit.com/), industry-vertical conferences)
- YouTube channel (engineering / leadership talks)
- Podcast appearances ([Acquired](https://www.acquired.fm/), [Lenny's Podcast](https://www.lennyspodcast.com/), industry podcasts)

**Inference rubric:**

| Signal | Inferred direction |
|---|---|
| Engineering blog post on new technical pattern | Feature using that pattern within 6-12mo |
| Conference talk on roadmap-adjacent topic | Public-facing maturity for that surface |
| Year-over-year shift in talk topics | Strategic pivot |
| New "we built X with Y" case study | Validation of internal infrastructure decision |

**Time horizon:** 6-18 months — talks/blog posts are typically about work already in production, but reveal the patterns the entity is doubling down on.

---

## §6 — Channel E: Beta-program leaks + community chatter (variable horizon)

**Sources:**
- Reddit `r/<vertical>` threads — beta-feature mentions
- Trade-press blog posts ("we got early access to <entity>'s new X")
- Forum / Discord chatter
- Twitter (X) employee posts about beta features
- Status-page incident posts referencing pre-release surfaces

**Time horizon:** highly variable — beta programs can be weeks-from-launch or year-out experiments. Lower confidence than other channels.

---

## §7 — Output template (§7.X Roadmap Inference)

```markdown
## §7.X Roadmap Inference

> **Methodology:** Multi-channel public-source inference per `roadmap-inference.md`. Each signal is labeled with confidence band + time horizon. Inferences are NOT roadmap commitments — they are direction-of-travel signals.

### §7.X.1 Job-postings signal (3-9 month horizon)

| Role-area | Posting count | Signal strength | Inferred direction |
|---|---:|---|---|
| <area> | <N> | <High / Medium / Low> | <inference> |

**Top inferred priorities** (job-posting density → 6-12mo roadmap):
1. ...
2. ...
3. ...

### §7.X.2 GitHub signal (1-3 month horizon)

[Per §3 above]

### §7.X.3 Patent signal (12-36 month horizon)

| Filing | Date | Topic | Likelihood of shipping |
|---|---|---|---|
| <patent-ID> | YYYY-MM | <topic> | <Low/Med/High; cite abandonment-rate caveat> |

### §7.X.4 Conference / blog signal (6-18 month horizon)

[Per §5 above]

### §7.X.5 Beta-program / community signal (variable horizon)

[Per §6 above]

### §7.X.6 Convergent roadmap inference

**12-month outlook (most likely shipping):**
- <bullet>
- <bullet>

**12-36 month outlook (in-development, lower confidence):**
- <bullet>
- <bullet>

**Honest framing:** Roadmap inferences are **directional, not predictive**. Patent abandonment rate is 40-60%; job postings can be filled and the role pivot before shipping; conference talks describe past work, not future commitments. Confidence bands per signal must be respected.
```

---

## §8 — Anti-hallucination discipline (Cat J extensions)

- **#79 — Patent-filing ≠ product-shipping**: every patent inference must include the 12-36 month lag caveat AND the 40-60% abandonment-rate caveat. Never present a patent as "they're shipping X."
- **#80 — Job-posting count → time-horizon labeling**: every job-posting-derived inference must label the 3-9 month time horizon. Never present job postings as "they're building X" without horizon.
- **#81 — Conference-talk ≠ shipping-feature**: talks describe past work or in-production patterns. 6-18 month lag from talk to public availability for the same surface.
- **#82 — GitHub-commit ≠ feature-direction**: most production code is private; public GitHub shows DevRel / OSS / SDK surface. Never extrapolate full-product roadmap from public GitHub alone.
- **#87 — Multi-channel convergence requirement**: a roadmap claim must be supported by ≥2 independent channels (e.g., job postings + patents) for confidence "Medium"; ≥3 channels for "High."
- **#88 — Counter-evidence check**: if entity has 5+ ML engineers but no ML feature shipped in 24 months, that's actually LOW-confidence ML signal (could be R&D, exploration, or hiring without strategic priority).

---

## §9 — When to load this file

- **Auto-load** for `--depth=deep` AND `--type=competitive|due-diligence|investment`
- **Manual load** when `--roadmap` flag set
- User asks "what are they building next?" / "what's their roadmap?" / "where is the entity heading?"
- Composes with `osint-public.md` (which covers job postings as part of broader OSINT) — this file specifically focuses on roadmap-direction synthesis from those signals.

---

## §10 — Composability

| Concern | File |
|---|---|
| Job posting OSINT (Greenhouse / Lever / Ashby) | `osint-public.md` |
| Patent search (USPTO / EUIPO / WIPO) | `data-sources-extended.md` |
| GitHub developer-tool inference | `data-sources-extended.md` |
| Conference / press-coverage analysis | `press-analysis.md` |
| Multi-method estimation discipline | `internal-consistency.md` technique #55 |

---

## §11 — Anti-patterns

- ❌ Presenting a patent filing as "<entity> is shipping X" — patents have 40-60% abandonment + 12-36mo lag
- ❌ Presenting job postings as "<entity> is building X" without 3-9mo horizon caveat
- ❌ Inferring full-product roadmap from public GitHub alone (most production code is private)
- ❌ Presenting conference-talk topics as "future" features — talks describe past or in-production work
- ❌ Single-channel roadmap inference — always require ≥2 channels for "Medium" confidence
- ❌ Ignoring counter-evidence (5 ML engineers / 0 ML features over 24mo = LOW signal)
- ❌ Treating roadmap inference as roadmap commitment — they are direction signals, not predictions

---

## §12 — Industry validation

- [Rathvane Patent Analysis as Competitive Intelligence](https://rathvane.ai/blog/patent-analysis-competitive-intelligence.html) — definitive primary source on patent CI
- [Visualping What is Competitive Intelligence](https://visualping.io/blog/what-is-competitive-intelligence)
- [Aqute Intelligence patent search for competitor analysis](https://www.aqute.com/blog/patent-search-tools-for-competitor-analysis)
- [FieldReport CI automation analysis](https://www.fieldreport.ai/insights/competitive-intelligence-automation) — 450% market growth, 340% ROI, $12B opportunity
- [Klue Win-Loss Analysis Guide](https://klue.com/blog/win-loss-analysis-guide) — adjacent practice
