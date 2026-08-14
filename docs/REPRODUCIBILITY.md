# Reproducibility

## Integrity first

From the repository root run:

```bash
python code/verify_sha256.py
```

The script checks every entry in `SHA256SUMS.txt`. Then inspect `ARTIFACT_INVENTORY.csv`: the `Physical bytes in v2 archive` column distinguishes files physically included from historical records whose hashes are known only through recovered checkpoints.

## Evidence layers

1. **Regional informational layer (D1.5).** Scientific qualification and independent audit are recovered. The historical replay return is not recovered and no byte-identical replay claim is used for D1.5 in this archive.
2. **Conditional representation layer (D1.6A).** Final qualification and independent byte-identical replay audit are recovered. The collective temporal structure is supplied, not derived.
3. **Staged local-clock/calibration reconstruction (D1.6B).** B1 final qualification is recovered. B2A/B2B/B2C/B3 later final hashes, counts, and replay status are bound by recovered primary transition checkpoints; not all final ZIP bytes are physically present.
4. **Typed interface composition and collaborative reconstructibility.** TIME-RED-1 and TIME-COLLAB launch/transport handoffs are physically present; later qualification hashes and finite counts are retained in the registry.
5. **Lifecycle, atlas, finite-scale, typed-interaction, and gauge/Hodge/provenance layers.** Public claims are bounded by the claim matrix and registry. CERT-016 is physically recovered with verified sidecar; several other downstream packages remain hash-known but not mounted in this reconstructed continuity set.

## Exact algebra versus finite validation

Exact finite propositions, constructive finite campaigns, prospective synthetic holdouts, semantic audits, and reproducibility records are different evidence classes. They are not added together into a universal or experimental claim.

## Numerical reproducibility note for CERT-016

The cross-platform replay reproduces all structural fields, classifications, gates, and the verdict exactly. Four of 216 records differ only in last-bit floating-point values; the maximum relevant difference is `4.441e-16`. It must therefore be described as scientifically/structurally identical, not byte-identical.
