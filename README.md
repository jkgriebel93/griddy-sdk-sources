# Griddy SDK Sources

This repository contains the source OpenAPI specification and tooling for generating Griddy SDKs across multiple languages.

## Repository Structure

- `openapi.yaml` - The source OpenAPI specification for the Griddy API
- `sdk-configs/` - Configuration files for each SDK language
- Generated SDKs are pushed to separate language-specific repositories

## Development Workflow

### 1. Making Changes to the API Specification

Edit the `openapi/nfl-com-api.yaml` file to add, modify, or remove API endpoints, schemas, or documentation.

### 2. Generating SDKs

Run the provided script to generate all SDKs:

```bash
./generate-sdks.sh
```

This will generate SDKs for:
- TypeScript (Axios)
- Python
- Java
- Go
- C#

All generated SDKs will be placed in the `sdks/` directory.

### 3. Testing Generated SDKs

After generation, test each SDK in its respective directory:

```bash
# TypeScript
cd sdks/typescript
npm install
npm test
npm run build

# Python
cd sdks/python
pip install -e .
pytest

# Go
cd sdks/go
go mod tidy
go test ./...
go build

# Java
cd sdks/java
mvn clean install
mvn test

# C#
cd sdks/csharp
dotnet build
dotnet test
```

### 4. Committing and Pushing Changes

#### In this repository (griddy-sdk-sources):

```bash
git add openapi/nfl-com-api.yaml
git commit -m "Update API specification: <describe changes>"
git push origin master
```

#### In each SDK repository:

Copy the generated SDK to its repository and commit:

```bash
# Example for TypeScript
cp -r sdks/typescript/* ../griddy-sdk-typescript/
cd ../griddy-sdk-typescript
git add .
git commit -m "Regenerate SDK from updated OpenAPI spec"
git push origin main
```

Repeat for each SDK language.

### 5. Publishing SDKs (when ready)

Each SDK repository contains its own publishing workflow:

- **TypeScript**: `npm publish`
- **Python**: `python -m build && twine upload dist/*`
- **Go**: Tag releases with `git tag v<version>` and push tags
- **Java**: `mvn deploy`

## Prerequisites

- [OpenAPI Generator CLI](https://openapi-generator.tech/docs/installation) installed
- Git configured with appropriate access to all SDK repositories
- Language-specific toolchains installed (Node.js, Python, Go, Java/Maven, .NET)

## SDK Repositories

After generation, SDKs should be copied to their respective repositories:
- TypeScript: `../griddy-sdk-typescript`
- Python: `../griddy-sdk-python`
- Go: `../griddy-sdk-go`
- Java: `../griddy-sdk-java`
- C#: `../griddy-sdk-csharp`

## Notes

- Always regenerate and test all SDKs after making changes to `openapi/nfl-com-api.yaml`
- Keep SDK versions synchronized across all languages
- Document breaking changes in each SDK's CHANGELOG
- Use semantic versioning for SDK releases