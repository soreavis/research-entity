@../AGENTS.md

The same guidance applies to Claude Code. The import resolves relative to this
file, hence `../`; an import loads the content, a link is only a suggestion.

This lives in `.claude/` rather than the repo root on purpose: at the root it
would sit at the plugin root once installed, where it is never loaded, and
`claude plugin validate --strict` flags it.
