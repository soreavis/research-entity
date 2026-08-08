# Security policy

## Scope of this skill

`research-entity` ships only Markdown text — there is no executable code in the published artifact, no server, no auth flow, and no user data is collected or stored. The skill runs inside [Claude Code](https://docs.claude.com/claude-code), and the only outbound network calls it makes are the web searches and URL fetches the user's research request triggers.

This narrows the meaningful security surface to:

| Surface | Risk | Treatment |
|---|---|---|
| **Factual content** | A wrong claim about a real company could damage its reputation or lead a reader to a costly decision | Anti-hallucination contract + cross-validation + confidence labeling — report via the **factual-correction** issue template |
| **Source URLs** | A dead URL in a register/source file could redirect to a malicious or impersonating domain | Report via a regular issue with the replacement primary-source URL |
| **Dispatch logic in `SKILL.md`** | A crafted entity name or argument could route to the wrong template or skip verification steps | Report privately via Security Advisory (below) if exploitable |
| **GitHub Actions workflows** | CI reads repo files only | `permissions:` scoped to `contents: read`, no secrets, only `actions/*` actions |

## What to report privately vs publicly

**Report privately** via [GitHub Security Advisory](https://github.com/soreavis/research-entity/security/advisories/new) if you discover:

- A way to make the skill exfiltrate conversation data or credentials through a crafted research target
- A prompt-injection vector in a segment file that could override the anti-hallucination contract
- A supply-chain risk in the actions referenced in `.github/workflows/`
- An impersonation issue (e.g. a fork republishing under a confusingly similar name)

**Report publicly** via regular issues for:

- Wrong facts in register/source files (use **factual-correction**)
- Dead or moved source URLs
- A dossier section that produced ungrounded output (that's a bug in the skill's guardrails)

## Disclosure timeline

- Acknowledgement target: **72 hours**
- Coordinated disclosure preferred — please do not publish a working exploit before a patch lands

## Versions covered

Only the latest state of `main` is actively maintained. There is no LTS branch.

## Acknowledgement

Reporters of confirmed vulnerabilities are credited in `CHANGELOG.md` under "Security", unless they prefer anonymity.
