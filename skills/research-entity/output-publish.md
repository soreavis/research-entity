# Direct Publish — `--publish=notion|confluence|gdocs|coda`

Loaded by the `research-entity` skill at Step 7 (Export) when `--publish=` is set. Pushes the dossier directly to a collaborative platform instead of (or in addition to) writing local files.

This is for teams that want the dossier discoverable / commentable / linkable without a "share this MD" step.

## Supported destinations

| Destination | Auth env var | Setup | Limitations |
|---|---|---|---|
| Notion | `NOTION_TOKEN` + `NOTION_PARENT_PAGE_ID` | Create internal integration; share parent page with integration | Mermaid → image only; no live render |
| Confluence | `CONFLUENCE_BASE_URL` + `CONFLUENCE_TOKEN` + `CONFLUENCE_SPACE_KEY` | Generate API token; pick space | Markdown-flavored storage format; mermaid via macros |
| Google Docs | `GOOGLE_SERVICE_ACCOUNT_JSON` + `GDOCS_PARENT_FOLDER_ID` | OAuth or service account; share folder with service account | Tables OK; mermaid → image |
| Coda | `CODA_API_TOKEN` + `CODA_DOC_ID` | Generate API token | Tables become Coda tables; mermaid → image |

## Authentication setup

The skill does NOT store credentials. User must export env vars before running:

```bash
# Notion
export NOTION_TOKEN="secret_..."
export NOTION_PARENT_PAGE_ID="abc123..."

# Confluence
export CONFLUENCE_BASE_URL="https://yourcompany.atlassian.net/wiki"
export CONFLUENCE_TOKEN="api_token_..."
export CONFLUENCE_SPACE_KEY="RES"

# Google Docs (service account)
export GOOGLE_SERVICE_ACCOUNT_JSON="$(cat ~/.config/gcloud/service-account.json)"
export GDOCS_PARENT_FOLDER_ID="folder-id-..."

# Coda
export CODA_API_TOKEN="..."
export CODA_DOC_ID="..."
```

If env vars not set, the skill prompts: "Notion publish requested but `NOTION_TOKEN` not set in environment. Set it and re-run, or use `--publish=skip` to fall back to local file."

## Workflow per destination

### Notion

```bash
# 1. Convert MD to Notion blocks (use martian or similar converter)
npx @tryfabric/martian < "$DOSSIER_MD" > /tmp/notion-blocks.json

# 2. POST to Notion API
curl -X POST https://api.notion.com/v1/pages \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d @/tmp/notion-payload.json

# Returns the new page URL
```

**Notion-specific gotchas:**
- Block type limits: ≤2000 chars per text block; ≤100 children per parent
- Mermaid → not natively supported; convert to PNG via mmdc and upload as image
- Tables → Notion tables (limited columns); for very wide tables (comparison mode), output a JSON-as-code-block alternative
- Long URLs in Inline links break Notion's URL parser; use rich-text link formatting

**Notion publish prompt back to user:**
> "Published to Notion: [Acme Corp Research](https://notion.so/...). 23 sections, 8 mermaid diagrams (rendered as images), 73 sources. Estimated read time: 14 min."

### Confluence

```bash
# 1. Convert MD to Confluence storage format (XHTML-like)
pandoc "$DOSSIER_MD" -t docbook5 | xsltproc - confluence.xsl > /tmp/confluence-body.xml

# 2. POST to Confluence REST API
curl -X POST "$CONFLUENCE_BASE_URL/rest/api/content" \
  -H "Authorization: Bearer $CONFLUENCE_TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/confluence-payload.json
```

**Confluence-specific gotchas:**
- Mermaid → use Confluence's native mermaid macro: `<ac:structured-macro ac:name="mermaid">...`
- Tables → wide tables OK; Confluence renders horizontal scroll
- Long pages (1500+ lines) auto-collapse; offer to split by section into a parent page + N child pages
- ScrollViewport / Refined Themes vendors may add custom rendering rules

**Confluence publish prompt:**
> "Published to Confluence space `RES`: [Acme Corp Research](https://yourcompany.atlassian.net/wiki/spaces/RES/pages/...). Page id: 12345. Use `--publish=confluence --update` to update on next run."

### Google Docs

```bash
# Use Google Docs API via Python (or curl + service-account-flow)
python3 -m research_entity.publish_gdocs \
  --md "$DOSSIER_MD" \
  --folder "$GDOCS_PARENT_FOLDER_ID" \
  --service-account "$GOOGLE_SERVICE_ACCOUNT_JSON"
```

**Google Docs-specific gotchas:**
- Mermaid → render to PNG and insert via `Document.batchUpdate` with `InsertInlineImageRequest`
- Tables → Docs tables; column-width auto-calc may break for wide tables
- Comments → preserve sources as inline comments? (defer to user preference)

### Coda

```bash
# Coda Pages API
curl -X POST "https://coda.io/apis/v1/docs/$CODA_DOC_ID/pages" \
  -H "Authorization: Bearer $CODA_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/coda-payload.json
```

**Coda-specific gotchas:**
- Coda's "page content" accepts a subset of MD; mermaid → image
- Tables become Coda tables (interactive — sortable, filterable)

## Update vs. create

By default, `--publish=` creates a new page each time. To update an existing page (vs. duplicating):

```
--publish=notion --update=<page-id>
--publish=confluence --update=<page-id>
```

This re-uses the same page slot and adds a version stamp (e.g., `Updated 2026-04-27 from research-entity skill v1.2`).

## Composition with other exports

`--publish=` composes with `--export=`:

```
--export=md,html --publish=notion
```

Generates local MD + HTML AND publishes to Notion. Useful for "always have a local copy + always publish".

## Confidentiality warning

Before publishing, surface a confirmation:

> "About to publish to Notion: workspace `<workspace-name>`, parent page `<page-id>`. Dossier contains <N> external citations (some may be paywalled / non-public). Anyone with workspace access will be able to read. Continue? [y/N]"

Skip this with `--publish=notion --no-confirm` for scripted runs.

## Anti-patterns

- ❌ Storing API tokens in the skill files (always read from env)
- ❌ Publishing without surfacing the destination URL back to user
- ❌ Auto-updating existing pages without `--update=` flag (silent overwrites are dangerous)
- ❌ Publishing to public Notion / shared Google Doc without confirmation (data leak risk)
- ❌ Embedding service-account JSON in a Bash command (history captures it)

## When to load this file

- `--publish=` flag set
- User asks "publish to Notion" / "send to Confluence" / "create a Google Doc"
- After successful local export, when user asks "now share it with my team"
