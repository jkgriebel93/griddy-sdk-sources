# AWS CodeArtifact Setup Guide

This guide covers publishing the generated SDKs to AWS CodeArtifact repositories instead of public registries.

## AWS CodeArtifact Setup

### 1. Create CodeArtifact Domain and Repository

```bash
# Set your AWS account ID and region
export AWS_ACCOUNT_ID="123456789012"
export AWS_REGION="us-east-1"
export DOMAIN_NAME="griddy"
export REPO_NAME="nfl-sdks"

# Create CodeArtifact domain
aws codeartifact create-domain \
  --domain $DOMAIN_NAME \
  --region $AWS_REGION

# Create repository
aws codeartifact create-repository \
  --domain $DOMAIN_NAME \
  --repository $REPO_NAME \
  --region $AWS_REGION
```

### 2. Configure Upstream Repositories (Optional)

Allow CodeArtifact to fetch dependencies from public registries:

```bash
# Create upstream repository for PyPI
aws codeartifact create-repository \
  --domain $DOMAIN_NAME \
  --repository pypi-store \
  --region $AWS_REGION

aws codeartifact associate-external-connection \
  --domain $DOMAIN_NAME \
  --repository pypi-store \
  --external-connection public:pypi \
  --region $AWS_REGION

# Create upstream repository for npm
aws codeartifact create-repository \
  --domain $DOMAIN_NAME \
  --repository npm-store \
  --region $AWS_REGION

aws codeartifact associate-external-connection \
  --domain $DOMAIN_NAME \
  --repository npm-store \
  --external-connection public:npmjs \
  --region $AWS_REGION

# Add upstream repositories to your main repository
aws codeartifact update-repository \
  --domain $DOMAIN_NAME \
  --repository $REPO_NAME \
  --upstreams repositoryName=pypi-store \
  --region $AWS_REGION

aws codeartifact update-repository \
  --domain $DOMAIN_NAME \
  --repository $REPO_NAME \
  --upstreams repositoryName=npm-store \
  --region $AWS_REGION
```

### 3. Create IAM User for GitHub Actions

Create an IAM user with permissions to publish to CodeArtifact:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "codeartifact:GetAuthorizationToken",
        "codeartifact:GetRepositoryEndpoint",
        "codeartifact:PublishPackageVersion",
        "codeartifact:PutPackageMetadata",
        "codeartifact:ReadFromRepository"
      ],
      "Resource": [
        "arn:aws:codeartifact:${AWS_REGION}:${AWS_ACCOUNT_ID}:domain/${DOMAIN_NAME}",
        "arn:aws:codeartifact:${AWS_REGION}:${AWS_ACCOUNT_ID}:repository/${DOMAIN_NAME}/${REPO_NAME}"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "sts:GetServiceBearerToken",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "sts:AWSServiceName": "codeartifact.amazonaws.com"
        }
      }
    }
  ]
}
```

## GitHub Secrets Configuration

Add the following secrets to your GitHub repository (`Settings` → `Secrets and variables` → `Actions`):

### Required Secrets

| Secret Name | Description | Example Value |
|-------------|-------------|---------------|
| `AWS_ACCESS_KEY_ID` | AWS IAM user access key | `AKIAIOSFODNN7EXAMPLE` |
| `AWS_SECRET_ACCESS_KEY` | AWS IAM user secret key | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| `AWS_REGION` | AWS region where CodeArtifact is hosted | `us-east-1` |
| `AWS_ACCOUNT_ID` | Your AWS account ID | `123456789012` |
| `CODEARTIFACT_DOMAIN` | CodeArtifact domain name | `griddy` |
| `CODEARTIFACT_REPO` | CodeArtifact repository name | `nfl-sdks` |
| `SPEAKEASY_API_KEY` | Speakeasy API key | Get from https://app.speakeasyapi.dev/ |
| `SDK_DEPLOY_TOKEN` | GitHub PAT with `repo` scope | `ghp_xxxxxxxxxxxx` |

## Installing Packages from CodeArtifact

### Python (with uv)

```bash
# Get CodeArtifact credentials
export CODEARTIFACT_TOKEN=$(aws codeartifact get-authorization-token \
  --domain griddy \
  --domain-owner $AWS_ACCOUNT_ID \
  --query authorizationToken \
  --output text)

export CODEARTIFACT_URL=$(aws codeartifact get-repository-endpoint \
  --domain griddy \
  --repository nfl-sdks \
  --format pypi \
  --query repositoryEndpoint \
  --output text)

# Install using uv
uv pip install \
  --index-url "https://aws:${CODEARTIFACT_TOKEN}@${CODEARTIFACT_URL#https://}simple/" \
  griddy-nfl
```

### Python (with pip)

```bash
# Configure pip
pip config set global.index-url "https://aws:${CODEARTIFACT_TOKEN}@${CODEARTIFACT_URL#https://}simple/"

# Or use environment variable
export PIP_INDEX_URL="https://aws:${CODEARTIFACT_TOKEN}@${CODEARTIFACT_URL#https://}simple/"

# Install package
pip install griddy-nfl
```

### TypeScript/Node.js

```bash
# Get CodeArtifact credentials
export CODEARTIFACT_TOKEN=$(aws codeartifact get-authorization-token \
  --domain griddy \
  --domain-owner $AWS_ACCOUNT_ID \
  --query authorizationToken \
  --output text)

export CODEARTIFACT_URL=$(aws codeartifact get-repository-endpoint \
  --domain griddy \
  --repository nfl-sdks \
  --format npm \
  --query repositoryEndpoint \
  --output text)

# Configure npm
npm config set registry "${CODEARTIFACT_URL}"
npm config set //${CODEARTIFACT_URL#https://}:_authToken="${CODEARTIFACT_TOKEN}"
npm config set //${CODEARTIFACT_URL#https://}:always-auth=true

# Install package
npm install griddy-nfl
```

### Using .npmrc file

Create a `.npmrc` file in your project:

```ini
registry=https://griddy-123456789012.d.codeartifact.us-east-1.amazonaws.com/npm/nfl-sdks/
//griddy-123456789012.d.codeartifact.us-east-1.amazonaws.com/npm/nfl-sdks/:_authToken=${CODEARTIFACT_AUTH_TOKEN}
//griddy-123456789012.d.codeartifact.us-east-1.amazonaws.com/npm/nfl-sdks/:always-auth=true
```

Then export the token:

```bash
export CODEARTIFACT_AUTH_TOKEN=$(aws codeartifact get-authorization-token \
  --domain griddy \
  --domain-owner $AWS_ACCOUNT_ID \
  --query authorizationToken \
  --output text)
```

## Automated Token Refresh

CodeArtifact tokens expire after 12 hours. For local development, create a helper script:

### Python Script (`ca-login.sh`)

```bash
#!/bin/bash
export AWS_ACCOUNT_ID="123456789012"
export CODEARTIFACT_DOMAIN="griddy"
export CODEARTIFACT_REPO="nfl-sdks"

export CODEARTIFACT_TOKEN=$(aws codeartifact get-authorization-token \
  --domain $CODEARTIFACT_DOMAIN \
  --domain-owner $AWS_ACCOUNT_ID \
  --query authorizationToken \
  --output text)

export CODEARTIFACT_URL=$(aws codeartifact get-repository-endpoint \
  --domain $CODEARTIFACT_DOMAIN \
  --repository $CODEARTIFACT_REPO \
  --format pypi \
  --query repositoryEndpoint \
  --output text)

export PIP_INDEX_URL="https://aws:${CODEARTIFACT_TOKEN}@${CODEARTIFACT_URL#https://}simple/"

echo "CodeArtifact credentials configured for pip/uv"
```

Usage: `source ca-login.sh`

## Workflow Details

The GitHub Actions workflow:

1. **Generates SDKs** using Speakeasy from the OpenAPI spec
2. **Commits and pushes** generated code to dedicated SDK repositories
3. **Authenticates with AWS** using IAM credentials
4. **Gets CodeArtifact token** valid for 12 hours
5. **Builds packages**:
   - Python: Uses `uv build` (hatchling backend)
   - TypeScript: Uses `npm run build`
6. **Publishes to CodeArtifact**:
   - Python: Uses `uv publish` with CodeArtifact endpoint
   - TypeScript: Uses `npm publish` with configured registry

## Package Versioning

To manage versions, update the version in:
- Python: `src/griddy_nfl/__init__.py` or `pyproject.toml`
- TypeScript: `package.json`

Consider using semantic versioning and automating version bumps based on commits.

## Troubleshooting

### Authentication Issues

```bash
# Test CodeArtifact access
aws codeartifact list-repositories --domain griddy

# Verify token generation
aws codeartifact get-authorization-token \
  --domain griddy \
  --domain-owner $AWS_ACCOUNT_ID
```

### Package Not Found

```bash
# List packages in repository
aws codeartifact list-packages \
  --domain griddy \
  --repository nfl-sdks

# Describe package
aws codeartifact describe-package \
  --domain griddy \
  --repository nfl-sdks \
  --format pypi \
  --package griddy-nfl
```

### Permission Errors

Ensure the IAM user has:
- `codeartifact:PublishPackageVersion`
- `codeartifact:PutPackageMetadata`
- `sts:GetServiceBearerToken`

## Cost Considerations

AWS CodeArtifact pricing (as of 2024):
- **Storage**: $0.05 per GB-month
- **Requests**: $0.05 per 10,000 requests
- **Data Transfer**: Standard AWS data transfer rates apply

Most small to medium SDK usage will cost less than $5/month.
