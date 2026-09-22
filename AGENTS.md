# Repository Guidelines

## Project Structure & Module Organization

This repository is currently an empty project scaffold. Add application code under `src/`, tests under `tests/`, and non-code resources under `assets/` unless the chosen framework establishes a different conventional layout. Keep modules focused and group related implementation, types, and fixtures by feature. Document any new top-level directory in this file or the project README.

## Build, Test, and Development Commands

No build system, package manager, or test runner is configured yet. When introducing one, provide standard entry points and update this section in the same change. Prefer a small, predictable command set, for example:

- `make build` — produce distributable artifacts.
- `make test` — run the complete automated test suite.
- `make lint` — run formatting and static checks without changing files.
- `make dev` — start the local development environment.

Do not document commands until they work from the repository root.

## Coding Style & Naming Conventions

Follow the formatter and linter conventions of the language or framework added to the project, and commit their configuration. Use spaces unless the formatter requires otherwise. Choose descriptive names: `snake_case` for Python files and functions, `camelCase` for JavaScript or TypeScript variables, and `PascalCase` for exported types and components. Keep generated files separate from hand-written source.

## Testing Guidelines

Add tests with each behavior change. Mirror the source layout under `tests/` when practical, and name tests after observable behavior rather than implementation details. Include success, failure, and boundary cases. Bug fixes should include a regression test that fails without the fix. Record any coverage threshold in the test configuration and CI workflow.

## Commit & Pull Request Guidelines

There is no readable commit history from which to infer an existing convention. Use short, imperative commit subjects such as `Add configuration loader` and keep unrelated changes separate. Pull requests should explain the problem, summarize the solution, list validation performed, and link relevant issues. Include screenshots or logs when output or user-visible behavior changes. Call out configuration changes, compatibility concerns, and follow-up work explicitly.

## Security & Configuration

Never commit credentials, tokens, private keys, or local environment files. Provide sanitized examples such as `.env.example`, document required variables, and keep machine-specific configuration out of version control.
