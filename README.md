# 🚀 MyPass

A small desktop password manager written in Python with Tkinter, made for Udemy's
*100 Days of Code: The Complete Python Pro Bootcamp* (Day 29). It is for course
participants who want a readable, runnable solution and for visitors browsing for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

MyPass generates a strong random password (8 to 10 letters, 2 to 4 symbols and 2 to 4
digits), saves it with the website and email after you confirm, and copies it to the
clipboard. It has no runtime dependencies: only the Python standard library.

![The empty form](docs/images/mypass-empty.png)
![A generated password](docs/images/mypass-generated.png)

The wiki is available in [English][wiki], [Dansk][wiki-da] and [Bahasa Malaysia][wiki-ms].
Its pages live in `wiki/` and are published automatically when a change reaches `main`
(`.gitea/workflows/publish-wiki.yml`).

### Project layout

```text
src/mypass/        the application: constants, password generator, storage, window
src/main.py        start script (python src/main.py)
tests/             pytest tests
docs/              project documents (business case, plan, milestones, reviews, ADR), images
wiki/              sources of the wiki in English, Danish and Bahasa Malaysia
.gitea/workflows/  continuous integration and wiki publishing
pyproject.toml     project configuration
Doxyfile           Doxygen configuration
```

The project follows the planning-first process of the SQA and QC framework in
`framework/`; see the project documents in the appendix.

## 📋 Requirements

- Python 3.13 or newer, to run the application and the tests.
- Tkinter, the standard Python GUI toolkit, for the window. It is included with Python on
  Windows and macOS (python.org installer) and is the `python3-tk` package on Debian.
- Git, to clone the repository.
- Optional: Doxygen, to build the source documentation.

## 🛠️ Setup

Create a virtual environment named `.venv` in the project folder, activate it, upgrade
`pip` and install the project. Run the commands from the repository root.

### Windows powershell

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager.git
cd 029-password-manager
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell refuses to run the activation script, allow it for this window only with
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`.

### Linux debian

```bash
sudo apt install python3 python3-venv python3-tk git
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager.git
cd 029-password-manager
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### MacOS

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager.git
cd 029-password-manager
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

`.[dev]` also installs the test and check tools. To only run the application,
`python -m pip install -e .` is enough. With Homebrew's Python, add Tkinter with
`brew install python-tk@3.13`.

## ▶️ Run

With the virtual environment active:

```bash
python -m mypass
```

Without installing the project, from the repository root: `python src/main.py`.

Fill in the website, check the email, click **Generate Password**, then **Add** and
confirm. Each saved entry is one line `website | email | password` in `data.txt` in the
folder you started the program from. The file is plain text and not encrypted, so do not
use it for real passwords. `data.txt` is ignored by Git.

### Build the source documentation

The source uses Doxygen comments. With [Doxygen](https://www.doxygen.nl/) installed:

```bash
doxygen Doxyfile
```

Open `docs/doxygen/html/index.html` afterwards. The output folder is ignored by Git.

## 🧪 Tests

Run the tests with the virtual environment active:

```bash
python -m pytest
```

The tests of the logic need no display. The tests of the window are skipped when no display
is available. With [actionlint](https://github.com/rhysd/actionlint) installed, the same
run also checks the workflows (`.gitea/actionlint.yaml` declares the `mypass-ci` label).

### Continuous integration

The workflow [`.gitea/workflows/ci.yml`](.gitea/workflows/ci.yml) runs on every push to
`main` and every pull request. It installs the project with the `dev` extra, checks
formatting (`ruff format --check`), lint (`ruff check`), types (`mypy --strict`), YAML
(`yamllint`) and the workflow itself (`actionlint`, downloaded at a pinned version and
checksum), and runs `pytest` under a virtual display (`xvfb-run`), so the window tests run
too. It runs on a runner with the label `mypass-ci`, backed by an Ubuntu image pinned by
digest (`catthehacker/ubuntu`). The setup, the digest and the Tk and Xvfb versions are
recorded in the workflow header and `env`. To use another runner, change `runs-on`.

## 📄 License

GNU Affero General Public License v3.0, see [LICENSE](LICENSE).

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[wiki]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/wiki/Home
[wiki-da]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/wiki/Home.da
[wiki-ms]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/wiki/Home.ms
[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
