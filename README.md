# Sparse-sensor full-field recovery for digital twins

Code and recorded results for *Stable Sparse-Sensor Full-Field Recovery for Industrial Digital Twins* (accepted in *Data-Centric Engineering*).

The study compares standard POD/SVD with recovery-aware subspace design (RASD). It separates representation error, latent identifiability, noise amplification, ridge bias, and performance after a change in operating regime. RASD does **not** outperform SVD in every setting.

## Install and test

Requires Python 3.10 or newer. From the repository root:

```bash
python -m pip install -e . pytest
python -m pytest -q
python examples/synthetic_sparse_recovery_demo.py
```

## Check the published numbers (no data download)

The original experiment outputs are under `results/`; the derived tables and plots are under `publication_evidence/`. To rebuild and compare the numerical tables:

```bash
python scripts/verify_release.py
python scripts/build_publication_evidence.py --results-root results --out evidence_rebuilt
python scripts/verify_archived_evidence.py --rebuilt evidence_rebuilt
```

These checks reproduce the numerical summaries **from saved JSON outputs**. They do not repeat the experiments or independently validate the underlying measurements.

## Rerun the experiments

The two data sources are:

| Data | Reference |
| --- | --- |
| Ponte Moesa bridge strain | https://doi.org/10.3929/ethz-b-000716850 |
| GridEye PMU measurements | https://doi.org/10.5281/zenodo.17648863 |

Raw datasets are not included. Respect the source licences. To inspect the acquisition plan and attempt the public downloads:

```bash
python scripts/download_all.py --profile paper --root data --max-gb 5 --dry-run
python scripts/download_all.py --profile paper --root data --max-gb 5
python scripts/audit_data.py --root data
```

The validation expects `data/raw/ponte_moesa_2025/Strain Data.zip` and `data/raw/grideye_real_pmu_2025/Steady state data.zip`. Optional GridEye event archives are described in `docs/DATA_SOURCES.md`. If a provider changes its download structure, acquire the named archives manually from the cited records.

Run a short check before a full run:

```bash
python scripts/dce_real_validation.py ponte --data-root data --quick
python scripts/dce_real_validation.py grideye --data-root data --quick
```

Publication settings are in `configs/validation.json`:

```bash
python scripts/dce_real_validation.py ponte --data-root data --publication
python scripts/dce_real_validation.py grideye --data-root data --publication
python scripts/build_publication_evidence.py --results-root runs --out evidence_fresh
```

**New experiments write to `runs/`; they do not overwrite `results/` or `publication_evidence/`.** The full run may require substantial memory and time. Record the dataset hashes, Git commit, Python versions, and configuration when comparing reruns. Exact numerical equality across environments is not guaranteed.

## Files

- `dce_data/`: data acquisition and provenance code
- `scripts/`: validation, diagnostics, evidence construction and verification
- `configs/`: experimental settings and data catalogue
- `tests/`, `examples/`: offline tests and demonstration
- `results/`: frozen experiment JSON, **not** original measurements
- `publication_evidence/`: paper tables, figures and recorded hashes
- `docs/`: sources, verification limits and release instructions

`SHA256SUMS.txt` lets readers verify the frozen results. `CITATION.cff` gives the software citation. The MIT licence applies to the original code, not the external datasets. Full end-to-end independent replication has **not** been verified as part of this release preparation; see `docs/VERIFICATION_SCOPE.md`.
