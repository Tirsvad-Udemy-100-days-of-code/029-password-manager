"""Smoke tests: the package imports and its constants are consistent."""

from pathlib import Path

import mypass
from mypass import constants

ASSETS_DIR = Path(mypass.__file__).parent / "assets"


def test_version_is_set() -> None:
    assert mypass.__version__ == "0.1.0"


def test_count_ranges_are_ordered() -> None:
    for low, high in (
        constants.LETTER_COUNT_RANGE,
        constants.SYMBOL_COUNT_RANGE,
        constants.NUMBER_COUNT_RANGE,
    ):
        assert 0 < low <= high


def test_character_sets_have_expected_sizes() -> None:
    assert len(constants.LETTERS) == 52
    assert len(constants.NUMBERS) == 10
    assert len(constants.SYMBOLS) == 9


def test_logo_file_exists_in_assets() -> None:
    assert (ASSETS_DIR / constants.LOGO_FILE_NAME).is_file()


def test_templates_format_with_expected_fields() -> None:
    body = constants.CONFIRM_BODY_TEMPLATE.format(email="a@b.c", password="pw")
    assert "a@b.c" in body
    assert constants.CONFIRM_TITLE_TEMPLATE.format(website="site") == "site"
