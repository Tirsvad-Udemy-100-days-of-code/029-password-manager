**English** | [Dansk](Usage.da) | [Bahasa Malaysia](Usage.ms)

# Usage

## Add an entry

1. Type the website in **Website**.
2. Check or change the email in **Email/Username**.
3. Click **Generate Password**. The password appears and is copied to the clipboard.
4. Click **Add**. A dialog shows what will be saved.
5. Click **OK** to save. The website and password fields are cleared.

![A generated password](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/raw/branch/main/docs/images/mypass-generated.png)

![The confirmation dialog](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/raw/branch/main/docs/images/mypass-confirm.png)

## Empty fields

If the website or the password is empty, a warning is shown and nothing is saved.

## Where the data goes

Each entry is one line in `data.txt` in the folder you start the program from, in the form `website | email | password`.

> Warning: the file is plain text and not encrypted. Do not use it for real passwords.
