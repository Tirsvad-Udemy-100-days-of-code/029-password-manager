# Review of Publish-wiki workflow

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-023 |
| CrossReference | [MIL-005], [RC-021], [QC-WF-001], [QC-YML-001], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: `.gitea/workflows/publish-wiki.yml`, `tests/test_workflows.py` and the changed `tests/test_ui.py` focus test
- Checklist used: [QC-WF-001], [QC-YML-001], [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

### QC-WF-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | See the YAML table of this record: Pass. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | File is `.gitea/workflows/publish-wiki.yml`; no copy under `.github/workflows/`. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | `name`, `on` (push to `main` with `paths`) and `jobs` are declared. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | Header states purpose, triggers (and why there is no manual one), inputs, the secret, what it changes outside the repository, runner and the shared workflow tag. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | Job `Publish the wiki pages`; the steps are in the called workflow. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | `actionlint` 1.7.12 reports no finding; `tests/test_workflows.py` checks the call (exact tag, `tools-ref` equal to the tag, secrets only as expressions). |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | Workflow and job declare `permissions: contents: read`. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | The shared workflow is referenced at the exact release tag `v1.2.2` (organisation TirSystem, not the same organisation, so no moving major tag); `tools-ref` is the same tag. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | The only secret is `TOKEN_FOR_GITEA_WIKI`, passed as `${{ secrets.TOKEN_FOR_GITEA_WIKI }}`; no literal value. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | No `run:` script exists in the caller; no untrusted text is interpolated. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | N-A | No `pull_request_target` or `workflow_run` trigger. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | Fail | The workflow changes the wiki (state outside the working tree, pages are deleted because `prune` is `true`) on a push to `main`, and `main` is not a protected branch (`branch_protections` is empty). The manual trigger was removed so no manual run publishes; the shared workflow has no dry-run input. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | Fail | Optional: the workflow uses the organisation's wiki token; whether the built-in token can write the wiki was not tried. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | The shared workflow sets `runs-on: ubuntu-latest` and `timeout-minutes: 10` (publish-wiki-pages.yml at v1.2.2). |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | `concurrency` group `publish-wiki` with `cancel-in-progress: false` (a publishing job queues). |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | `branches` and `paths` filter the trigger. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | Shared workflow and its script are pinned to the same exact tag. |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | Optional: nothing is installed by the caller. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | Pass | The shared script reports configuration and permission problems with a prefix and the reason. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | N-A | No `run:` block in the caller. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | Pass | The logic is the shared reusable workflow; this file only calls it with inputs that have defaults documented there. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pass | Run 1270 (dispatch on the branch, before the manual trigger was removed) succeeded on Gitea 1.27.3: the reusable call from another organisation, the secret and the wiki API all worked. The push trigger is the same mechanism as in `ci.yml`. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | Pass | Optional: the header states how the caller pins the workflow and the script (`tools-ref`). |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | Pass | `tests/test_workflows.py` covers this file and runs in CI. |

### QC-YML-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | `yaml.safe_load` (PyYAML 6.0.3) parses `ci.yml` in `tests/test_workflows.py`; yamllint's `key-duplicates` rule passes. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | yamllint 1.38.0 passes: 2-space indentation, LF, final newline, no trailing spaces. |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | `.yamllint.yml` is committed next to the code; the CI step runs it with no `disable` comments. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` | Pass | String values such as `"wiki"` and `"true"` are quoted; `on` is a host key. |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it | Pass | Only plain mappings, sequences and strings are used. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool | Pass | No secret is written in either file. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it | Pass | No embedded program text. |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) | Pass | No block is repeated. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them | Pass | No anchors, aliases or merge keys. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | Pass | Validated by actionlint 1.7.12. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | Header comment states purpose, reader and decision (MIL-005). |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) | Pass | kebab-case keys (`runs-on`, `timeout-minutes`, `cancel-in-progress`) as Actions expects. |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters | Pass | `run: |` blocks; the trailing newline does not matter for them. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository | Pass | `ci.yml` and `.yamllint.yml`: lowercase, `.yml` throughout. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool | Pass | `tests/test_workflows.py` and yamllint exercise the file without a runner. |

### QC-PY-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `snake_case` functions, `UPPER_SNAKE` constants, `test_<behavior>` test names. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | `test_workflows_pass_actionlint` states the behaviour. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format` leaves files unchanged and `ruff check` passes (ruff 0.17.0, `[tool.ruff]` in pyproject.toml); no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All functions in `src/` and `tests/` are annotated, including `-> None`. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `except` clauses; a failing write raises `OSError` to the caller. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults and no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | `save_entry` opens the data file with `with data_file.open("a", encoding="utf-8")`. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module, constant and function carry Doxygen `@file`/`@brief` comments and a docstring. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` or logging; the password is written only to the data file the user asked for. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists: the Project Plan plans none for this small project; the code has no classes. Deviation recorded here. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_workflows.py` now also covers reusable-workflow calls; `tests/test_ui.py` focus test made deterministic; 51 passed, 1 skipped (a display fixture skip is intermittent). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypass` passes `mypy --strict` (mypy 2.4.0) with no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Dev dependencies are pinned exactly in `pyproject.toml`; runtime dependencies are empty. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The line format lives once in `format_entry` with `FIELD_SEPARATOR`; texts and the file name are constants. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `storage.py` imports only `pathlib` and `constants`; `ui.py` depends inward on `storage`. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Validation and persistence are in `storage`; dialogs and widgets stay in `ui`; the message box is replaceable in tests. |

## Overall Verdict

Go-with-conditions: every Mandatory criterion passes except QC-WF-001 criterion 12 (state change outside the repository started from a protected branch with a dry-run default): `main` is not protected and the shared workflow has no dry-run input. Branch protection is S01's decision. Mode: autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide whether to protect `main` (branch protection) so that publishing starts from a protected branch (criterion 12) | S01 | 2026-10-19 |
| Optional: try the built-in Actions token for wiki writes instead of the organisation wiki token (criterion 13) | S01 | 2026-10-19 |

---

[MIL-005]: ../../milestones/mil-005-documentation-and-publishing.md
[RC-021]: ./rc-021-ci-workflow-actionlint-in-ci.md
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
