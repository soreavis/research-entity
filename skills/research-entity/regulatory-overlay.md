# Regulatory + Geographic Overlay

Loaded by the `research-entity` skill when the entity has international operations, regulated-vertical exposure (healthcare / fintech / govtech / AI), or is a target of compliance-sensitive due diligence. Combines two public-methodology layers: **(1) Ghemawat's CAGE Distance Framework** (international expansion analysis) and **(2) regulatory-exposure overlay** (OFAC sanctions, EU AI Act, GDPR territorial scope, India DPDP Act, China PIPL, US state privacy laws, sectoral regs).

---

## §1 — CAGE Distance Framework (Ghemawat)

### Why this matters

For any entity claiming international expansion (or being evaluated for international entry), Ghemawat's CAGE Distance Framework is the standard mid-2000s+ MBA-curriculum tool for analyzing "distance" between markets. It catches the failure mode where a vendor assumes "Europe" is one market or "Asia" is interchangeable.

### Verified methodology citation

- **Pankaj Ghemawat**, "Distance Still Matters: The Hard Reality of Global Expansion," *Harvard Business Review*, September 2001 → [hbr.org/2001/09/distance-still-matters-the-hard-reality-of-global-expansion](https://hbr.org/2001/09/distance-still-matters-the-hard-reality-of-global-expansion)
- **Pankaj Ghemawat**, *Redefining Global Strategy: Crossing Borders in a World Where Differences Still Matter* (Harvard Business Review Press, 2007)
- **NYU Stern (Ghemawat's home institution)** publishes CAGE comparator — [globalization.nyu.edu](https://globalization.stern.nyu.edu)
- **Globalization Index (DHL Connectedness)** uses CAGE-derived distance metrics → [dhl.com/global/en/delivered/globalization](https://www.dhl.com/global-en/microsites/core/global-connectedness.html)

### The four CAGE dimensions

| Dimension | What it measures | Example signals |
|---|---|---|
| **Cultural** | Language, religion, social norms, ethnic groups | Common language? Same major religion? Hofstede dimensions distance? |
| **Administrative** | Currency, political ties, trade blocs, regulations | Same trade bloc (EU, NAFTA/USMCA, ASEAN)? Currency union? Common law tradition? |
| **Geographic** | Physical distance, transport infrastructure, time zones | Time zone overlap? Direct flights? Internet latency? |
| **Economic** | Income levels, cost of labor, infrastructure, market sophistication | GDP per capita ratio? Disposable-income difference? Banking penetration? |

### CAGE matrix template (added to §10 or new §17.X for international entities)

```markdown
### 17.X CAGE Distance Analysis (Entity HQ: <City, Country> → Target Market: <Country>)

| Dimension | Distance | Specific factors | Strategic implication |
|---|---|---|---|
| **Cultural** | High / Medium / Low | Language: same/different · Hofstede individualism delta: X · ... | Localization required: Yes/No · Cultural adaptation: high/low |
| **Administrative** | High / Medium / Low | Currency: same/different · Trade bloc: same/different · Common law: yes/no · ... | Compliance overhead: high/low · Tax complexity: ... |
| **Geographic** | High / Medium / Low | Distance: X km · Time zone delta: X hrs · ... | Customer support coverage: difficulty level · Travel cost: ... |
| **Economic** | High / Medium / Low | GDP/cap ratio: X · Infrastructure: rank · ... | Pricing localization needed: yes/no · Channel partner reliance: ... |
```

### When to apply

| Scenario | Apply CAGE? |
|---|---|
| Entity claims "global presence" | ✅ Always — verify it's real or marketing |
| Entity expanding to new country | ✅ Always — assess fit |
| `--vertical=consumer` (B2C) | ✅ Always — consumer products are CAGE-sensitive |
| `--type=investment` AND international footprint | ✅ Always — for international thesis |
| Single-market entity, no expansion plans | ❌ Skip |

### Anti-patterns

- ❌ **Citing CAGE without specifying source markets** — distance is between two markets; can't compute in isolation.
- ❌ **Reducing CAGE to a single number** — 4 dimensions don't sum cleanly.
- ❌ **Treating CAGE distance as "bad"** — high distance can also mean differentiation opportunity. Frame neutrally.

---

## §2 — Regulatory exposure overlay

### Why this matters

Compliance regimes have material business impact: **GDPR fines** can be 4% of global revenue; **EU AI Act** takes effect 2026-2027 with high-risk-system requirements; **OFAC sanctions** can wipe out market access; **HIPAA** breaches are settlement-bearing in healthcare; **PCI DSS** non-compliance excludes payment processing. A complete dossier flags applicable regulatory regimes.

### Verified methodology citations

| Regime | Authority | Free / public source |
|---|---|---|
| **GDPR (EU/UK)** | European Data Protection Board (EDPB) | [edpb.europa.eu](https://www.edpb.europa.eu/) |
| **EU AI Act** | European Commission | [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) (unofficial), [eur-lex.europa.eu](https://eur-lex.europa.eu/) (official) |
| **EU DSA / DMA** | European Commission | [eur-lex.europa.eu](https://eur-lex.europa.eu/) |
| **NIS2 Directive** | European Commission | [eur-lex.europa.eu](https://eur-lex.europa.eu/) |
| **DORA (financial)** | European Commission | [eur-lex.europa.eu](https://eur-lex.europa.eu/) |
| **OFAC (US sanctions)** | US Treasury | [treasury.gov/ofac/downloads/sdnlist.txt](https://sanctionslist.ofac.treas.gov/Home/SdnList) |
| **CFIUS (US foreign investment)** | US Treasury | [home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius](https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius) |
| **HIPAA (US health)** | HHS OCR | [hhs.gov/hipaa](https://www.hhs.gov/hipaa/) |
| **GLBA (US finance)** | FTC | [ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act](https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act) |
| **CCPA / CPRA (California)** | California AG | [oag.ca.gov/privacy/ccpa](https://oag.ca.gov/privacy/ccpa) |
| **State privacy laws (CO/CT/UT/VA/...)** | State AGs | [iapp.org/resources/article/state-comparison-of-consumer-privacy-laws](https://iapp.org/resources/article/us-state-privacy-legislation-tracker) |
| **DPDP Act (India)** | MeitY | [meity.gov.in](https://www.meity.gov.in/) |
| **PIPL (China)** | Cyberspace Administration of China | [cac.gov.cn](http://www.cac.gov.cn/) (English summaries via NYU Asia Society) |
| **LGPD (Brazil)** | ANPD | [gov.br/anpd](https://www.gov.br/anpd/) |
| **POPIA (South Africa)** | Information Regulator | [inforegulator.org.za](https://inforegulator.org.za/) |
| **PIPEDA (Canada)** | OPC | [priv.gc.ca](https://www.priv.gc.ca/) |
| **Privacy Act (Australia)** | OAIC | [oaic.gov.au](https://www.oaic.gov.au/) |
| **PDPO (Hong Kong)** | PCPD | [pcpd.org.hk](https://www.pcpd.org.hk/) |
| **PDPA (Singapore)** | PDPC | [pdpc.gov.sg](https://www.pdpc.gov.sg/) |
| **PCI DSS (payment cards)** | PCI Security Standards Council | [pcisecuritystandards.org](https://www.pcisecuritystandards.org/) |
| **SOC 2 (US)** | AICPA | [aicpa.org](https://www.aicpa.org/) |
| **ISO 27001 / 27701 / 9001** | ISO | [iso.org](https://www.iso.org/) |
| **FedRAMP (US gov cloud)** | GSA | [fedramp.gov](https://www.fedramp.gov/) |
| **StateRAMP (US states)** | StateRAMP | [stateramp.org](https://www.stateramp.org/) |
| **C5 (Germany cloud)** | BSI | [bsi.bund.de](https://www.bsi.bund.de/EN/) |
| **TISAX (German automotive)** | ENX | [enx.com/tisax](https://enx.com/tisax/) |
| **NIST CSF / 800-53** | NIST | [nist.gov/cyberframework](https://www.nist.gov/cyberframework) |
| **HITRUST (healthcare)** | HITRUST Alliance | [hitrustalliance.net](https://hitrustalliance.net/) |
| **NCSC Cyber Essentials (UK)** | NCSC | [ncsc.gov.uk/cyberessentials](https://www.ncsc.gov.uk/cyberessentials/overview) |

### Regulatory-exposure subsection (added to §14 or new §16.X for due-diligence)

```markdown
### 16.X Regulatory Exposure Map

#### Applicable regimes (verified — entity does X / serves Y / processes Z)

| Regime | Applicability | Vendor stated? | Verification | Risk level |
|---|---|---|---|---|
| GDPR | EU/UK customers cited | ✅ on Trust page | DPA published | Low |
| CCPA / CPRA | California customers (>50% likely) | ⚠️ partial | "California residents" phrase | Medium |
| EU AI Act | Uses ML for ranking/scoring (high-risk system?) | ❌ not addressed | No public AI Act response | High (regulatory-readiness gap) |
| HIPAA | No healthcare claim → N/A | N/A | — | N/A |
| OFAC | No foreign-government customers cited; US HQ | ✅ implicit | — | Low |
| ... | ... | ... | ... | ... |

#### Compliance certifications (verified vs claimed)

| Certification | Vendor claim | Verified | Source |
|---|---|---|---|
| SOC 2 Type II | ❌ not claimed | — | — |
| ISO 27001:2022 | ✅ claimed | ✅ via certification body | [link to ISO cert] |
| GDPR DPA | ✅ claimed | ✅ public DPA | [link to DPA] |
| ... | ... | ... | ... |
```

### Apply when

- `--vertical=` includes any of: `healthcare`, `fintech`, `govtech`, `legaltech`, `edtech` → auto-load
- `--type=due-diligence` AND entity has named-customer base in regulated sectors
- Entity claims any compliance certification (verify the claim)
- Entity is HQ'd outside the US AND has US customers (cross-border data scrutiny)

### Anti-patterns

- ❌ **Treating "GDPR-compliant" as a binary yes/no** — GDPR has data-subject-rights, lawful-basis, DPO, breach-notification, DPIA — verify the specific dimensions claimed.
- ❌ **Listing every possible regime** — overkill in a competitive dossier; focus on applicable + load-bearing.
- ❌ **Conflating "ISO 27001 certified" with "SOC 2 Type II audited"** — different scopes; ISO is procedural, SOC 2 is operational.
- ❌ **Taking Trust Center claims at face value** — verify the auditor named (Big 4 vs lower-tier) and the audit period (annual vs. once-ever).

---

## §3 — Workflow integration

**Step 2 — source gathering**: when entity HQ + customer geography + vertical are known, identify applicable regimes:

```python
applicable_regimes = []
if entity_hq in ["EU", "UK"] or any_customer_in_eu_uk:
    applicable_regimes.append("GDPR")
if vertical == "healthcare":
    applicable_regimes.append("HIPAA")
    applicable_regimes.append("HITRUST" if any_us_health_customer else None)
if vertical in ["fintech", "payment"]:
    applicable_regimes.append("PCI DSS")
    applicable_regimes.append("DORA" if any_eu_finance_customer else None)
if uses_ml_for_decision_making:
    applicable_regimes.append("EU AI Act")
# ... etc
```

**Step 4 — draft**: write §16.X Regulatory Exposure Map using the verification template.

**Step 5 — validate**: cross-check vendor compliance claims against publicly listed certifications (e.g., FedRAMP marketplace, ISO certification bodies' search portals, SOC 2 disclosure registers).

---

## §4 — Anti-patterns (cross-cutting)

- ❌ **Citing CAGE without market-pair specification** — always state both the source HQ market and the target market.
- ❌ **Listing regulatory regimes as if all apply equally** — applicability depends on customers + vertical + geography.
- ❌ **Treating regulatory exposure as static** — EU AI Act enforcement begins 2026-2027; US state privacy laws cascade quarterly.

---

## §5 — When to load this file

- `--type=due-diligence|investment` AND entity has international operations
- `--vertical=healthcare|fintech|govtech|legaltech|edtech`
- Entity HQ'd outside US/UK with US/UK customers (or vice versa)
- User asks "what compliance burden does this entity have?"
- User asks "is this entity ready for an EU AI Act audit?"

---

## §6 — Related

- `frameworks.md` — PESTEL has overlap with this file's regulatory layer
- `data-sources-extended.md` — broader OSINT including FedRAMP marketplace
- `audits.md` — `--audit=customer-concentration` overlaps with regulatory exposure
