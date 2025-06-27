# Presentatie 4B - Good Afternoon GUI

## Dependencies

- Python 3.12 via pyenv
- Pillow library for image processing
- Tkinter for GUI

> Pyenv and 3.12 are required because of pillow and tkinter. They don't support uv.

## Setup
```bash
brew install tcl-tk@8 pyenv
./install_python.sh
pyenv local 3.12.3
```

Set up the env:

```bash
~/.pyenv/shims/python3.12 -m venv .venv
source ./.venv/bin/activate.fish
pip install --upgrade pip
pip install --no-binary :all: pillow
```

# Run the Application
```bash
./main.py <name>
```