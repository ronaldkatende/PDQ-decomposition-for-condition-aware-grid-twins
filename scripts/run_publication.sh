#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
DATA_ROOT="${1:-data}"
python scripts/dce_real_validation.py ponte --data-root "$DATA_ROOT" --publication
python scripts/dce_real_validation.py grideye --data-root "$DATA_ROOT" --publication
python scripts/build_publication_evidence.py --results-root runs --data-root "$DATA_ROOT" --out evidence_fresh
