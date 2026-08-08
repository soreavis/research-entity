# Installation

`research-entity` is one skill tree with a thin manifest per platform, so you install it with whatever plugin or skill manager your agent already has. Pick your lane below — they all end in the same place: a `/research-entity` command (or equivalent) in your agent.

## Prerequisites

- macOS, Linux, or WSL
- One of the agent runtimes below
- Git — only for the manual symlink lane

## Claude Code

```
/plugin marketplace add soreavis/research-entity
/plugin install research-entity@research-entity
```

That's it — `/research-entity` now works in any session. Updates arrive when a new version is published, not on every commit. Third-party marketplaces have auto-update **off** by default; to turn it on: run `/plugin`, open the **Marketplaces** tab, select **research-entity**, choose **Enable auto-update**.

## Claude web / Desktop / Cowork

On paid plans: **Customize → Plugins → + → Add marketplace**, then paste `https://github.com/soreavis/research-entity`. Updates follow the marketplace automatically.

Alternatively, upload the skill zip directly under **Customize → Skills** — see [Building the zip](#building-the-zip) below.

## Codex

```
codex plugin marketplace add soreavis/research-entity
codex plugin add research-entity@research-entity
```

Update later with `codex plugin marketplace upgrade`.

## Cursor

```
npx skills add soreavis/research-entity -a cursor
```

Update with `npx skills update`.

## Gemini CLI

```
gemini extensions install https://github.com/soreavis/research-entity
```

Update with `gemini extensions update research-entity`.

## Copilot / GitHub CLI

```
gh skill install soreavis/research-entity research-entity
```

Update with `gh skill update research-entity`. Note `gh skill` is in preview — its flags may change.

## Grok

```
grok plugin marketplace add soreavis/research-entity
grok plugin install soreavis/research-entity --trust
```

Update with `grok plugin update research-entity`.

## ChatGPT

ChatGPT takes a zip upload rather than a repo reference: **Skills → Create → Upload from your computer**, then pick `research-entity.zip` — grab it from the latest release (once one exists), from the `skill-zips` artifact on any [CI run](https://github.com/soreavis/research-entity/actions), or build it yourself:

## Building the zip

```bash
# Build the distributable zip
bash scripts/build-skill-zips.sh

# → dist/research-entity.zip
```

The script stages the skill folder and makes two dist-only adjustments: it strips `user-invocable` and `argument-hint` (Claude Code extensions the uploaders reject as unknown fields) and swaps in a short `description` (the claude.ai uploader caps it at ~200 characters, stricter than the open spec's 1024). The repo copy of the skill is never touched.

## Any other Agent Skills runtime

```
npx skills add soreavis/research-entity
```

## Manual symlink (development)

If you want to hack on the skill and see edits immediately, symlink the **skill subdirectory** (not the repo root — the runtime expects `SKILL.md` at the symlink's root):

```bash
# Clone, then symlink the skill subdirectory so edits apply immediately
git clone https://github.com/soreavis/research-entity ~/code/research-entity
ln -s ~/code/research-entity/skills/research-entity ~/.claude/skills/research-entity
```

## Verify

Type `/res` in a session — `/research-entity` should appear in the command picker. Or run a worked example:

```
/research-entity "Stripe" --depth=quick
```

If the command isn't recognised:

- **Plugin lane**: confirm it loaded with `/plugin list` (or your runtime's equivalent)
- **Symlink lane**: confirm the link resolves — `readlink ~/.claude/skills/research-entity` should print a path ending in `skills/research-entity`

## For a team or a repo

Add this to a project's `.claude/settings.json` and everyone who trusts the folder is prompted to install it:

```json
{
  "extraKnownMarketplaces": {
    "research-entity": {
      "source": { "source": "github", "repo": "soreavis/research-entity" }
    }
  },
  "enabledPlugins": {
    "research-entity@research-entity": true
  }
}
```
