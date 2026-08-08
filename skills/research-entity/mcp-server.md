# Self-MCP Server — Expose Past Dossiers as MCP

Loaded by the `research-entity` skill when the user asks "expose dossiers as MCP" or runs `--mcp-serve`. Lets future Claude / Cursor / IDE sessions query the user's accumulated dossier library through MCP — semantic search, dossier-by-name lookup, structured-field extraction.

## Why this exists

After running the skill on dozens of entities, the user has a corpus of structured intel. Without MCP, that corpus is local files. With MCP, any future Claude conversation can ask: "what do I know about Acme Corp?" / "list all dossiers in the fintech vertical I've researched" / "summarize all my dossiers from Q1 2026" without re-running research.

## Architecture

A small TypeScript / Python MCP server that:

1. Indexes `~/.claude/dossiers/` (or user-configured directory) by:
   - Entity name (slug)
   - Vertical (parsed from `--vertical` flag in front matter)
   - Stage (parsed from `--stage` flag)
   - Date (research_date front matter)
   - Composite confidence (parsed from §23)
2. Exposes MCP tools:
   - `list_dossiers` — returns array of {entity, vertical, stage, date, confidence, path}
   - `get_dossier(entity)` — returns full MD content
   - `search_dossiers(query)` — semantic search across §0 BLUF + Scorecard rows
   - `get_field(entity, field)` — extract structured field (e.g., "founders", "funding", "competitors")
   - `compare_dossiers(entity_a, entity_b)` — invoke comparison-mode logic
3. Optionally runs as `npx @user/research-mcp` or as Docker container

## Setup

```bash
# Install
npm install -g @user/research-entity-mcp

# Initialize
research-entity-mcp init --dossier-dir=~/.claude/dossiers

# Add to Claude Desktop config (~/Library/Application Support/Claude/claude_desktop_config.json):
```

```json
{
  "mcpServers": {
    "research-entity": {
      "command": "npx",
      "args": ["-y", "@user/research-entity-mcp"],
      "env": {
        "DOSSIER_DIR": "~/.claude/dossiers"
      }
    }
  }
}
```

For Claude Code projects, add to `.mcp.json`:

```json
{
  "mcpServers": {
    "research-entity": {
      "command": "research-entity-mcp",
      "args": ["serve", "--dossier-dir=~/.claude/dossiers"]
    }
  }
}
```

## Tool surface

### `list_dossiers`

Returns all dossiers with metadata:

```json
[
  {
    "entity": "acme-corp",
    "name": "Acme Corp",
    "vertical": "fintech",
    "stage": "series-b",
    "research_date": "2026-04-27",
    "composite_confidence": 87,
    "path": "~/research/acme-corp-research.md",
    "size_lines": 1542
  }
]
```

Filters: `?vertical=fintech&stage=series-b&min_confidence=80&since=2026-01-01`

### `get_dossier(entity, sections?)`

Returns full MD or specified sections:

```
get_dossier("acme-corp", sections=["§0", "§16", "§23"])
```

### `search_dossiers(query, mode="semantic")`

Modes:
- `semantic` — embeddings-based (requires OpenAI / local embedder)
- `keyword` — grep-based, no embedding dep

Returns matches with snippet + path:
```json
[
  {"entity": "acme-corp", "snippet": "...AI-native CRM with proprietary data graph...", "path": "...", "match_score": 0.89}
]
```

### `get_field(entity, field)`

Extract structured field via the JSON export schema:
```
get_field("acme-corp", "founders")  # returns array of {name, linkedin, role, prior}
get_field("acme-corp", "competitors")  # returns array of competitor names + tier + url
get_field("acme-corp", "risk_scan.composite")  # returns "Medium"
get_field("acme-corp", "compliance.soc2.type")  # returns "II"
```

### `compare_dossiers(a, b, mode="side-by-side"|"yoy")`

Invokes comparison-mode logic; returns the comparison MD inline.

### `freshness(entity?)`

Checks staleness (load `stale-detection.md` logic):
```json
[
  {"entity": "acme-corp", "age_days": 60, "decay": -3, "current_confidence": 84, "recommendation": "fresh"}
]
```

## Reference implementation skeleton

```typescript
// research-entity-mcp/src/index.ts
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import * as fs from "fs/promises";
import * as path from "path";

const DOSSIER_DIR = process.env.DOSSIER_DIR || `${process.env.HOME}/.claude/dossiers`;

const server = new Server({
  name: "research-entity",
  version: "1.0.0"
}, {
  capabilities: { tools: {} }
});

server.setRequestHandler("tools/list", async () => ({
  tools: [
    { name: "list_dossiers", description: "..." },
    { name: "get_dossier", description: "..." },
    { name: "search_dossiers", description: "..." },
    { name: "get_field", description: "..." },
    { name: "compare_dossiers", description: "..." },
    { name: "freshness", description: "..." }
  ]
}));

server.setRequestHandler("tools/call", async (req) => {
  const { name, arguments: args } = req.params;
  switch (name) {
    case "list_dossiers": return { content: await listDossiers(args) };
    case "get_dossier": return { content: await getDossier(args.entity) };
    case "search_dossiers": return { content: await search(args.query) };
    case "get_field": return { content: await getField(args.entity, args.field) };
    case "compare_dossiers": return { content: await compare(args.a, args.b, args.mode) };
    case "freshness": return { content: await checkFreshness(args.entity) };
  }
});

async function listDossiers(filters: any) {
  const files = await fs.readdir(DOSSIER_DIR);
  const results = await Promise.all(
    files.filter(f => f.endsWith(".md")).map(async (f) => {
      const content = await fs.readFile(path.join(DOSSIER_DIR, f), "utf-8");
      const fm = parseFrontMatter(content);
      return { ...fm, path: path.join(DOSSIER_DIR, f) };
    })
  );
  return applyFilters(results, filters);
}
// ... rest of implementations

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Future Claude conversation example

```
User: "I'm meeting with Acme Corp tomorrow. Refresh my memory on what I know."

Claude (with MCP): 
[invoking research-entity:get_dossier(entity="acme-corp", sections=["§0"])]

Acme Corp — last researched 2026-02-15, confidence 87/100, fintech series-b.

BLUF: ...
3 strengths: ...
3 risks: ...

Shall I check freshness or pull the full dossier?
```

## Distribution

Three options:

1. **Self-host** (default) — user runs `research-entity-mcp` locally; dossiers stay on their machine
2. **Internal team server** — host on internal network for team-wide dossier library; auth via API token
3. **Cloud-hosted** — defer; not recommended (dossiers contain competitive intel; cloud=leak risk)

## Security

- Dossiers may contain confidential research; the MCP server should be local-only by default
- If publishing as a npm package, default to `127.0.0.1`-only binding
- Add `?auth_token=` query param for any non-localhost access
- Never log query content (queries themselves can leak strategy)

## Anti-patterns

- ❌ Hosting MCP server publicly without auth (immediate competitive intel leak)
- ❌ Using cloud embeddings API to search dossiers without consent (may forward content to third party)
- ❌ Auto-executing `compare_dossiers` for very large dossiers (slow + token-expensive)
- ❌ Returning entire dossiers when a section would suffice (use `sections=[]` filter)
- ❌ Caching old `freshness()` results — always recompute on demand

## When to load this file

- User asks "expose as MCP" / "make this queryable" / "MCP server for my dossiers"
- User has 5+ dossiers in their library (worth the setup cost)
- User wants future Claude sessions to know about their corpus
