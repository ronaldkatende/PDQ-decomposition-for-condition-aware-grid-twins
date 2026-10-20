# Publication Evidence Audit

This report is generated directly from the publication JSON files. It is deliberately conservative: Ponte significance is evaluated at the record level, with an additional bootstrap clustered by M2 row, rather than treating every sensor-budget configuration as independent.

## 1. Ponte Moesa: real sparse-to-dense strain recovery

All 15 non-empty records completed successfully.
The publication analysis contains 75 record-budget configurations across sensor budgets [4, 8, 16, 32, 64].

### Budget-wise paired evidence

- **4 sensors:** median SVD error 2.058%, median RASD error 2.088%; median relative RASD change -1.08% (cluster-bootstrap 95% CI [-5.77, 0.01]); 4 wins / 1 ties / 10 losses; Wilcoxon p=0.1688, Holm-adjusted p=0.5065.
- **8 sensors:** median SVD error 2.022%, median RASD error 2.020%; median relative RASD change 0.13% (cluster-bootstrap 95% CI [-2.11, 0.27]); 9 wins / 0 ties / 6 losses; Wilcoxon p=0.8904, Holm-adjusted p=1.
- **16 sensors:** median SVD error 1.889%, median RASD error 1.909%; median relative RASD change -0.00% (cluster-bootstrap 95% CI [-3.61, 0.15]); 6 wins / 3 ties / 6 losses; Wilcoxon p=0.6788, Holm-adjusted p=1.
- **32 sensors:** median SVD error 1.868%, median RASD error 1.908%; median relative RASD change -0.16% (cluster-bootstrap 95% CI [-2.68, 0.19]); 4 wins / 1 ties / 10 losses; Wilcoxon p=0.04126, Holm-adjusted p=0.165.
- **64 sensors:** median SVD error 1.799%, median RASD error 1.907%; median relative RASD change -0.24% (cluster-bootstrap 95% CI [-1.40, 0.07]); 4 wins / 2 ties / 9 losses; Wilcoxon p=0.02155, Holm-adjusted p=0.1077.

### Across budgets without pseudo-replication

Each bridge record was first collapsed across sensor budgets. Across 15 records (5 row clusters), the mean record-level relative RASD change was -1.21% and the median was -0.25%. The row-cluster bootstrap 95% CI for the mean record-level change is [-3.27, 0.15]. Record-level Wilcoxon p=0.1876.

Rank-deficient sensed bases occurred in 2 SVD configurations and 2 RASD configurations. In these cases the correct smallest singular value is zero and the ridge-bias factor should be one; this directly distinguishes regularized solvability from latent identifiability.

## 2. GridEye: cross-regime deployment

- **1 site(s)** (1_5), rank 8: SVD noon/evening error 11.915% / 1.591%; RASD 11.850% / 0.657%; RASD relative change 58.72%.
- **2 site(s)** (1_10;1_5), rank 10: SVD noon/evening error 6.425% / 0.119%; RASD 6.415% / 0.235%; RASD relative change -97.10%.
- **3 site(s)** (1_10;1_5;1_8), rank 12: SVD noon/evening error 6.097% / 0.645%; RASD 6.104% / 0.649%; RASD relative change -0.64%.
- **4 site(s)** (1_10;1_5;1_8;1_9), rank 20: SVD noon/evening error 3.972% / 0.239%; RASD 3.723% / 0.240%; RASD relative change -0.27%.
- **5 site(s)** (1_10;1_5;1_6;1_7;1_8), rank 20: SVD noon/evening error 2.226% / 0.220%; RASD 2.226% / 0.220%; RASD relative change 0.01%.
- **6 site(s)** (1_10;1_5;1_6;1_7;1_8;1_9), rank 20: SVD noon/evening error 2.146% / 0.657%; RASD 2.147% / 0.657%; RASD relative change -0.01%.

### Fixed-rank nested sensor path

From 1 to 6 sites, $\sigma_{\min}$ changed from 0.2766 to 0.9204, while exact amplification changed from 3.569 to 1.086. Evening test error changed from 2.295% to 30.395% (13.24x).
Monotonic checks: sigma_min nondecreasing = True; amplification nonincreasing = True; test error nondecreasing = False.
Spearman trends across the six nested points: site count vs sigma_min rho=1.000; site count vs amplification rho=-1.000; site count vs test error rho=0.257. Because n=6, these trend statistics are descriptive, not stand-alone inferential evidence.

## 3. Event-file integrity check

Hashed 6 event CSV files; unique hashes = 4.
Exact byte-identical duplicates were detected and should not be counted as independent events:
- 12ae5b64c79f1de8: Frequency events.zip::Underfrequency event 2.csv; Frequency events.zip::Overfrequency event.csv; Frequency events.zip::Underfrequency event.csv

## 4. Claims that the data support

1. Real sparse-to-dense recovery can be evaluated without imputing the Ponte benchmark: all reported Ponte fields use spatial coordinates observed at every snapshot.
2. Recovery-aware basis learning is conditional rather than universally dominant. The paper should report both improvements and deteriorations.
3. Rank, smallest sensed singular value, exact sensor-to-field amplification, ridge bias, and deployment error are empirically distinct quantities.
4. The GridEye fixed-rank nested experiment directly tests whether improved nominal sensing geometry is sufficient for cross-regime deployment. The numerical sequence should be shown in full rather than reduced to a single cherry-picked comparison.
5. Event results should be described as separate event stress tests only after the hash audit confirms which files are genuinely distinct.

## 5. Claims to avoid

- Do not claim that RASD universally outperforms POD/SVD.
- Do not count the 75 Ponte configurations as 75 independent experiments.
- Do not infer that lower condition number alone guarantees deployment reliability.
- Do not call ERA statistics SCADA or operational state measurements.
- Do not treat multiple event files with identical hashes as independent validation.
