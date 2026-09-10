# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repository is

`BrinksHomeKHenseler/BrinksHomeKHenseler` is a **GitHub profile repository**.
Because the repository name matches the account name, `README.md` renders
directly on <https://github.com/BrinksHomeKHenseler>. It is public.

There is no application code here — the deliverable is documentation plus the
small amount of config that keeps it tidy.

## Repository layout

| Path | Purpose |
| --- | --- |
| `README.md` | The profile page. Anything changed here is publicly visible. |
| `LICENSE` | MIT. |
| `CLAUDE.md` | This file. |
| `.editorconfig` | Shared editor defaults (LF, UTF-8, 2-space indent; CRLF + 4 spaces for PowerShell). |
| `.gitattributes` | Line-ending normalization and binary/export rules. |
| `.gitignore` | OS cruft, editor files, Node tooling, local secrets. |
| `.markdownlint-cli2.jsonc` | Markdown lint rules used by CI and locally. |
| `.github/dependabot.yml` | Weekly GitHub Actions version bumps. |
| `.github/workflows/lint.yml` | CI: Markdown lint + YAML syntax check. |
| `.github/scripts/check_yaml.py` | The YAML syntax check, runnable locally. |

## Checks to run before pushing

```bash
# Markdown lint (same version CI pins)
npx --yes markdownlint-cli2@0.23.2

# YAML syntax
python3 -m pip install --quiet pyyaml   # once
python3 .github/scripts/check_yaml.py
```

Both must pass; `lint.yml` runs them on every push to `main` and every PR.

## Content rules — this is a public page

Kenneth works in IT infrastructure, identity, and collaboration systems at
Brinks Home. That means most of his day-to-day context is **not** publishable.
When editing `README.md`:

- **Never** include internal hostnames, server names, IP ranges, tenant IDs,
  internal URLs, ticket numbers, vendor contract details, or internal project
  or team names.
- Keep technology references generic and public (for example "Exchange Online",
  "Entra ID", "VDI") rather than naming internal deployments.
- Do not add credentials, tokens, or connection strings — not even redacted
  examples.
- Do not claim skills, certifications, employers, or job titles that Kenneth
  has not stated himself. If a detail is uncertain, leave it out and ask.
- The email address `khenseler@brinkshome.com` is already published here
  deliberately. Do not add other personal contact details without asking.

## Style

- Keep the README skimmable: short intro, tables or bullets, no walls of text.
- Badges come from `img.shields.io` only — avoid third-party stat services that
  can rate-limit or disappear.
- Prefer plain Markdown; inline HTML is allowed but keep it minimal.
- Prose lines may run long (`MD013` is disabled) — do not hard-wrap mid-sentence.

## Git conventions

- Default branch is `main`.
- Work on a topic branch and push with `git push -u origin <branch>`.
- Do not open a pull request unless asked.
