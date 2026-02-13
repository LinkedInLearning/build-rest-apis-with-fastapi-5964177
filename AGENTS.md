# AGENTS.md — AI agent guidance and prompt templates

Purpose: provide an `AGENTS.md` that AI assistants and platform admins can use to work effectively on this repo.

Recommended model

- Preferred: GPT-5 mini for code edits, tests, and explanations. (This repo cannot enable models for your org; see admin steps below.)

Quick repo facts (for prompts)

- This repository contains many small, self-contained FastAPI examples under `ChNN/NN_NN/`.
- Each lesson uses `server.py` with `app = FastAPI()` and often `config.py` (Dynaconf) + `settings.yaml`.
- Example request files: `requests.http` and `request.json`; static assets under `Ch03/.../static/`.

Admin / platform steps to enable GPT-5 mini

1. Use your provider's admin console or support process to enable the GPT-5 mini model for your organization or workspace.
2. Document the change in a private devops/engineering doc and update CI secrets if you plan to run automated agents in CI.
3. Optionally add a repo-level `AGENTS.md` (this file) and a `CONTRIBUTING.md` note pointing to the org request steps.

Example system prompt (use as the assistant's system message)
"""
You are an expert coding assistant for the LinkedIn Learning FastAPI examples repository. Be concise, follow the repository conventions (each lesson is self-contained in `ChNN/NN_NN/`), prefer minimal, lesson-scoped edits, and avoid cross-chapter refactors unless explicitly requested. When editing files, run tests or quick smoke commands locally if possible and update the TODO list with progress. Ask clarifying questions only when necessary.
"""

Example user prompt templates

- Small change / bugfix:
"""
Make a minimal fix in `Ch03/03_03/server.py`: [describe bug]. Show the exact patch (git-style) and a one-line test command to verify locally.
"""

- New lesson example:
"""
Add a new lesson at `Ch06/06_01/` that demonstrates a POST endpoint accepting JSON with fields `x` and `y`. Create `server.py`, a `requests.http` example, and `settings.yaml`. Keep changes local to the new folder and follow the style in `Ch02/02_01/server.py`.
"""

Prompt engineering tips

- Provide filenames and exact edits; prefer `apply_patch`-style diffs as output when changing files.
- Ask for the minimal reproduction steps and an accompanying smoke test (`curl` or `pytest` command) before running broad refactors.
- When recommending runtime commands, use `python -m uvicorn ChNN.NN_NN.server:app --reload` or `python ChNN/NN_NN/server.py` depending on presence of `uvicorn.run`.

Local runtime checklist to include in prompts when relevant

- Install dependencies: `pip install -r requirements.txt`
- Run via uvicorn: `python -m uvicorn Ch03.03_03.server:app --reload` or `python Ch05/05_01/server.py`
- Use `SERVER_` env vars to override `dynaconf` settings, e.g. `SERVER_PORT=9090 python Ch05/05_01/server.py`.

Safety constraints for agents (explicit rules)

- Do not perform cross-chapter refactors without explicit approval.
- Avoid adding new external dependencies unless the user requests and documents why.
- Keep edits minimal and local; update `README.md` or `copilot-instructions.md` only with explicit user approval.

If you want, I can produce a short example PR template and a sample prompt for running an automated code-edit agent in CI.
