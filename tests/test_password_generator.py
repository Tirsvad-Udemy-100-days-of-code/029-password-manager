import subprocess
import sys

from mypass.constants import (
    LETTER_COUNT_RANGE,
    LETTERS,
    NUMBER_COUNT_RANGE,
    NUMBERS,
    SYMBOL_COUNT_RANGE,
    SYMBOLS,
)
from mypass.password_generator import generate_password

SAMPLE_SIZE = 1000


def _count_in(password: str, allowed: tuple[str, ...]) -> int:
    return sum(1 for character in password if character in allowed)


def test_generate_password_returns_str() -> None:
    assert isinstance(generate_password(), str)


def test_generate_password_has_counts_within_ranges() -> None:
    for _ in range(SAMPLE_SIZE):
        password = generate_password()
        letters = _count_in(password, LETTERS)
        symbols = _count_in(password, SYMBOLS)
        numbers = _count_in(password, NUMBERS)
        assert LETTER_COUNT_RANGE[0] <= letters <= LETTER_COUNT_RANGE[1]
        assert SYMBOL_COUNT_RANGE[0] <= symbols <= SYMBOL_COUNT_RANGE[1]
        assert NUMBER_COUNT_RANGE[0] <= numbers <= NUMBER_COUNT_RANGE[1]


def test_generate_password_uses_only_allowed_characters() -> None:
    allowed = set(LETTERS) | set(SYMBOLS) | set(NUMBERS)
    for _ in range(SAMPLE_SIZE):
        assert set(generate_password()) <= allowed


def test_generate_password_length_is_within_bounds() -> None:
    minimum = LETTER_COUNT_RANGE[0] + SYMBOL_COUNT_RANGE[0] + NUMBER_COUNT_RANGE[0]
    maximum = LETTER_COUNT_RANGE[1] + SYMBOL_COUNT_RANGE[1] + NUMBER_COUNT_RANGE[1]
    assert (minimum, maximum) == (12, 18)
    for _ in range(SAMPLE_SIZE):
        assert minimum <= len(generate_password()) <= maximum


def test_generate_password_differs_between_calls() -> None:
    assert len({generate_password() for _ in range(50)}) > 1


def test_generate_password_shuffles_character_kinds() -> None:
    letters = set(LETTERS)
    first_characters = [generate_password()[0] for _ in range(200)]
    assert any(character not in letters for character in first_characters)


def test_password_generator_module_does_not_import_tkinter() -> None:
    code = (
        "import sys, mypass.password_generator; "
        "sys.exit(1 if 'tkinter' in sys.modules else 0)"
    )
    result = subprocess.run([sys.executable, "-c", code], check=False)
    assert result.returncode == 0
