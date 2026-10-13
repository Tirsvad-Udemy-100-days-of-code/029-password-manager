# MIL-004 Save and validate

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [US-001], [MIL-003] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether entries are saved safely: only after confirmation, never with empty fields, and the form is reset afterwards.

## Deliverable

An Add button that validates input, asks for confirmation, appends `website | email | password` to `data.txt`, clears the fields and informs the user, with tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Add with an empty website or password shows a warning and writes nothing | Met | Any one not met |
| 2 | Add with all fields shows the confirmation; Cancel writes nothing | Met | Any one not met |
| 3 | OK appends exactly one line in the format `website \| email \| password` | Met | Any one not met |
| 4 | the website and password fields are cleared and focus returns to the website entry | Met | Any one not met |
| 5 | tests cover these cases without a display | Met | Any one not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | the Add button lives in the user interface (UI) |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 objective 4, success criterion 4; US-001.04, US-001.05, US-001.06 | [BC-001], [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-17 — within the one-week window of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement save_entry logic | A function that appends one line (website, email and password separated by a space, a pipe and a space) to `data.txt` (path from `constants.py`) in append mode, plus a validation function for empty fields; called by the UI. | Yes | US-001.04 |
| 2 | Validate empty fields | Show a `messagebox.showwarning` when the website or password is empty and stop the save. | Yes | US-001.05 |
| 3 | Confirm before saving | Use `messagebox.askokcancel` with the entered values; save only when the answer is OK. | Yes | US-001.04 |
| 4 | Clear fields after saving | Delete the website and password text, return focus to the website entry and show a success `showinfo`. | Yes | US-001.06 |
| 5 | Test saving and validation | pytest tests using a temporary file and a stubbed message box for empty, cancelled and confirmed saves. | No |  |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[MIL-003]: ./mil-003-tkinter-user-interface.md
