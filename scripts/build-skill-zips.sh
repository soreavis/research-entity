#!/usr/bin/env bash
# Build one zip per skill for runtimes that take skill folders rather than a plugin
# (claude.ai Customize → Skills, ChatGPT Skills → Upload).
#
# The zip root must be the skill folder itself, and that folder name must equal the
# SKILL.md `name` field, or the upload is rejected.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills="$root/skills"
dist="$root/dist"
rm -rf "$dist"
mkdir -p "$dist"

for skill in "$skills"/*/; do
  name="$(basename "$skill")"
  staging="$(mktemp -d)"
  cp -R "$skill" "$staging/$name"

  # Two dist-only rewrites of SKILL.md frontmatter:
  # 1. user-invocable and argument-hint are Claude Code extensions, not part of the
  #    open Agent Skills spec — the claude.ai uploader rejects unknown fields.
  # 2. The claude.ai uploader caps `description` at ~200 chars (stricter than the
  #    spec's 1024), so the dist copy gets a short description while the repo
  #    skill keeps its rich one.
  python3 - "$staging/$name/SKILL.md" <<'PY'
import sys

SHORT = ("Board-ready competitive-intelligence and due-diligence dossiers on any "
         "company - 23 sections, cross-validated public sources, red-flag scan, "
         "confidence scoring, HTML/PDF export.")
assert len(SHORT) <= 200, f"short description is {len(SHORT)} chars"

path = sys.argv[1]
out, in_fm = [], False
for line in open(path):
    if line.rstrip() == '---':
        in_fm = not in_fm
        out.append(line)
        continue
    if in_fm:
        if line.startswith(('user-invocable:', 'argument-hint:')):
            continue
        if line.startswith('description:'):
            out.append(f'description: {SHORT}\n')
            continue
    out.append(line)
open(path, 'w').writelines(out)
PY

  # -x keeps macOS/editor droppings out of a published artifact.
  (cd "$staging" && zip -qr "$dist/$name.zip" "$name" \
    -x '*/.DS_Store' '*/__pycache__/*' '*/.git/*' '*.bak-*')
  rm -rf "$staging"
  echo "dist/$name.zip  ($(du -h "$dist/$name.zip" | cut -f1))"
done
