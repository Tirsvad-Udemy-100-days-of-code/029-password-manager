# MIL-002 Password generator logic

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [US-001], [MIL-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [b4c2611] |

---

## Purpose

Decide whether the password generation logic is correct and testable without a display before it is wired to the interface.

## Deliverable

A `generate_password` function in the `mypass` package that returns a shuffled password of 8-10 letters, 2-4 symbols and 2-4 digits, with passing tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `generate_password()` returns a `str` for 1000 consecutive calls | Met | Any one not met |
| 2 | every result has 8-10 letters, 2-4 symbols and 2-4 digits | Met | Any one not met |
| 3 | all characters come from the constants lists | Met | Any one not met |
| 4 | tests pass and do not import Tkinter | Met | Any one not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | pyproject, layout and constants must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 objective 2, success criterion 1; US-001.02 | [BC-001], [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-15 — within the one-week window of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add generator constants | Put the letters, numbers and symbols lists and the min and max counts in `constants.py`, as in the assignment's lists, so rules are changed in one place. | No |  |
| 2 | Implement generate_password | Build the password with list comprehensions, combine the three lists, `shuffle` them and `join`; keeps the assignment's function name `generate_password` and takes no input. | Yes | US-001.02 |
| 3 | Test generate_password | pytest tests for length bounds, character classes, randomness (calls differ over many runs) and that only allowed characters appear. | No |  |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[MIL-001]: ./mil-001-baseline-and-tooling.md
[b4c2611]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/commit/b4c26115f240097da76782a8e84a5367198226b5
