# Publication sequence for v2.0.0 after DOI reservation

The version DOI is already reserved: `10.5281/zenodo.21938420`. The final tree is therefore DOI-bound.

1. From the extracted repository root, run `python code/verify_sha256.py`; it must pass every manifest entry.
2. Review `ARTIFACT_INVENTORY.csv`, especially rows with `Physical bytes in v2 archive = NO`; those are explicit historical references, not missing files silently represented as present.
3. Commit the exact final tree to the existing GitHub repository without rewriting historical tags `v1.0.0` or `v1.0.1`.
4. **Confirm that the Zenodo GitHub auto-archiving toggle remains OFF before creating GitHub release `v2.0.0`.** It was switched OFF after saving the manual Zenodo new-version draft with reserved DOI `10.5281/zenodo.21938420`; leaving automatic ingestion enabled would risk creating a competing deposition/version.
5. Create/tag GitHub release `v2.0.0` from the exact frozen tree, using `docs/RELEASE_NOTES_v2.0.0.md`.
6. Return to the existing Zenodo new-version draft (do not create another record). Do not use **Import files** from v1.x. Upload the single exact frozen ZIP `LQTA_D_GITHUB_ZENODO_v2_0_0_FINAL_DOI_BOUND_TARGET_RELATION_EXPLICIT.zip` and fill/confirm metadata using `docs/ZENODO_METADATA_v2.0.0.md`.
7. Preview the Zenodo record, verify DOI `10.5281/zenodo.21938420`, version `2.0.0`, title/creator, public visibility, and chosen record-level license. Then publish the draft. Publishing registers the reserved DOI.
8. Confirm the DOI resolves, the version is linked under concept DOI `10.5281/zenodo.21931499`, and the GitHub `v2.0.0` tag/release points to the frozen tree. Optionally re-enable GitHub auto-archiving for future releases only after confirming there is no duplicate v2 ingestion pending.
9. Run the final JMP submission audit using manuscript v15.3 / its journal-formatted derivative and the now-public DOI.

No post-publication modification of historical v1.x records is required.
