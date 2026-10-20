# Reproducibility protocol

1. Install from `pyproject.toml` and record `python --version` and `python -m pip freeze`.
2. Run no-data tests and the synthetic example.
3. Verify the archived figures/tables from frozen JSON using commands in `README.md`.
4. For a fresh scientific run, acquire Ponte Moesa and GridEye data from the cited original archives. Their availability and licences are controlled by providers.
5. Preserve `data/provenance/` and `data/metadata/` from acquisition, including hashes.
6. Run the quick configuration before publication mode; record the selected mode and the exact `configs/validation.json` SHA-256.
7. Rerun Ponte and GridEye via `scripts/dce_real_validation.py`; use training-only scaling, chronological/cross-regime splits, and validation-selected rank/ridge.
8. Rebuild evidence from fresh outputs under a **new folder**. Never overwrite the bundled original publication results without recording the change.
9. Compare outputs with the bundled tables, document any differences, and archive data-source hashes, commit, runtime versions, and logs.

The original paper does not establish universal superiority of RASD over standard POD/SVD. Sensor rank, geometry, ridge bias, regime validity, and reconstruction error must be interpreted separately.
