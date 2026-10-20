# Verification scope

This package includes the experiment scripts, frozen result JSON, evidence tables and plots supplied for the accepted article. The preparation checks confirm that the source compiles, the offline tests and synthetic example run, the frozen files match their hashes, and key tables/statistics can be rebuilt from the saved JSON.

**Not verified in this preparation:** fresh downloads of the two measurement datasets; an independent, full publication-mode rerun; identity of regenerated outputs across operating systems and dependency versions; and eligibility for Cambridge's Open Data or Open Materials badges.

These are separate claims. Anyone conducting a fresh study should preserve the data hashes, software release, dependency versions, configuration and logs. New runs write to `runs/` and `evidence_fresh/`, without replacing the frozen publication evidence.
