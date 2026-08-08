# Contributing

Thanks for helping make Research Entity better. This repo ships only Markdown — there is no build step and no runtime code, which keeps contributing simple. For dev setup, the CI gates, and how to run them locally, see [docs/for-contributors.md](docs/for-contributors.md).

## What to contribute

- **Factual corrections** — a register URL that moved, a review platform that changed its access model, a data source that died. Open an issue with the **factual-correction** template, or a PR with the fix and a primary-source link.
- **New sources** — business registers, court records, OSINT layers, review platforms. Cite the primary source and note any access limits (paywall, rate limit, login wall).
- **New verticals / stage templates** — follow the structure of the existing files in `skills/research-entity/`.
- **Failure modes** — if the skill produced a wrong or ungrounded claim, that is a bug. File it; confirmed patterns get added to `lessons.md`.

## Ground rules

1. **Source-or-silence.** Every factual claim added to a segment file needs a citation to a primary source. No "commonly known" facts without a URL.
2. **Spec limits are hard limits.** `SKILL.md` frontmatter must pass the Agent Skills spec: `description` ≤ 1024 chars, `name` matches the folder, no angle brackets in either. CI measures this — a skill that fails the spec silently fails to load in conformant runtimes.
3. **Keep segments modular.** New reference content goes in a segment file with a load condition documented in the `SKILL.md` structure table — not inline in `SKILL.md`.
4. **Match the voice.** Read `voice-and-style.md` before writing dossier-template prose.

## Workflow

1. Fork, branch from `main` (`fix/…` or `feature/…`).
2. Make the change; run `markdownlint` locally if you have it (CI runs it either way).
3. Open a PR using conventional commit style in the title (`fix:`, `feat:`, `docs:`).
4. One change per PR — a source fix and a new vertical are two PRs.

## Code of conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md).
