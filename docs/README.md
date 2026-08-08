# Documentation index

Guides for **research-entity**. The [root README](../README.md) is the overview; these pages go deeper on one thing at a time.

## Getting started

- **[Install](./install.md)** — every install lane (Claude Code, Codex, Cursor, Gemini CLI, Copilot, Grok, ChatGPT, Claude web), the manual symlink for development, and how to verify it worked
- **[Usage](./usage.md)** — your first dossier, the wizard, worked examples, and how to read what comes back
- **[How it works](./how-it-works.md)** — the modular skill tree, the trust machinery, and how one repo installs everywhere
- **[For contributors](./for-contributors.md)** — dev setup, the CI gates, source-health maintenance, and the PR workflow

## Project documentation (at repo root)

| File | What it covers |
|---|---|
| [README.md](../README.md) | Overview, install matrix, usage, badges |
| [AGENTS.md](../AGENTS.md) | Maintenance guidance for AI agents working on this repo, incl. the release checklist |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | Ground rules — source-or-silence, spec limits, modularity |
| [SECURITY.md](../SECURITY.md) | What to report privately vs publicly, disclosure timeline |
| [CHANGELOG.md](../CHANGELOG.md) | CalVer release history |
| [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) | Contributor Covenant |

## Skill internals

The skill itself lives in [`skills/research-entity/`](../skills/research-entity/) — [`SKILL.md`](../skills/research-entity/SKILL.md) is the entrypoint and documents which segment file loads when.
