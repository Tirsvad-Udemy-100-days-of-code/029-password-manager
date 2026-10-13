import tkinter as tk
from collections.abc import Iterator

import pytest

from mypass.constants import (
    ADD_BUTTON_WIDTH,
    CANVAS_SIZE,
    DEFAULT_EMAIL,
    EMAIL_ENTRY_WIDTH,
    LETTER_COUNT_RANGE,
    NUMBER_COUNT_RANGE,
    PASSWORD_ENTRY_WIDTH,
    SYMBOL_COUNT_RANGE,
    WEBSITE_ENTRY_WIDTH,
    WINDOW_TITLE,
)
from mypass.ui import PasswordManagerApp


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
def app(root: tk.Tk) -> PasswordManagerApp:
    return PasswordManagerApp(root)


def test_window_title_is_password_manager(app: PasswordManagerApp) -> None:
    assert app.root.title() == WINDOW_TITLE == "Password Manager"


def test_canvas_has_configured_size(app: PasswordManagerApp) -> None:
    app.root.update()
    assert int(app.canvas.cget("width")) == CANVAS_SIZE == 200
    assert int(app.canvas.cget("height")) == CANVAS_SIZE


def test_logo_image_is_drawn_at_canvas_centre(app: PasswordManagerApp) -> None:
    items = app.canvas.find_all()
    assert len(items) == 1
    assert str(app.canvas.type(items[0])) == "image"
    assert app.canvas.coords(items[0]) == [CANVAS_SIZE // 2, CANVAS_SIZE // 2]


def test_website_entry_has_focus_on_start(app: PasswordManagerApp) -> None:
    # A withdrawn toplevel resets its focus memory to itself, so map it first.
    app.root.deiconify()
    app.root.update()
    # Tk remembers the focus target per toplevel regardless of OS window focus.
    assert str(app.root.tk.call("focus", "-lastfor", ".")) == str(app.website_entry)


def test_email_entry_is_prefilled_with_default_email(app: PasswordManagerApp) -> None:
    assert app.email_entry.get() == DEFAULT_EMAIL


def test_widgets_are_placed_in_the_expected_grid_cells(
    app: PasswordManagerApp,
) -> None:
    def cell(widget: tk.Widget) -> tuple[int, int, int]:
        info = widget.grid_info()
        return (int(info["row"]), int(info["column"]), int(info["columnspan"]))

    assert cell(app.canvas) == (0, 1, 1)
    assert cell(app.website_entry) == (1, 1, 2)
    assert cell(app.email_entry) == (2, 1, 2)
    assert cell(app.password_entry) == (3, 1, 1)
    assert cell(app.generate_button) == (3, 2, 1)
    assert cell(app.add_button) == (4, 1, 2)


def test_entries_and_add_button_have_configured_widths(
    app: PasswordManagerApp,
) -> None:
    assert int(app.website_entry.cget("width")) == WEBSITE_ENTRY_WIDTH
    assert int(app.email_entry.cget("width")) == EMAIL_ENTRY_WIDTH
    assert int(app.password_entry.cget("width")) == PASSWORD_ENTRY_WIDTH
    assert int(app.add_button.cget("width")) == ADD_BUTTON_WIDTH == 36


def test_generate_fills_password_entry_and_clipboard(
    app: PasswordManagerApp,
) -> None:
    app.generate_password_action()

    password = app.password_entry.get()
    letters = sum(c.isalpha() for c in password)
    digits = sum(c.isdigit() for c in password)
    symbols = len(password) - letters - digits
    assert LETTER_COUNT_RANGE[0] <= letters <= LETTER_COUNT_RANGE[1]
    assert NUMBER_COUNT_RANGE[0] <= digits <= NUMBER_COUNT_RANGE[1]
    assert SYMBOL_COUNT_RANGE[0] <= symbols <= SYMBOL_COUNT_RANGE[1]
    assert app.root.clipboard_get() == password


def test_generate_twice_replaces_previous_password(
    app: PasswordManagerApp, monkeypatch: pytest.MonkeyPatch
) -> None:
    passwords = iter(["first-Pass1", "second-Pass2"])
    monkeypatch.setattr("mypass.ui.generate_password", lambda: next(passwords))

    app.generate_password_action()
    app.generate_password_action()

    assert app.password_entry.get() == "second-Pass2"
    assert app.root.clipboard_get() == "second-Pass2"


def test_generate_button_runs_generate_action(
    app: PasswordManagerApp, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("mypass.ui.generate_password", lambda: "clicked-Pass1")

    app.generate_button.invoke()

    assert app.password_entry.get() == "clicked-Pass1"
