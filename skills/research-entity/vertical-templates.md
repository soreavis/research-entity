# Vertical Templates — `--vertical=<industry>`

Loaded by the `research-entity` skill at Step 1 (Plan) when `--vertical=` is set OR auto-detected from `/about` page keywords. Tunes which compliance frameworks, integration ecosystems, and regulators to surface, plus which review platforms and competitor lists are most salient.

A vertical-aware dossier surfaces the regulatory failure modes that will actually kill the deal — without `--vertical`, those get bucketed into a generic "compliance" sentence and missed.

## Supported verticals

| Vertical | Auto-detect keywords | Required compliance focus | Key competitor lists | Review platforms (priority) |
|---|---|---|---|---|
| `healthcare` | EHR, HIPAA, hospital, clinic, patient, provider, physician, telehealth, PHI | HIPAA, HITRUST CSF, FDA SaMD, 21 CFR Part 11, state breach notification, BAA template | Epic, Cerner, Athena, Allscripts, eClinicalWorks, Veeva, Doximity | KLAS, Black Book, G2, Capterra |
| `fintech` | bank, lending, payment, card, deposit, broker, KYC, AML, neobank | PCI-DSS, SOC 2 Type II, ISO 27001, BSA/AML, OCC, NYDFS, FCA, FINRA, GDPR | Plaid, Stripe, Adyen, Marqeta, Brex, Ramp | G2, Trustpilot, BBB, FINRA broker check |
| `govtech` | federal, state, agency, FedRAMP, public sector, GSA, CJIS, defense, DoD | FedRAMP (Low/Mod/High), StateRAMP, CJIS, DoD IL2-IL6, NIST 800-171/800-53, FISMA, ITAR | Salesforce.gov, Palantir, Granicus, Tyler Tech, OpenGov, Civis, Mark43 | GSA Schedule, FedScout, GovWin |
| `edtech` | school, district, K-12, higher ed, student, teacher, LMS, learning | FERPA, COPPA (under 13), CIPA, IMS Global (Caliper, QTI, OneRoster), state district procurement | Canvas, PowerSchool, Blackboard, Schoology, Clever, ClassLink | EdSurge, Common Sense, G2 |
| `legaltech` | law firm, attorney, court, e-discovery, contract, IP | ABA Model Rules 5.4 (UPL), ABA Formal Opinion 477R, e-discovery EDRM, ISO 27001, SOC 2 | LexisNexis, Westlaw, Clio, MyCase, Relativity, Litera, Ironclad | G2, Capterra, ABA TechReport |
| `devtools` | developer, API, SDK, CLI, library, framework, deploy, build, CI/CD | License compliance (open-source), SOC 2, SBOM, supply-chain attestation (SLSA, Sigstore) | GitHub, GitLab, JetBrains, Vercel, Netlify, Cloudflare, Datadog | GitHub stars, npm/PyPI downloads, Stack Overflow, HackerNews |
| `consumer` | DTC, mobile, app, subscription, marketplace, social | App Store / Play Store policy, COPPA (under 13), CCPA, GDPR | Stripe, Shopify, Amplitude, Segment, Mixpanel | App Store, Play Store, Trustpilot, BBB, Reddit |
| `saas` | SaaS, B2B, cloud, subscription, productivity, workflow (default) | SOC 2 Type II, ISO 27001, GDPR, CCPA, HIPAA-on-request | Varies by sub-vertical | G2, Capterra, Trustpilot, Glassdoor |
| `deeptech` | AI/ML model, hardware, robotics, biotech, materials, quantum | Patent portfolio, IP defensibility, scientific advisors, regulatory pathway (FDA/EPA/FAA) | Highly entity-specific | Academic citations, patent counts, scientist hires |

## Per-vertical template overrides

### `--vertical=healthcare`

Required dossier additions:
- **§14.X HIPAA + HITRUST posture** — BAA template availability, breach-notification SLA, audit cadence
- **§13.X EHR Integrations** — explicit list of which EHRs (Epic, Cerner, Athena, etc.) — this is the deal-killer / deal-maker for healthcare buyers
- **§16.X Reimbursement risk** — does revenue depend on CMS / state reimbursement codes? CPT codes? FQHC eligibility?
- **§16.X PHI data residency** — where is PHI stored, how is it encrypted, who has access
- Add to §11 Community: KLAS reviews (only KLAS-rated vendors get hospital RFPs)

Search additions:
- `<entity> HIPAA BAA`
- `<entity> EHR integration Epic Cerner`
- `<entity> KLAS review`
- `<entity> HITRUST certified`
- `<entity> breach OCR fine`

### `--vertical=fintech`

Required dossier additions:
- **§14.X Banking partnerships** — sponsor bank if lending / deposit / card-issuing (Cross River, Evolve, Sutton, Lead, etc.)
- **§14.X Regulatory licenses** — money transmitter (state-by-state), broker-dealer (FINRA), banking charter, OCC fintech charter
- **§16.X Regulatory risk** — recent CFPB / OCC / NYDFS / FCA / FINRA actions; state-level enforcement
- **§16.X Sponsor-bank concentration** — single-sponsor-bank dependency

Search additions:
- `<entity> sponsor bank`
- `<entity> CFPB enforcement`
- `<entity> NYDFS BitLicense`
- `<entity> FINRA broker check`
- `<entity> SOC 2 Type II report`

### `--vertical=govtech`

Required dossier additions:
- **§14.X FedRAMP / StateRAMP status** — In Process vs. Authorized; ATO sponsor; impact level (Low / Moderate / High)
- **§13.X Government contract vehicles** — GSA Schedule (which SIN), SEWP V, CIO-CS, OASIS, ITES, agency-specific BPAs
- **§9.X Agency customer logos** — by tier (federal / state / city), by agency, with contract numbers from FPDS where possible
- **§16.X Contract concentration risk** — single agency > 25% revenue?

Search additions:
- `<entity> FedRAMP marketplace status`
- `<entity> GSA Schedule contract number`
- `<entity> FPDS contract awards`
- `<entity> SAM.gov registration`
- `<entity> CJIS compliant`

### `--vertical=edtech`

Required dossier additions:
- **§14.X FERPA / COPPA compliance** — vendor-as-school-official designation, student-data-pledge signatory
- **§13.X LMS integrations** — Canvas, Schoology, Blackboard, PowerSchool — deal-killer/maker
- **§13.X SSO standards** — Clever / ClassLink / OneRoster / OAuth — district procurement requires these
- **§9.X District customer logos** — public-sector procurement is highly transparent; check district board minutes

Search additions:
- `<entity> FERPA student data privacy pledge`
- `<entity> Common Sense Privacy`
- `<entity> LMS integration Canvas`
- `<entity> district contract bid award`

### `--vertical=legaltech`

Required dossier additions:
- **§14.X ABA Model Rule 5.4 / UPL posture** — for legal-AI tools, what's the disclaimer about unauthorized practice of law
- **§14.X ISO 27001 + SOC 2** — table-stakes for AmLaw 200 procurement
- **§13.X Practice management integrations** — Clio, MyCase, PracticePanther, Litify
- **§16.X Privilege risk** — how is attorney-client privilege protected; what happens to data on subpoena

Search additions:
- `<entity> ABA opinion 477R`
- `<entity> AmLaw 200 customer`
- `<entity> e-discovery EDRM`

### `--vertical=devtools`

Required dossier additions:
- **§6.X Developer experience** — onboarding time, SDK quality, docs depth (use Algolia + DocSearch counts)
- **§9.X GitHub footprint** — load `data-sources-extended.md`; report stars, contributors, last commit, dependents-graph size
- **§9.X Package downloads** — npm / PyPI / Maven Central monthly downloads (npmtrends, PyPI Stats)
- **§11.X HackerNews + Reddit r/programming presence** — distinctive engagement signal for devtools

Search additions:
- `<entity> GitHub stars`
- `<entity> npm downloads`
- `<entity> Stack Overflow tag`
- `<entity> HackerNews discussion`
- `<entity> Show HN`

### `--vertical=consumer`

Required dossier additions:
- **§7.X App Store / Play Store metadata** — rating, review count, install count band, last update
- **§8.X Pricing — IAP** — in-app purchase tiers, subscription tiers, free-tier limits
- **§16.X Platform-policy risk** — App Store guideline compliance, recent rejections, COPPA exposure if under-13 users
- **§9.X Viral coefficient signals** — social sharing, referral mechanics

Search additions:
- `<entity> App Store rating`
- `<entity> Play Store install count`
- `<entity> COPPA settlement FTC`

### `--vertical=deeptech`

Required dossier additions:
- **§3.X Scientific advisors** — named PhDs, papers cited, lab affiliations
- **§7.X Patent portfolio** — load `data-sources-extended.md`; USPTO assignee search; granted vs. pending; key claims
- **§16.X Regulatory pathway** — FDA (510(k), De Novo, PMA), EPA, FAA, NRC, CE Mark
- **§4.X Grant funding** — SBIR / STTR / DARPA / NSF / NIH non-dilutive funding (often signals technical credibility)

Search additions:
- `<entity> USPTO patent assignee`
- `<entity> Google Scholar citations`
- `<entity> SBIR award DoD NSF NIH`
- `<entity> FDA 510k clearance`

## Vertical auto-detection

Run on canonical `/about` + `/products` + `/customers` pages:

```bash
# Walk verticals in priority order; first match wins
for v in healthcare fintech govtech edtech legaltech devtools deeptech consumer saas; do
  case "$v" in
    healthcare) PATTERN='HIPAA|EHR|hospital|clinic|patient|physician|telehealth|provider|PHI' ;;
    fintech) PATTERN='bank|lending|payment|card|deposit|broker|KYC|AML|neobank' ;;
    govtech) PATTERN='FedRAMP|federal agency|state government|GSA|CJIS|defense' ;;
    edtech) PATTERN='K-12|district|student|teacher|LMS|FERPA' ;;
    legaltech) PATTERN='law firm|attorney|court|e-discovery|legal' ;;
    devtools) PATTERN='developer|SDK|API|CLI|library|framework|build pipeline|CI/CD' ;;
    deeptech) PATTERN='AI model|robotics|biotech|materials|quantum|hardware' ;;
    consumer) PATTERN='consumer|DTC|mobile app|subscription|marketplace' ;;
    saas) PATTERN='SaaS|B2B|cloud platform' ;;
  esac
  if grep -qiE "$PATTERN" "$ABOUT_TEXT $PRODUCTS_TEXT $CUSTOMERS_TEXT"; then
    DETECTED=$v; break
  fi
done
echo "Detected vertical: ${DETECTED:-unknown}"
```

If auto-detected, surface: "Detected `--vertical=fintech` from /about + /products text. Use `--vertical=` to override."

## Composing stage + vertical

Stage and vertical compose independently. A `series-b healthcare` company gets:
- Series-B section emphasis (R40, NRR, magic number)
- Healthcare compliance stack (HIPAA, HITRUST, EHR integrations)
- Healthcare review platforms (KLAS, Black Book)
- Healthcare risk factors (PHI breach, reimbursement)

## When to load this file

- `--vertical=` flag set
- Auto-detection triggers
- Wizard Question 9 (vertical selection, when added)
- User asks vertical-specific questions ("how does this compare in fintech?")
