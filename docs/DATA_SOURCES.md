# Data sources

The paper's experiments use these original datasets:

| Dataset | DOI | Expected downloaded archive |
| --- | --- | --- |
| Ponte Moesa Campagnola bridge strain | https://doi.org/10.3929/ethz-b-000716850 | `data/raw/ponte_moesa_2025/Strain Data.zip` |
| GridEye PMU measurements | https://doi.org/10.5281/zenodo.17648863 | `data/raw/grideye_real_pmu_2025/Steady state data.zip` |

Optional GridEye events are `Frequency events.zip` and `Voltage events.zip` in the same directory as `Steady state data.zip`. The acquisition catalogue is in `configs/sources.json`. Its other sources are **not** part of the published Ponte/GridEye validation.

The downloader may need adjustment if the data providers change filenames or access endpoints. No third-party raw data are bundled or relicensed here.
