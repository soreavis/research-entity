#!/usr/bin/env bash
# Run every repo gate locally — the same implementations CI runs.
# Wire it as a pre-push hook once: git config core.hooksPath .githooks
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

echo "== markdownlint"
npx --yes markdownlint-cli2 "**/*.md" "!node_modules"

python3 scripts/checks.py all

echo "== zips build"
bash scripts/build-skill-zips.sh

echo "ALL GATES GREEN"
