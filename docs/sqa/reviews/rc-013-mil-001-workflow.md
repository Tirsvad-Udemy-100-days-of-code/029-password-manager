# Review of MIL-001 CI workflow

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [MIL-001], [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [ea1b121] |

---

## Artifact Under Review

- Instance reviewed: `.gitea/workflows/ci.yml` delivered by [MIL-001]
- Checklist used: [QC-WF-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

### QC-WF-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | See the YAML record RC-012: Pass. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | File is `.gitea/workflows/ci.yml`; no copy under `.github/workflows/`. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | `name`, `on` (push and pull_request with `branches`, `paths-ignore`) and `jobs` are declared. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | Header states purpose, triggers, inputs, secrets (none), outside changes (none), runner and the milestone. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | Job `Run pytest`; steps have unique descriptive names. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | `tests/test_workflows.py` is the project's workflow validation test (pytest 9.1.1, PyYAML 6.0.3); `actionlint` is not installed. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | Workflow and job both declare `permissions: contents: read`. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | `actions/checkout@v4.2.2` and `actions/setup-python@v5.6.0`: exact release tags, checked by a test. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | No secrets are used. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | No `${{ }}` expression is used inside a `run:` script. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | N-A | No `pull_request_target` or `workflow_run` trigger. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | N-A | The workflow changes nothing outside the repository. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | N-A | No token is used. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | `runs-on: ubuntu-latest` and `timeout-minutes: 10`. |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | `concurrency` with `cancel-in-progress: true` for a check. |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | `branches` and `paths-ignore` filter the triggers. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | Python version in `env.PYTHON_VERSION`; dev tools pinned exactly in `pyproject.toml`. |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | Optional: the install takes seconds; a cache would not matter. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | Pass | ruff, mypy, yamllint and pytest name tool, file and reason in their output. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | Pass | Longest `run:` block is three lines. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | Pass | One workflow; no logic shared with another workflow. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Fail | Gitea 1.27.3 (API `/version`) has no registered runner (`actions/runners` total_count 0), so the workflow has not run on its host. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | N-A | Optional: not a reusable workflow. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | Pass | `tests/test_workflows.py` runs in CI on every pull request (valid YAML, keys, permissions, runner, script length). |

## Overall Verdict

Go-with-conditions: criterion 22 (verified on the instance that runs it) fails because the host has no runner, so the workflow cannot yet be run. Every other Mandatory criterion passes. The file is merged unproven; the condition is closed by the first successful run. Mode: autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Register a Gitea Actions runner for the organisation or repository and record the first run of CI (Gitea 1.27.3) | S01 | 2026-10-19 |

---

[MIL-001]: ../../milestones/mil-001-baseline-and-tooling.md
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
[ea1b121]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/commit/ea1b1217349a64c536b312c41b8dd7236ade4c62
