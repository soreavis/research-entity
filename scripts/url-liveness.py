#!/usr/bin/env python3
"""Source-URL liveness sweep for the research-entity skill.

Stdlib-only (no deps): extracts every https?:// URL from skills/**/*.md,
checks each with a browser User-Agent, and classifies with a bot-wall-aware
taxonomy — a 403 from a datacenter IP is "blocked, likely valid", never dead.

Exit code is always 0: a dead external site is maintenance work, not a broken
build. The workflow turns the report into a GitHub issue instead.

Usage:
    python3 scripts/url-liveness.py            # full sweep, report to stdout
    python3 scripts/url-liveness.py --max 40   # spot-check the first N URLs
    python3 scripts/url-liveness.py --json     # machine-readable results
"""

import argparse
import concurrent.futures
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
BLOCKED_CODES = {401, 403, 406, 409, 419, 429, 999}
# RFC 2606 / RFC 6761 reserved names — documentation placeholders, never checked.
PLACEHOLDER = re.compile(r"(^|\.)(example\.(com|org|net)|example|test|invalid|localhost)$")


def extract_urls():
    urls = set()
    for f in (ROOT / "skills").rglob("*.md"):
        for m in re.finditer(r"https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9._/?=&%~+#-]*)?", f.read_text()):
            url = m.group(0).rstrip('.,;)"')
            host = urlparse(url).netloc
            if "." in host and not PLACEHOLDER.search(host):
                urls.add(url)
    return sorted(urls)


def check(url):
    # api.* hosts are documented endpoint patterns, not fetchable pages — a GET
    # without auth/body legitimately returns 4xx, so checking them is pure noise.
    if urlparse(url).netloc.startswith("api."):
        return url, "API_ENDPOINT_SKIPPED", 0
    # curl rather than urllib: some government and vendor sites reject
    # non-browser TLS fingerprints outright, which urllib misreports as dead.
    try:
        proc = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L",
             "--max-time", "15", "-A", UA, url],
            capture_output=True, text=True, timeout=25,
        )
        code = int(proc.stdout.strip() or 0)
    except Exception:
        code = 0
    if code == 0:
        return url, "UNREACHABLE", 0
    if 200 <= code < 400:
        return url, "LIVE", code
    if code in BLOCKED_CODES:
        return url, "BLOCKED_LIKELY_VALID", code
    if code in (404, 410):
        return url, "DEAD", code
    return url, "ERROR", code


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=0, help="check only the first N URLs")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    urls = extract_urls()
    if args.max:
        urls = urls[: args.max]

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as ex:
        results = list(ex.map(check, urls))

    buckets = {}
    for url, status, code in results:
        buckets.setdefault(status, []).append((url, code))

    if args.json:
        json.dump(
            {s: [{"url": u, "http": c} for u, c in rows] for s, rows in buckets.items()},
            sys.stdout, indent=1,
        )
        return

    print(f"# URL liveness — {len(urls)} URLs checked\n")
    for status in ("DEAD", "UNREACHABLE", "ERROR", "BLOCKED_LIKELY_VALID", "API_ENDPOINT_SKIPPED", "LIVE"):
        rows = buckets.get(status, [])
        print(f"## {status}: {len(rows)}")
        if status != "LIVE":
            for url, code in sorted(rows):
                print(f"- `{code}` {url}")
        print()
    actionable = len(buckets.get("DEAD", [])) + len(buckets.get("UNREACHABLE", [])) + len(buckets.get("ERROR", []))
    print(f"Actionable (dead + unreachable + error): {actionable}")


if __name__ == "__main__":
    main()
