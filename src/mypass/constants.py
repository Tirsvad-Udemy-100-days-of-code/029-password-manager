## @file constants.py
## @brief All fixed values of the MyPass application, defined once.
##
## This module is free of GUI imports so the values can be used and tested
## without a display.

import string

## @brief Title of the main window.
WINDOW_TITLE: str = "Password Manager"

## @brief Padding around the window content, in pixels.
WINDOW_PADDING: int = 50

## @brief Width and height of the logo canvas, in pixels.
CANVAS_SIZE: int = 200

## @brief File name of the logo inside the assets directory.
LOGO_FILE_NAME: str = "logo.png"

## @brief File name of the file where saved entries are appended.
DATA_FILE_NAME: str = "data.txt"

## @brief Email address pre-filled in the email entry.
DEFAULT_EMAIL: str = "user@example.com"

## @brief Separator between fields of one saved entry.
FIELD_SEPARATOR: str = " | "

## @brief Letters used in generated passwords (a-z, A-Z).
LETTERS: tuple[str, ...] = tuple(string.ascii_letters)

## @brief Digits used in generated passwords (0-9).
NUMBERS: tuple[str, ...] = tuple(string.digits)

## @brief Symbols used in generated passwords.
SYMBOLS: tuple[str, ...] = ("!", "#", "$", "%", "&", "(", ")", "*", "+")

## @brief Inclusive range of how many letters a generated password has.
LETTER_COUNT_RANGE: tuple[int, int] = (8, 10)

## @brief Inclusive range of how many symbols a generated password has.
SYMBOL_COUNT_RANGE: tuple[int, int] = (2, 4)

## @brief Inclusive range of how many digits a generated password has.
NUMBER_COUNT_RANGE: tuple[int, int] = (2, 4)

## @brief Width of the website entry, in characters.
WEBSITE_ENTRY_WIDTH: int = 35

## @brief Width of the email entry, in characters.
EMAIL_ENTRY_WIDTH: int = 35

## @brief Width of the password entry, in characters.
PASSWORD_ENTRY_WIDTH: int = 21

## @brief Text of the website label.
LABEL_WEBSITE: str = "Website:"

## @brief Text of the email label.
LABEL_EMAIL: str = "Email/Username:"

## @brief Text of the password label.
LABEL_PASSWORD: str = "Password:"

## @brief Text of the generate-password button.
BUTTON_GENERATE: str = "Generate Password"

## @brief Text of the add button.
BUTTON_ADD: str = "Add"

## @brief Title of the warning dialog.
WARNING_TITLE: str = "Oops"

## @brief Warning shown when a field is left empty.
WARNING_EMPTY_FIELDS: str = "Please don't leave any fields empty!"

## @brief Title template of the save confirmation dialog.
CONFIRM_TITLE_TEMPLATE: str = "{website}"

## @brief Body template of the save confirmation dialog.
CONFIRM_BODY_TEMPLATE: str = (
    "These are the details entered:\n"
    "Email: {email}\n"
    "Password: {password}\n"
    "Is it ok to save?"
)

## @brief Message shown after an entry was saved.
INFO_SAVED: str = "Entry saved."
