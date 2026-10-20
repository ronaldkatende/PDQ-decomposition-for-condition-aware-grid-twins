"""Check regenerated evidence against the archived publication output.

Checks are intentionally limited to key numeric tables and JSON statistics.
Event SHA-256 hashes need the original source files and are not compared offline.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
NUMERIC_TABLES = {
    "ponte_budget_summary.csv": ["sensor_count", "svd_median_error_percent", "rasd_median_error_percent", "wilcoxon_p_holm"],
    "grideye_main.csv": ["sites", "svd_test_relerr", "rasd_test_relerr"],
    "grideye_nested_fixed_rank.csv": ["site_count", "test_relerr", "sigma_min", "exact_amplification"],
}

def check_table(archived: Path, rebuilt: Path) -> None:
    a = pd.read_csv(archived)
    b = pd.read_csv(rebuilt)
    if list(a.columns) != list(b.columns) or a.shape != b.shape:
        raise AssertionError(f"Table layout differs for {archived.name}: {a.shape} vs {b.shape}")
    for col in a.columns:
        if pd.api.types.is_numeric_dtype(a[col]) and pd.api.types.is_numeric_dtype(b[col]):
            if not np.allclose(a[col].to_numpy(dtype=float), b[col].to_numpy(dtype=float), rtol=1e-10, atol=1e-12, equal_nan=True):
                raise AssertionError(f"Values differ for {archived.name}: {col}")
        else:
            if not a[col].fillna('<NA>').astype(str).equals(b[col].fillna('<NA>').astype(str)):
                raise AssertionError(f"Values differ for {archived.name}: {col}")

def compare_obj(a, b, location='root'):
    if isinstance(a, dict) and isinstance(b, dict):
        if a.keys()!=b.keys(): raise AssertionError(f"Keys differ in {location}")
        for k in a: compare_obj(a[k],b[k],location+'.'+k)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a)!=len(b): raise AssertionError(f"List size differs in {location}")
        for i,(x,y) in enumerate(zip(a,b)): compare_obj(x,y,f'{location}[{i}]')
    elif isinstance(a,(int,float)) and not isinstance(a,bool) and isinstance(b,(int,float)) and not isinstance(b,bool):
        if not np.isclose(a,b,rtol=1e-10,atol=1e-12,equal_nan=True):
            raise AssertionError(f'Number differs in {location}: {a} vs {b}')
    elif a!=b:
        raise AssertionError(f'Value differs in {location}: {a} vs {b}')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--rebuilt',type=Path,required=True)
    ap.add_argument('--original',type=Path,default=ROOT/'publication_evidence')
    args=ap.parse_args()
    for f in NUMERIC_TABLES:
        check_table(args.original/f,args.rebuilt/f)
        print('PASS',f)
    a=json.loads((args.original/'key_statistics.json').read_text())
    b=json.loads((args.rebuilt/'key_statistics.json').read_text())
    compare_obj(a,b)
    print('PASS key_statistics.json')
    print('PASS: archived numerical evidence reproducible from frozen JSON')

if __name__=='__main__': main()
