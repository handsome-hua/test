# Temperature Converter

A small Python example project for practicing Git and Codex review workflows.

## Run

Convert Celsius to Fahrenheit from the repository root:

```bash
python -m src.temperature 25
```

## Test

```bash
python -m unittest discover -s tests -v
```

Before committing a change, run the tests and use `/review` in Codex to inspect
the uncommitted working tree.
