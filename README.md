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


## Release status

This tree is the **pre-Zenodo public release candidate** for GitHub release `v1.0.0`.
The manuscript and evidence are frozen for repository upload, but the Data Availability statement
will be rebound to the public GitHub/Zenodo record and DOI before the final JMP submission.

The manuscript figures in this candidate are the final audited versions: identical-connectivity
typed relations, discrete temporal Hodge sectors, and provenance-aware transport/conditional conservation.


## Historical certification lineage

This is a successor repository, not an isolated snapshot. The public archive includes CERT-010 through CERT-017 plus the exact TC8A/TC9A-C foundations, and it preserves selected failed/abandoned precursor records that materially shaped later frozen campaigns. CERT-001 through CERT-008 remain part of the predecessor article line; CERT-009 records the nonretroactive governance boundary.

See `docs/CERTIFICATION_LINEAGE.md` for the dependency map and the distinction between historical governance, prerequisites, direct manuscript evidence, exact foundations, and preserved negative-path history.

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
