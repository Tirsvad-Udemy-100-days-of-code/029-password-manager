[English](Installation) | **Dansk** | [Bahasa Malaysia](Installation.ms)

# Installation

## Krav

- Python 3.13 eller nyere.
- Tkinter (følger med Python på Windows og macOS fra python.org; en pakke på Debian).
- Git til at klone repositoryet.

## Opsætning

Klon repositoryet og opret et virtuelt miljø med navnet `.venv`:

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

## Kør

Start programmet med en af kommandoerne:

```bash
python -m mypass
python src/main.py
```
