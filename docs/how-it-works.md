# How it works

## One entrypoint, many segments

The skill is a single [`SKILL.md`](../skills/research-entity/SKILL.md) that acts as a router. It defines the workflow and the arguments, and delegates everything heavy to segment files that load **only when needed**:

- Ask for a German company and `registers.md` loads — the catalog of business registers, court records, and filing sources beyond the US.
- Ask for `--export=pdf` and `exports.md` loads with the render pipeline.
- Write §11 Community Reception and `reviews-platforms.md` loads with per-platform guidance on what review counts actually mean.
- Go `--depth=deep` on a security vendor and `osint-public.md` brings in job-posting velocity, DNS/certificate transparency, MITRE ATT&CK, and trademark search.

This keeps any single context load small while the skill's total reference base stays large. The full load-condition table is at the top of `SKILL.md`.

## The trust machinery

The skill assumes the model *will* hallucinate if allowed to, and builds the workflow so it can't do so quietly:

- **Cross-validation.** Every datapoint is checked against multiple independent public sources. Data only an aggregator can supply is labeled aggregator-derived, never laundered into fact.
- **Source-or-silence.** A claim without a source doesn't ship. Gaps are stated as gaps.
- **Load-bearing claim rule.** Any claim repeated across three or more sections must trace to at least two independent sources — repetition is not corroboration.
- **Vendor-metric labeling.** Round numbers ("40,000+ users") and suspicious precision ("96.4% satisfaction") get an explicit "methodology not disclosed" label.
- **Competitor-row verification.** Before a market-positioning section ships, lead investors, HQ cities, and round structures in competitor tables are re-verified against primary sources — the exact cells that most often go wrong.
- **The lessons file.** `lessons.md` is a numbered catalog of real failure modes caught in production, each with the rule that prevents it. The draft is reviewed against it before shipping.
- **Confidence decay.** Dossiers age. The §23 appendix scores freshness per source category, and a re-run knows which sections are past their TTL.

## One repo, every agent

The skill tree in `skills/research-entity/` is the single source of truth. Around it sit thin manifests, one per platform — `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`, `.grok-plugin/`, `.agents/plugins/`, `gemini-extension.json` — all carrying the same name, version, and description. CI fails if any of them drifts.

Two runtimes (claude.ai, ChatGPT) take zip uploads instead of repo references. [`scripts/build-skill-zips.sh`](../scripts/build-skill-zips.sh) builds `dist/research-entity.zip` for those, stripping the two Claude-only frontmatter fields and shortening the description to the uploader's stricter cap — dist-only changes; the repo skill keeps its rich metadata.

The gates that keep all of this honest run in CI — see [For contributors](./for-contributors.md#what-runs-in-ci).
