# Contribution Agreement

This repository does not accept pull requests (PRs). All pull requests will be closed.

However, if any contributions (through pull requests, issues, feedback or otherwise) are provided, as a contributor, you represent that the code you submit is your original work or that of your employer (in which case you represent you have the right to bind your employer). By submitting code (or otherwise providing feedback), you (and, if applicable, your employer) are licensing the submitted code (and/or feedback) to LinkedIn and the open source community subject to the BSD 2-Clause license.

Note for contributors and agents:

- This repository includes example AI agent guidance in `AGENTS.md` and secrets documentation in `SECRETS.md`. If you run automated agent checks or CI that call external AI providers, follow the instructions in those files and add secrets only to GitHub repository/organization secrets.
- Keep changes lesson-scoped (one `ChNN/NN_NN/` folder) unless explicitly requested by maintainers.

Local agent run (developer)

- Install dependencies locally:

  ```bash
  pip install -r requirements.txt
  ```

- Dry-run the agent runner (safe — prints the prompt, no external calls):

  ```bash
  python scripts/agent_runner.py --dry-run
  ```

- To run live (CI or developer machine): set secrets and run (use with caution):

  ```bash
  export OPENAI_API_KEY=your_key_here
  export MODEL_NAME=gpt-5-mini
  python scripts/agent_runner.py
  ```
