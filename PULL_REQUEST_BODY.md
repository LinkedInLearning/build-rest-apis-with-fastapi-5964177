chore(agent): add agent runner, AGENTS.md, CI template, and docs for AI workflow

Summary

- Adds `scripts/agent_runner.py` — safe dry-run + optional OpenAI Responses API integration
- Adds `AGENTS.md` with prompt templates and admin guidance
- Adds `.github/workflows/agent-runner.yml` (template CI job)
- Adds `SECRETS.md` documenting required secrets: `OPENAI_API_KEY`, `MODEL_NAME`
- Updates `.github/copilot-instructions.md` and `CONTRIBUTING.md` to reference agent docs
- Adds `.github/pull_request_template.md` for lesson-scoped PRs

Checklist

- [ ] I verified `scripts/agent_runner.py --dry-run` prints `AGENTS.md` context
- [x] I verified `scripts/agent_runner.py --dry-run` prints `AGENTS.md` context
- [ ] No cross-chapter refactors were made (changes are lesson/infra scoped)
- [ ] If enabling live CI, add `OPENAI_API_KEY` and `MODEL_NAME` to repo/orga secrets

Notes

Workflow runs in dry-run if `OPENAI_API_KEY` is not set. If you want me to open
the PR draft for you, provide a GitHub Personal Access Token (PAT) with repo
access and confirm `draft=yes` or `draft=no`.
