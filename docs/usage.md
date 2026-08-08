# Usage

You give it a company name. It gives you back a dossier you could hand to a board. This page walks through what happens in between — and how to steer it.

## Your first dossier

```
/research-entity "Stripe"
```

With no flags, a short wizard asks the questions that shape the report: what kind of research this is (competitive? due diligence?), how deep to go, who will read it, and how you want it exported. Answer them — or skip the wizard entirely:

```
/research-entity "Stripe" --no-wizard
```

That runs with sensible defaults: standard depth, operator audience, Markdown output.

A `--depth=quick` run gives you fundamentals and a red-flag scan in a few minutes. `--depth=standard` is the full 23 sections. `--depth=deep` additionally spawns parallel cross-validation agents that independently re-verify the load-bearing claims — slowest, and the one you want for anything with money attached.

## The invocations you'll actually use

**Sizing up a competitor** — what they ship, what they charge, where they're weak:

```
/research-entity "Acme Corp" --type=competitive --audience=operator --depth=deep
```

**Vetting a vendor or acquisition target** — the full treatment, exported for circulation:

```
/research-entity "Acme Corp" --type=due-diligence --audience=investor --depth=deep --export=both
```

**A vertical-aware run** — the stage and vertical templates change what "normal" looks like (a Series B healthtech company is judged differently from a bootstrapped devtool):

```
/research-entity "Healthtech Co" --vertical=healthcare --stage=series-b
/research-entity "DevTool X" --vertical=devtools --data-sources=github,linkedin --audit=tech-stack
```

**Re-checking an entity you researched before** — finds your prior dossier and reports what changed:

```
/research-entity "Acme Corp" --year-over-year
```

**Comparing two dossiers side by side:**

```
/research-entity --compare=./acme-research.md,./globex-research.md
```

**A focused audit instead of (or added to) the full report:**

```
/research-entity "Acme Corp" --audit=pricing
/research-entity "Acme Corp" --audit=pricing,tech-stack,customer-concentration,ai-maturity --depth=deep
```

**Benchmarking against a cohort:**

```
/research-entity "Public SaaS Y" --stage=public --benchmark --data-sources=sec
```

## Exports

`--export=` takes: `md` (default), `html`, `pdf` (needs `pandoc` + `xelatex`), `exec` (one-page summary), `battle-card` (for sales teams), `vc-memo` (investment-memo format), `json` (structured dump), and two interview kits — `expert-call-questions` and `customer-reference-questions` — for when the desk research is done and it's time to talk to humans.

## Reading the dossier

Three conventions carry the trust model:

- **Signal labels.** Scorecard cells are never a bare dot — always `🟢 Strong`, `🟡 Unverified`, `🔴 Absent`, or `⚪ N/A`, so a glance tells you both the verdict and its evidentiary weight.
- **Source labels.** Anything that could only be found on an aggregator (Crunchbase, Tracxn, and friends) is marked as aggregator-derived. Vendor-claimed numbers are labeled with why they can't be independently verified — rounded magnitudes and suspiciously precise percentages both get flagged.
- **The appendix (§23).** Every dossier ends with its own methodology: what was cross-validated, what decayed, and a composite confidence score. If a dossier is old, the freshness-decay section tells you which parts to re-pull rather than making you redo everything.

If the skill can't verify something, it says so instead of filling the gap — that's the design, not a limitation.

## Steering how hard it verifies

`--agents=solo|validation|parallel|max` controls how much independent re-verification you buy: `solo` is one pass, `validation` adds a checking agent, `parallel` fans out per-section, `max` is everything at once. `--source-rating=admiralty` additionally grades every source on the two-axis [Admiralty scale](https://en.wikipedia.org/wiki/Admiralty_code) (reliability A–F, credibility 1–6).

## The full flag reference

Everything above is a curated subset. The complete argument list — including `--framework=` analytic frameworks, `--publish=` destinations, output paths, and the `--no-*` toggles — lives in the frontmatter of [`SKILL.md`](../skills/research-entity/SKILL.md).
