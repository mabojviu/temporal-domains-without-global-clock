# Publication workflow — step by step

This follows the same publication/reproducibility sequence used for the previous JMP article.

## Frozen sequence

1. **Clean public package**
   - remove private working files;
   - keep manuscript, figures, frozen evidence, public documentation, licences, and hashes.

2. **Public-package audit**
   - verify every SHA-256;
   - verify that manuscript claims do not exceed the archived evidence;
   - verify that no primitive spatial geometry is silently introduced;
   - verify the distinction between exact foundations and finite campaign evidence.

3. **Create the GitHub repository**
   - proposed repository: `mabojviu/temporal-domains-without-global-clock`;
   - initialize without auto-generated README/licence if uploading this package as-is.

4. **Upload the clean repository contents**
   - upload the contents of this package, not the outer ZIP itself as the repository tree;
   - verify the root contains `README.md`, `CITATION.cff`, `SHA256SUMS.txt`, `manuscript/`, `evidence/`, etc.

5. **Enable Zenodo–GitHub integration**
   - connect the GitHub account to Zenodo;
   - enable archiving for this repository **before** creating the archival release.

6. **Create GitHub release `v1.0.0`**
   - use the prepared release notes in `docs/RELEASE_DRAFT_NOTES.md`;
   - do not change scientific files after the release is cut.

7. **Archive the release on Zenodo**
   - confirm Zenodo has ingested GitHub release `v1.0.0`;
   - complete metadata using `docs/ZENODO_METADATA_DRAFT.txt`;
   - publish the Zenodo record and obtain the version DOI.

8. **Bind the DOI into the manuscript/repository**
   - add the final DOI to the Data Availability / reproducibility statement and repository metadata;
   - update `CITATION.cff`;
   - if the manuscript changes, create a new manuscript hash and, if needed, a new repository release.
   - never silently replace files under an existing frozen release.

9. **Recompile/finalize the manuscript**
   - produce the final submission PDF;
   - rerun page-by-page visual inspection;
   - recompute the manuscript SHA-256.

10. **Optional preprint**
    - prepare arXiv only after the archival DOI/repository state is stable, if desired.

11. **Submit to Journal of Mathematical Physics**
    - upload the compiled manuscript PDF;
    - use the prepared cover letter;
    - disclose the related manuscript `JMP26-AR-02157`;
    - preserve the exact claim boundary.

## Operating rule

Proceed one micro-step at a time. After each external action, record the actual state before moving on.
Do not infer that GitHub, Zenodo, arXiv, or the JMP portal completed an action until the UI confirms it.

## Current checkpoint — 2026-08-14

Completed before repository upload:
- author metadata bound;
- three manuscript figures revised and coherence-audited;
- DOCX/PDF preflight clean;
- internal author metadata corrected from a stale anonymized value;
- exact claim boundary retained;
- GitHub candidate rebuilt and SHA-audited in Step 4.

Next external action after this candidate is accepted: upload the repository tree to GitHub.
