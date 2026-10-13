## @file storage.py
## @brief Validation and persistence of saved password entries.
##
## This module is free of GUI imports so it can be tested without a display.

from pathlib import Path

from mypass.constants import FIELD_SEPARATOR


## @brief Tell whether the required fields of an entry are filled in.
## @param website The website field.
## @param password The password field.
## @return False when either value is empty or only whitespace.
def is_entry_complete(website: str, password: str) -> bool:
    """Return True when both website and password hold visible text."""
    return bool(website.strip()) and bool(password.strip())


## @brief Format one entry as a single line of text, without newline.
## @param website The website field.
## @param email The email or username field.
## @param password The password field.
## @return The fields joined by the field separator.
def format_entry(website: str, email: str, password: str) -> str:
    """Join the three fields with the field separator."""
    return FIELD_SEPARATOR.join((website, email, password))


## @brief Append one entry as a line to the data file.
## @param website The website field.
## @param email The email or username field.
## @param password The password field.
## @param data_file The file to append to; created when missing.
def save_entry(website: str, email: str, password: str, data_file: Path) -> None:
    """Append the formatted entry and a newline to ``data_file``."""
    with data_file.open("a", encoding="utf-8") as file:
        file.write(format_entry(website, email, password) + "\n")
