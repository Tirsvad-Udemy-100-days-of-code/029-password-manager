[English](Installation) | [Dansk](Installation.da) | **Bahasa Malaysia**

# Pemasangan

## Keperluan

- Python 3.13 atau lebih baharu.
- Tkinter (disertakan dengan Python di Windows dan macOS dari python.org; sebuah pakej di Debian).
- Git untuk mengklon repositori.

## Persediaan

Klon repositori dan cipta persekitaran maya bernama `.venv`:

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

## Jalankan

Mulakan aplikasi dengan salah satu arahan:

```bash
python -m mypass
python src/main.py
```
