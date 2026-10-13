# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [UCD-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Executive Summary

Websites demand passwords that are long, varied and unique, and people cannot
remember them. MyPass is a small desktop password manager built with Python and
Tkinter as Day 29 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp".
It lets the user store a website, an email and a password, generate a strong
random password with one click, and copy it to the clipboard. The project is
delivered as a readable, runnable, tested and documented repository so that
other course participants and GitHub visitors can learn from it. The
recommendation is to proceed.

## Methodological and Standards Foundation

- Planning follows the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/`: Business
  Case, Stakeholder Analysis, Project Plan, milestones, tasks as issues, then code.
- Product quality is described with International Organization for Standardization and International Electrotechnical Commission (ISO/IEC) standard 25010:2023 characteristics, as the
  QC checklists tag each criterion with one.
- Source code follows the project's Python conventions (`coding-conventions`
  skill) and is documented with Doxygen comments.

## Problem Statement

- Password rules differ per website (length, symbols, digits), so users reuse
  weak passwords or forget strong ones.
- Rules that frustrate people are easy for computers to guess around, so they
  add effort without adding safety.
- Typing a generated password by hand into a sign-up form is error-prone.

## Business Opportunity

A tool that generates a compliant random password, keeps it with the website and
email it belongs to, and puts it on the clipboard removes the memorising and
retyping. As a course project it also gives other participants a reference
solution they can compare with their own.

## Objectives

1. Provide a Tkinter window "Password Manager" with the MyPass logo and a grid
   layout of website, email and password fields (Udemy Day 29 challenges 1 and 2).
2. Generate a random password of 8 to 10 letters, 2 to 4 symbols and 2 to 4
   digits, shuffled, with no user input (`generate_password`).
3. Copy a generated password to the clipboard without a runtime dependency.
4. Save website, email and password to `data.txt` after the user confirms, and
   refuse to save when the website or password is empty.
5. Ship the project with tests (pytest), a README, a Doxygen configuration, continuous integration (CI),
   and a wiki in English, Danish and Bahasa Malaysia with screenshots.

## Scope

### In Scope

- The MyPass desktop application (`src/`) with the assignment's function names.
- Automated tests of the password generation and the saving logic (`tests/`).
- Python project configuration (`pyproject.toml`), constants in `constants.py`,
  Python `.gitignore`, local `.venv` instructions, Doxyfile.
- README and a three-language wiki with screenshots.
- Repository description and topics on the git host.

### Out of Scope

- Encryption of stored data, a master password, or retrieving saved passwords
  (later course days).
- Packaging for distribution (installers, PyPI).
- Mobile or web versions.

## Expected Benefits

### Tangible Benefits

- A working, tested reference solution for Day 29.
- A repository other participants can clone and run in minutes.

### Intangible Benefits

- Practice with the planning-first workflow and review records.
- A clearer public profile for GitHub viewers browsing for ideas.

## Strategic Alignment

The project supports the course participant's goal of completing the 100 Days of
Code bootcamp with work that is shareable and documented to a professional
standard.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Generated password follows the rules | 100 % of 1000 generated passwords have 8-10 letters, 2-4 symbols, 2-4 digits | pytest |
| 2 | Tests pass on a clean checkout | 0 failures | `pytest` and CI run |
| 3 | Runtime dependencies | 0 packages beyond the Python standard library | `pyproject.toml` |
| 4 | Required entries saved only when complete | 0 rows written with an empty website or password | pytest |
| 5 | Documentation complete | README sections of the template, wiki pages in 3 languages, at least 1 screenshot each | `check-readme.sh`, file review |
| 6 | Repository metadata | Description and at least 5 topics set | git host application programming interface (API) |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Tkinter is missing in a Python install (some Linux packages) | The app cannot start | README names the `python3-tk` package for Debian; logic is kept free of Tkinter so tests run without a display |
| GUI tests need a display in CI | CI fails | Keep logic in testable functions; only the thin user interface (UI) layer needs Tkinter |
| Token leaks through `.env` | Account compromise | `.env` stays untracked and in `.gitignore`; it is never imported or tested by the project |
| Plain-text `data.txt` stores passwords | Secrets exposed | Out of scope for this day; README states the limitation and `data.txt` is git-ignored |
| Wiki translations drift apart | Inconsistent documentation | One page structure per language, reviewed together |

## Assumptions

- The Product Owner is the course participant (S01) and also develops and reviews.
- The git host `git.tirsystem.com` is reachable and `GITEA_TOKEN` in `.env` has
  repository write access.
- "Python greater than 3.13" is read as Python 3.13 or newer (`>=3.13`), the
  version installed on the development machine.
- The clipboard can be filled with Tkinter's own clipboard methods, so
  `pyperclip` from the lecture is not needed.

## Constraints

- Python 3.13 or newer, a local `.venv`, pytest for tests.
- Source in `src/`, tests in `tests/`, documents in `docs/`.
- Constants in `constants.py`; Doxygen-style comments in source.
- No runtime dependencies unless needed.
- Supervised review is replaced by autonomous mode in this session: reviews are
  stand-in reviews and say so.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About one working day of effort by S01 and the AI assistant | A finished, documented reference project |
| No licence or infrastructure cost beyond the existing git host | Reusable planning and CI setup for later course days |

The assessment is qualitative because this is a learning project with no revenue.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes the assignment, owns the plan and reviews the work |
| S02 | Reads, runs and compares the solution |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, the risks have mitigations and the result is useful to all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[UCD-001]: ./use-case-diagram.md
