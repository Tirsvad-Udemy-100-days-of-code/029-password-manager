# MIL-001 Baseline and tooling

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether the repository foundation (project configuration, layout, ignore rules, documentation tooling and continuous integration (CI)) is solid enough to build the application on.

## Deliverable

A repository with pyproject.toml, src/ and tests/ layout, constants.py, Python .gitignore, Doxyfile, a CI workflow and an Architecture Decision Record (ADR) on the clipboard approach.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pip install -e .[dev]` in a fresh `.venv` succeeds on Python 3.13 | Met | Any one not met |
| 2 | `pytest` runs (even with a single smoke test) and passes | Met | Any one not met |
| 3 | `.gitignore` excludes `.venv`, `.env` and `data.txt` | Met | Any one not met |
| 4 | `doxygen Doxyfile` runs without errors | Met | Any one not met |
| 5 | CI workflow file is present and valid YAML | Met | Any one not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 objective 5, success criteria 2 and 3 | [BC-001], [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — within the one-week window of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml | Project configuration with `requires-python = ">=3.13"`, no runtime dependencies, `pytest` as an optional `dev` dependency, a `src` layout and pytest settings (`testpaths`, `pythonpath`). Gives S02 one file that explains how the project installs and tests. | No |  |
| 2 | Add Python .gitignore | Standard Python ignore rules plus `.env`, `data.txt` and Doxygen output (`docs/doxygen/`). Keeps tokens and saved passwords out of the repository. | No |  |
| 3 | Create src/ and tests/ layout with constants.py | Create package `mypass` under `src/` with `constants.py` holding window title, padding, file name and password rules, and a `tests/` folder with a smoke test. The assignment logo is copied to `src/mypass/assets/logo.png`. | No |  |
| 4 | Add Doxyfile | Doxygen configuration for `src/` with Python optimisation enabled and output under `docs/doxygen/`, so source comments can be built into HTML. | No |  |
| 5 | Add CI workflow | Gitea Actions workflow that sets up Python 3.13, installs the project with the `dev` extra and runs pytest on every push and pull request. | No |  |
| 6 | Write ADR on clipboard without pyperclip | Record the decision to use Tkinter clipboard_clear and clipboard_append instead of the lecture's `pyperclip`, because S03 wants no runtime dependencies. | No |  |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
