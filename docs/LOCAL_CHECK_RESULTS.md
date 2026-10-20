# Local verification completed for this prepared release

The following checks succeeded in the preparation environment:

- Python project compiles (`python -m compileall -q dce_data scripts tests examples`).
- 15 offline tests pass (`python -m pytest -q`).
- The synthetic sparse-recovery demo runs and reports a finite error and diagnostics.
- The evidence builder successfully rebuilds the reported numerical tables and statistics from the supplied frozen raw JSON.
- The evidence verifier matches: Ponte budget summary, GridEye main table, GridEye fixed-rank nested table, and `key_statistics.json`.
- The `paper` acquisition dry-run enumerates only Ponte Moesa and GridEye **without network access**.
- The project is installable as an editable Python package without resolving dependencies in the preparation environment.

**Verification boundary:** The two raw third-party measurement datasets were not bundled or newly downloaded. An independent end-to-end reproduction using newly acquired data has not yet been performed. The original recorded outputs are preserved for inspection.
