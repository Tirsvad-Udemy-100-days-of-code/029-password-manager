## @file password_generator.py
## @brief Random password generation for the MyPass application.
##
## This module is free of GUI imports so it can be used and tested without a
## display.

import random

from mypass.constants import (
    LETTER_COUNT_RANGE,
    LETTERS,
    NUMBER_COUNT_RANGE,
    NUMBERS,
    SYMBOL_COUNT_RANGE,
    SYMBOLS,
)

# Passwords need unpredictable randomness, so the OS entropy source is used
# instead of the global Mersenne Twister generator.
_RANDOM = random.SystemRandom()


## @brief Generate a random password of shuffled letters, symbols and digits.
## @return The generated password.
def generate_password() -> str:
    """Return a random password mixing letters, symbols and digits.

    The number of each kind of character is drawn from the inclusive ranges
    defined in ``mypass.constants``, and the characters are shuffled.
    """
    letter_count = _RANDOM.randint(*LETTER_COUNT_RANGE)
    symbol_count = _RANDOM.randint(*SYMBOL_COUNT_RANGE)
    number_count = _RANDOM.randint(*NUMBER_COUNT_RANGE)

    password_characters = (
        [_RANDOM.choice(LETTERS) for _ in range(letter_count)]
        + [_RANDOM.choice(SYMBOLS) for _ in range(symbol_count)]
        + [_RANDOM.choice(NUMBERS) for _ in range(number_count)]
    )
    _RANDOM.shuffle(password_characters)
    return "".join(password_characters)
