<p align="center">
  <img src="docs/assets/hero.jpg" alt="A robed archivist raises a glowing lantern toward a towering wall of card-catalog drawers in a vast dark archive, a few drawers lit amber high above the dust." width="100%">
</p>

# The Dossier Machine

[![CI](https://github.com/soreavis/research-entity/actions/workflows/ci.yml/badge.svg)](https://github.com/soreavis/research-entity/actions/workflows/ci.yml)
![Version](https://img.shields.io/static/v1?label=version&message=2026.08.1&color=blue)
![License](https://img.shields.io/badge/license-MIT-blue)
![Agent Skills](https://img.shields.io/badge/Agent%20Skills-23%20sections-green)

> **An independent project, built and maintained by Julian Soreavis.** Not affiliated with, endorsed by, or sponsored by any of the vendors whose tools it installs into. Product names and trademarks belong to their respective owners, used here only to describe compatibility. Use at your own risk.

**`research-entity` — board-ready competitive-intelligence and due-diligence dossiers on any legal entity: company, startup, or vendor.** Drop in a name: the skill gathers evidence from free public sources, cross-validates every datapoint, and returns a structured 23-section Markdown dossier — executive briefing up front, methodology appendix at the back.

Ships as an [Agent Skill](https://agentskills.io) with one skill tree and thin per-platform manifests, so it installs into **Claude Code, Claude web/Desktop/Cowork, Codex, Cursor, Gemini CLI, Copilot, Grok, ChatGPT**, and any other Agent Skills runtime — see [Install](#install).

> **Decision-support, not investment, legal, or hiring advice.** Every figure carries its source and a confidence label — read them before acting on it.

## What it does

1. Takes an entity name (plus optional dimensions: research type, depth, audience, funding stage, vertical)
2. Gathers evidence from free public sources — registries, filings, review platforms, job boards, press, OSINT layers
3. Cross-validates every datapoint across independent sources; labels anything aggregator-only
4. Runs an always-on 8-pattern red-flag scan and a hallucination audit
5. Outputs a 23-section dossier to Markdown, with optional HTML, PDF, one-page exec summary, sales battle card, VC memo, or JSON export

### The dossier (23 sections, stable numbering)

- **§0 Executive Briefing** — BLUF, 15-row scorecard with labeled signals, SWOT, strategic position heat map, persona-aware response playbook, monitoring watchlist
- **§1–§18 Company profile** — fundamentals, founders and related entities, funding and investors, product and technical architecture, feature catalog, pricing, customers, market positioning, community reception, data asset, integrations, security posture, content and analyst coverage, risks, strategic analysis, ecosystem view
- **§16.X Red-Flag Scan** — layoffs, exec departures, lawsuits, breaches, regulatory actions, employee-review signals, status-page outages, leadership controversy
- **§19–§23 Evidence layer** — sources, quote bank, final assessment, glossary, confidence-and-methodology appendix

### Why you can trust the output

- Every datapoint checked against multiple free public sources; aggregator-only data explicitly labeled
- Source-or-silence on facts; numeric figures verified to be present in the cited source
- Optional [Admiralty source rating](https://en.wikipedia.org/wiki/Admiralty_code) (`--source-rating=admiralty`) and per-section confidence scoring
- Competitor rows verified against primary sources before market-positioning sections ship
- Every mermaid diagram render-validated before export

## Install

Use your platform's native plugin or skill manager where one exists — those lanes keep the runtime's own update path.

| Platform | Install | Update |
|---|---|---|
| **Claude Code** | `/plugin marketplace add soreavis/research-entity` then `/plugin install research-entity@research-entity` | `/plugin marketplace update research-entity`, or enable marketplace auto-update |
| **Codex** | `codex plugin marketplace add soreavis/research-entity` then `codex plugin add research-entity@research-entity` | `codex plugin marketplace upgrade` |
| **Cursor** | `npx skills add soreavis/research-entity -a cursor` | `npx skills update` |
| **Gemini CLI** | `gemini extensions install https://github.com/soreavis/research-entity` | `gemini extensions update research-entity` |
| **Copilot / GitHub CLI** | `gh skill install soreavis/research-entity research-entity` | `gh skill update research-entity` |
| **Grok** | `grok plugin marketplace add soreavis/research-entity` then `grok plugin install soreavis/research-entity --trust` | `grok plugin update research-entity` |
| **Claude web / Desktop / Cowork** | Customize → Plugins → **+** → Add marketplace → `https://github.com/soreavis/research-entity` | automatic on marketplace sync |
| **ChatGPT** | Skills → **Create** → **Upload from your computer** — the `research-entity.zip` built by [`scripts/build-skill-zips.sh`](scripts/build-skill-zips.sh) | re-upload the newer zip |
| **Other agents** | `npx skills add soreavis/research-entity` | `npx skills update` |

> [!NOTE]
> `gh skill` is in preview and its flags may change.

Step-by-step instructions, the manual-symlink lane for development, and verification steps are in **[docs/install.md](docs/install.md)**.

## Usage

```
/research-entity "Stripe"                       # wizard asks type/depth/audience/export
/research-entity "Acme Corp" --type=due-diligence --audience=investor --depth=deep --export=both
/research-entity "DevTool X" --vertical=devtools --data-sources=github,linkedin --audit=tech-stack
/research-entity "Acme Corp" --year-over-year   # auto-finds prior dossier, generates delta
/research-entity "Public SaaS Y" --stage=public --benchmark --data-sources=sec
/research-entity --compare=./a-research.md,./b-research.md
/research-entity "Acme Corp" --export=battle-card
```

The dimensions that shape a dossier:

| Flag | Values |
|---|---|
| `--type` | `competitive` · `due-diligence` · `partnership` · `investment` · `research` |
| `--depth` | `quick` · `standard` · `deep` (deep spawns parallel cross-validation agents) |
| `--audience` | `c-suite` · `technical` · `investor` · `board` · `operator` |
| `--stage` | `seed` → `public` (7 stage templates) |
| `--vertical` | `healthcare` · `fintech` · `govtech` · `edtech` · `legaltech` · `devtools` · `consumer` · `saas` · `deeptech` |
| `--framework` | `swot` · `pestel` · `porter5` · `vrio` · `value-chain` · `all` (+ 7 Powers moat scoring) |
| `--audit` | `pricing` · `tech-stack` · `customer-concentration` · `ai-maturity` |
| `--export` | `md` · `html` · `pdf` · `exec` · `battle-card` · `vc-memo` · `json` · expert-call / customer-reference question batteries |
| `--agents` | `solo` · `validation` · `parallel` · `max` — how much parallel cross-validation to spend |
| `--source-rating` | `admiralty` — grade every source A–F / 1–6 |
| `--data-sources` | `sec` · `wayback` · `github` · `linkedin` · `uspto` · `pacer` and more |
| `--benchmark` / `--compare` / `--year-over-year` | cohort benchmarks · side-by-side dossier diff · delta vs your prior dossier |

Worked examples with expected output are in **[docs/usage.md](docs/usage.md)**; the full argument reference lives in [`SKILL.md`](skills/research-entity/SKILL.md).

## What a full dossier costs

Token usage measured across four full-depth production runs (one dossier each, sessions dominated by the run):

| Metric | Observed range | Median of the four runs |
|---|---|---|
| Output tokens | 0.55M – 1.5M | ≈ 0.7M |
| Cache reads | 80M – 330M | ≈ 130M |
| Cache writes | 1.7M – 7.2M | ≈ 4.4M |
| Fresh (uncached) input | 30k – 250k | ≈ 80k |

The top of each range is the run that used the heaviest multi-agent verification mode; the skill leans hard on prompt caching, so most input arrives as cache reads billed at a fraction of the fresh-input rate. Quick-depth runs cost substantially less but haven't been measured yet.

## How it's built

A lean `SKILL.md` entrypoint routes to a library of segment files that load on demand — business/court/trademark registers, review-platform playbooks, OSINT layers, roadmap inference, moat scoring, expert-call question batteries, export pipelines, and a curated lessons file of known failure modes. The design is explained in **[docs/how-it-works.md](docs/how-it-works.md)**.

Requirements: an Agent Skills runtime. Optional: [Tavily MCP](https://docs.tavily.com) for higher-quality search (falls back to built-in web search automatically), `pandoc` + `xelatex` for PDF export.

## Versioning

[CalVer](https://calver.org/) — `YYYY.0M.MICRO`, kept in lockstep across all 8 platform manifests and the version badge above; CI fails on drift. Installed users only get an update when the version number changes.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Factual corrections are especially welcome — use the **factual-correction** issue template. Agents maintaining this repo start at [AGENTS.md](AGENTS.md).

## License

[MIT](LICENSE) © [Julian Soreavis](https://github.com/soreavis)
