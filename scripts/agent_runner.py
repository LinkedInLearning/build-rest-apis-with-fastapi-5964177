#!/usr/bin/env python3
"""
Simple agent-runner stub used by the example CI workflow.

This script is intentionally a safe stub — it prints the prompt that would be
sent to an AI agent and supports a `--dry-run` flag. To enable real calls,
wire in your provider's SDK and set `OPENAI_API_KEY` (or your provider secret).
"""
import os
import sys
from pathlib import Path


def build_prompt():
    repo_root = Path(__file__).resolve().parent.parent
    agents_md = repo_root / 'AGENTS.md'
    prompt = """Repository agent run — use AGENTS.md guidance.

Context (first 4000 chars of AGENTS.md):
"""
    if agents_md.exists():
        content = agents_md.read_text(encoding='utf8')[:4000]
        prompt += content
    else:
        prompt += "(AGENTS.md not found)"
    return prompt


def main(dry_run=False):
    prompt = build_prompt()
    print('=== AGENT PROMPT START ===')
    print(prompt)
    print('=== AGENT PROMPT END ===')

    api_key = os.environ.get('OPENAI_API_KEY')
    model = os.environ.get('MODEL_NAME', 'gpt-5-mini')

    if dry_run or not api_key:
        print('\nDry run: no requests will be sent to an external API.')
        if not api_key:
            print('Hint: set OPENAI_API_KEY and MODEL_NAME in workflow/secrets to enable live calls.')
        return 0

    try:
        from openai import OpenAI
    except Exception as exc:  # pragma: no cover - environment dependent
        print('openai package not installed. Install requirements to enable API calls.')
        print('Exception:', exc)
        return 1

    client = OpenAI(api_key=api_key)
    try:
        # Use the Responses API which returns a structured `output` field.
        resp = client.responses.create(model=model, input=prompt, max_output_tokens=1024)

        # Try to extract textual content from the structured response.
        text = None
        try:
            out = getattr(resp, 'output', None) or resp.get('output', None)
            if out:
                parts = []
                for item in out:
                    # item may be dict-like with `content` array
                    content_list = item.get('content', []) if isinstance(item, dict) else []
                    for c in content_list:
                        if isinstance(c, dict) and 'text' in c:
                            parts.append(c['text'])
                        elif isinstance(c, str):
                            parts.append(c)
                if parts:
                    text = ''.join(parts)
        except Exception:
            text = None

        # fallback to output_text if present
        if not text:
            text = getattr(resp, 'output_text', None) or resp.get('output_text', None) if isinstance(resp, dict) else None

        print('\n=== MODEL RESPONSE START ===')
        print(text or resp)
        print('=== MODEL RESPONSE END ===')
    except Exception as e:
        print('API call failed:', e)
        return 2

    return 0


if __name__ == '__main__':
    dry = '--dry-run' in sys.argv
    raise SystemExit(main(dry_run=dry))
