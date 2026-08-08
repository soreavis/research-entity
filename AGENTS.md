# AGENTS.md

Guidance for AI agents working **on this repository**. (If you are looking for the skill itself, it lives in `skills/research-entity/` — this file is about maintaining it.)

## What this repo is

`research-entity` packages a competitive-intelligence / due-diligence dossier generator as an [Agent Skill](https://agentskills.io), distributed to every agent platform that can install a skill or plugin. One skill tree, many thin manifests.

```
skills/research-entity/SKILL.md   entrypoint — router, arguments, workflow
skills/research-entity/*.md       segment files; load on demand per the SKILL.md structure table
docs/                             end-user guides
scripts/build-skill-zips.sh       builds dist/ zips for upload-based runtimes (claude.ai, ChatGPT)
.claude/CLAUDE.md                 imports this file for Claude Code; not at the root, where a plugin ignores it
.claude-plugin/  .codex-plugin/  .cursor-plugin/  .grok-plugin/
.agents/plugins/  gemini-extension.json
```

## Rules

- **Version lives in lockstep across all 8 manifests and the README badge.** There is no release automation yet — when bumping, change every manifest and the badge together; CI's `manifests` job fails on drift.
- **The SKILL.md `description` must pass the Agent Skills spec** (≤1024 chars, no angle brackets, name equals folder). CI measures it. The claude.ai uploader is stricter (≤200) — `scripts/build-skill-zips.sh` swaps in a short description in the dist copy only, so the repo skill keeps its rich one.
- **`user-invocable` and `argument-hint` are Claude Code extensions**, not part of the open spec. They stay in the repo SKILL.md and are stripped from dist zips, where the uploader would reject them.
- **Keep segments modular.** New reference content goes in a segment file with a load condition documented in the SKILL.md structure table — not inline in SKILL.md.
- **No personal, employer, or client names** anywhere in the skill. Production-case lessons keep their calibration data (figures, dates) but anonymize the researched entity — and anonymization means *unsearchable*, not just relabelled. A case called "Acme CRM" still leaks if it keeps the real founder names, sibling brands, law firm, or a metric fingerprint precise enough to reverse-search. Strip the identity anchors; keep the pattern. CI's `hygiene` gate enforces this against a hashed denylist (hashed, so the guard never republishes what it forbids) and blocks session-transcript quotes.
- **Every factual claim in a segment file cites a primary source.** Source-or-silence; see CONTRIBUTING.md.
- **Run the CI checks locally before committing**: the spec measurement, `npx --yes markdownlint-cli2 "**/*.md" "!node_modules"`, and `bash scripts/build-skill-zips.sh`.

## Going-public checklist

The repo is private. When flipping it public, in this order — each later step is impossible while private:

1. Flip the repo public (`gh repo edit soreavis/research-entity --visibility public`).
2. Upload `docs/assets/hero.jpg` under Settings → General → Social preview. There is no API for this, and the section does not appear on a private repo.
3. Enable private vulnerability reporting — a public-repo-only feature that SECURITY.md's primary link depends on.
4. Smoke-test the install lanes in the README table — none can fetch a private repo, so nothing is functionally proven until then.
5. Cut a release and attach the dist zips, so the ChatGPT lane has a stable download.
