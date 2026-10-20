# Archived publication evidence

These tables, charts, event hashes, LaTeX tables, and reports are the frozen publication evidence supplied with the accepted manuscript. They are stored as recorded and should not be overwritten in place. To regenerate their analytical aggregates from frozen experiment JSON, run:

```bash
python scripts/build_publication_evidence.py --results-root results --out evidence_rebuilt
python scripts/verify_archived_evidence.py --rebuilt evidence_rebuilt
```

The original `grideye_event_hashes.csv` requires the original source archives to recompute; an offline evidence rebuild will not fabricate those hashes.
