# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [b4c2611] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | [SA-001], [UCD-001] | [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [US-001], [UCD-001] | [RC-002] |
| [UCD-001] | Use Case Diagram | en | it | [BC-001], [SA-001] | [US-001] | [RC-003] |
| [US-001] | User Story | en | it | [BC-001], [UCD-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-004] |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | none (no checklist; accepted by S01) |
| [MIL-001] | Milestone | en | it | [BC-001], [US-001] | [MIL-002] | [RC-005] |
| [MIL-002] | Milestone | en | it | [BC-001], [US-001], [MIL-001] | [MIL-003] | [RC-006] |
| [MIL-003] | Milestone | en | it | [BC-001], [US-001], [MIL-002] | [MIL-004] | [RC-007] |
| [MIL-004] | Milestone | en | it | [BC-001], [US-001], [MIL-003] | [MIL-005] | [RC-008] |
| [MIL-005] | Milestone | en | it | [BC-001], [US-001], [MIL-004] | - | [RC-017] (revision 2; first [RC-009]) |
| [ADR-0001] | Architecture Decision Record | - | - | [BC-001], [SA-001] | [MIL-001], [MIL-003] | [RC-010] |
| MIL-001 Python (src, tests) | Python Source Code | - | - | [MIL-001], [ADR-0001] | - | [RC-011] |
| MIL-001 YAML (ci.yml, .yamllint.yml) | YAML File | - | - | [MIL-001] | - | [RC-012] |
| MIL-001 CI workflow (ci.yml) | CI Workflow | - | - | [MIL-001] | - | [RC-019] (supersedes [RC-018] and [RC-013]) |
| MIL-002 Python (generator, tests) | Python Source Code | - | - | [MIL-002] | - | [RC-014] |
| MIL-003 Python (ui, tests) | Python Source Code | - | - | [MIL-003], [ADR-0001] | - | [RC-015] |
| MIL-004 Python (storage, ui save, tests) | Python Source Code | - | - | [MIL-004] | - | [RC-016] |

## Coverage Notes

- No instance exists yet for DM, SSD, OC, SD, DCD, ERD, UC, DICT, KPI, BMC, BPMN or RA: the project is small and the Project Plan needs none of them.
- `-` in Upstream means foundational; in Downstream, nothing is built on it yet.
- RC-001 to RC-019 are autonomous stand-in reviews, not independent.

---

[BC-001]: ../business-case.md
[MIL-001]: ../milestones/mil-001-baseline-and-tooling.md
[MIL-002]: ../milestones/mil-002-password-generator-logic.md
[MIL-003]: ../milestones/mil-003-tkinter-user-interface.md
[MIL-004]: ../milestones/mil-004-save-and-validate.md
[MIL-005]: ../milestones/mil-005-documentation-and-publishing.md
[PP-001]: ../project-plan.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-use-case-diagram.md
[RC-004]: ./reviews/rc-004-user-stories.md
[RC-005]: ./reviews/rc-005-mil-001.md
[RC-006]: ./reviews/rc-006-mil-002.md
[RC-007]: ./reviews/rc-007-mil-003.md
[RC-008]: ./reviews/rc-008-mil-004.md
[RC-009]: ./reviews/rc-009-mil-005.md
[SA-001]: ../stakeholder-analysis.md
[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
[b4c2611]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/commit/b4c26115f240097da76782a8e84a5367198226b5
[ADR-0001]: ../adr/adr-0001-clipboard-without-pyperclip.md
[RC-010]: ./reviews/rc-010-adr-0001.md
[RC-011]: ./reviews/rc-011-mil-001-python.md
[RC-012]: ./reviews/rc-012-mil-001-yaml.md
[RC-013]: ./reviews/rc-013-mil-001-workflow.md
[RC-014]: ./reviews/rc-014-mil-002-python.md
[RC-015]: ./reviews/rc-015-mil-003-python.md
[RC-016]: ./reviews/rc-016-mil-004-python.md
[RC-017]: ./reviews/rc-017-mil-005-rev2.md
[RC-018]: ./reviews/rc-018-ci-workflow-rereview.md
[RC-019]: ./reviews/rc-019-ci-workflow-pinned.md
