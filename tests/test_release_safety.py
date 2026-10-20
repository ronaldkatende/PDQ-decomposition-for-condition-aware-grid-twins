from pathlib import Path
import hashlib
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def test_citation_matches_repository_and_software_version():
    txt = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    assert "cff-version: 1.2.0" in txt
    assert "Ronald" in txt and "Katende" in txt
    assert "https://github.com/ronaldkatende/PDQ-decomposition-for-condition-aware-grid-twins" in txt
    assert "version: 1.0.0" in txt

def test_frozen_data_hashes():
    for row in (ROOT / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if not row.strip():
            continue
        checksum, name = row.split(None, 1)
        assert hashlib.sha256((ROOT / name.strip()).read_bytes()).hexdigest() == checksum

def test_publication_cli_does_not_default_to_frozen_results():
    command = [sys.executable, str(ROOT / "scripts" / "dce_real_validation.py"), "--help"]
    p = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=True)
    assert "--out-root" in p.stdout
    assert "default: runs" in p.stdout
