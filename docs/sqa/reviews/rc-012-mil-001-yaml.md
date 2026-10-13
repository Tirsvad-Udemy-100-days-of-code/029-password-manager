# Review of MIL-001 YAML files

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [MIL-001], [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [ea1b121] |

---

## Artifact Under Review

- Instance reviewed: `.gitea/workflows/ci.yml` and `.yamllint.yml` delivered by [MIL-001]
- Checklist used: [QC-YML-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

### QC-YML-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | `yaml.safe_load` (PyYAML 6.0.3) parses `ci.yml` in `tests/test_workflows.py`; yamllint's `key-duplicates` rule passes. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | yamllint 1.38.0 passes: 2-space indentation, LF, final newline, no trailing spaces. |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | `.yamllint.yml` is committed next to the code; the CI step runs it with no `disable` comments. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` | Pass | `python-version` value `"3.13"` is quoted; `on` is a host key, covered by `truthy: check-keys: false` with a comment. |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it | Pass | Only plain mappings, sequences and strings are used. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool | Pass | No secret is written in either file. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it | Pass | Longest `run:` block is three lines. |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) | Pass | No block is repeated. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them | Pass | No anchors, aliases or merge keys. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | Fail | Optional: no schema validator (such as actionlint) is installed locally; `tests/test_workflows.py` covers required keys instead. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | Both files have a header comment on purpose, reader and decision (MIL-001). |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) | Pass | kebab-case keys (`runs-on`, `timeout-minutes`, `cancel-in-progress`) as Actions expects. |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters | Pass | `run: |` blocks; the trailing newline does not matter for them. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository | Pass | `ci.yml` and `.yamllint.yml`: lowercase, `.yml` throughout. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool | Pass | `tests/test_workflows.py` and yamllint exercise the file without a runner. |

## Overall Verdict

Go: every Mandatory criterion of QC-YML-001 passes; the optional criterion 10 fails and has an action item. Mode: autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Validate the workflow with actionlint once available (optional criterion 10) | S01 | 2026-10-19 |

---

[MIL-001]: ../../milestones/mil-001-baseline-and-tooling.md
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
[ea1b121]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/commit/ea1b1217349a64c536b312c41b8dd7236ade4c62
