# Copilot Instructions

## About this codebase

This software is written with assistance from GitHub Copilot. The code is structured to be readable, modifiable, and extendable by Copilot (and other LLM-based agents). Every design decision should reinforce that.

### Guidelines for LLM-friendly code

- **Flat, explicit control flow.** Prefer straightforward if/else and early returns over deeply nested logic, complex inheritance hierarchies, or metaprogramming. Every function should be understandable from its source alone.
- **Small, single-purpose functions.** Keep functions short (ideally under ~40 lines). Each function does one thing with a clear name that describes it. This gives the LLM better context boundaries.
- **Descriptive naming over comments.** Variable and function names should make intent obvious. Use comments only when *why* isn't clear from the code — never to explain *what*.
- **Colocate related logic.** Keep constants, helpers, and the code that uses them close together (or in the same small file). Avoid scattering related pieces across many modules — LLMs work best when relevant context is nearby.
- **Consistent patterns.** When multiple functions do similar things, structure them identically. Consistent shape lets the LLM reliably extend the pattern.
- **No magic.** Avoid decorators that hide behavior, dynamic attribute access, implicit registration, or monkey-patching. Everything should be traceable by reading the code top-to-bottom.
- **Graceful error handling.** Wrap I/O and external calls in try/except (or the language's equivalent). Never let a transient failure crash the main workflow. Log the error and continue.
- **Minimal dependencies.** Only add a dependency when it provides substantial value. Fewer deps mean less surface area for the LLM to misunderstand.
- **One concept per file.** Each module owns a single concern. Don't mix unrelated responsibilities in the same file.
- **Design for testability.** Separate pure decision logic from I/O and subprocess calls so core functions can be tested without mocking. Pass dependencies as arguments rather than hard-coding them inside functions when practical. Keep side-effect-free helpers (parsing, validation, data transforms) in their own functions so they can be unit tested directly.

### Documentation maintenance

- When completing a task that changes the project structure, key files, architecture, or conventions, update `.github/copilot-instructions.md` to reflect the change.
- Keep the project-specific sections (Project structure, Key files, Architecture, Conventions) accurate and current.
- Never modify the coding guidelines or testing conventions sections above.
- This file is a **style guide**, not a spec. Describe file **roles** (e.g. 'server entry point'), not implementation details (e.g. 'uses List<T> with auto-incrementing IDs'). Conventions describe coding **patterns** (e.g. 'consistent JSON error envelope'), not implementation choices (e.g. 'store data in a static variable'). SPEC.md covers what to build — this file covers how to write code that fits the project.

## Project structure

This project is intentionally minimal and flat. The Streamlit app lives in `app.py` as the single entry point for UI rendering and button interaction. Python dependency setup is declared in `requirements.txt`, while project intent and specification docs live at the repo root (`REQUIREMENTS.md`, `SPEC.md`, `README.md`). There is no application package structure yet; keep additions small and direct unless the project grows beyond its demo scope.

## Key files

- `app.py` — Streamlit entry point that renders the interface and handles the Hello World interaction.
- `requirements.txt` — Python package requirements for the app.
- `README.md` — quick-start instructions for running the project locally.
- `SPEC.md` — technical specification and architecture notes for the project.
- `REQUIREMENTS.md` — original user-facing requirement summary for the minimal Streamlit app.

## Architecture

This project uses a very thin architecture: Streamlit owns the interface lifecycle, and the app logic stays in a single Python entry module. User clicks trigger local control flow in `app.py`, which updates the displayed greeting directly without a service layer or persistent backend. The dependency direction stays simple—UI code depends on Python and Streamlit, with no cross-layer abstractions or shared models. Because the app is intentionally minimal, data flow is direct and easy to trace from interaction to rendered output.

## Testing conventions

- **Use the project's test framework.** Plain functions with descriptive names.
- **Test the contract, not the implementation.** A test should describe expected behavior in terms a user would understand — not mirror the code's internal branching. If the test would break when you refactor internals without changing behavior, it's too tightly coupled.
- **Name tests as behavioral expectations.** `test_expired_token_triggers_refresh` not `test_check_token_returns_false`. The test name should read like a requirement.
- **Use realistic inputs.** Feed real-looking data, not minimal one-line synthetic strings. Edge cases should be things that could actually happen — corrupted inputs, empty files, missing fields.
- **Prefer regression tests.** When a bug is found, write the test that would have caught it before fixing it. This is the highest-value test you can write.
- **Don't test I/O wrappers.** Functions that just read a file and call a pure helper don't need their own tests — test the pure helper directly.
- **No mocking unless unavoidable.** Extract pure functions for testability so you don't need mocks. If you find yourself mocking, consider whether you should be testing a different function.

## Conventions

- Keep the application intentionally small and direct; prefer straightforward Python code over premature abstraction.
- Use clear, descriptive names and simple control flow so the interaction path is easy to follow from top to bottom.
- Keep UI output and state changes local to the entry module unless a real need for decomposition appears.
- Prefer explicit, minimal error surfacing in the interaction flow rather than hidden fallback logic.
- Maintain a lightweight dependency footprint; add libraries only when they demonstrably improve the demo's runtime or usability.
