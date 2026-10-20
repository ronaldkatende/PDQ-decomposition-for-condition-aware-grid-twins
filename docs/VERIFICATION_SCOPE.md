# Verification scope

The frozen result JSON and derived CSV/PNG/PDF files were supplied with the accepted-manuscript reproducibility archive. Copying them into this software release does not independently validate their generation.

**Offline checks:** Python tests (including algorithmic invariance and diagnostics), project install, synthetic demonstration, and evidence-builder reproducibility from supplied frozen JSON.

**Not yet re-executed here:** obtaining the upstream measurements, retraining the recovery-aware basis, and a new end-to-end publication-mode experiment on Ponte Moesa and GridEye. Those steps require downloadable third-party datasets and the specified runtime. Accordingly, this release should not be presented as an independently rerun publication experiment until those checks have been performed.

The release makes original software and the previously recorded outputs inspectable. If results are regenerated on another platform, the library environment, Git commit, data hashes, and parameter configuration should be recorded.
