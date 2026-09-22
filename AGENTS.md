# Repository Guidelines

## Project Structure & Module Organization

Application code lives under `src/`, and automated tests live under `tests/`. Keep modules focused and mirror the source layout in the test suite. Place non-code resources under `assets/` if the project needs them. Document any new top-level directory here or in the project README.

## Build, Test, and Development Commands

The sample project uses only the Python standard library:

- `python -m unittest discover -s tests -v` — run all automated tests.
- `python -m src.temperature 25` — convert a Celsius value from the command line.
- `python -m compileall -q src tests` — check Python syntax without running tests.

Do not document commands until they work from the repository root.

## Coding Style & Naming Conventions

Use four-space indentation and descriptive `snake_case` names for Python files, functions, and variables. Use `PascalCase` for classes. Add type hints to public functions and concise docstrings where behavior is not obvious. Keep generated files separate from hand-written source.

## Testing Guidelines

Tests use the standard-library `unittest` framework. Name modules `test_*.py` and test methods `test_<behavior>`. Include success, failure, and boundary cases. Bug fixes should include a regression test that fails without the fix. Run the full suite before committing.

## Commit & Pull Request Guidelines

There is no readable commit history from which to infer an existing convention. Use short, imperative commit subjects such as `Add configuration loader` and keep unrelated changes separate. Pull requests should explain the problem, summarize the solution, list validation performed, and link relevant issues. Include screenshots or logs when output or user-visible behavior changes. Call out configuration changes, compatibility concerns, and follow-up work explicitly.

## Security & Configuration

Never commit credentials, tokens, private keys, or local environment files. Provide sanitized examples such as `.env.example`, document required variables, and keep machine-specific configuration out of version control.
