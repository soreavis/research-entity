# Citation Style — Inline vs. Footnotes

Loaded by the `research-entity` skill during Step 4 (Draft) and any post-draft revision. Controlled by `--citations=<style>`.

## Two supported styles

### `inline` (default)

Every claim is linked directly in-place. Reader can click any phrase to jump to source.

```markdown
The company was founded in **2011** ([Entity About page](https://www.example.com/about/)).
Per [Latka, June 2024](https://getlatka.com/companies/example), revenue is ~$16M.
```

**Pros:** instant navigation, reader sees source immediately, no jumping.
**Cons:** when one source is cited 30+ times, the URL appears 30 times in the source MD; visually noisy when reading raw markdown; HTML export has many duplicate hyperlinks.

### `footnotes` (cleaner for source-heavy dossiers)

Sources defined once at the document bottom, referenced via named tags throughout the body.

```markdown
The company was founded in **2011** [^about]. Per Latka [^latka], revenue is ~$16M.

...

[^about]: [Entity About page](https://www.example.com/about/)
[^latka]: [Latka, June 2024](https://getlatka.com/companies/example)
```

**Pros:** body reads cleanly without URL noise; same source referenced N times = 1 footnote definition; consistent with academic / research-paper style; easier to audit "is every source still live?" (one URL list, not scattered).
**Cons:** one extra click for reader (footnote → link); some MD renderers don't auto-jump; pandoc handles natively.

### `endnotes` (variant of footnotes — sources only at §19)

Same as `footnotes` but no inline reference markers in body — every claim is sourced by §-number / line-number reference, with the master list in §19 Sources.

```markdown
The company was founded in **2011** (see §19 [Entity About page]).
```

This is more academic but harder to read; rarely used. Default to `footnotes` if the user wants "cleaner body".

## Choosing the style

Default: `inline`. Override with `--citations=footnotes` or `--citations=endnotes`.

**Use `footnotes` when:**
- Dossier is `--depth=deep` with 100+ citations (inline becomes overwhelming)
- Output is intended for printing (footnotes look better on page)
- The same 5–10 sources are cited across many sections (massive deduplication wins)
- User explicitly asks for "academic style" or "cleaner body"

**Use `inline` when:**
- Dossier is `--depth=quick` or `standard` (under 50 citations)
- Output is intended for digital reading (clicking links is the fast path)
- Each claim has a unique source (no deduplication win)
- User wants the most click-friendly format

## Footnote naming convention

Use **descriptive lowercase tags**, not auto-numbered references. This way, the same source naturally gets the same tag whenever cited.

**Good** (descriptive, deduplicating):
```
[^crunchbase]: [Crunchbase: Example Inc](https://www.crunchbase.com/organization/example)
[^pr-2026-04-09]: [PRNewswire, 2026-04-09](https://www.prnewswire.com/...)
[^trust-page]: [Trust Page](https://www.example.com/security/)
[^bizfile-ca]: [California SOS](https://bizfileonline.sos.ca.gov/)
```

**Bad** (auto-numbered, breaks deduplication):
```
[^1]: [Crunchbase: Example Inc](...)
[^2]: [PRNewswire, 2026-04-09](...)
```

Pattern: `[^<source-or-domain>-<optional-date-or-context>]`

Common tag prefixes:
- `[^crunchbase]`, `[^pitchbook]`, `[^tracxn]`, `[^latka]` — aggregators
- `[^pr-YYYY-MM-DD]` — press releases by date
- `[^about]`, `[^trust]`, `[^pricing]`, `[^team]`, `[^press]` — primary site sub-pages
- `[^g2]`, `[^capterra]`, `[^trustpilot]`, `[^glassdoor]` — review platforms
- `[^bizfile-ca]`, `[^orsr-sk]`, `[^firmenbuch-at]`, `[^handelsregister-de]` — business registers
- `[^wikipedia]`, `[^fortune]`, `[^techcrunch]` — third-party press

## Citation format rules (both styles)

Regardless of style, **every claim that can be sourced must have a citation.** This is non-negotiable. The voice rule "back every claim with a source" applies always.

What needs a citation:
- ✅ Every numeric fact (dates, dollar amounts, counts, percentages)
- ✅ Every proper noun used as a fact (company names, people, products)
- ✅ Every quoted statement (verbatim quotes)
- ✅ Every claim about another company (competitor funding, product launches)
- ✅ Every regulatory / compliance / certification claim
- ✅ Every customer logo / case study claim

What does NOT need a citation:
- ❌ Analyst opinion (SWOT, Heat Map, Playbook content) — these are bucketed under §0 framework disclaimer
- ❌ Synthesis / inference clearly labeled as such ("Reading these together suggests...")
- ❌ Generic statements without specific facts ("CRMs typically integrate with email")

## Conversion between styles (post-draft)

If the user runs the skill in `inline` mode and later asks "convert to footnotes", or vice versa, the transformation is mechanical:

### Inline → Footnotes

```bash
# Strategy: extract all unique URLs, assign descriptive tags, replace inline links

# 1. Find all inline link patterns: [text](url)
grep -oE '\[[^]]+\]\([^)]+\)' "$OUTPUT" > /tmp/all-inline-links.txt

# 2. Group by URL, assign tags (manual review for tag naming)
# 3. Replace each [text](url) with text[^tag]
# 4. Append [^tag]: [text](url) section at end

# Pandoc supports both natively, so post-conversion validates with:
pandoc "$OUTPUT" -t html5 -o /tmp/test.html
```

### Footnotes → Inline

Each `[^tag]` reference is replaced with the inline link from the footnote definition. Footnote section at end is removed.

## Section §19 (Sources) interaction

Both styles still produce a §19 Sources section as the canonical category-organized list. Difference:

- **`inline` mode**: §19 is the master categorized list (Primary / Press / Aggregators / Reviews / Competitors / etc.); body links are in addition.
- **`footnotes` mode**: §19 is the same categorized list, AND every footnote at the bottom of the document is one entry from §19. Pandoc footnote rendering creates the bottom-of-document list naturally; §19 is the curated/categorized version.
- **`endnotes` mode**: §19 is the only list. Body refs to §19 by entry number.

## Implementation in the draft

When `--citations=footnotes` is set:
1. The model maintains a "source dictionary" while drafting (URL → tag mapping)
2. First reference to a URL coins the tag; subsequent references reuse it
3. Footnote definitions are appended at the end of the body, before §19 Sources
4. §19 Sources remains the categorized clickable list (this is independent of footnote definitions)

When `--citations=inline` (default):
1. Every fact gets a `[Source](url)` inline immediately
2. §19 Sources is the categorized clickable index of unique URLs

## Quality checklist additions

For both styles:
- [ ] Every numeric fact has a citation (inline or footnote)
- [ ] Every proper-noun fact has a citation
- [ ] Every quoted statement has attribution + citation
- [ ] Every competitor / customer / investor named has a clickable URL

For `footnotes` mode specifically:
- [ ] Same URL → same footnote tag (deduplication working)
- [ ] All `[^tag]` references have matching `[^tag]: ...` definitions
- [ ] Pandoc HTML/PDF export renders footnotes correctly (test with sample export)
- [ ] No orphan footnotes (defined but never referenced)

## When to load this file

Load `citations.md` when:
- About to draft (Step 4) — to know the citation style
- User explicitly asks to "convert to footnotes" / "switch to inline" / "deduplicate sources"
- Quality checklist review for citation discipline
- HTML/PDF export step (pandoc handles both styles natively but config differs slightly)
