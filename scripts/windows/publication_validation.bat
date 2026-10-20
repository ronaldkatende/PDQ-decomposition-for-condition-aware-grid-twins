@echo off
cd /d "%~dp0\..\.."
python scripts\dce_real_validation.py ponte --data-root data --publication || exit /b 1
python scripts\dce_real_validation.py grideye --data-root data --publication || exit /b 1
python scripts\build_publication_evidence.py --results-root runs --data-root data --out evidence_fresh || exit /b 1
