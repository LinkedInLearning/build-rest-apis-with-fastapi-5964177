# SECRETS.md — Required GitHub secrets for agent CI

If you intend to run the `agent-runner` workflow with live AI calls, add these secrets to the repository (or organization) secrets in GitHub Actions.

- `OPENAI_API_KEY` (required for live OpenAI calls): API key with permission to call the chosen model.
- `MODEL_NAME` (required if `OPENAI_API_KEY` is set): the model string to use, e.g. `gpt-5-mini`.

Notes:

- If `OPENAI_API_KEY` is not set, the workflow runs `scripts/agent_runner.py --dry-run` and will not call external APIs.
- Keep secrets scoped to the minimal required permission set and rotate them regularly.
