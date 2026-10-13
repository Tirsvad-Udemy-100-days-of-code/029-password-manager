# MIL-005 Documentation and publishing

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [US-001], [MIL-004] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [b4c2611] |

---

## Purpose

Decide whether the project can be published: README follows the template, screenshots exist, the wiki is complete in three languages and the repository is described.

## Deliverable

README.md from the template, screenshots, a wiki in English, Danish and Bahasa Malaysia, and the repository description and topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `check-readme.sh` passes | Met | Any one not met |
| 2 | README commands for Windows PowerShell, Linux Debian and macOS are standard `venv` commands and the Windows ones were run | Met | Any one not met |
| 3 | wiki has the same pages in en, da and ms, each with a screenshot | Met | Any one not met |
| 4 | repository description and at least 5 topics are set | Met | Any one not met |
| 5 | `pytest` and `doxygen Doxyfile` pass on the final branch | Met | Any one not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] | documented behaviour must be complete |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 objective 5, success criteria 5 and 6; US-001.07 | [BC-001], [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-19 — within the one-week window of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write README | README.md using the template headings: requirements, set up for Windows PowerShell, Linux Debian and macOS (create `.venv`, `python -m pip install --upgrade pip`), run, tests, continuous integration (CI), source documentation, layout and licence. | Yes | US-001.07 |
| 2 | Capture screenshots | Run the app and save screenshots of the empty form, the generated password and the confirmation dialog under `docs/images/` for the README and the wiki. | Yes | US-001.07 |
| 3 | Write the wiki in three languages | Wiki pages Home, Installation, Usage, Development and Testing in English, Danish and Bahasa Malaysia, following the structure of the TirSystem github-action wiki, with a language switch on each page. | Yes | US-001.07 |
| 4 | Set repository description and topics | Update the repository on the git host through its application programming interface (API) with a one-sentence description and topics such as python, tkinter, password-manager, password-generator, 100-days-of-code, udemy, pytest. | Yes | US-001.07 |
| 5 | Final verification | Run pytest, Doxygen and the README commands on a clean clone and record the results in the milestone's review record. | No |  |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[MIL-004]: ./mil-004-save-and-validate.md
[b4c2611]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/commit/b4c26115f240097da76782a8e84a5367198226b5
