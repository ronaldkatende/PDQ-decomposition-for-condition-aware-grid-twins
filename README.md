# Sparse-sensor full-field recovery for digital twins

Reproducibility code for the research paper **Stable Sparse-Sensor Full-Field Recovery for Industrial Digital Twins** (*Data-Centric Engineering*, accepted manuscript). This release contains the original numerical workflow, its frozen output JSON files, and the tables and figures derived from them. No third-party raw measurements are redistributed.

## What the project does

The workflow reconstructs spatial strain and electrical measurement fields using sparse observations and a reduced basis. It compares proper orthogonal decomposition / singular value decomposition (POD/SVD) with recovery-aware subspace design (RASD). It reports field reconstruction error, representation error, latent identifiability, sensor-to-field amplification, and ridge-regularization bias. It also tests transfer across measurement regimes.

The main evidence comes from two publicly available datasets:

| Dataset | Source | Purpose |
| --- | --- | --- |
| Ponte Moesa Campagnola bridge | https://doi.org/10.3929/ethz-b-000716850 | Distributed strain; 15 records; chronological splits |
| GridEye phasor measurements | https://doi.org/10.5281/zenodo.17648863 | Electrical fields; morning train, noon validation, evening test |

Additional sources in `configs/sources.json` are optional acquisition examples. They **are not** evidence supporting the paper's main results.

## Quick start (Windows, Linux, macOS)

Create a Python 3.10+ virtual environment:

```bash
python -m venv .venv
```

Activate it with `.venv\Scripts\activate` on Windows or `source .venv/bin/activate` on Linux/macOS. Install the project and run local no-data checks:

```bash
python -m pip install -e . pytest
python -m pytest -q
python examples/synthetic_sparse_recovery_demo.py
```

The synthetic example is a **software test only**, not a source of reported scientific evidence. All scripts use project-relative defaults; no personal computer directories are needed.

## Verify the paper's tables without downloading data

The exact recorded publication outputs are provided under:

```text
results/ponte/publication/{ponte_results.json,ponte_manifest.json}
results/grideye/publication/grideye_results.json
publication_evidence/
```

Rebuild the tables, figures, and statistics from the frozen result JSON files:

```bash
python scripts/build_publication_evidence.py --results-root results --out evidence_rebuilt
python scripts/verify_archived_evidence.py --rebuilt evidence_rebuilt
```

The verifier checks core numerical tables/statistics against the archived evidence. Event hash provenance in `publication_evidence/grideye_event_hashes.csv` was recorded during the original run: it can only be independently recomputed if you download the raw GridEye events. The evidence rebuild itself does **not** rerun the model training or the recovery experiments.

## Rerun the full experiments from original datasets

Dry-run the acquisition plan:

```bash
python scripts/download_all.py --profile paper --root data --max-gb 5 --dry-run
```

Then fetch the public data (network access and source availability required):

```bash
python scripts/download_all.py --profile paper --root data --max-gb 5
python scripts/audit_data.py --root data
```

The `paper` acquisition profile limits the downloader to Ponte Moesa and GridEye. The validation pipeline expects the following downloaded archives under `data/raw/` (see `docs/DATA_SOURCES.md` and `docs/REPRODUCIBILITY.md`):

```text
data/raw/ponte_moesa_2025/Strain Data.zip
data/raw/grideye_real_pmu_2025/Steady state data.zip
```

If available, GridEye `Frequency events.zip` and `Voltage events.zip` enable the event stress tests. Acquisition of upstream data may be affected by provider access and file layout changes. The recorded output JSON files remain available for auditing even if downloads fail.

Run a quick validation first:

```bash
python scripts/dce_real_validation.py ponte --data-root data --quick
python scripts/dce_real_validation.py grideye --data-root data --quick
```

Run the specified publication-mode configuration:

```bash
python scripts/dce_real_validation.py ponte --data-root data --publication
python scripts/dce_real_validation.py grideye --data-root data --publication
python scripts/build_publication_evidence.py --results-root results --data-root data --out evidence_fresh
```

Batch/shell wrappers are provided under `scripts/windows/` and `scripts/*.sh`. This can take substantial time and memory depending on the downloaded data and hardware. The paper's specific sensor budgets, rank grid, ridge grid, and random seed are recorded in `configs/validation.json`. No benchmark is promised to be identical across changed library versions and source datasets.

## Repository structure

```text
configs/                  data-source catalogue and experiment settings
dce_data/                 portable acquisition library
scripts/                  validation, evidence building, checks, helpers
tests/                    fast offline software and numerical tests
examples/                 no-download synthetic demonstration
results/                  frozen experiment JSON files (not raw data)
publication_evidence/     frozen article tables, statistics, plots and hashes
docs/                     data sources, reproducibility and release checks
data/                     runtime-only downloads (excluded from Git)
```

The publication work compares bases at fixed sensor sites. RASD is **not** claimed to dominate SVD: the paper reports mixed results on real bridge and grid datasets. In particular, stronger nominal sensing geometry did not guarantee lower evening transfer error on GridEye. The released JSON and report allow readers to inspect both improvements and failures.

## Integrity, limitations and reuse

- `SHA256SUMS.txt` records the included frozen results and evidence files; do not edit those outputs when presenting them as the paper's original evidence.
- `python scripts/verify_archived_evidence.py --rebuilt evidence_rebuilt` checks key results without raw data.
- The repository is not anonymized at the GitHub/Zenodo account level. No personal machine paths, private tokens, or outdated personal repository links are required in the source package.
- The software is offered under the MIT License (see `LICENSE`). This licence covers original code only. Third-party datasets keep their own terms.
- Cite the associated paper and the **version-specific Zenodo DOI** once issued. See `docs/RELEASE_CHECKLIST.md`.
