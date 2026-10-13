# Review of CI workflow with pinned runner image and packages

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-019 |
| CrossReference | [MIL-001], [RC-018], [QC-WF-001], [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [5d8fbc7] |

---

## Artifact Under Review

- Instance reviewed: `.gitea/workflows/ci.yml` (changed since [RC-018])
- Checklist used: [QC-WF-001], [QC-YML-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

### QC-WF-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | See the YAML table of this record: Pass. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | File is `.gitea/workflows/ci.yml`; no copy under `.github/workflows/`. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | `name`, `on` (push and pull_request with `branches`, `paths-ignore`) and `jobs` are declared. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | Header states purpose, triggers, inputs, secrets (none), outside changes (none), runner and the milestone. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | Job `Run pytest`; steps have unique descriptive names. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | `tests/test_workflows.py` (pytest 9.1.1, PyYAML 6.0.3) passes; `actionlint` is still not installed. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | Workflow and job both declare `permissions: contents: read`. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | `actions/checkout@v4.2.2` and `actions/setup-python@v5.6.0`: exact release tags, checked by a test. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | No secrets are used. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | No `${{ }}` expression is used inside a `run:` script. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | N-A | No `pull_request_target` or `workflow_run` trigger. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | N-A | The workflow changes nothing outside the repository. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | N-A | No token is used. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | `runs-on: mypass-ci` and `timeout-minutes: 10`. |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | `concurrency` with `cancel-in-progress: true` for a check. |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | `branches` and `paths-ignore` filter the triggers. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | Runner image pinned by digest `sha256:c58e2b36...80ff43` through the local tag `mypass-ci-ubuntu:c58e2b364da0` (run 1227 pulled that tag); `libtk8.6=8.6.14-1build1` and `xvfb=2:21.1.12-1ubuntu1.8` are exact in `env`; Python tools are pinned in pyproject.toml. Transitive apt dependencies come from the pinned image's archive and are not listed individually. |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | Optional: the install takes seconds; a cache would not matter. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | Pass | ruff, mypy, yamllint and pytest name tool, file and reason in their output. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | Pass | Longest `run:` block is four lines. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | Pass | One workflow; no logic shared with another workflow. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pass | Run 1227 (pull request) succeeded on Gitea 1.27.3 with act_runner v0.6.1 on the own runner: 41 passed, 1 skipped; the job log shows `docker pull image=mypass-ci-ubuntu:c58e2b364da0`. A digest label (`@sha256`) is ignored by act_runner 0.6.1 (run 1223 fell back to the default image); recorded in the header. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | N-A | Optional: not a reusable workflow. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | Pass | `tests/test_workflows.py` runs in CI on every pull request (valid YAML, keys, permissions, runner, script length). |

### QC-YML-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | `yaml.safe_load` (PyYAML 6.0.3) parses `ci.yml` in `tests/test_workflows.py`; yamllint's `key-duplicates` rule passes. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | yamllint 1.38.0 passes: 2-space indentation, LF, final newline, no trailing spaces. |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | `.yamllint.yml` is committed next to the code; the CI step runs it with no `disable` comments. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` | Pass | `python-version` value `"3.13"` is quoted; `on` is a host key, covered by `truthy: check-keys: false` with a comment. |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it | Pass | Only plain mappings, sequences and strings are used. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool | Pass | No secret is written in either file. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it | Pass | Longest `run:` block is four lines (limit five). |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) | Pass | No block is repeated. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them | Pass | No anchors, aliases or merge keys. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | Fail | Optional: no schema validator (such as actionlint) is installed locally; `tests/test_workflows.py` covers required keys instead. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | Both files have a header comment on purpose, reader and decision (MIL-001). |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) | Pass | kebab-case keys (`runs-on`, `timeout-minutes`, `cancel-in-progress`) as Actions expects. |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters | Pass | `run: |` blocks; the trailing newline does not matter for them. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository | Pass | `ci.yml` and `.yamllint.yml`: lowercase, `.yml` throughout. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool | Pass | `tests/test_workflows.py` and yamllint exercise the file without a runner. |

## Overall Verdict

Go: every Mandatory criterion of QC-WF-001 and QC-YML-001 passes. Corrections to earlier records: RC-013 and RC-018 said the host had no runner; that was wrong, because the repository API does not list instance-level runners. A shared runner (ubuntu-latest) existed and ran CI from PR 26 on; CI was red for PRs 28 to 30 and the main pushes after them (no Tk library in its image) until PR 32. The workflow now runs only on the own pinned runner. Mode: autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Validate the workflow with actionlint when available (YAML optional criterion 10) | S01 | 2026-10-19 |

---

[MIL-001]: ../../milestones/mil-001-baseline-and-tooling.md
[RC-018]: ./rc-018-ci-workflow-rereview.md
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
[5d8fbc7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/commit/5d8fbc73d52d5b62f962e883dfb64a7fe5b866f7
