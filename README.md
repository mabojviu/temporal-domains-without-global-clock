# Temporal Domains Without a Global Clock

Public reproducibility and archival package for the manuscript:

**Temporal Domains Without a Global Clock: Partial Gluing, Holonomy, and Gauge-Invariant Field Structure in Finite Relational Event Networks**

## Scope

This repository supports a finite relational framework in which temporal coordination is built from typed local relations without assuming a primitive globally scalar clock.

The public claims are deliberately limited. The package does **not** claim:
- a continuum spacetime theorem;
- Lorentz symmetry or a spacetime metric;
- gravity or Einstein dynamics;
- that the relational complex is a spatial geometry;
- literal creation or destruction of physical time.

## Main mathematical objects

- ORD: local/collective precedence relations.
- CAL: affine temporal calibration relations.
- CORR: correlation witnesses that do not, by themselves, imply precedence or calibration.
- `gamma`: log-scale CAL 1-cochain.
- `D0 s`: exact/gradient sector.
- `D1 gamma`: registered-cell temporal circulation/curl.
- `eta = P_perp gamma`: gauge-invariant nonintegrable CAL content.
- `rho_i`: local gauge-invariant density of that content.
- `J`: provenance-selected gauge-invariant transport current.
- `Delta rho + div_T J = S`: continuity/balance equation.

## Conditional conservation law

For a closed provenance patch,

`Delta Q_T = sum_i S_i`, with `Q_T = sum_i rho_i = ||eta||^2`.

Hence pure redistribution (`sum_i S_i = 0`) conserves `Q_T` exactly.

This is a balance-law consequence of the discrete continuity equation; it is **not** presented as a Noether charge.

## Repository map

- `manuscript/` — public manuscript PDF and editable DOCX.
- `figures/` — manuscript figures.
- `evidence/certifications/` — frozen finite campaign certification packages.
- `evidence/foundations/` — exact structural/foundational packages.
- `docs/` — scope, reproducibility, release, and publication guidance.
- `code/` — integrity/reproduction helpers.
- `licenses/` — code and documentation/data licences.
- `SHA256SUMS.txt` — cryptographic inventory for the public release.

## Reproducibility layers

1. **Finite holdout/campaign evidence** — CERT-015/016/017.
2. **Exact algebraic foundations** — TC8A and TC9A/B/C.
3. **Manuscript-level claims** — restricted to what the archived evidence supports.

See `docs/REPRODUCIBILITY.md` and `docs/CLAIM_BOUNDARY.md`.
