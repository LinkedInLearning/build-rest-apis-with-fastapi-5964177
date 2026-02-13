#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <lesson_module> [port]"
  echo "Example: $0 Ch05.05_03 8081"
  exit 1
fi

MODULE="$1.server"
PORT="${2:-8080}"

# Use the repo root as PYTHONPATH so lessons can import local modules
export PYTHONPATH="$(pwd)"

# Allow overriding the python executable via VENV_PY
VENV_PY="${VENV_PY:-python}"

exec "$VENV_PY" -m uvicorn "$MODULE:app" --reload --port "$PORT"
