"""Verify that frozen experiment outputs match the release checksum manifest."""
from __future__ import annotations
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    manifest = ROOT / "SHA256SUMS.txt"
    entries = 0
    for row in manifest.read_text(encoding="utf-8").splitlines():
        if not row.strip():
            continue
        checksum, name = row.split(None, 1)
        rel = Path(name.strip())
        if rel.is_absolute() or ".." in rel.parts:
            raise ValueError(f"Unsafe manifest path: {rel}")
        src = ROOT / rel
        if not src.is_file():
            raise FileNotFoundError(rel)
        got = hashlib.sha256(src.read_bytes()).hexdigest()
        if checksum != got:
            raise AssertionError(f"SHA-256 mismatch: {rel}")
        entries += 1
    if not entries:
        raise ValueError("Empty SHA256SUMS.txt")
    print(f"PASS: {entries} frozen evidence files match SHA256SUMS.txt")

if __name__ == "__main__":
    main()
