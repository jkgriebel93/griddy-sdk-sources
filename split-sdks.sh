#!/bin/bash

# Script to split generated SDKs into separate git repositories
# This script creates individual repositories for each SDK language

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
BASE_DIR="$(pwd)"
SDKS_DIR="sdks"
PARENT_DIR="../"
SPEC_FILE="openapi/nfl-com-api.yaml"
CI_TEMPLATES_DIR="ci-templates"

# SDK configurations
declare -A SDK_CONFIGS=(
    ["typescript"]="griddy-nfl-sdk-typescript"
    ["python"]="griddy-nfl-sdk-python"
    ["java"]="griddy-nfl-sdk-java"
    ["go"]="griddy-nfl-sdk-go"
    ["csharp"]="griddy-nfl-sdk-csharp"
)

echo -e "${YELLOW}🚀 Starting SDK repository split process...${NC}"

# Function to create a new repository for an SDK
create_sdk_repository() {
    local sdk_type=$1
    local repo_name=$2
    local sdk_path="$SDKS_DIR/$sdk_type"
    local repo_path="$PARENT_DIR$repo_name"

    if [ ! -d "$sdk_path" ]; then
        echo -e "${YELLOW}⚠️  SDK not found: $sdk_path - skipping${NC}"
        return 0
    fi

    echo -e "${BLUE}📁 Creating repository: $repo_name${NC}"

    # Create new directory for the repository
    mkdir -p "$repo_path"

    # Copy SDK files
    cp -r "$sdk_path/"* "$repo_path/"

    # Copy the OpenAPI spec file
    mkdir -p "$repo_path/openapi"
    cp "$SPEC_FILE" "$repo_path/openapi/"

    # Copy CI/CD workflows
    if [ -d "$CI_TEMPLATES_DIR/$sdk_type/.github" ]; then
        echo -e "${BLUE}📋 Adding CI/CD workflows for $sdk_type${NC}"
        cp -r "$CI_TEMPLATES_DIR/$sdk_type/.github" "$repo_path/"
    fi

    # Initialize git repository
    cd "$repo_path"

    if [ ! -d ".git" ]; then
        git init
        echo -e "${GREEN}✅ Initialized git repository${NC}"
    fi

    # Create/update .gitignore based on language
    create_gitignore "$sdk_type"

    # Create README.md
    create_readme "$sdk_type" "$repo_name"

    # Create generation script
    create_generation_script "$sdk_type"

    # Copy publishing setup documentation
    cp "$BASE_DIR/PUBLISHING_SETUP.md" . 2>/dev/null || echo "Publishing setup guide not found"

    # Stage and commit files
    git add .
    git commit -m "Initial SDK setup with CI/CD

Generated from NFL API OpenAPI specification
- SDK type: $sdk_type
- Generated files and documentation
- CI/CD workflows included
- Publishing configuration ready

🤖 Generated with Claude Code" || echo "No changes to commit"

    cd "$BASE_DIR"
    echo -e "${GREEN}✅ Repository created: $repo_name${NC}"
}

# Function to create language-specific .gitignore
create_gitignore() {
    local sdk_type=$1

    case $sdk_type in
        "typescript")
            cat > .gitignore << 'EOF'
# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
package-lock.json
yarn.lock

# Build outputs
dist/
build/
*.tsbuildinfo

# Environment files
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Coverage
coverage/
*.lcov
EOF
            ;;
        "python")
            cat > .gitignore << 'EOF'
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec

# Virtual environments
venv/
ENV/
env/
.venv/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Testing
.pytest_cache/
.coverage
htmlcov/

# Environment files
.env
.env.local
EOF
            ;;
        "java")
            cat > .gitignore << 'EOF'
# Compiled class file
*.class

# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# Maven
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
pom.xml.next
release.properties
dependency-reduced-pom.xml
buildNumber.properties
.mvn/timing.properties
.mvn/wrapper/maven-wrapper.jar

# Gradle
.gradle
build/
!gradle/wrapper/gradle-wrapper.jar
!**/src/main/**/build/
!**/src/test/**/build/

# IDEs
.idea/
.vscode/
*.swp
*.swo
*.iml

# OS
.DS_Store
Thumbs.db
EOF
            ;;
        "go")
            cat > .gitignore << 'EOF'
# Binaries for programs and plugins
*.exe
*.exe~
*.dll
*.so
*.dylib

# Test binary, built with `go test -c`
*.test

# Output of the go coverage tool
*.out

# Dependency directories
vendor/

# Go workspace file
go.work

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment files
.env
.env.local
EOF
            ;;
        "csharp")
            cat > .gitignore << 'EOF'
# Build results
[Dd]ebug/
[Dd]ebugPublic/
[Rr]elease/
[Rr]eleases/
x64/
x86/
build/
bld/
[Bb]in/
[Oo]bj/

# Visual Studio
.vs/
*.rsuser
*.suo
*.user
*.userosscache
*.sln.docstates

# .NET Core
project.lock.json
project.fragment.lock.json
artifacts/

# NuGet
*.nupkg
*.snupkg
.nuget/

# IDEs
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment files
.env
.env.local
EOF
            ;;
    esac
}

# Function to create README.md
create_readme() {
    local sdk_type=$1
    local repo_name=$2

    cat > README.md << EOF
# NFL SDK for ${sdk_type^}

Official ${sdk_type^} SDK for the NFL API, providing comprehensive access to NFL data including games, teams, players, statistics, and more.

## Features

- **Complete API Coverage**: Access to all NFL API endpoints
- **Type Safety**: Full type definitions and interfaces
- **Modern Architecture**: Built using OpenAPI Generator
- **Well Documented**: Comprehensive documentation and examples
- **CI/CD Ready**: Automated testing and publishing workflows
- **Multi-Platform**: Supports multiple ${sdk_type} versions

## Installation

EOF

    case $sdk_type in
        "typescript")
            cat >> README.md << 'EOF'
```bash
npm install @griddy/nfl-sdk
# or
yarn add @griddy/nfl-sdk
```

## Quick Start

```typescript
import { Configuration, DefaultApi } from '@griddy/nfl-sdk';

const config = new Configuration({
    basePath: 'https://api.nfl.com',
    accessToken: 'your-access-token'
});

const api = new DefaultApi(config);

// Get current season games
const games = await api.getGames();
console.log(games.data);
```

## Development

```bash
# Install dependencies
npm install

# Build the SDK
npm run build

# Run tests
npm test

# Regenerate from OpenAPI spec
./generate.sh
```
EOF
            ;;
        "python")
            cat >> README.md << 'EOF'
```bash
pip install griddy-nfl-sdk
```

## Quick Start

```python
import griddy_nfl_sdk
from griddy_nfl_sdk.rest import ApiException

# Configure API client
configuration = griddy_nfl_sdk.Configuration(
    host = "https://api.nfl.com",
    access_token = 'your-access-token'
)

# Create API instance
with griddy_nfl_sdk.ApiClient(configuration) as api_client:
    api_instance = griddy_nfl_sdk.DefaultApi(api_client)

    try:
        # Get current season games
        api_response = api_instance.get_games()
        print(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_games: %s\n" % e)
```

## Development

```bash
# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Format code
black .
isort .

# Regenerate from OpenAPI spec
./generate.sh
```
EOF
            ;;
        "java")
            cat >> README.md << 'EOF'
```xml
<dependency>
    <groupId>com.griddy</groupId>
    <artifactId>nfl-sdk</artifactId>
    <version>1.0.0</version>
</dependency>
```

## Quick Start

```java
import com.griddy.nfl.client.*;
import com.griddy.nfl.client.auth.*;
import com.griddy.nfl.model.*;
import com.griddy.nfl.api.DefaultApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://api.nfl.com");

        // Configure HTTP bearer authorization
        HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        Bearer.setBearerToken("your-access-token");

        DefaultApi apiInstance = new DefaultApi(defaultClient);

        try {
            // Get current season games
            Object result = apiInstance.getGames();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DefaultApi#getGames");
            e.printStackTrace();
        }
    }
}
```

## Development

```bash
# Build with Maven
mvn clean compile

# Run tests
mvn test

# Package
mvn package

# Regenerate from OpenAPI spec
./generate.sh
```
EOF
            ;;
        "go")
            cat >> README.md << 'EOF'
```bash
go get github.com/griddy/nfl-sdk-go
```

## Quick Start

```go
package main

import (
    "context"
    "fmt"
    "log"

    nflsdk "github.com/griddy/nfl-sdk-go"
)

func main() {
    configuration := nflsdk.NewConfiguration()
    apiClient := nflsdk.NewAPIClient(configuration)

    // Configure authentication
    auth := context.WithValue(context.Background(), nflsdk.ContextAccessToken, "your-access-token")

    // Get current season games
    resp, r, err := apiClient.DefaultApi.GetGames(auth).Execute()
    if err != nil {
        log.Fatalf("Error when calling DefaultApi.GetGames: %v\n", err)
    }

    fmt.Printf("Response: %v\n", resp)
}
```

## Development

```bash
# Download dependencies
go mod download

# Build
go build

# Run tests
go test ./...

# Format code
go fmt ./...

# Regenerate from OpenAPI spec
./generate.sh
```
EOF
            ;;
        "csharp")
            cat >> README.md << 'EOF'
```bash
dotnet add package Griddy.NFL.SDK
```

## Quick Start

```csharp
using System;
using Griddy.NFL.SDK.Client;
using Griddy.NFL.SDK.Api;
using Griddy.NFL.SDK.Model;

namespace Example
{
    public class Program
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.nfl.com";
            config.AccessToken = "your-access-token";

            var apiInstance = new DefaultApi(config);

            try
            {
                // Get current season games
                var result = apiInstance.GetGames();
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling DefaultApi.GetGames: " + e.Message);
            }
        }
    }
}
```

## Development

```bash
# Restore packages
dotnet restore

# Build
dotnet build

# Run tests
dotnet test

# Format code
dotnet format

# Regenerate from OpenAPI spec
./generate.sh
```
EOF
            ;;
    esac

    cat >> README.md << EOF

## API Documentation

Full API documentation is available in the \`docs/\` directory.

## Publishing

This SDK is automatically published to package registries when releases are created:

EOF

    case $sdk_type in
        "typescript")
            echo "- 📦 **npm**: \`@griddy/nfl-sdk\`" >> README.md
            ;;
        "python")
            echo "- 🐍 **PyPI**: \`griddy-nfl-sdk\`" >> README.md
            ;;
        "java")
            echo "- ☕ **Maven Central**: \`com.griddy:nfl-sdk\`" >> README.md
            ;;
        "go")
            echo "- 🔷 **Go Modules**: \`github.com/griddy/nfl-sdk-go\`" >> README.md
            ;;
        "csharp")
            echo "- 🔷 **NuGet**: \`Griddy.NFL.SDK\`" >> README.md
            ;;
    esac

    cat >> README.md << EOF

## Contributing

1. Fork the repository
2. Create your feature branch (\`git checkout -b feature/amazing-feature\`)
3. Commit your changes (\`git commit -m 'Add some amazing feature'\`)
4. Push to the branch (\`git push origin feature/amazing-feature\`)
5. Open a Pull Request

## Regeneration

To regenerate the SDK from the latest OpenAPI specification:

\`\`\`bash
./generate.sh
\`\`\`

This will update all generated files while preserving your custom configurations.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

- 📧 Email: support@griddy.com
- 🐛 Issues: [GitHub Issues](https://github.com/griddy/$repo_name/issues)
- 📖 Documentation: [API Docs](https://docs.griddy.com/nfl-sdk)

---

Generated using OpenAPI Generator from the official NFL API specification.
EOF
}

# Function to create generation script
create_generation_script() {
    local sdk_type=$1

    cat > generate.sh << EOF
#!/bin/bash

# SDK Generation Script
# Regenerates the SDK from the OpenAPI specification

set -e

echo "🚀 Regenerating $sdk_type SDK..."

# Check if openapi-generator-cli is available
if ! command -v openapi-generator-cli &> /dev/null; then
    echo "❌ openapi-generator-cli not found. Please install it first:"
    echo "npm install -g @openapitools/openapi-generator-cli"
    exit 1
fi

# Check if Java is available
if ! command -v java &> /dev/null; then
    echo "❌ Java not found. Please install Java first."
    exit 1
fi

SPEC_FILE="openapi/nfl-com-api.yaml"

if [ ! -f "\$SPEC_FILE" ]; then
    echo "❌ OpenAPI spec file not found: \$SPEC_FILE"
    exit 1
fi

# Backup existing files
if [ -d "backup" ]; then
    rm -rf backup
fi
mkdir -p backup

EOF

    case $sdk_type in
        "typescript")
            cat >> generate.sh << 'EOF'
# Backup important files
cp package.json backup/ 2>/dev/null || true
cp README.md backup/ 2>/dev/null || true
cp .gitignore backup/ 2>/dev/null || true
cp -r .github backup/ 2>/dev/null || true

# Generate SDK
openapi-generator-cli generate \
    -i "$SPEC_FILE" \
    -g typescript-axios \
    -o . \
    --additional-properties="npmName=@griddy/nfl-sdk,npmVersion=1.0.0,withInterfaces=true,withoutRuntimeChecks=false" \
    --skip-validate-spec \
    --global-property models,apis,supportingFiles

# Restore backed up files
cp backup/README.md . 2>/dev/null || true
cp backup/.gitignore . 2>/dev/null || true
cp -r backup/.github . 2>/dev/null || true

echo "✅ TypeScript SDK regenerated successfully!"
EOF
            ;;
        "python")
            cat >> generate.sh << 'EOF'
# Backup important files
cp setup.py backup/ 2>/dev/null || true
cp pyproject.toml backup/ 2>/dev/null || true
cp README.md backup/ 2>/dev/null || true
cp .gitignore backup/ 2>/dev/null || true
cp -r .github backup/ 2>/dev/null || true

# Generate SDK
openapi-generator-cli generate \
    -i "$SPEC_FILE" \
    -g python \
    -o . \
    --additional-properties="packageName=griddy_nfl_sdk,packageVersion=1.0.0,projectName=griddy-nfl-sdk" \
    --skip-validate-spec \
    --global-property models,apis,supportingFiles

# Restore backed up files
cp backup/README.md . 2>/dev/null || true
cp backup/.gitignore . 2>/dev/null || true
cp -r backup/.github . 2>/dev/null || true

echo "✅ Python SDK regenerated successfully!"
EOF
            ;;
        "java")
            cat >> generate.sh << 'EOF'
# Backup important files
cp pom.xml backup/ 2>/dev/null || true
cp build.gradle backup/ 2>/dev/null || true
cp README.md backup/ 2>/dev/null || true
cp .gitignore backup/ 2>/dev/null || true
cp -r .github backup/ 2>/dev/null || true

# Generate SDK
openapi-generator-cli generate \
    -i "$SPEC_FILE" \
    -g java \
    -o . \
    --additional-properties="groupId=com.griddy,artifactId=nfl-sdk,artifactVersion=1.0.0,apiPackage=com.griddy.nfl.api,modelPackage=com.griddy.nfl.model,invokerPackage=com.griddy.nfl.client" \
    --skip-validate-spec \
    --global-property models,apis,supportingFiles

# Restore backed up files
cp backup/README.md . 2>/dev/null || true
cp backup/.gitignore . 2>/dev/null || true
cp -r backup/.github . 2>/dev/null || true

echo "✅ Java SDK regenerated successfully!"
EOF
            ;;
        "go")
            cat >> generate.sh << 'EOF'
# Backup important files
cp go.mod backup/ 2>/dev/null || true
cp README.md backup/ 2>/dev/null || true
cp .gitignore backup/ 2>/dev/null || true
cp -r .github backup/ 2>/dev/null || true

# Generate SDK
openapi-generator-cli generate \
    -i "$SPEC_FILE" \
    -g go \
    -o . \
    --additional-properties="packageName=nflsdk,packageVersion=1.0.0,moduleName=github.com/griddy/nfl-sdk-go" \
    --skip-validate-spec \
    --global-property models,apis,supportingFiles

# Restore backed up files
cp backup/README.md . 2>/dev/null || true
cp backup/.gitignore . 2>/dev/null || true
cp -r backup/.github . 2>/dev/null || true

echo "✅ Go SDK regenerated successfully!"
EOF
            ;;
        "csharp")
            cat >> generate.sh << 'EOF'
# Backup important files
cp *.csproj backup/ 2>/dev/null || true
cp README.md backup/ 2>/dev/null || true
cp .gitignore backup/ 2>/dev/null || true
cp -r .github backup/ 2>/dev/null || true

# Generate SDK
openapi-generator-cli generate \
    -i "$SPEC_FILE" \
    -g csharp \
    -o . \
    --additional-properties="packageName=Griddy.NFL.SDK,packageVersion=1.0.0,clientPackage=Griddy.NFL.SDK.Client,packageCompany=Griddy,packageDescription=NFL SDK for .NET" \
    --skip-validate-spec \
    --global-property models,apis,supportingFiles

# Restore backed up files
cp backup/README.md . 2>/dev/null || true
cp backup/.gitignore . 2>/dev/null || true
cp -r backup/.github . 2>/dev/null || true

echo "✅ C# SDK regenerated successfully!"
EOF
            ;;
    esac

    chmod +x generate.sh
}

# Main execution
echo -e "${BLUE}📋 SDK Repositories to create:${NC}"
for sdk_type in "${!SDK_CONFIGS[@]}"; do
    echo "  - ${SDK_CONFIGS[$sdk_type]} ($sdk_type)"
done

echo

# Create repositories for each SDK
for sdk_type in "${!SDK_CONFIGS[@]}"; do
    create_sdk_repository "$sdk_type" "${SDK_CONFIGS[$sdk_type]}"
done

echo
echo -e "${GREEN}🎉 All SDK repositories created successfully!${NC}"
echo -e "${YELLOW}📁 Created repositories:${NC}"
for sdk_type in "${!SDK_CONFIGS[@]}"; do
    repo_name="${SDK_CONFIGS[$sdk_type]}"
    if [ -d "$PARENT_DIR$repo_name" ]; then
        echo "  - $PARENT_DIR$repo_name"
    fi
done

echo
echo -e "${BLUE}📝 Next steps:${NC}"
echo "1. Navigate to each repository and set up remote origins"
echo "2. Push to your Git hosting service (GitHub, GitLab, etc.)"
echo "3. Set up package registry accounts and configure secrets"
echo "4. Create your first release to trigger automatic publishing"
echo
echo -e "${YELLOW}Example commands for each repo:${NC}"
echo "cd ../[repo-name]"
echo "git remote add origin https://github.com/your-org/[repo-name].git"
echo "git push -u origin main"
echo
echo -e "${BLUE}📦 Package Publishing Setup:${NC}"
echo "See PUBLISHING_SETUP.md in each repository for detailed instructions"
