# SDK Publishing Setup Guide

This guide explains how to configure package publishing for each SDK language.

## 📦 TypeScript/JavaScript (npm)

### Setup Steps:
1. Create an npm account at https://www.npmjs.com
2. Generate an access token in your npm account settings
3. Add the token as `NPM_TOKEN` secret in your GitHub repository

### Package Configuration:
```json
{
  "name": "@griddy/nfl-sdk",
  "version": "1.0.0",
  "description": "Official NFL SDK for TypeScript/JavaScript",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "repository": {
    "type": "git",
    "url": "https://github.com/griddy/nfl-sdk-typescript.git"
  },
  "publishConfig": {
    "access": "public"
  }
}
```

### Installation:
```bash
npm install @griddy/nfl-sdk
```

---

## 🐍 Python (PyPI)

### Setup Steps:
1. Create a PyPI account at https://pypi.org
2. Generate an API token in your account settings
3. Add the token as `PYPI_API_TOKEN` secret in your GitHub repository

### Package Configuration:
Create `pyproject.toml`:
```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "griddy-nfl-sdk"
version = "1.0.0"
description = "Official NFL SDK for Python"
authors = [{name = "Griddy Team", email = "support@griddy.com"}]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.10"
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
]

[project.urls]
Homepage = "https://github.com/griddy/nfl-sdk-python"
Repository = "https://github.com/griddy/nfl-sdk-python.git"
Issues = "https://github.com/griddy/nfl-sdk-python/issues"
```

### Installation:
```bash
pip install griddy-nfl-sdk
```

---

## ☕ Java (Maven Central)

### Setup Steps:
1. Create a Sonatype JIRA account
2. Request a new project namespace (com.griddy)
3. Set up GPG signing keys
4. Add secrets to GitHub repository:
   - `MAVEN_USERNAME`
   - `MAVEN_PASSWORD`
   - `GPG_PRIVATE_KEY`
   - `GPG_PASSPHRASE`

### Package Configuration:
Update `pom.xml`:
```xml
<groupId>com.griddy</groupId>
<artifactId>nfl-sdk</artifactId>
<version>1.0.0</version>
<name>NFL SDK for Java</name>
<description>Official NFL SDK for Java applications</description>
<url>https://github.com/griddy/nfl-sdk-java</url>

<licenses>
  <license>
    <name>MIT License</name>
    <url>https://opensource.org/licenses/MIT</url>
  </license>
</licenses>

<developers>
  <developer>
    <name>Griddy Team</name>
    <email>support@griddy.com</email>
    <organization>Griddy</organization>
  </developer>
</developers>

<scm>
  <connection>scm:git:git://github.com/griddy/nfl-sdk-java.git</connection>
  <developerConnection>scm:git:ssh://github.com:griddy/nfl-sdk-java.git</developerConnection>
  <url>https://github.com/griddy/nfl-sdk-java/tree/main</url>
</scm>
```

### Installation:
```xml
<dependency>
    <groupId>com.griddy</groupId>
    <artifactId>nfl-sdk</artifactId>
    <version>1.0.0</version>
</dependency>
```

---

## 🔷 Go (Go Modules)

### Setup Steps:
1. Create the GitHub repository
2. Tag releases with semantic versioning (v1.0.0)
3. Go modules are automatically available via GitHub

### Module Configuration:
```go
module github.com/griddy/nfl-sdk-go

go 1.22

require (
    // dependencies will be listed here
)
```

### Installation:
```bash
go get github.com/griddy/nfl-sdk-go
```

---

## 🔷 C#/.NET (NuGet)

### Setup Steps:
1. Create a Microsoft account
2. Get a NuGet API key from https://www.nuget.org/account/apikeys
3. Add the key as `NUGET_API_KEY` secret in your GitHub repository

### Package Configuration:
Update `.csproj`:
```xml
<PropertyGroup>
  <TargetFramework>net6.0</TargetFramework>
  <PackageId>Griddy.NFL.SDK</PackageId>
  <PackageVersion>1.0.0</PackageVersion>
  <Title>NFL SDK for .NET</Title>
  <Description>Official NFL SDK for .NET applications</Description>
  <Authors>Griddy Team</Authors>
  <Company>Griddy</Company>
  <PackageProjectUrl>https://github.com/griddy/nfl-sdk-csharp</PackageProjectUrl>
  <RepositoryUrl>https://github.com/griddy/nfl-sdk-csharp.git</RepositoryUrl>
  <RepositoryType>git</RepositoryType>
  <PackageLicenseExpression>MIT</PackageLicenseExpression>
  <PackageReadmeFile>README.md</PackageReadmeFile>
  <GeneratePackageOnBuild>true</GeneratePackageOnBuild>
</PropertyGroup>
```

### Installation:
```bash
dotnet add package Griddy.NFL.SDK
```

---

## 🔐 Required Secrets for GitHub Actions

Each repository needs these secrets configured in GitHub Settings > Secrets and variables > Actions:

### TypeScript:
- `NPM_TOKEN`: npm access token

### Python:
- `PYPI_API_TOKEN`: PyPI API token

### Java:
- `MAVEN_USERNAME`: Sonatype username
- `MAVEN_PASSWORD`: Sonatype password
- `GPG_PRIVATE_KEY`: GPG private key for signing
- `GPG_PASSPHRASE`: GPG key passphrase

### Go:
- No secrets required (uses GitHub releases)

### C#:
- `NUGET_API_KEY`: NuGet API key

---

## 🚀 Publishing Process

1. **Development**: Push changes to `main` or `develop` branch
2. **Testing**: CI/CD runs tests automatically
3. **Release**: Create a GitHub release with semantic version (v1.0.0)
4. **Publishing**: CI/CD automatically publishes to package registry
5. **Availability**: Package becomes available for installation

Each SDK will be independently versioned and can be released at different cadences based on updates and stability.