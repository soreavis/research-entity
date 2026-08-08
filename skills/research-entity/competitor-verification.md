# Competitor-Row Pre-Publication Verification

Loaded by the `research-entity` skill before finalizing §10 Market Positioning & Competition. This is a **mandatory** structural check for `--type=competitive|due-diligence|investment` dossiers because §10 is the section that most often becomes ammunition in real meetings, and three error classes (lead investor, HQ, round structure) recur across production runs.

This file codifies post-correction lessons #41–45 from `lessons.md` into an executable verification protocol.

---

## Why this file exists

Three real production errors that survived a full v2.4 audit pipeline (URL validation + hallucination audit + cross-validation pass) and only surfaced when the user re-checked against primary sources:

1. **Aurasell lead investor** — dossier said "Menlo Ventures (lead) + Next47 + Unusual"; correct was "Next47 (lead) + Menlo + Unusual" per Sacra + Tech Startups + AIM Media (Lak Ananth quote) + Daily Company News.
2. **Aurasell HQ** — dossier said "San Mateo"; correct was "San Francisco" per GlobeNewswire press release dateline + SaaS News + FinSMEs + BusinessWire + company own site.
3. **Reevo $80M structure** — dossier said "$80M seed"; correct was "$10M seed (Zhu Ventures) + $70M Series A (Khosla + Kleiner co-led)" per Bloomberg primary breakdown.

All three errors have a common structural cause: the model accepted the **first plausible reading** from secondary outlets without driving down to primary sources. This file enforces primary-source verification at the row level.

---

## The three error classes

### Class 1: Lead-investor identity (highest-frequency error)

**Failure pattern:** Outlets routinely use ambiguous phrasing — "Funding from X, Y, and Z" — that conflates leading and participating investors. Some lazier outlets list co-participants as if jointly leading. The error compounds when a press release uses "co-led by X and Y" but the actual cap table has X as sole lead and Y as a strategic co-investor.

**The diagnostic:** the lead investor's CEO or partner is usually quoted in the announcement. **If a quote attributes leadership to someone, that is the load-bearing signal.** The Aurasell case: Lak Ananth, CEO of **Next47**, was quoted as "we led this round" — that settles it regardless of how secondary outlets paraphrased it.

**Source preference order:**
1. **Press release with explicit "led by [name]"** + named-partner quote → highest confidence
2. **Primary financial press (Bloomberg / TechCrunch / The Information / Pitchbook)** with explicit breakdown → high confidence
3. **Sacra / PitchBook / Crunchbase** structured summary → medium confidence
4. **Secondary outlet paraphrase** ("backed by," "with," "and") → low confidence — never publish lead identity from this tier alone

**Verification rule:** require ≥3 sources from tier 1-3 for lead-investor identity. If sources disagree, the source carrying named-partner attribution wins.

---

### Class 2: HQ city (transcription-error pattern)

**Failure pattern:** Bay-Area-specific gotcha — San Mateo / San Francisco / Mountain View / Palo Alto are routinely confused in transcribed business news. A single secondary outlet's transcription error can propagate across aggregator-syndicated coverage.

**The diagnostic:** the **press release dateline is canonical** because press releases are issued by the company's own PR function. If GlobeNewswire / BusinessWire / PR Newswire dateline reads "SAN FRANCISCO, [date]," that is the load-bearing signal.

**Source preference order:**
1. **Official press release dateline** (GlobeNewswire / BusinessWire / PR Newswire) → highest confidence
2. **Company's own /about page or footer address** → high confidence
3. **LinkedIn header location** → medium confidence
4. **Secondary outlet "based in X"** → low confidence

**Verification rule:** when secondary outlets disagree on HQ, **the press release dateline wins**. Never rely on a single secondary outlet for HQ city in a competitor row.

---

### Class 3: Bundled-announcement funding rounds

**Failure pattern:** Companies announcing simultaneously at GA / public launch routinely bundle seed + Series A in the headline ("$80M in funding"). The structural breakdown — which round, what stage, who led each, on what date — disappears in the company's own framing because they want a single big number for the press cycle. Outlets following the company's framing copy the bundling; primary financial press usually breaks them out.

**The diagnostic:** if the announcement involves a sub-2-year-old company with a "GA"/"launch"/"public debut" framing AND the headline number is large (>$50M), there is a high prior that this is **two rounds bundled**. Bloomberg, TechCrunch, and The Information typically have the structural breakdown.

**Source preference order:**
1. **Bloomberg / TechCrunch / The Information** with explicit "$Xm seed + $Ym Series A" structure → highest confidence
2. **PitchBook / Crunchbase** funding-round records (if available) → high confidence
3. **Company's own bundled press release** → use only if no primary financial press source exists; mark structure as `unverified-bundled`
4. **Secondary outlet paraphrasing the bundled headline** → never publish from this alone

**Verification rule:** for any peer announcing $50M+ at GA / public launch, **search Bloomberg / TechCrunch / The Information for the structural breakdown** before publishing. Format the result as `$Xm seed (Lead) + $Ym Series A (Co-leads), date1 + date2` not `$Zm seed`. This is especially load-bearing when seed and Series A have **different lead investors**, which materially changes cap-table interpretation.

---

### Class 4: Numeric-figure attribution drift (Pento pattern)

**Failure pattern:** When citing a specific number to a specific article, the model can attribute a plausible-sounding number to a real source where the article discusses the topic but does not contain the precise figure. The result is **false specificity attributed to a real source** — the URL works, the article is real, the topic is right, but the specific number isn't actually in there.

**The diagnostic:** if a numeric claim is load-bearing (cited multiple times, used in BLUF, used in glossary), the cited source must contain that exact number or the same magnitude.

**Verification rule:** when a number is cited 2+ times in a dossier and tied to one source, run a final pass: **fetch the cited URL, search for the number** (or its order of magnitude). If absent, either find a source that does cite the number, or soften to a corroborated range across multiple sources.

---

## Pre-publication checklist (mandatory before §10 ships)

Run this as a final gate before draft → audit → ship.

For **every competitor row** in §10 Tier B/C/D:

```markdown
### Peer name: <name>

#### Lead investor verification
- [ ] ≥3 sources cited for lead investor identity
- [ ] At least one source has named-partner attribution (CEO quote, term sheet press release)
- [ ] Source phrasing checked for "led by" vs. "with" vs. "from" — if ambiguous, escalated to primary
- [ ] No reliance on single-outlet paraphrase

#### HQ verification
- [ ] Press release dateline checked
- [ ] Company /about page checked
- [ ] LinkedIn header checked
- [ ] Bay-Area gotcha avoided (SF/SM/MTV/PA confusion)
- [ ] No reliance on single-outlet "based in X"

#### Round structure verification
- [ ] If $50M+ raise at GA / public launch: Bloomberg/TC/Information searched for breakdown
- [ ] Format: `$Xm seed (Lead) + $Ym Series A (Co-leads)` if bundled
- [ ] Different lead investors per round explicitly noted
- [ ] Date-of-record per round (not just "co-announced date")

#### Numeric-attribution verification
- [ ] Any specific number cited to a specific article: URL fetched, number confirmed in body
- [ ] If load-bearing (cited 2+ times): cross-validated against ≥2 independent sources
- [ ] Soften to range if single-source

#### Founders verification
- [ ] Founder names cross-validated against LinkedIn + company /about
- [ ] Prior employer attribution confirmed via LinkedIn (not just press paraphrase)
```

---

## How the skill loads this file

1. **Mandatory load** for `--type=competitive|due-diligence|investment` at the start of Step 4 (Draft) when §10 begins assembly
2. **Mandatory check** for every Tier B/C/D peer row before §10 is committed to the draft
3. **Optional load** for `--type=research|partnership` when §10 has 5+ peer rows

Failure to satisfy the mandatory check produces a `⚠️` flag in the §23 Confidence appendix under "Multi-source corroboration" — the dossier can ship but the score is capped.

---

## Anti-patterns

- ❌ **Quoting the company's own press release as primary source for round structure** — companies bundle simultaneously-announced rounds for press impact; the structural breakdown lives in primary financial press.
- ❌ **Using a single secondary outlet for HQ** — transcription errors propagate.
- ❌ **Treating "with" or "and" or "backed by" as evidence of a lead investor** — these are deliberately ambiguous in PR copy.
- ❌ **Skipping this check because URL validation passed** — URL validation tells you the page exists, not that the page supports your claim.
- ❌ **Skipping this check because hallucination audit passed** — hallucination audit checks consistency between §0 and the body, not between the body and primary sources.

---

## Related

- `lessons.md` — lessons #41-45 codify the failure patterns
- `source-rating.md` — Admiralty Code formal source-quality notation
- `analytic-techniques.md` — Quality of Information Check (QIC) layer
- `voice-and-style.md` — competitor-row voice/format rules
