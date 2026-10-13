**English** | [Dansk](Development.da) | [Bahasa Malaysia](Development.ms)

# Development

## Project layout

- `src/mypass/`: the application
- `tests/`: pytest tests
- `docs/`: project documents, ADR and screenshots
- `wiki/`: the sources of this wiki

## Run the tests

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

## Continuous integration

The workflow `.gitea/workflows/ci.yml` installs the project, checks formatting, lint, types and YAML, and runs pytest on every push and pull request.

## Source documentation

Build the HTML documentation with Doxygen; open `docs/doxygen/html/index.html` afterwards.

```bash
doxygen Doxyfile
```

## Design decision

The clipboard uses Tkinter's own methods instead of `pyperclip`, so nothing has to be installed (ADR-0001 in `docs/adr/`).
