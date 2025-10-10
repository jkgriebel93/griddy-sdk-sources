# SDK Generation Workflow Setup Guide

## Overview
This guide will help you set up automated SDK generation across your language-specific repositories.

## Prerequisites

1. **GitHub Personal Access Token (PAT)**
   - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Click "Generate new token (classic)"
   - Required scopes:
     - `repo` (Full control of private repositories)
     - `workflow` (Update GitHub Action workflows)
   - Save the token securely

2. **Repository Structure**
   ```
   griddy-sdk-sources/         # Source of truth
   ├── openapi/
   │   └── nfl-com-api.yaml
   └── .github/
       └── workflows/
           └── generate-sdks.yml
   
   griddy-sdk-python/          # Python SDK
   ├── .speakeasy-preserve
   └── ... (generated files)
   
   griddy-sdk-typescript/      # TypeScript SDK
   ├── .speakeasy-preserve
   └── ... (generated files)
   
   griddy-sdk-go/              # Go SDK
   ├── .speakeasy-preserve
   └── ... (generated files)
   ```

## Setup Steps

### 1. Add PAT to Source Repository

1. Go to `griddy-sdk-sources` repository
2. Navigate to Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `PAT_TOKEN`
5. Value: Your GitHub PAT from prerequisites
6. Click "Add secret"

### 2. Add Workflow to Source Repository

1. Create `.github/workflows/generate-sdks.yml` in `griddy-sdk-sources`
2. Copy the workflow content from the artifact above
3. Commit and push to master

### 3. Configure Each SDK Repository

For each SDK repository (`griddy-sdk-python`, `griddy-sdk-typescript`, etc.):

1. Create a `.speakeasy-preserve` file in the root:
   ```
   # Files to preserve during regeneration
   README.md
   CONTRIBUTING.md
   LICENSE
   examples/custom_*.py
   .github/workflows/custom-*.yml
   ```

2. Customize the list based on what files you want to keep

### 4. Test the Workflow

#### Option A: Make a change to the spec
1. Edit `openapi/nfl-com-api.yaml` in `griddy-sdk-sources`
2. Commit and push to master
3. Watch the Actions tab for the workflow run

#### Option B: Manual trigger
1. Go to Actions tab in `griddy-sdk-sources`
2. Select "Generate SDKs" workflow
3. Click "Run workflow"
4. Choose languages to generate (or leave default)
5. Click "Run workflow"

## Workflow Behavior

### When It Triggers
- Automatically when `openapi/nfl-com-api.yaml` is changed on master
- Manually via workflow dispatch

### What It Does
1. Generates SDKs for all configured languages in parallel
2. Checks out each SDK repository
3. Preserves files listed in `.speakeasy-preserve`
4. Copies generated SDK code
5. Creates a PR if changes are detected
6. Skips PR creation if no changes

### PR Details
- **Branch name**: `auto-update-sdk-<commit-sha>`
- **Title**: "🤖 Update {language} SDK from spec changes"
- **Labels**: `automated`, `sdk-update`, `{language}`
- **Body**: Contains source commit info and review checklist

## Customization Options

### Add More Languages

Edit the workflow matrix in `generate-sdks.yml`:
```yaml
strategy:
  matrix:
    language: [python, typescript, go, java, ruby]
```

### Preserve Additional Files

Add to `.speakeasy-preserve` in each SDK repo:
```
# Custom documentation
docs/custom-guide.md

# Modified configuration
.eslintrc.json
tsconfig.json

# Custom tests
tests/custom_test.py
```

### Change Branch Strategy

Modify the PR creation step:
```yaml
- name: Create Pull Request
  uses: peter-evans/create-pull-request@v5
  with:
    branch: sdk-updates  # Use fixed branch
    # or
    branch: auto-update-${{ github.run_id }}  # Use run ID
```

### Add Validation Steps

Add before PR creation:
```yaml
- name: Run tests
  run: |
    cd griddy-sdk-${{ matrix.language }}
    # Run language-specific tests
    npm test  # for TypeScript
    pytest    # for Python
    go test   # for Go
```

## Troubleshooting

### Issue: Workflow doesn't trigger
- **Check**: Path filter matches your spec location
- **Fix**: Update `paths:` in workflow to match your spec path

### Issue: Permission denied when creating PR
- **Check**: PAT has correct scopes
- **Fix**: Regenerate PAT with `repo` and `workflow` scopes

### Issue: Files not being preserved
- **Check**: File paths in `.speakeasy-preserve` are correct
- **Check**: Files exist in SDK repository
- **Fix**: Use paths relative to repository root

### Issue: Empty PRs being created
- **Check**: Change detection logic
- **Fix**: Review the `check_changes` step output

### Issue: SDK generation fails
- **Check**: Speakeasy CLI version
- **Check**: OpenAPI spec validity
- **Fix**: Run `speakeasy validate` locally first

## Best Practices

1. **Version Your SDKs**: Add versioning logic before creating PRs
2. **Validate Spec**: Add validation step before generation
3. **Test Generated Code**: Add automated tests to PR workflow
4. **Review PRs**: Don't auto-merge - review generated changes
5. **Document Changes**: Keep CHANGELOG.md updated
6. **Semantic Versioning**: Use SemVer for breaking changes

## Advanced Features

### Auto-merge for minor updates
```yaml
- name: Enable auto-merge
  if: steps.check_changes.outputs.has_changes == 'true'
  run: |
    gh pr merge --auto --squash
  env:
    GH_TOKEN: ${{ secrets.PAT_TOKEN }}
```

### Notify on Slack
```yaml
- name: Notify Slack
  uses: slackapi/slack-github-action@v1
  with:
    payload: |
      {
        "text": "SDK updated for ${{ matrix.language }}"
      }
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

### Version bumping
```yaml
- name: Bump version
  run: |
    cd sdk-repo
    # Logic to bump version based on changes
    npm version patch  # for TypeScript
```

## Maintenance

- **Monthly**: Review preserved files list
- **Quarterly**: Update Speakeasy CLI version
- **As needed**: Adjust matrix for new languages
- **Before major releases**: Test workflow manually

## Support

- Speakeasy docs: https://docs.speakeasy.com/
- GitHub Actions docs: https://docs.github.com/actions
- Create issue in source repo for workflow problems
