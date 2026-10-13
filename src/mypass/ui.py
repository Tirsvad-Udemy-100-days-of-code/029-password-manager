## @file ui.py
## @brief Tkinter user interface of the MyPass application.

import tkinter as tk
from pathlib import Path
from tkinter import messagebox

from mypass.constants import (
    ADD_BUTTON_WIDTH,
    BUTTON_ADD,
    BUTTON_GENERATE,
    CANVAS_SIZE,
    CONFIRM_BODY_TEMPLATE,
    CONFIRM_TITLE_TEMPLATE,
    DATA_FILE_NAME,
    DEFAULT_EMAIL,
    EMAIL_ENTRY_WIDTH,
    INFO_SAVED,
    INFO_TITLE,
    LABEL_EMAIL,
    LABEL_PASSWORD,
    LABEL_WEBSITE,
    LOGO_FILE_NAME,
    PASSWORD_ENTRY_WIDTH,
    WARNING_EMPTY_FIELDS,
    WARNING_TITLE,
    WEBSITE_ENTRY_WIDTH,
    WINDOW_PADDING,
    WINDOW_TITLE,
)
from mypass.password_generator import generate_password
from mypass.storage import is_entry_complete, save_entry

_LOGO_PATH = Path(__file__).parent / "assets" / LOGO_FILE_NAME


## @brief The main window of the password manager.
class PasswordManagerApp:
    """Builds the widgets of the main window and handles their actions."""

    ## @brief Build the window content on the given root.
    ## @param root The Tk root window to build on.
    ## @param data_file The file where saved entries are appended.
    def __init__(self, root: tk.Tk, data_file: Path = Path(DATA_FILE_NAME)) -> None:
        """Create all widgets on ``root`` and lay them out in a grid."""
        self.root = root
        self.data_file = data_file
        root.title(WINDOW_TITLE)
        root.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING)

        self.canvas = tk.Canvas(
            root, width=CANVAS_SIZE, height=CANVAS_SIZE, highlightthickness=0
        )
        # Tk does not keep a reference to the image, so it is stored here.
        self._logo = tk.PhotoImage(file=str(_LOGO_PATH))
        self.canvas.create_image(CANVAS_SIZE // 2, CANVAS_SIZE // 2, image=self._logo)
        self.canvas.grid(row=0, column=1)

        tk.Label(root, text=LABEL_WEBSITE).grid(row=1, column=0)
        tk.Label(root, text=LABEL_EMAIL).grid(row=2, column=0)
        tk.Label(root, text=LABEL_PASSWORD).grid(row=3, column=0)

        self.website_entry = tk.Entry(root, width=WEBSITE_ENTRY_WIDTH)
        self.website_entry.grid(row=1, column=1, columnspan=2)
        self.website_entry.focus()

        self.email_entry = tk.Entry(root, width=EMAIL_ENTRY_WIDTH)
        self.email_entry.grid(row=2, column=1, columnspan=2)
        self.email_entry.insert(0, DEFAULT_EMAIL)

        self.password_entry = tk.Entry(root, width=PASSWORD_ENTRY_WIDTH)
        self.password_entry.grid(row=3, column=1)

        self.generate_button = tk.Button(
            root, text=BUTTON_GENERATE, command=self.generate_password_action
        )
        self.generate_button.grid(row=3, column=2)

        self.add_button = tk.Button(
            root, text=BUTTON_ADD, width=ADD_BUTTON_WIDTH, command=self.save
        )
        self.add_button.grid(row=4, column=1, columnspan=2)

    ## @brief Fill the password entry with a new password and copy it.
    def generate_password_action(self) -> None:
        """Put a generated password in the entry and on the clipboard."""
        password = generate_password()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.root.clipboard_clear()
        self.root.clipboard_append(password)

    ## @brief Command of the Add button.
    def save(self) -> None:
        """Validate, confirm and append the entry, then reset the form."""
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not is_entry_complete(website, password):
            messagebox.showwarning(WARNING_TITLE, WARNING_EMPTY_FIELDS)
            return

        confirmed = messagebox.askokcancel(
            title=CONFIRM_TITLE_TEMPLATE.format(website=website),
            message=CONFIRM_BODY_TEMPLATE.format(email=email, password=password),
        )
        if not confirmed:
            return

        save_entry(website, email, password, self.data_file)
        self.website_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.website_entry.focus()
        messagebox.showinfo(INFO_TITLE, INFO_SAVED)


## @brief Start the application and run its event loop.
def main() -> None:
    """Create the root window, build the app and run the main loop."""
    root = tk.Tk()
    PasswordManagerApp(root)
    root.mainloop()
