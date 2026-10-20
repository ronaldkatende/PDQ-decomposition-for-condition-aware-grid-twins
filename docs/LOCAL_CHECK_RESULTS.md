# Release preparation checks

The release was checked without downloading the external datasets. Commands and outcomes:

- `python -m compileall -q dce_data scripts tests examples`: passed.
- `python -m pytest -q`: passed (test count recorded in release audit).
- `python examples/synthetic_sparse_recovery_demo.py`: passed.
- `python scripts/verify_release.py`: passed.
- `python scripts/build_publication_evidence.py --results-root results --out evidence_rebuilt`: completed.
- `python scripts/verify_archived_evidence.py --rebuilt evidence_rebuilt`: matched the key frozen numerical summaries.
- `python scripts/download_all.py --profile paper --root data --max-gb 5 --dry-run`: listed Ponte Moesa and GridEye without accessing the network.

These checks do not establish independent reproduction of all reported physical-data experiments. See `docs/VERIFICATION_SCOPE.md`.
