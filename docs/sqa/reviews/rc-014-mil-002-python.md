# Review of MIL-002 Python source and tests

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: `src/mypass/password_generator.py` and `tests/test_password_generator.py` delivered by [MIL-002]
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
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | `generate_password`, `letter_count`, `symbol_count`, `number_count` state purpose. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format` leaves files unchanged and `ruff check` passes (ruff 0.17.0, `[tool.ruff]` in pyproject.toml); no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All functions in `src/` and `tests/` are annotated, including `-> None`. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `except` clauses exist. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults and no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | No files, locks or connections are opened. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module, constant and function carry Doxygen `@file`/`@brief` comments and a docstring. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` or logging; the password is returned, not logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists: the Project Plan plans none for this small project; the code has no classes. Deviation recorded here. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_password_generator.py` has 7 behaviour tests over 1000 calls, independent of order and network; 16 tests pass in total. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypass` passes `mypy --strict` (mypy 2.4.0) with no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Dev dependencies are pinned exactly in `pyproject.toml`; runtime dependencies are empty. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Character sets and count ranges are read from `constants.py`, not repeated. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `password_generator.py` imports only `random` and `mypass.constants`; no GUI, no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One function with one reason to change (the generation rule); the random source is a module-level `SystemRandom`. |

## Overall Verdict

Go: every Mandatory criterion of QC-PY-001 passes; criterion 10 is N-A because no Design Class Diagram exists (recorded in RC-011). Mode: autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| none | S01 | 2026-10-13 |

---

[MIL-002]: ../../milestones/mil-002-password-generator-logic.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
