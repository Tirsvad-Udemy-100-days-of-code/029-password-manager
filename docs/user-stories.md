# User Story

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [BC-001], [SA-001], [UCD-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [b4c2611] |

---

## Purpose and Scope

The stories cover the single epic of the MyPass password manager (Udemy Day 29): the user stories of the assignment, delivered through gateways MIL-001 to MIL-005. Actors are those of [UCD-001], each traced to a stakeholder of [SA-001].

## Story List

### US-001.01 — See the MyPass window

**As a** User (S01), **I want** to open MyPass and see a window titled "Password Manager" with the logo and labelled website, email and password fields, **so that** I know what to fill in.

**Acceptance Criteria**

- Given the app is started, when the window opens, then the title is "Password Manager" and a 200 x 200 canvas shows the logo with 20 px padding.
- Given the window is open, then website, email and password entries, a Generate Password button and an Add button are laid out on a grid of three columns and five rows.

| Traces to | Size | INVEST exceptions |
| --- | --- | --- |
| [MIL-003] | fits one iteration | none |

### US-001.02 — Generate a strong password

**As a** User (S01), **I want** to click Generate Password and get a random password in the password field, **so that** I do not have to invent one that meets website rules.

**Acceptance Criteria**

- Given an empty password field, when I click Generate Password, then it holds 8 to 10 letters, 2 to 4 symbols and 2 to 4 digits in random order.
- Given a password was already generated, when I click again, then the field is replaced with a new password.

| Traces to | Size | INVEST exceptions |
| --- | --- | --- |
| [MIL-002], [MIL-003] | fits one iteration | none |

### US-001.03 — Copy the password to the clipboard

**As a** User (S01), **I want** to have a generated password copied to the clipboard, **so that** I can paste it straight into a sign-up form.

**Acceptance Criteria**

- Given I click Generate Password, when I paste elsewhere, then the pasted text equals the password field.

| Traces to | Size | INVEST exceptions |
| --- | --- | --- |
| [MIL-003] | fits one iteration | none |

### US-001.04 — Save an entry after confirming

**As a** User (S01), **I want** to review website, email and password in a confirmation dialog before they are saved, **so that** I do not store a wrong entry.

**Acceptance Criteria**

- Given all fields are filled, when I click Add, then a dialog shows the three values and OK or Cancel.
- Given I choose OK, then a line "website | email | password" is appended to data.txt.
- Given I choose Cancel, then nothing is written and the fields keep their values.

| Traces to | Size | INVEST exceptions |
| --- | --- | --- |
| [MIL-004] | fits one iteration | none |

### US-001.05 — Be warned about empty fields

**As a** User (S01), **I want** to be told when the website or password is empty, **so that** an incomplete entry is never saved.

**Acceptance Criteria**

- Given the website or the password is empty, when I click Add, then a warning dialog appears and data.txt is unchanged.

| Traces to | Size | INVEST exceptions |
| --- | --- | --- |
| [MIL-004] | fits one iteration | none |

### US-001.06 — Start ready for the next entry

**As a** User (S01), **I want** to have the cursor in the website field, the email pre-filled and the fields cleared after saving, **so that** I can add the next entry quickly.

**Acceptance Criteria**

- Given the app starts, then the website entry has focus and the email holds the default email.
- Given an entry was saved, then the website and password entries are empty and focus is back on the website entry.

| Traces to | Size | INVEST exceptions |
| --- | --- | --- |
| [MIL-003], [MIL-004] | fits one iteration | none |

### US-001.07 — Run and read the project in my language

**As a** Reader (S02, S03), **I want** to find run and test instructions in the README and a wiki in English, Danish and Bahasa Malaysia, **so that** I can run the code and learn from it.

**Acceptance Criteria**

- Given the README, when I follow Set up and Run for my platform, then the app starts.
- Given the wiki, then each of the three languages has the same pages with screenshots.
- Given the repository page, then a description and topics are shown.

| Traces to | Size | INVEST exceptions |
| --- | --- | --- |
| [MIL-005] | fits one iteration | none |

## INVEST Check

All stories are Independent, Negotiable, Valuable, Estimable, Small and Testable. Exception: US-001.03 depends on US-001.02 for the generated value; the dependency is explicit in the acceptance criteria.

---

[BC-001]: ./business-case.md
[MIL-001]: ./milestones/mil-001-baseline-and-tooling.md
[MIL-002]: ./milestones/mil-002-password-generator-logic.md
[MIL-003]: ./milestones/mil-003-tkinter-user-interface.md
[MIL-004]: ./milestones/mil-004-save-and-validate.md
[MIL-005]: ./milestones/mil-005-documentation-and-publishing.md
[SA-001]: ./stakeholder-analysis.md
[UCD-001]: ./use-case-diagram.md
[b4c2611]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/commit/b4c26115f240097da76782a8e84a5367198226b5
