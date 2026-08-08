# For contributors

How to work on this repo without tripping over its gates. The short ground rules live in [CONTRIBUTING.md](../CONTRIBUTING.md); this page is the practical companion. If you're an AI agent maintaining the repo, start at [AGENTS.md](../AGENTS.md) instead.

## Dev setup

```bash
# Clone, then symlink the skill subdirectory — not the repo root
git clone https://github.com/soreavis/research-entity ~/code/research-entity
ln -s ~/code/research-entity/skills/research-entity ~/.claude/skills/research-entity
```

The symlink makes your working copy the live skill — edits are picked up immediately, no reinstall loop.

## Repo layout

```
skills/research-entity/   the skill: SKILL.md router + on-demand segment files
docs/                     end-user guides (this folder)
scripts/                  build-skill-zips.sh (dist), url-liveness.py (source health)
.github/workflows/        CI — see below
.claude-plugin/ etc.      one thin manifest per platform; version in lockstep
```

## Run the checks locally before pushing

```bash
# Every CI gate, the same implementation CI runs
bash scripts/check.sh          # every CI gate, same implementation CI runs
```

Better: make git refuse to push anything CI would reject —

```bash
# Make git refuse to push anything CI would reject
git config core.hooksPath .githooks
```

The gates live in `scripts/checks.py` and CI calls the very same file, so local green and CI green cannot drift apart. (`python3 scripts/url-liveness.py --max 40` spot-checks source URLs; it's scheduled, not a push gate.)

## What runs in CI

Every push and PR runs (`.github/workflows/ci.yml`):

- **Agent Skills spec measurement** — an over-limit description doesn't warn; the skill silently vanishes from the loader
- **markdownlint**
- **manifest JSON + version lockstep** — all 8 platform manifests plus the README badge must agree
- **relative-link check** — repo navigation only; skill segment files are excluded because they contain template pseudo-links like `[Source](url)`
- **argument-hint ↔ README drift** — a flag nobody documents is a feature nobody finds
- **hygiene guard** — no user-specific absolute paths, no private email addresses
- **upload-zip build** — `dist/research-entity.zip` attached as a CI artifact

PRs additionally require a CHANGELOG entry under `[Unreleased]` unless labeled trivial (`skip changelog`, `documentation`, `ci`, `dependencies`).

On a schedule (not on PRs — external sites are slow and flaky):

- **URL liveness** (`url-liveness.yml`, monthly + manual dispatch) — sweeps every `https://` URL in the skill files with a bot-wall-aware classifier and files/updates a report issue when something looks dead. It never turns the repo red: a dead external site is maintenance work, not a broken build.

## Keeping the sources trustworthy

The CI sweep is only the deterministic half. The semantic half — "does this register still serve what the skill claims?" — is the skill's own maintenance mode:

```
/research-entity --validate-skill-sources
```

Run it monthly (or before a release). It cross-references `sources-of-record.md`, flags stale verifications and registry drift, and prints a remediation plan without touching any files.

## Making changes

1. Branch from `main` (`fix/…` or `feature/…`), one logical change per PR.
2. Every new factual claim needs a primary-source URL — source-or-silence.
3. New reference content goes in a segment file with a load condition documented in the `SKILL.md` structure table, not inline in `SKILL.md`.
4. Add a line under `[Unreleased]` in `CHANGELOG.md` — or label the PR if it's genuinely trivial.
5. Match the voice: read `voice-and-style.md` before writing dossier-template prose.

## Versioning

CalVer (`YYYY.0M.MICRO`). When bumping: change all 8 manifests **and** the README version badge together — CI fails on drift. There is no release automation yet, so lockstep is manual.
