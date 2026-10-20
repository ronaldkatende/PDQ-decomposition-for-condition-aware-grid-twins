# Preparing a public, citable software release

## Before uploading

1. Confirm you have the rights to release the original software under `LICENSE` and that it contains no private material.
2. Preserve the frozen JSON and publication evidence as supplied: do not silently regenerate or overwrite the originals.
3. Run `python -m pip install -e . pytest`, then `python -m pytest -q` and `python examples/synthetic_sparse_recovery_demo.py`.
4. Run `python scripts/build_publication_evidence.py --results-root results --out evidence_rebuilt`, then `python scripts/verify_archived_evidence.py --rebuilt evidence_rebuilt`.
5. Review `git diff`, including hidden files, and confirm no downloaded third-party raw datasets, tokens, or local paths were added.
6. Provide accurate author and citation metadata **at the release/Zenodo record level**. This distributable package does not fabricate or embed a person's identity. If desired, add a correctly attributed `CITATION.cff` before publication.

## Upload to your existing GitHub repository

Do **not** upload the ZIP as a single file to the repository: extract it and copy the contents to the repository root. Preserve `.git/` in the clone. Back up any previous code first. For example:

```bash
git clone <YOUR_REPOSITORY_URL>
cd <REPOSITORY_DIRECTORY>
# Copy all extracted release files here, including .github/ and .gitignore
git status
git add -A
git commit -m "Prepare public DCE reproducibility release"
git push
```

## Create the DOI

On Zenodo, ensure GitHub is linked and this repository is ON. Then on GitHub select **Releases** > **Draft a new release**, add a version tag such as `v1.0.0`, describe it, and publish. Zenodo ingests new GitHub releases and issues a version-specific DOI. Check the Zenodo record's creator and licence metadata. Use the **version-specific DOI** in the article's Data Availability Statement, not a placeholder.

Never claim the Open Data/Open Materials badges merely because a DOI exists. Verify independent access to the datasets and the reproducibility of procedures first.
