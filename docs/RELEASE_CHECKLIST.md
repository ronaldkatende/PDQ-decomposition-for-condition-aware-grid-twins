# Publish this repository and archive it on Zenodo

1. Extract the release ZIP. Upload **its contents**, including `.github/`, `.gitignore`, and `CITATION.cff`, to the root of the existing GitHub repository. Do not upload the ZIP itself or a nested release folder.
2. In GitHub's online editor, open **Source Control**, enter `Prepare DCE reproducibility release`, and choose **Commit & Push**. Confirm the files appear on the `main` branch.
3. In GitHub, check **Actions**. The `tests` workflow should finish successfully. It checks Python tests, the synthetic demonstration, frozen-file hashes, and archived numerical evidence.
4. Review the `LICENSE` and `CITATION.cff`. They identify the software creator and licence. Confirm you have rights to release all original code under MIT; third-party raw data are not included.
5. Open **Releases > Draft a new release** on GitHub. Create tag `v1.0.0` targeting `main`, then publish the release.
6. Zenodo is already linked to GitHub and the repository is enabled. Refresh Zenodo's GitHub integration. Open the archived release and check its title, creators, licence, files, and **version DOI**.
7. Add that **real DOI** to the article's Data Availability Statement as a written-out `https://doi.org/...` URL. Do not insert an unissued DOI in this repository.

**Limits:** A DOI establishes a preserved software version; it does not establish that an independent researcher can reproduce the complete experiments. Confirm the Open Data and Open Materials badge criteria separately.
