## Summary

Describe the change in one sentence. Keep PRs small and lesson-scoped.

## Checklist

- [ ] The change is local to a single `ChNN/NN_NN/` folder unless a cross-chapter change is explicitly requested.
- [ ] Ran the example locally (see `README.md` and chapter `requests.http` for smoke tests).
- [ ] If code changes were made, include an `apply_patch`-style diff in the PR body.
- [ ] If the PR used an AI agent, update `.github/copilot-instructions.md` or `AGENTS.md` if you changed repository conventions.

## How to run / smoke test

Provide 1-2 commands reviewers can run to verify the change (example below):

```
pip install -r requirements.txt
python Ch05/05_01/server.py
curl http://localhost:8080/health
```

## Notes

Link to related lesson or issue and mention any manual setup (DB creation, secrets).
