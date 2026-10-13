# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [b4c2611] |

---

## Purpose

This analysis names the people who care about the MyPass project, how much power
and interest each has, and what they need from it. It uses the Power/Interest
grid and maps each concern to a FURPS+ (Functionality, Usability, Reliability, Performance, Supportability, plus constraints) attribute.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finish the Day 29 assignment with work worth sharing |
| S02 | Udemy coursists | Fellow course participants | Udemy 100 Days of Code | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors browsing for ideas | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, accepts the plan, and reviews every
  artifact; nothing proceeds without them.
- **Keep Informed (S02):** cannot change the project but are its main readers; they
  need accurate README and wiki content.
- **Monitor (S03):** casual visitors; they are served by a good first impression
  (description, topics, README) and need no direct communication.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Assignment is complete and passes its own tests | Functionality |
| S01 | Work follows the planning-first process | Supportability |
| S02 | Assignment function names (`generate_password`, `save`) are used | Functionality |
| S02 | Code is readable and runs after following the README | Usability |
| S03 | Repository explains itself in seconds | Usability |
| S03 | No runtime dependencies to install | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Accepted plan, review records, run summary | All |
| S02 | README and wiki (en, da, ms) | Once per release | Run and test instructions, screenshots | Documentation milestone |
| S03 | Repository description, topics, README | Once | Repository metadata | Documentation milestone |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| The lecture uses `pyperclip`, but viewers want no runtime dependencies | S02, S03 | Use Tkinter's clipboard; record the decision in an Architecture Decision Record (ADR) |
| Assignment structure is one script, but the course asks for `src/` and `tests/` | S02, S01 | Keep the assignment's function names and split user interface (UI) from logic in modules |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Complete, tested assignment | Objectives 1 to 5 of [BC-001] |
| S02 | Runnable, readable code with documentation | Objectives 2, 4 and 5 of [BC-001] |
| S03 | Repository description, topics and README | Objective 5 of [BC-001] |

## Sign-Off

Pending the review of S01 (stand-in review in autonomous mode).

---

[BC-001]: ./business-case.md
[b4c2611]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/commit/b4c26115f240097da76782a8e84a5367198226b5
