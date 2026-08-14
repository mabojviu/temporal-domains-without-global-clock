# JMP hostile-referee audit — Temporal Domains Without a Global Clock

## Overall verdict

**Scientific/content preflight: PASS. Public-repository binding: pending GitHub/Zenodo publication.**

The manuscript has passed the author-metadata, figure/coherence, and PDF preflight stages. The
remaining work is administrative binding of the frozen public repository to GitHub/Zenodo and then
replacement of the provisional Data Availability statement by the resulting public record/DOI.

## 1. Novelty versus the related JMP submission

**Attack:** The editor could interpret the paper as a segmented continuation of the earlier serialization/hazard manuscript.

**Response:** The Introduction states the distinct scientific question: the earlier line asks whether event dynamics admits a scalar-time representation; this manuscript classifies the temporal structure that remains when no global scalar is assumed. The planned cover letter explicitly discloses `JMP26-AR-02157` and separates its objects/results from temporal domains, partial gluing, CAL Hodge sectors, and provenance-aware divergence.

**Status:** Addressed.

## 2. Hidden geometric prior

**Attack:** Graphs, registered 2-cells, Hodge decomposition, or a cochain inner product might secretly impose Euclidean or another preferred geometry.

**Response:** Vertices have no primitive coordinates, distances, angles, dimensions, embeddings, or physical metric. Registered 2-cells are compositional CAL certificates, not spatial faces. The unit-weight cochain inner product is an auxiliary permutation-invariant combinatorial choice, not a spacetime metric.

**Status:** Addressed. No Euclidean, spherical, hyperbolic, Lorentzian, or other geometric class is favored a priori.

## 3. Divergence/source overclaim

**Attack:** The provenance current might look engineered to force the continuity equation, or the source residual might be read as creation/destruction of physical time.

**Response:** The provenance-tree result is explicitly conditional on routing/provenance supplied by the micro-event law. The admissible divergence acts on a gauge-invariant provenance current `J`, not on the gauge-dependent connection `gamma`. The manuscript prohibits interpreting `S` as creation/destruction of physical time.

**Status:** Addressed.

## 4. Conservation / Noether overclaim

**Attack:** Conditional conservation of `Q_T` might be presented as a Noether charge without an action principle.

**Response:** The manuscript derives `Delta Q_T = sum_i S_i` algebraically from the continuity equation and states that `Q_T` is conserved for pure redistribution/zero net source. It explicitly does **not** claim a Noether derivation; an action/Noether program is reserved for future work.

**Status:** Addressed.

## 5. Reproducibility and holdout governance

**Attack:** Internal PASS/CERT labels or hashes could be mistaken for substitutes for proof or external replication.

**Response:** Exact algebraic foundations and finite holdout/campaign evidence are archived as distinct evidence layers. The manuscript treats computational checks as reproducibility/regression evidence and not as replacements for algebraic proof.

**Status:** Addressed.

## 6. Figure/coherence audit

- Figure 1 now states **identical connectivity**, not topology, and distinguishes ORD/CAL/CORR without relying on color.
- Figure 2 uses the formal labels exact/gradient, coexact/circulation, and harmonic.
- Figure 3 makes the reference orientation explicit, states the sign convention for `J`, and displays the pure-redistribution conservation consequence.

**Status:** Addressed.

## Remaining actions before final JMP upload

1. Publish this audited tree to the public GitHub repository.
2. Create GitHub release `v1.0.0` only after Zenodo integration is enabled.
3. Archive/publish the release in Zenodo and obtain the public DOI.
4. Replace the provisional Data Availability statement with the DOI-backed public record.
5. Recompile and re-hash the final journal-submission manuscript if that statement changes the file.
6. Keep the related-manuscript disclosure in the cover letter explicit.
