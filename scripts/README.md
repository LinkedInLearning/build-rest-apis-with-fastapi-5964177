Run helper for lesson servers
=============================

Usage
-----

Run a lesson module by passing the chapter module name and optional port:

```bash
./scripts/run_lesson.sh Ch05.05_03 8081
```

Notes
-----

- The script sets `PYTHONPATH` to the repository root so lesson-local modules (like `users.py`) import correctly when running as a module.
- To use a specific Python interpreter (for example your virtualenv), set `VENV_PY`:

```bash
VENV_PY=/path/to/venv/bin/python ./scripts/run_lesson.sh Ch05.05_03 8081
```

- This helper is intended for local development and smoke tests; CI should run lightweight import/syntax checks instead of starting long-lived servers.
