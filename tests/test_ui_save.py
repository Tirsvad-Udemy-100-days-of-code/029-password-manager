import tkinter as tk
from collections.abc import Iterator
from pathlib import Path

import pytest

from mypass.constants import (
    DEFAULT_EMAIL,
    INFO_SAVED,
    WARNING_EMPTY_FIELDS,
    WARNING_TITLE,
)
from mypass.ui import PasswordManagerApp


class FakeMessagebox:
    """Records dialog calls and answers askokcancel with a set value."""

    def __init__(self) -> None:
        self.answer = True
        self.warnings: list[tuple[str, str]] = []
        self.confirms: list[tuple[str, str]] = []
        self.infos: list[tuple[str, str]] = []

    def showwarning(self, title: str, message: str) -> None:
        self.warnings.append((title, message))

    def askokcancel(self, title: str, message: str) -> bool:
        self.confirms.append((title, message))
        return self.answer

    def showinfo(self, title: str, message: str) -> None:
        self.infos.append((title, message))


@pytest.fixture
def root() -> Iterator[tk.Tk]:
    try:
        window = tk.Tk()
    except tk.TclError:
        pytest.skip("no display available")
    window.withdraw()
    try:
        yield window
    finally:
        window.destroy()


@pytest.fixture
def dialogs(monkeypatch: pytest.MonkeyPatch) -> FakeMessagebox:
    fake = FakeMessagebox()
    monkeypatch.setattr("mypass.ui.messagebox", fake)
    return fake


@pytest.fixture
def data_file(tmp_path: Path) -> Path:
    return tmp_path / "data.txt"


@pytest.fixture
def app(root: tk.Tk, data_file: Path) -> PasswordManagerApp:
    return PasswordManagerApp(root, data_file=data_file)


def fill(app: PasswordManagerApp, website: str, password: str) -> None:
    app.website_entry.insert(0, website)
    app.password_entry.insert(0, password)


def test_save_warns_and_writes_nothing_when_website_empty(
    app: PasswordManagerApp, dialogs: FakeMessagebox, data_file: Path
) -> None:
    fill(app, "", "pw")

    app.save()

    assert dialogs.warnings == [(WARNING_TITLE, WARNING_EMPTY_FIELDS)]
    assert dialogs.confirms == []
    assert not data_file.exists()
    assert app.password_entry.get() == "pw"


def test_save_warns_and_writes_nothing_when_password_empty(
    app: PasswordManagerApp, dialogs: FakeMessagebox, data_file: Path
) -> None:
    fill(app, "site", "")

    app.save()

    assert dialogs.warnings == [(WARNING_TITLE, WARNING_EMPTY_FIELDS)]
    assert not data_file.exists()
    assert app.website_entry.get() == "site"


def test_save_cancel_writes_nothing_and_keeps_fields(
    app: PasswordManagerApp, dialogs: FakeMessagebox, data_file: Path
) -> None:
    dialogs.answer = False
    fill(app, "site", "pw")

    app.save()

    assert len(dialogs.confirms) == 1
    assert dialogs.infos == []
    assert not data_file.exists()
    assert app.website_entry.get() == "site"
    assert app.password_entry.get() == "pw"


def test_save_confirmed_writes_one_line_and_clears_fields(
    app: PasswordManagerApp, dialogs: FakeMessagebox, data_file: Path
) -> None:
    fill(app, "site", "pw")

    app.save()

    lines = data_file.read_text(encoding="utf-8").splitlines()
    assert lines == [f"site | {DEFAULT_EMAIL} | pw"]
    assert app.website_entry.get() == ""
    assert app.password_entry.get() == ""
    assert app.email_entry.get() == DEFAULT_EMAIL
    assert dialogs.infos[0][1] == INFO_SAVED
    assert dialogs.warnings == []


def test_save_confirmation_dialog_shows_entered_details(
    app: PasswordManagerApp, dialogs: FakeMessagebox
) -> None:
    fill(app, "site", "pw")

    app.save()

    title, body = dialogs.confirms[0]
    assert "site" in title
    assert DEFAULT_EMAIL in body
    assert "pw" in body


def test_add_button_runs_save(
    app: PasswordManagerApp, dialogs: FakeMessagebox, data_file: Path
) -> None:
    fill(app, "site", "pw")

    app.add_button.invoke()

    assert data_file.exists()
