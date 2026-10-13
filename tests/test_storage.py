from pathlib import Path

import pytest

from mypass.constants import FIELD_SEPARATOR
from mypass.storage import format_entry, is_entry_complete, save_entry


def test_entry_is_complete_when_website_and_password_filled() -> None:
    assert is_entry_complete("site", "pw")


@pytest.mark.parametrize(
    ("website", "password"),
    [("", "pw"), ("site", ""), ("   ", "pw"), ("site", "  \t"), ("", "")],
)
def test_entry_is_incomplete_when_a_field_is_blank(website: str, password: str) -> None:
    assert not is_entry_complete(website, password)


def test_format_entry_joins_fields_with_separator_without_newline() -> None:
    line = format_entry("site", "me@example.com", "pw")

    assert line == f"site{FIELD_SEPARATOR}me@example.com{FIELD_SEPARATOR}pw"
    assert line == "site | me@example.com | pw"
    assert "\n" not in line


def test_save_entry_writes_exactly_one_line(tmp_path: Path) -> None:
    data_file = tmp_path / "data.txt"

    save_entry("site", "me@example.com", "pw", data_file)

    assert data_file.read_text(encoding="utf-8") == "site | me@example.com | pw\n"


def test_save_entry_appends_second_line(tmp_path: Path) -> None:
    data_file = tmp_path / "data.txt"

    save_entry("site", "me@example.com", "pw", data_file)
    save_entry("other", "me@example.com", "pw2", data_file)

    lines = data_file.read_text(encoding="utf-8").splitlines()
    assert lines == ["site | me@example.com | pw", "other | me@example.com | pw2"]


def test_save_entry_creates_missing_file(tmp_path: Path) -> None:
    data_file = tmp_path / "data.txt"
    assert not data_file.exists()

    save_entry("site", "me@example.com", "pw", data_file)

    assert data_file.exists()
