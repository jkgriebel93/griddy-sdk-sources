## Griddy SDK Sources

For now, the `README` in this repo is just my notebook. Currently, I'm imlementing the CI/CD. The pipeline should look something like:
1. When changes to `nfl-com-api.yaml` are pushed to any branch, run the `lint-api-spec.yml` workflow
    - This workflow/job should use [Spectral by Stoplight](https://docs.stoplight.io/docs/spectral/674b27b261c3c-overview)
1. Upon merging spec changes to `master`, the following jobs should be run:
   - Run linting again
   - Generate SDK code with [Speakeasy](https://www.speakeasy.com/docs/create-client-sdks)
     - From this repository's root: `speakeasy generate sdk --schema openapi/nfl-com-api.yaml --lang python --out griddy-sdk`
   - Push the generated SDK to the `griddy-sdk` repo as a pull request
     - Will have to modify `copy_and_commit_sdk.py` so that the `origin` remote is configured correctly
1. Once the pull request is created in the `griddy-sdk` repo, run quality checks
    - `black`, `pytest`, `mypy`, `isort`, `coverage`, etc.
    - Report results, make changes as necessary, and so on
    - **Note:** It is important to make sure the SDK version is bumped before merging
1. After the quality checks are all green, merge the pull request
1. On merge to `master`, use `uv` to build and then publish the SDK to AWS CodeArtifact


### Outstanding Questions and Considerations
- What do the Speakeasy generated tests actually look like?
- When/how are the tests generated?
- What about creating the docs and/or developer portal?
  - Depending on pricing we may not even be able to do this step
- Where/how should documentation be hosted?