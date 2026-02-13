# Copilot instructions for this repository

Purpose: Help an AI coding assistant be immediately productive in this LinkedIn Learning FastAPI course repository.

## Big picture
- The repo is a set of small, self-contained FastAPI example apps organized under `ChNN/NN_NN/`. There is no single monolith—each `server.py` is intended to be run independently to demonstrate a lesson.
- Typical module responsibilities:
  - `server.py`: FastAPI `app = FastAPI()` and lesson endpoints (entrypoint for running).
  - `config.py` + `settings.yaml`: optional `dynaconf`-based configuration.
  - `requests.http` or `request.json`: example requests used by the lesson.
  - `static/`: simple static HTML assets (see `Ch03/03_03/static/`).

## Developer workflows (concrete)
- Run a lesson quickly by invoking its `server.py`. Example:

  python Ch05/05_01/server.py

- Use `uvicorn` directly for auto-reload and module-style runs:

  python -m uvicorn Ch05.05_01.server:app --reload

  Ensure the repository root is on `PYTHONPATH` if running module-style from the workspace root.
- Override dynaconf settings via environment variables prefixed `SERVER_`. Example (change port):

  SERVER_PORT=9090 python Ch05/05_01/server.py

- Use the `requests.http` files for quick API examples with the VSCode REST Client, or convert them to `curl` using the provided JSON in `request.json` files (e.g., `Ch01/01_03/request.json`).
- DB-related lessons include helper scripts. Example: `Ch05/05_04/create-db.sh` creates `trades.db` from `schema.sql` (uses `sqlite3`).

## Project conventions & common patterns
- Entrypoint: every example exposes `app = FastAPI()` in `server.py`; new examples should follow that pattern so they are runnable via uvicorn.
- Config: `dynaconf` is used when present. See `Ch05/05_01/config.py`:

  from dynaconf import Dynaconf

  settings = Dynaconf(envvar_prefix='SERVER', settings_files=['settings.yaml', '.secrets.yaml'])

- Static files are mounted via `StaticFiles` (see `Ch03/03_03/server.py`) and reachable under `/static`.
- Some examples demonstrate raw HTTP or payload structure (e.g., `Ch01/01_02/post.sh` uses `nc` to send raw HTTP; `Ch01/01_03/request.json` shows a JSON payload example).

## Integration points & external deps
- Dependencies are listed in `requirements.txt`: primary libs are `fastapi`, `dynaconf`, and `pillow`.
- Database setup (when present) uses plain SQLite scripts and shell helpers (see `Ch05/05_04/create-db.sh` and `schema.sql`). No ORMs are required by the examples.

## Debugging and testing tips specific to this repo
- Use `uvicorn --reload` when editing a lesson.
- Check mounted static paths when a handler returns `RedirectResponse` (see `Ch03/03_03/server.py`)—static files live relative to the lesson folder.
- When changing settings, prefer `settings.yaml` in the lesson folder or `SERVER_` env vars rather than editing code.

## What not to do
- Avoid cross-chapter refactors or introducing shared packages—examples are intentionally isolated for teaching.
- Do not assume CI or automated tests; tests are manual via `requests.http` or shell scripts.

## Quick file references
- Lesson entry: `Ch05/05_01/server.py` (argument parsing + `uvicorn.run`).
- Config example: `Ch05/05_01/config.py` + `Ch05/05_01/settings.yaml` (default port 8080).
- Static example: `Ch03/03_03/server.py` and `Ch03/03_03/static/`.
- Raw HTTP example: `Ch01/01_02/post.sh` (netcat), payload example: `Ch01/01_03/request.json`.

If you'd like, I can add a short checklist for running a specific chapter (example commands to run `Ch05/05_01` and `Ch03/03_03`) or expand the notes for a particular lesson—tell me which chapter to focus on.
