#!/usr/bin/env python3
"""Repo gates — single source of truth for CI and the pre-push hook.

Each gate is a function; CI runs them as separate jobs (`checks.py spec`),
the pre-push hook runs them all (`checks.py all`). Keeping one implementation
means local green and CI green are the same thing.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", "_local", "dist"}

# Identities scrubbed from the anonymized production cases (see AGENTS.md).
# Stored as hashes so this guard never republishes what it exists to forbid.
BANNED_TERMS = {
    "b735ff34e057ce0c4db091dc55c9402c", "493fd30fffc3130f9b36668e9e20afed",
    "d88280d4f5eae95da39f7809885aa5b2", "75b0054be5a90f54347c252fe755be65",
    "fa9aee55ce83a967d667507f27fdfbae", "0a1cb13114e9b3d2a67c7a917f655af8",
    "2638b28d9d8fea1d94d277ae276e9953",
}

# Session-transcript provenance: describe the pattern, never the exchange.
PROVENANCE = [
    (r"\bthe user (pushed back|said|asked me|complained|wrote|replied)\b",
     "quotes the session transcript — state the pattern, not the exchange"),
    (r"\b(my|our) (employer|client|company)\b", "first-person employer/client reference"),
]

# Generic ("non-provider") secret shapes: private keys, credentialed connection
# strings, auth headers, long assigned literals. GitHub scans provider tokens on
# public repos for free, but generic-pattern scanning needs an org-owned repo on
# Team+ with Secret Protection — so this repo cannot have it, and gates it here.
SECRETS = [
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key block"),
    (r"[a-z][a-z0-9+.\-]*://[^/\s:@]+:[^/\s:@]+@", "credentialed connection string"),
    (r"(?i)authorization\s*:\s*(bearer|basic)\s+[A-Za-z0-9._~+/=\-]{16,}", "auth header with credential"),
    (r"(?i)\b(api[_-]?key|secret|token|password|passwd|credential)s?\b\W{0,3}[:=]\s*"
     r"[\"'][A-Za-z0-9/+_.\-]{16,}[\"']", "assigned credential literal"),
]

MANIFESTS = [
    ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json",
    ".codex-plugin/plugin.json", ".cursor-plugin/plugin.json",
    ".grok-plugin/plugin.json", ".grok-plugin/marketplace.json",
    ".agents/plugins/marketplace.json", "gemini-extension.json",
]


def fail(msg):
    print(f"FAIL {msg}")
    return True


def spec():
    """SKILL.md frontmatter meets the Agent Skills spec (over-cap = silent drop)."""
    import yaml
    failed = False
    for f in ROOT.rglob("SKILL.md"):
        if SKIP_DIRS & set(f.parts):
            continue
        fm = yaml.safe_load(re.match(r"^---\n(.*?)\n---", f.read_text(), re.S).group(1))
        d, n = fm.get("description", ""), fm.get("name", "")
        bad = [m for m, c in (
            ("desc>1024", len(d) > 1024),
            ("desc-empty", not d),
            ("name!=folder", n != f.parent.name),
            ("name-bad-chars", not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", str(n))),
            ("angle-brackets", any(ch in f"{n}{d}" for ch in "<>")),
        ) if c]
        print(("FAIL " if bad else "ok   ") + f"{f.relative_to(ROOT)} desc={len(d)} " + " ".join(bad))
        failed |= bool(bad)
    return failed


def manifests():
    """All 8 platform manifests and the README badge carry one version."""
    versions = set()
    for m in MANIFESTS:
        data = json.loads((ROOT / m).read_text())
        if "version" in data:
            versions.add(data["version"])
        for p in data.get("plugins", []):
            versions.add(p["version"])
        print(f"ok   {m}")
    badge = re.search(r"label=version&message=([0-9.]+)", (ROOT / "README.md").read_text())
    if not badge:
        return fail("README version badge not found")
    versions.add(badge.group(1))
    if len(versions) != 1:
        return fail(f"version drift across manifests/badge: {sorted(versions)}")
    print(f"version: {versions.pop()} (8 manifests + README badge in lockstep)")
    return False


def links():
    """Relative markdown links resolve. skills/ is excluded (template pseudo-links)."""
    failed = False
    for f in ROOT.rglob("*.md"):
        if (SKIP_DIRS | {"skills"}) & set(f.parts):
            continue
        in_fence = False
        for i, line in enumerate(f.read_text().splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            line = re.sub(r"`[^`]*`", "", line)  # inline code may show pseudo-links
            for target in re.findall(r"\]\(([^)\s]+)\)", line):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                if not (f.parent / target.split("#")[0]).resolve().exists():
                    failed = fail(f"{f.relative_to(ROOT)}:{i} broken relative link: {target}")
    if not failed:
        print("links ok")
    return failed


def drift():
    """Every dimension flag in SKILL.md argument-hint is mentioned in the README."""
    content = (ROOT / "skills/research-entity/SKILL.md").read_text()
    m = re.search(r'argument-hint:\s*"([^"]+)"', content)
    if not m:
        print("warn: could not parse argument-hint")
        return False
    flags = set(re.findall(r"--([a-z][a-z0-9-]*)", m.group(1)))
    control_only = {
        "about", "validate-skill-sources", "url", "analytic-rigor",
        "output", "publish", "mcp-serve", "language", "dry-run",
        "no-reddit", "no-competitors", "no-glossary", "no-risk-scan",
    }
    readme = (ROOT / "README.md").read_text()
    missing = [fl for fl in sorted(flags - control_only) if f"--{fl}" not in readme]
    for fl in sorted(flags - control_only):
        print(f"  {'✗' if fl in missing else '✓'} --{fl}")
    if missing:
        return fail(f"argument-hint drift: {missing} in SKILL.md but not README.md")
    print("all dimension flags documented in README")
    return False


def _tokens(line):
    """Normalized 1- and 2-grams, for matching against BANNED_TERMS hashes."""
    words = [w.rstrip(".-") for w in
             re.findall(r"[a-z][a-z.\-]*", line.replace("&", " ").lower())]
    for i, w in enumerate(words):
        yield w
        if i + 1 < len(words):
            yield f"{w} {words[i + 1]}"


def hygiene():
    """No user-specific paths, real emails, scrubbed identities, or transcript quotes."""
    failed = False
    email = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}")
    allowed = re.compile(r"example\.(com|org)$|users\.noreply\.github\.com$")
    for f in ROOT.rglob("*"):
        if (SKIP_DIRS | {".github"}) & set(f.parts) or f.suffix not in (".md", ".json", ".sh"):
            continue
        if f.name == "checks.py":
            continue
        for i, line in enumerate(f.read_text(errors="ignore").splitlines(), 1):
            where = f"{f.relative_to(ROOT)}:{i}"
            if "/Users/" in line:
                failed = fail(f"{where} user-specific absolute path — use ~/")
            for m in email.finditer(line):
                if not allowed.search(m.group(0)):
                    failed = fail(f"{where} non-placeholder email: {m.group(0)}")
            for tok in _tokens(line):
                if hashlib.sha256(tok.encode()).hexdigest()[:32] in BANNED_TERMS:
                    failed = fail(f"{where} scrubbed identity reintroduced — anonymize it")
            for pattern, why in PROVENANCE:
                if re.search(pattern, line, re.I):
                    failed = fail(f"{where} {why}")
            for pattern, why in SECRETS:
                if re.search(pattern, line):
                    failed = fail(f"{where} {why} — never commit a live credential")
    if not failed:
        print("hygiene clean")
    return failed


GATES = {"spec": spec, "manifests": manifests, "links": links, "drift": drift, "hygiene": hygiene}


def main():
    names = sys.argv[1:] or ["all"]
    run = list(GATES) if names == ["all"] else names
    failed = False
    for name in run:
        print(f"== {name}")
        failed |= GATES[name]()
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
