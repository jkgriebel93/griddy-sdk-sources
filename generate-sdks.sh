#!/bin/bash

# OpenAPI Generator SDK Generation Script
# This script generates SDKs for multiple programming languages using the NFL API spec

set -e

SPEC_FILE="openapi/nfl-com-api.yaml"
OUTPUT_BASE="sdks"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}🚀 Starting SDK generation...${NC}"

# Check if spec file exists
if [ ! -f "$SPEC_FILE" ]; then
    echo -e "${RED}❌ OpenAPI spec file not found: $SPEC_FILE${NC}"
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_BASE"

# Function to generate SDK
generate_sdk() {
    local generator=$1
    local output_dir=$2
    local additional_properties=$3

    echo -e "${YELLOW}📦 Generating $generator SDK...${NC}"

    openapi-generator-cli generate \
        -i "$SPEC_FILE" \
        -g "$generator" \
        -o "$output_dir" \
        --additional-properties="$additional_properties" \
        --skip-validate-spec \
        --global-property models,apis,supportingFiles \
        --global-property modelTests=false,apiTests=false,modelDocs=false,apiDocs=false

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ $generator SDK generated successfully${NC}"
    else
        echo -e "${RED}❌ Failed to generate $generator SDK${NC}"
        return 1
    fi
}

# Generate TypeScript/Axios SDK
generate_sdk "typescript-axios" "$OUTPUT_BASE/typescript" \
    "npmName=@griddy/nfl-api,npmVersion=1.0.0,withInterfaces=true,withoutRuntimeChecks=false"

# Generate Python SDK
generate_sdk "python" "$OUTPUT_BASE/python" \
    "packageName=griddy_nfl_api,packageVersion=1.0.0,projectName=griddy-nfl-api"

# Generate Java SDK
generate_sdk "java" "$OUTPUT_BASE/java" \
    "groupId=com.griddy,artifactId=nfl-api,artifactVersion=1.0.0,apiPackage=com.griddy.nfl.api,modelPackage=com.griddy.nfl.model,invokerPackage=com.griddy.nfl.client"

# Generate Go SDK
generate_sdk "go" "$OUTPUT_BASE/go" \
    "packageName=nflapi,packageVersion=1.0.0,moduleName=github.com/griddy/nfl-api-go"

# Generate C# SDK
generate_sdk "csharp" "$OUTPUT_BASE/csharp" \
    "packageName=Griddy.NFL.Api,packageVersion=1.0.0,clientPackage=Griddy.NFL.Api.Client,packageCompany=Griddy,packageDescription=NFL API SDK for .NET"

echo -e "${GREEN}🎉 All SDKs generated successfully!${NC}"
echo -e "${YELLOW}📁 SDKs are available in the following directories:${NC}"
echo "  - TypeScript: $OUTPUT_BASE/typescript"
echo "  - Python: $OUTPUT_BASE/python"
echo "  - Java: $OUTPUT_BASE/java"
echo "  - Go: $OUTPUT_BASE/go"
echo "  - C#: $OUTPUT_BASE/csharp"