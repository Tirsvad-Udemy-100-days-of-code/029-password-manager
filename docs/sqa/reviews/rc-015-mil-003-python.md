# Review of MIL-003 Python source and tests

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: `src/mypass/ui.py`, `src/mypass/__main__.py`, `src/main.py` and `tests/test_ui.py` delivered by [MIL-003]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

### QC-PY-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `snake_case` functions, `UPPER_SNAKE` constants, `test_<behavior>` test names. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | `PasswordManagerApp`, `generate_password_action`, `website_entry`, `add_button` state purpose; no abbreviations. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format` leaves files unchanged and `ruff check` passes (ruff 0.17.0, `[tool.ruff]` in pyproject.toml); no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All functions in `src/` and `tests/` are annotated, including `-> None`. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `except` clauses exist. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults and no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | No files are opened by this code; the logo is read by `tk.PhotoImage(file=...)`. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module, constant and function carry Doxygen `@file`/`@brief` comments and a docstring. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` or logging; the password is returned, not logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists: the Project Plan plans none for this small project; the code has no classes. Deviation recorded here. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_ui.py` covers title, canvas size, logo position, grid positions, default email, generation, clipboard and replacement; 25 pass, 1 skipped (focus assertion needs a focused window). The focus target was verified by hand with `focus -lastfor` (`.!entry` is the website entry). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypass` passes `mypy --strict` (mypy 2.4.0) with no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Dev dependencies are pinned exactly in `pyproject.toml`; runtime dependencies are empty. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Character sets and count ranges are read from `constants.py`, not repeated. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `ui.py` (delivery layer) imports `password_generator` and `constants`; those import no GUI code; no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | `PasswordManagerApp` builds and handles the window; password rules stay in `password_generator`; `save` is a documented no-op until MIL-004. |

## Overall Verdict

Go: every Mandatory criterion of QC-PY-001 passes; criterion 10 is N-A because no Design Class Diagram exists (recorded in RC-011). Mode: autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| none | S01 | 2026-10-13 |

---

[MIL-003]: ../../milestones/mil-003-tkinter-user-interface.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
