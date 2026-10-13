# MIL-003 Tkinter user interface

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [US-001], [MIL-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether the window matches the assignment's layout and the generator is connected, before saving is added.

## Deliverable

A runnable Tkinter window with logo canvas, grid layout, default email, initial focus and a working Generate Password button that fills the field and the clipboard.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m mypass` opens a window titled "Password Manager" | Met | Any one not met |
| 2 | logo canvas is 200 x 200 with 20 px padding | Met | Any one not met |
| 3 | grid has website, email, password entries and both buttons as in the assignment | Met | Any one not met |
| 4 | Generate Password fills the field and the clipboard | Met | Any one not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | the user interface (UI) calls `generate_password` |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 objectives 1 and 3; US-001.01, US-001.02, US-001.03, US-001.06 | [BC-001], [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-16 — within the one-week window of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create window and logo canvas | Create the `Tk` window titled "Password Manager" with padding, and a 200 x 200 canvas that draws the logo at its centre (100, 100) using `PhotoImage`; challenge 1 of the assignment. | Yes | US-001.01 |
| 2 | Lay out the grid | Place labels, entries (width 35, 35, 21) and the Generate Password and Add buttons on the three-column, five-row grid, with the Add button spanning two columns, as in challenge 2. | Yes | US-001.01 |
| 3 | Set initial focus and default email | Give the website entry focus on start and pre-fill the email entry with a default email using `focus` and `insert`. | Yes | US-001.06 |
| 4 | Wire Generate Password to the clipboard | The button calls `generate_password`, fills the password entry and copies the value with Tkinter's clipboard methods. | Yes | US-001.02, US-001.03 |
| 5 | Add application entry point | `python -m mypass` and a `main.py` script start the UI; UI code stays in a thin module so logic is testable without a display. | No |  |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[MIL-002]: ./mil-002-password-generator-logic.md
