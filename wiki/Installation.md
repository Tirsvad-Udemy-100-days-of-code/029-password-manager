**English** | [Dansk](Installation.da) | [Bahasa Malaysia](Installation.ms)

# Installation

## Requirements

- Python 3.13 or newer.
- Tkinter (included with Python on Windows and macOS from python.org; a package on Debian).
- Git, to clone the repository.

## Set up

Clone the repository and create a virtual environment named `.venv`:

### Windows PowerShell

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager.git
cd 029-password-manager
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
```

### Linux Debian

```bash
sudo apt install python3 python3-venv python3-tk git
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager.git
cd 029-password-manager
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

### macOS

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager.git
cd 029-password-manager
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

## Run

Start the application with either command:

```bash
python -m mypass
python src/main.py
```
