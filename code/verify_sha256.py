#!/usr/bin/env python3
from pathlib import Path
import hashlib, sys

root = Path(__file__).resolve().parents[1]
manifest = root / "SHA256SUMS.txt"

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

bad = []
for line in manifest.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    expected, rel = line.split("  ", 1)
    path = root / rel
    if not path.exists():
        bad.append((rel, "MISSING", expected))
        continue
    actual = sha256(path)
    if actual != expected:
        bad.append((rel, actual, expected))

if bad:
    for rel, actual, expected in bad:
        print(f"FAIL {rel}: {actual} != {expected}")
    sys.exit(1)

print("PASS: all SHA-256 entries verified.")
