# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

A minimal Python project managed with `uv`. The main entry point is a trivial hello-world script, plus a small example that fetches a URL with `requests`. There's also a standalone `index.html` — a space-themed personal landing page with CSS animations and vanilla JS.

## Commands

```bash
# Run the main script
uv run python main.py

# Run the example
uv run python example.py

# Start a local HTTP server to view index.html
uv run python -m http.server 8080
# then open http://localhost:8080/index.html
```

## Architecture

```
uvtest/
├── main.py          # Entry point: prints "Hello from uvtest!"
├── example.py        # Demonstrates using the `requests` dependency
├── pyproject.toml    # Project metadata, Python >=3.9, depends on requests
├── uv.lock           # Locked dependency versions
├── .python-version   # Python 3.9
├── index.html        # Standalone static page (unrelated to the Python code)
└── .vscode/main.js   # VS Code extension scaffold (unrelated)
```

- **Package manager**: `uv` — use `uv run` / `uv sync` / `uv add`, not bare `pip`.
- **Single dependency**: `requests` (used in `example.py`).
- No tests, no linting, no build pipeline.
