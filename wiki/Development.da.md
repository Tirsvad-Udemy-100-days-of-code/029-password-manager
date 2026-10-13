[English](Development) | **Dansk** | [Bahasa Malaysia](Development.ms)

# Udvikling

## Projektets opbygning

- `src/mypass/`: programmet
- `tests/`: pytest-tests
- `docs/`: projektdokumenter, ADR og skærmbilleder
- `wiki/`: kilderne til denne wiki

## Kør testene

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

## Kontinuerlig integration

Workflowet `.gitea/workflows/ci.yml` installerer projektet, kontrollerer formatering, lint, typer og YAML og kører pytest ved hvert push og hver pull request.

## Kildedokumentation

Byg HTML-dokumentationen med Doxygen; åbn derefter `docs/doxygen/html/index.html`.

```bash
doxygen Doxyfile
```

## Designbeslutning

Udklipsholderen bruger Tkinters egne metoder i stedet for `pyperclip`, så intet skal installeres (ADR-0001 i `docs/adr/`).
