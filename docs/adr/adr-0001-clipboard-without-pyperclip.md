# ADR-0001 Clipboard without pyperclip

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [SA-001], [MIL-001], [MIL-003] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The lecture copies the generated password to the clipboard with the
third-party package `pyperclip`. [BC-001] constrains the project to no runtime
dependencies unless needed, and [SA-001] records the conflict between S02, who
follow the lecture, and S03, who want nothing to install.

Options evaluated:

1. `pyperclip`: as in the lecture, one extra runtime package, and on Linux it
   needs a system tool such as `xclip`.
2. Tkinter's own clipboard (`clipboard_clear` and `clipboard_append` on the
   window): part of the standard library, already required for the interface.

## Decision

Use Tkinter's clipboard methods and add no runtime dependency; `pyperclip` is
not used.

## Consequences

**Positive:**

- `pip install` installs nothing beyond the project itself.
- No operating-system clipboard tool is needed on Linux.
- The clipboard code is covered by the same Tkinter requirement as the window.

**Negative:**

- The clipboard content lives only while the application window is open on some
  platforms, so a paste after closing the window may be empty.
- Differs from the lecture code, so S02 compare a different two lines.

## Affected Artifacts

- [BC-001] — success criterion 3 (no runtime dependencies) is met by this decision.
- [SA-001] — resolves the conflict between S02 and S03.
- [MIL-001] — the task that records this decision.
- [MIL-003] — the task "Wire Generate Password to the clipboard" implements it.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[MIL-001]: ../milestones/mil-001-baseline-and-tooling.md
[MIL-003]: ../milestones/mil-003-tkinter-user-interface.md
