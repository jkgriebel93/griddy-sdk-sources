# Griddy NFL API SDK Sources

This repository contains the OpenAPI specification for the NFL API and automated tooling for generating SDKs in multiple languages.

## Repository Structure

- `openapi/nfl-com-api.yaml` - The source OpenAPI specification for the NFL API
- `.github/workflows/generate-sdks.yml` - GitHub Actions workflow that automatically generates and publishes SDKs

## How It Works

When changes are made to the OpenAPI specification, a GitHub Actions workflow automatically:

1. Generates Python and TypeScript-Axios SDKs using `openapi-generator-cli`
2. Commits and pushes the generated SDKs to their respective repositories

The workflow runs:
- Automatically when `openapi/nfl-com-api.yaml` is pushed to the `master` branch
- Manually via the Actions tab (workflow_dispatch)

## Setup

### 1. Create SDK Repositories

Create two separate repositories for your SDKs:
- Python SDK repository (e.g., `your-org/nfl-api-python`)
- TypeScript SDK repository (e.g., `your-org/nfl-api-typescript`)

### 2. Create GitHub Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with `repo` scope (full control of private repositories)
3. Save the token securely

### 3. Configure Repository Secrets

Add the following secrets to this repository (Settings → Secrets and variables → Actions):

- `SDK_DEPLOY_TOKEN` - Your personal access token from step 2
- `PYTHON_SDK_REPO` - Full repository name (e.g., `username/nfl-api-python`)
- `TYPESCRIPT_SDK_REPO` - Full repository name (e.g., `username/nfl-api-typescript`)

## Making Changes

### 1. Update the OpenAPI Specification

Edit `openapi/nfl-com-api.yaml` to add, modify, or remove API endpoints, schemas, or documentation.

### 2. Commit and Push

```bash
git add openapi/nfl-com-api.yaml
git commit -m "Update API specification: <describe changes>"
git push origin master
```

### 3. Workflow Runs Automatically

The GitHub Actions workflow will automatically:
- Generate fresh Python and TypeScript SDKs
- Push the generated code to their respective repositories

You can monitor the workflow progress in the Actions tab.

## Generated SDKs

### Python SDK
- Generated using `openapi-generator-cli` with the `python` generator
- Package name: `nfl_api`
- Project name: `nfl-api-python`

### TypeScript-Axios SDK
- Generated using `openapi-generator-cli` with the `typescript-axios` generator
- Package name: `@nfl/api-client`
- Supports ES6+

## Customizing SDK Generation

To modify SDK generation options, edit `.github/workflows/generate-sdks.yml` and adjust the `--additional-properties` flags in the respective generation steps.

Available options can be found in the [OpenAPI Generator documentation](https://openapi-generator.tech/docs/generators/).

## Manual Workflow Trigger

To manually regenerate SDKs without pushing changes:

1. Go to the Actions tab in this repository
2. Select "Generate and Publish SDKs" workflow
3. Click "Run workflow"
4. Select the branch and click "Run workflow"

## Generator Config

| Setting        | Value         |
| packageName    | griddy_nfl    |
| packageUrl     | <URL here>    |
| projectName    | Griddy NFL    |
