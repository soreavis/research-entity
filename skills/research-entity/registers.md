# Free Public Business Registers — by Region

This file is loaded by the `research-entity` skill when the entity being researched is non-US or has international subsidiaries. The skill's two-source rule requires verifying entity legal facts (incorporation date, registered seat, share capital, directors, current status, beneficial owners) against the official business register of each jurisdiction the entity operates in.

**Hard rule: free sources only.** Paid services (D&B Hoovers paid tier, Bisnode, paid Compass.at fields) are explicitly excluded. The skill's user contract is reproducibility — anyone reading the dossier should be able to replicate the research with no subscription.

## Quick country lookup

| Region | Countries covered |
|---|---|
| **DACH** | Austria, Germany, Switzerland, Liechtenstein |
| **Western Europe** | UK, Ireland, France, Netherlands, Belgium, Luxembourg |
| **Southern Europe** | Spain, Portugal, Italy, Greece, Cyprus, Malta |
| **Central / Eastern Europe** | Slovakia, Czech Republic, Poland, Hungary, Romania, Slovenia, Croatia, Bulgaria, Serbia, Estonia, Latvia, Lithuania |
| **Nordic** | Sweden, Norway, Denmark, Finland, Iceland |
| **North America** | USA (federal + 50 states), Canada, Mexico |
| **Latin America** | Brazil, Argentina, Chile, Colombia, Peru, Uruguay |
| **APAC** | Australia, New Zealand, Singapore, Hong Kong, Japan, South Korea, India, China, Taiwan, Thailand, Indonesia, Malaysia, Philippines, Vietnam |
| **Middle East / Africa** | UAE, Saudi Arabia, Israel, South Africa, Nigeria, Kenya, Egypt, Morocco |
| **EU-wide** | BRIS, OpenCorporates, e-Justice |

---

## DACH

### Austria
- [Firmenbuch via WiEReG](https://www.bmf.gv.at/services/wiereg.html) — official, free public-data portion (BMF-hosted)
- [Compass.at](https://compass.at/) — basic free; many fields paywalled
- [firmenabc.at](https://www.firmenabc.at/) — free company directory + key figures
- [NorthData Austria](https://www.northdata.com/) — free EU company data, FN lookup
- [WKO Firmen](https://firmen.wko.at/) — Austrian Federal Economic Chamber free company search
- **Key field:** Firmenbuchnummer (FN) — e.g., `FN 123456a` — appears at Handelsgericht Wien (HG Wien) for Vienna-based GmbHs
- **Common gotcha:** older addresses in founder bios may not match current registered seat; always verify against current Firmenbuch entry

### Germany
- [Handelsregister](https://www.handelsregister.de/) — official federal register, fully free for basic data
- [Bundesanzeiger](https://www.bundesanzeiger.de/) — published annual financial reports (free; mandatory disclosure for GmbH/AG)
- [NorthData Germany](https://www.northdata.com/) — free EU data
- [Unternehmensregister](https://www.unternehmensregister.de/) — federal companies register
- [GENIOS Wirtschaft](https://www.genios.de/) — basic search free
- **Key field:** HRB number — e.g., `HRB 12345` — Local court (Amtsgericht) named in record
- **Status terms:** `aktiv` / `gelöscht` / `in Liquidation` / `abgemeldet`

### Switzerland
- [Zefix (federal)](https://www.zefix.admin.ch/en/search/entity/welcome) — official, fully free, all 26 cantons
- [Moneyhouse](https://www.moneyhouse.ch/) — Swiss company directory (basic free)
- [Handelsregister cantonal portals](https://www.zefix.admin.ch/en/search/entity/welcome) — per-canton (Zefix is the federation)
- **Key field:** UID (Unternehmens-Identifikationsnummer) — e.g., `CHE-123.456.789`
- **Documents:** Statutes / company documents (`Statuten`, `Handelsregisterauszug`) usually free

### Liechtenstein
- [Justice.li / Handelsregister](https://www.handelsregister.li/) — Office of Justice, free official register
- [Liechtensteinische Landesverwaltung](https://www.llv.li/en) — administrative search
- **Key field:** Firmennummer

---

## Western Europe

### UK
- [Companies House](https://find-and-update.company-information.service.gov.uk/) — official, fully free, includes all filings (annual accounts, confirmation statements, charges, PSC register)
- [Companies House API](https://developer.company-information.service.gov.uk/) — free API for programmatic lookup
- **Key field:** Company number (8-digit, e.g., `12345678`)
- **Status terms:** `Active` / `Dissolved` / `Liquidation` / `Administration`

### Ireland
- [Companies Registration Office (CRO)](https://www.cro.ie/) — official; basic search free, individual reports paid
- [CORE](https://core.cro.ie/) — CRO's online search portal
- [vision-net.ie](https://www.vision-net.ie/) — directory aggregator
- **Key field:** CRO number

### France
- [Pappers](https://www.pappers.fr/) — free aggregator with full Infogreffe data + financial filings
- [Infogreffe](https://www.infogreffe.com/) — official; basic free
- [INPI Société.com](https://data.inpi.fr/) — National Industrial Property Institute, free
- [Annuaire des Entreprises](https://annuaire-entreprises.data.gouv.fr/) — official government directory
- **Key field:** SIREN (9 digits) + SIRET (14 digits, includes establishment number)

### Netherlands
- [KVK (Kamer van Koophandel)](https://www.kvk.nl/) — official, basic free; full extracts paid
- [OpenKVK](https://overheid.io/) — open-data version
- **Key field:** KvK number (8 digits)

### Belgium
- [Banque-Carrefour des Entreprises (KBO/CBE)](https://kbopub.economie.fgov.be/) — official, fully free
- [Belfirst](https://belfirst.bvdinfo.com/) — basic free search
- **Key field:** BTW / TVA / VAT number (`BE 0123.456.789`)

### Luxembourg
- [Luxembourg Business Register (LBR)](https://www.lbr.lu/) — official, basic free; documents paid (small fee)
- [Registre de Commerce et des Sociétés (RCS)](https://www.lbr.lu/) — same portal
- [Mémorial C](https://legilux.public.lu/memorial-c) — published company-incorporation announcements
- **Key field:** RCSL number (e.g., `B 123456`)

---

## Southern Europe

### Spain
- [Registro Mercantil Central](https://www.rmc.es/) — federal company register
- [BORME (Boletín Oficial del Registro Mercantil)](https://www.boe.es/diario_borme/) — gazette of corporate filings
- [eInforma](https://www.einforma.com/) — basic free
- **Key field:** CIF / NIF + Tomo, Folio, Hoja del Registro

### Portugal
- [Portal Empresa](https://eportugal.gov.pt/) — government portal
- [Registo Nacional de Pessoas Coletivas (RNPC)](https://justica.gov.pt/) — official register
- [Portal das Finanças](https://www.portaldasfinancas.gov.pt/) — tax authority public search
- **Key field:** NIPC (Número de Identificação de Pessoa Coletiva)

### Italy
- [Registro Imprese](https://www.registroimprese.it/) — official; basic free; documents paid (small fee)
- [InfoCamere](https://www.infocamere.it/) — chamber of commerce backbone
- [InfoImprese](https://www.infoimprese.it/) — search portal
- **Key field:** REA number + codice fiscale (11-digit)

### Greece
- [GEMI (General Commercial Registry)](https://www.businessregistry.gr/) — official, free for basic data
- **Key field:** GEMI number

### Cyprus
- [Department of Registrar of Companies](https://efiling.drcor.mcit.gov.cy/) — official, fully free
- **Key field:** HE number

### Malta
- [Malta Business Registry](https://mbr.mt/) — official; basic free; documents paid
- **Key field:** C number (e.g., `C 12345`)

---

## Central / Eastern Europe

### Slovakia
- [Obchodný register SR (orsr.sk)](https://www.orsr.sk/) — official, fully free, full corporate history
- [Finstat](https://www.finstat.sk/) — free financial data (revenue, profit, employees) parsed from public filings
- [Register podnikov](https://register.peniaze.sk/) — free aggregator
- **Key field:** ICO (8-digit) — e.g., `12345678` + Sro/As court entry (e.g., `Sro 30957/B`)

### Czech Republic
- [Obchodní rejstřík (justice.cz)](https://or.justice.cz/) — official, fully free, includes all filings
- [ARES](https://ares.gov.cz/ekonomicke-subjekty) — Ministry of Finance free register, comprehensive
- [Veřejný rejstřík](https://or.justice.cz/ias/ui/rejstrik) — public register portal
- **Key field:** IČO (8-digit) + spisová značka

### Poland
- [Krajowy Rejestr Sądowy (KRS)](https://wyszukiwarka-krs.ms.gov.pl/) — official National Court Register, fully free
- [REGON](https://wyszukiwarkaregon.stat.gov.pl/) — Statistics Poland register, free
- [Centralna Informacja KRS](https://ekrs.ms.gov.pl/) — KRS document download (free for basic)
- **Key field:** KRS number (10-digit) + REGON (9 or 14 digit)

### Hungary
- [E-cégjegyzék](https://www.e-cegjegyzek.hu/) — official; basic free; full reports paid
- [OPTEN](https://www.opten.hu/) — basic free
- **Key field:** Cégjegyzékszám (e.g., `01-09-123456`)

### Romania
- [Oficiul Național al Registrului Comerțului (ONRC)](https://www.onrc.ro/) — official; basic free; documents paid (small fee)
- [RECOM](https://www.onrc.ro/) — ONRC's online portal
- **Key field:** CUI / J number

### Slovenia
- [AJPES (Agency of the Republic of Slovenia for Public Legal Records)](https://www.ajpes.si/) — official, fully free, includes financial statements
- [PRS (Poslovni register Slovenije)](https://www.ajpes.si/prs/) — business register
- **Key field:** Matična številka (7-digit)

### Croatia
- [Sudski registar](https://sudreg.pravosudje.hr/) — official court register, free
- [Fina](https://www.fina.hr/) — financial agency, free company data
- **Key field:** OIB (11-digit) + MBS

### Bulgaria
- [Търговски регистър (Commercial Register)](https://portal.registryagency.bg/) — official Registry Agency, fully free
- **Key field:** EIK (9 or 13 digit)

### Serbia
- [APR (Agency for Business Registers)](https://www.apr.gov.rs/) — official, fully free
- **Key field:** Matični broj (8-digit)

### Estonia
- [e-Business Register](https://ariregister.rik.ee/) — official, fully free, includes annual reports
- [Krediidiinfo](https://www.krediidiinfo.ee/) — free company info portal
- **Key field:** Registry code (8-digit) + ÄR

### Latvia
- [Lursoft](https://www.lursoft.lv/) — basic free
- [Uzņēmumu reģistrs](https://www.ur.gov.lv/) — official register
- **Key field:** Reg. No. (`40003123456`)

### Lithuania
- [Juridinių asmenų registras](https://www.registrucentras.lt/jar/) — official, fully free
- [Rekvizitai.lt](https://rekvizitai.lt/) — free aggregator
- **Key field:** Įmonės kodas (9-digit)

---

## Nordic

### Sweden
- [Bolagsverket](https://bolagsverket.se/en) — official, basic free; documents paid
- [Allabolag](https://www.allabolag.se/) — comprehensive free aggregator
- [Ratsit](https://www.ratsit.se/) — free company + person search
- **Key field:** Organisationsnummer (`556xxx-xxxx` for AB)

### Norway
- [Brønnøysundregistrene (Brønnøysund Register)](https://www.brreg.no/en/) — official, fully free, all entity types
- [Proff.no](https://www.proff.no/) — free company directory
- **Key field:** Organisasjonsnummer (9-digit)

### Denmark
- [CVR (Det Centrale Virksomhedsregister)](https://datacvr.virk.dk/) — official, fully free, all filings
- [Proff.dk](https://www.proff.dk/) — free directory
- **Key field:** CVR number (8-digit)

### Finland
- [YTJ (Business Information System)](https://www.ytj.fi/) — official, fully free
- [PRH (Patentti- ja rekisterihallitus)](https://www.prh.fi/) — patent and registration office
- **Key field:** Y-tunnus (`1234567-8`)

### Iceland
- [Skráning fyrirtækja (Company Registry)](https://www.skatturinn.is/fyrirtaekjaskra/leit/) — Tax Authority register, free
- [Keldan](https://www.keldan.is/) — basic free
- **Key field:** Kennitala (10-digit national ID for legal entities)

---

## North America

### USA — Federal
- [SEC EDGAR](https://www.sec.gov/edgar) — for public companies + S-1 / 10-K / 10-Q / 8-K + Form D (private placements often disclose investors)
- [USPTO](https://www.uspto.gov/) — patents and trademarks (free public search)
- [SAM.gov](https://sam.gov/) — federal contractor + DUNS / UEI lookup

### USA — States (50 + DC)
Each state has its own Secretary of State business search. Most are free for basic data; some require CAPTCHA solve. Top states by company concentration:

- **California**: [bizfileonline.sos.ca.gov](https://bizfileonline.sos.ca.gov/search/business) — CAPTCHA-walled; entity number is 7-digit with `C` prefix for corporations
- **Delaware**: [icis.corp.delaware.gov](https://icis.corp.delaware.gov/) — basic free; documents paid (Delaware is the dominant US incorporation state)
- **New York**: [dos.ny.gov/corps](https://apps.dos.ny.gov/publicInquiry/) — free
- **Texas**: [direct.sos.state.tx.us](https://direct.sos.state.tx.us/) — basic free; full reports paid
- **Florida**: [search.sunbiz.org](https://search.sunbiz.org/) — fully free including all filings
- **Illinois**: [ilsos.gov/corporatellc](https://www.ilsos.gov/corporatellc/) — free
- **Washington**: [ccfs.sos.wa.gov](https://ccfs.sos.wa.gov/) — free
- **Massachusetts**: [corp.sec.state.ma.us](https://corp.sec.state.ma.us/) — free
- **For other states**: search `<state name> secretary of state business search`

**Aggregator alternative:**
- [OpenCorporates US](https://opencorporates.com/companies/us) — covers all 50 states
- [BizApedia](https://www.bizapedia.com/) — free aggregator

### Canada
- [Corporations Canada](https://ised-isde.canada.ca/cc/lgcy/fdrlCrpSrch.html) — federal incorporation, free
- Provincial registers (free):
  - **Ontario**: [Ontario Business Registry](https://www.ontario.ca/page/ontario-business-registry)
  - **Quebec**: [Registraire des entreprises](https://www.registreentreprises.gouv.qc.ca/) (REQ)
  - **British Columbia**: [BC Registry Services](https://www.bcregistry.gov.bc.ca/)
  - **Alberta**: [Alberta Corporate Registry](https://www.alberta.ca/find-corporation-details)
  - **Saskatchewan / Manitoba / Maritimes**: each province has its own portal

### Mexico
- [Registro Público de Comercio (RPC)](https://www.gob.mx/se/acciones-y-programas/sistema-integral-de-gestion-registral) — federal commercial register
- [SAT (Servicio de Administración Tributaria)](https://www.sat.gob.mx/) — tax authority, RFC lookup
- [Buró de Crédito](https://www.burodecredito.com.mx/) — credit bureau (basic free)
- **Key field:** RFC (12 or 13 chars) + folio mercantil

---

## Latin America

### Brazil
- [Receita Federal CNPJ](https://servicos.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp) — federal tax authority CNPJ lookup, fully free
- [JUCERJA / state Junta Comercial](https://www.jucerja.rj.gov.br/) — per-state commercial registries (each state has its own)
- [REDESIM](https://www.gov.br/empresas-e-negocios/) — federal business portal
- [Consulta CNPJ](https://www.consultacnpj.com/) — free aggregator
- **Key field:** CNPJ (14-digit) — e.g., `12.345.678/0001-90`

### Argentina
- [IGJ (Inspección General de Justicia)](https://www.argentina.gob.ar/justicia/igj) — federal companies, free for basic data
- [AFIP](https://www.afip.gob.ar/) — federal tax authority, CUIT lookup
- **Key field:** CUIT (`30-12345678-9`)

### Chile
- [Registro de Empresas y Sociedades](https://www.registrodeempresasysociedades.cl/) — federal, free
- [SII (Servicio de Impuestos Internos)](https://www.sii.cl/) — tax authority RUT lookup
- **Key field:** RUT (`12.345.678-9`)

### Colombia
- [Cámara de Comercio](https://www.ccb.org.co/) — Bogotá CCB; per-region; basic free
- [Registro Único Empresarial y Social (RUES)](https://www.rues.org.co/) — national consolidated portal, free
- [DIAN](https://www.dian.gov.co/) — tax authority NIT lookup
- **Key field:** NIT (`900.123.456-7`)

### Peru
- [SUNARP (Superintendencia Nacional de los Registros Públicos)](https://www.sunarp.gob.pe/) — official, basic free
- [SUNAT (Superintendencia Nacional de Aduanas y de Administración Tributaria)](https://www.sunat.gob.pe/) — tax, RUC lookup
- **Key field:** RUC (11-digit)

### Uruguay
- [DGI (Dirección General Impositiva)](https://www.dgi.gub.uy/) — tax authority RUT
- [Registro Nacional de Comercio](https://www.dgr.gub.uy/) — commercial register
- **Key field:** RUT (12-digit)

### Other LatAm
- **Costa Rica**: [Registro Nacional](https://www.rnpdigital.com/) — free
- **Panama**: [Registro Público](https://www.rp.gob.pa/) — fully free
- **Ecuador**: [Superintendencia de Compañías](https://www.supercias.gob.ec/) — free

---

## APAC

### Australia
- [ASIC (Australian Securities and Investments Commission)](https://asic.gov.au/online-services/search-asics-registers/) — official; basic free, full extracts paid (~$15-40 AUD)
- [ABN Lookup](https://abr.business.gov.au/) — Australian Business Number lookup, fully free
- [Australian Business Register](https://abr.gov.au/) — federal
- **Key field:** ABN (11-digit) + ACN (9-digit, the company-only number)

### New Zealand
- [Companies Office](https://www.companiesoffice.govt.nz/) — official, fully free, all filings, all entity types
- [NZBN (NZ Business Number)](https://www.nzbn.govt.nz/) — universal entity ID, free
- **Key field:** Company number + NZBN (13-digit)

### Singapore
- [ACRA Bizfile+](https://www.bizfile.gov.sg/) — official; basic free, full reports paid (small fee)
- [Open ACRA Datasets](https://data.gov.sg/) — bulk public data
- **Key field:** UEN (Unique Entity Number)

### Hong Kong
- [ICRIS (Integrated Companies Registry Information System)](https://www.icris.cr.gov.hk/csci/) — official; basic free, full extracts paid (small HK$ fee)
- **Key field:** Company number (7-digit)

### Japan
- [National Tax Agency Corporate Number](https://www.houjin-bangou.nta.go.jp/) — federal tax registration, fully free
- [eGovernment Open Data](https://www.e-gov.go.jp/) — federal open-data portal
- [houjin-bangou.nta.go.jp](https://www.houjin-bangou.nta.go.jp/) — search by company name in Japanese or English
- **Key field:** Corporate Number (13-digit)

### South Korea
- [DART (Data Analysis, Retrieval and Transfer System)](https://dart.fss.or.kr/) — Financial Supervisory Service, public listed company filings, fully free
- [NICE Information Service](https://www.nice.co.kr/) — basic free
- [Court Companies Registry (대법원 인터넷등기소)](http://www.iros.go.kr/) — official, basic free; documents paid
- **Key field:** Business Registration Number (10-digit)

### China
- [National Enterprise Credit Information Publicity System (国家企业信用信息公示系统)](https://www.gsxt.gov.cn/index.html) — federal, free
- [QCC (企查查 / Qichacha)](https://www.qcc.com/) — free for basic; very comprehensive
- [Tianyancha (天眼查)](https://www.tianyancha.com/) — free for basic
- [QiXin](https://www.qixin.com/) — free for basic
- **Key field:** Unified Social Credit Code (USCC, 18-digit) — e.g., `91110108MA01ABCD12`

### Taiwan
- [MOEA Business Registration](https://findbiz.nat.gov.tw/) — Ministry of Economic Affairs, fully free
- **Key field:** Uniform Number (8-digit)

### India
- [MCA21 (Ministry of Corporate Affairs)](https://www.mca.gov.in/) — official, basic free; documents paid (small fee)
- [TIN-NSDL](https://www.protean-tinpan.com/) — tax / TAN lookup
- [GST Portal](https://www.gst.gov.in/) — GST number search, free
- **Key field:** CIN (Corporate Identification Number, 21-digit) + PAN

### Thailand
- [DBD (Department of Business Development)](https://www.dbd.go.th/) — official, basic free
- **Key field:** Tax ID (13-digit)

### Indonesia
- [AHU (Direktorat Jenderal AHU)](https://ahu.go.id/) — Ministry of Law and Human Rights, basic free
- [OSS (Online Single Submission)](https://oss.go.id/) — federal business licensing portal
- **Key field:** NIB (13-digit)

### Malaysia
- [SSM (Suruhanjaya Syarikat Malaysia)](https://www.ssm.com.my/) — Companies Commission, basic search free; reports paid
- **Key field:** Registration number

### Philippines
- [SEC (Securities and Exchange Commission)](https://www.sec.gov.ph/) — federal, basic free
- [DTI (Department of Trade and Industry)](https://www.dti.gov.ph/) — for sole proprietorships
- **Key field:** SEC registration number

### Vietnam
- [National Business Registration Portal (Cổng thông tin quốc gia về đăng ký doanh nghiệp)](https://dangkykinhdoanh.gov.vn/) — official, fully free
- **Key field:** Mã số doanh nghiệp (10-digit)

---

## Middle East / Africa

### UAE
- [DIFC Public Register](https://www.difc.ae/) — Dubai International Financial Centre, fully free
- [ADGM Public Register](https://www.adgm.com/public-registers) — Abu Dhabi Global Market, fully free
- [Department of Economy and Tourism (Dubai, formerly DED) — per-emirate equivalents exist](https://dubaidet.gov.ae/en/) — emirate-specific
- **Key field:** Trade License Number

### Saudi Arabia
- [MCI (Ministry of Commerce and Investment)](https://mc.gov.sa/en/pages/default.aspx) — federal, basic free
- [Najiz (FDS portal)](https://najiz.sa/) — federal portal
- **Key field:** Commercial Registration (CR) number

### Israel
- [Israel Corporations Authority (Rasham HaHavarot)](https://www.gov.il/en/departments/units/corporations) — basic free
- [Magistrate Courts company registry](https://www.gov.il/) — official
- **Key field:** Company number (9-digit)

### South Africa
- [CIPC (Companies and Intellectual Property Commission)](https://www.cipc.co.za/) — official; basic free, reports paid (small fee, R30-50)
- **Key field:** Registration number (e.g., `2020/123456/07`)

### Nigeria
- [CAC (Corporate Affairs Commission)](https://www.cac.gov.ng/) — official; basic free; documents paid
- **Key field:** RC number

### Kenya
- [BRS (Business Registration Service)](https://brs.go.ke/) — federal, fully free
- **Key field:** Registration number

### Egypt
- [GAFI (General Authority for Investment and Free Zones)](https://www.gafi.gov.eg/) — federal, basic free
- **Key field:** Commercial Register Number

### Morocco
- [OMPIC (Office Marocain de la Propriété Industrielle et Commerciale)](http://www.ompic.ma/) — federal, basic free
- **Key field:** RC number

---

## EU-wide / cross-border

- [BRIS (Business Registers Interconnection System)](https://e-justice.europa.eu/topics/registers-business-insolvency-land/business-registers-search-company-eu/general-information-find-company_en) — official EU portal connecting all member-state registers; the canonical first-stop for cross-border EU lookups
- [OpenCorporates](https://opencorporates.com/) — free aggregator with global coverage and limits
- [European e-Justice Portal](https://e-justice.europa.eu/) — all EU public-records portals
- [eIDAS Trust List](https://eidas.ec.europa.eu/) — for verifying digital-signature certificates of registered entities
- [VIES VAT Information Exchange](https://ec.europa.eu/taxation_customs/vies/) — verify EU VAT numbers, fully free

---

## Always-free aggregators (cross-check, not source of truth)

These compile data from multiple registers; useful for quick lookups but always verify against the primary register before publishing:

- [NorthData](https://www.northdata.com/) — EU-focused
- [OpenCorporates](https://opencorporates.com/) — global
- [Finstat (SK)](https://www.finstat.sk/) — Slovakia
- [firmenabc.at (AT)](https://www.firmenabc.at/) — Austria
- [Allabolag (SE)](https://www.allabolag.se/) — Sweden
- [Pappers (FR)](https://www.pappers.fr/) — France
- [Companies House (UK)](https://find-and-update.company-information.service.gov.uk/) — UK (this IS the primary register)
- [Receita Federal (BR)](https://servicos.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp) — Brazil (primary)
- [QCC / Qichacha (CN)](https://www.qcc.com/) — China
- [Bizapedia (US)](https://www.bizapedia.com/) — US states

## Anti-patterns

- ❌ **Don't use paid sources when free covers the case.** D&B Hoovers paid tier, Bisnode, paid Compass.at fields, paid Crunchbase Pro, paid PitchBook, paid Tracxn — all excluded.
- ❌ **Don't conflate the legal entity with the operating reality.** A legal subsidiary (per the foreign business register) might show "5–9 employees" while the parent runs a much larger team. Document both.
- ❌ **Don't trust founder bios for incorporation dates.** Always verify against the actual register entry. Bio dates often reflect informal predecessor activity, not legal incorporation.
- ❌ **Don't accept investor names from aggregators alone.** A named "VC" might not exist as a registered firm. Verify by checking the investor's own portfolio page.
- ❌ **Don't skip the EU BRIS check** for entities with cross-border EU operations — it surfaces subsidiary structures aggregators often miss.

## When to load this file

Load `registers.md` when:
- The entity HQ is non-US, OR
- The entity has subsidiaries in multiple jurisdictions, OR
- The §3.4 Related Entities section needs to verify any non-US legal entity, OR
- The cross-validation pass surfaces a foreign incorporation reference

Skip loading if the entity is purely US-domestic and a single-state Secretary of State search covers it.
