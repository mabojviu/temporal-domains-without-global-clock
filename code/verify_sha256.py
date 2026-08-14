#!/usr/bin/env python3
from pathlib import Path
import hashlib, sys

root = Path(__file__).resolve().parents[1]
manifest = root / "SHA256SUMS.txt"
failed = []
count = 0
for raw in manifest.read_text(encoding="utf-8").splitlines():
    if not raw.strip():
        continue
    digest, rel = raw.split("  ", 1)
    p = root / rel
    if not p.is_file():
        failed.append((rel, "MISSING")); continue
    h=hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""):
            h.update(chunk)
    actual=h.hexdigest(); count += 1
    if actual != digest:
        failed.append((rel, actual))
if failed:
    print(f"FAIL: {len(failed)} / {count+len([x for x in failed if x[1]=='MISSING'])} entries failed")
    for rel,actual in failed:
        print(rel, actual)
    sys.exit(1)
print(f"PASS: {count} SHA-256 entries verified")
