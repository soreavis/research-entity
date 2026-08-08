# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow CalVer (`YYYY.0M.MICRO`).

## [Unreleased]

### Changed

- Anonymized production cases in `lessons.md`, `internal-consistency.md` and `SKILL.md` no longer carry identity anchors. The cases kept their placeholder labels but retained real founder names, sibling brand names, the acquirer's law firm, and a metric fingerprint precise enough to reverse-search the subject in a single query. Identity anchors are stripped; the calibration figures are replaced with illustrative values that preserve each lesson's arithmetic and teaching point.
- Two lessons that framed their case around the requester's own employer are restated as general rules, and a verbatim session-transcript quote was removed.

### Added

- `hygiene` gate now blocks reintroduction of scrubbed identities (matched against a hashed denylist, so the guard never republishes what it forbids) and session-transcript quotes.

## [2026.08.1] - 2026-08-07

### Added

- `docs/for-contributors.md` — dev setup, local check commands, the CI gate list (moved out of how-it-works), source-health maintenance cadence
- `scripts/url-liveness.py` — stdlib-only monthly source sweep with bot-wall-aware taxonomy (curl-based; API endpoints and RFC 2606 placeholders excluded)
- `.github/workflows/url-liveness.yml` — scheduled sweep that files/updates a report issue instead of redding the repo
- Hero image, badges, and a restructured README with the multi-agent install matrix and a measured token-cost table (four production runs)
- Human-focused docs: `docs/install.md`, `docs/usage.md`, `docs/how-it-works.md`, and a docs index
- `AGENTS.md` maintenance guide (incl. going-public checklist) + `.claude/CLAUDE.md` import shim
- dist system: `scripts/build-skill-zips.sh` builds upload zips, stripping Claude-only frontmatter fields and shortening the description to the claude.ai uploader cap
- CI: upload-zip build artifact, relative-link check, argument-hint ↔ README drift gate, repo hygiene guard, README-badge version lockstep, changelog enforcer, Dependabot for actions
- `marketplace.json` metadata block and `strict` flag, matching the ai-docent marketplace pattern

### Fixed

- Source validation sweep (484 URLs; 10 Opus validators + adversarial verify): 34 sources repaired — 29 migrated URLs updated to verified new homes (USPTO Assignment Center / Patent Public Search / TM Search, Czech ARES, OFAC sanctions list, Luxembourg Legilux, CIA CSI paths, Battery, BVP, KeyBanc, ICONIQ, Forrester TEI, Qualtrics, NYU Stern, DHL, Databricks, Alberta, ADGM, AICPA, IAPP, e-Justice BRIS, Reuters Events, Saudi MC, Liechtenstein Handelsregister, India Protean, Morocco OMPIC) and 5 dead sources replaced with verified successors (Austrian WiEReG → BMF register page, Liechtenstein → llv.li, Dubai DED → DET, OpenView SaaS Benchmarks → High Alpha continuation, Sapphire benchmarks → Perspectives); 9 registry rows re-stamped

### Changed

- README and docs no longer state segment/line counts, so the prose can't drift from the tree
- Hero caption removed
- All CI gates consolidated into `scripts/checks.py`, shared by CI and the `.githooks/pre-push` hook (`git config core.hooksPath .githooks`) so local green and CI green cannot drift; link checker now ignores inline code spans
- Display name is now **The Dossier Machine** — README title, plugin `displayName`, and the GitHub About line; the skill/invocation name stays `research-entity`

## [2026.08.0] - 2026-08-07

### Added

- Initial public packaging of the `research-entity` skill: 23-section competitive-intelligence / due-diligence dossier generator with cross-validation, Admiralty source rating, confidence scoring, 8-pattern red-flag scan, mermaid render-validation, and HTML/PDF/battle-card/VC-memo export
- Modular skill tree: `SKILL.md` entrypoint + 43 on-demand segment files (registers, review platforms, OSINT layers, moat scoring, roadmap inference, expert-call batteries, stage and vertical templates, lessons)
- Plugin manifests for Claude Code, Codex, Cursor, Gemini CLI, and Grok
- CI: Agent Skills spec validation (frontmatter limits) + markdownlint
- Community files: README, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, LICENSE (MIT)
