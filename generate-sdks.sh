#!/bin/bash

# Speakeasy SDK Generation Script
# This script generates SDKs for multiple programming languages using the NFL API spec

set -e

SPEC_FILE="openapi/nfl-com-api.yaml"
OUTPUT_BASE="sdks"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Parse command line arguments
TARGET_SDK=$1
SUPPORTED_SDKS=("typescript" "python" "go" "java" "csharp")

# Validate target SDK if provided
if [ -n "$TARGET_SDK" ]; then
    if [[ ! " ${SUPPORTED_SDKS[@]} " =~ " ${TARGET_SDK} " ]]; then
        echo -e "${RED}❌ Unsupported SDK: $TARGET_SDK${NC}"
        echo -e "${YELLOW}Supported SDKs: ${SUPPORTED_SDKS[*]}${NC}"
        exit 1
    fi
fi

echo -e "${YELLOW}🚀 Starting SDK generation with Speakeasy...${NC}"

# Check if spec file exists
if [ ! -f "$SPEC_FILE" ]; then
    echo -e "${RED}❌ OpenAPI spec file not found: $SPEC_FILE${NC}"
    exit 1
fi

# Check if Speakeasy is installed
if ! command -v speakeasy &> /dev/null; then
    echo -e "${RED}❌ Speakeasy CLI is not installed${NC}"
    echo -e "${YELLOW}Install it from: https://www.speakeasy.com/docs/speakeasy-reference/cli/getting-started#install${NC}"
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_BASE"

# Function to generate SDK
generate_sdk() {
    local lang=$1
    local output_dir=$2

    echo -e "${YELLOW}📦 Generating $lang SDK...${NC}"

    speakeasy generate sdk \
        --schema "$SPEC_FILE" \
        --lang "$lang" \
        -o "$output_dir"

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ $lang SDK generated successfully${NC}"
    else
        echo -e "${RED}❌ Failed to generate $lang SDK${NC}"
        return 1
    fi
}

# Generate specific SDK or all SDKs
if [ -n "$TARGET_SDK" ]; then
    # Generate only the specified SDK
    generate_sdk "$TARGET_SDK" "$OUTPUT_BASE/$TARGET_SDK"
    echo -e "${GREEN}🎉 $TARGET_SDK SDK generated successfully!${NC}"
    echo -e "${YELLOW}📁 SDK available at: $OUTPUT_BASE/$TARGET_SDK${NC}"
else
    # Generate all SDKs
    generate_sdk "typescript" "$OUTPUT_BASE/typescript"
    generate_sdk "python" "$OUTPUT_BASE/python"
    generate_sdk "go" "$OUTPUT_BASE/go"
    generate_sdk "java" "$OUTPUT_BASE/java"
    generate_sdk "csharp" "$OUTPUT_BASE/csharp"

    echo -e "${GREEN}🎉 All SDKs generated successfully!${NC}"
    echo -e "${YELLOW}📁 SDKs are available in the following directories:${NC}"
    echo "  - TypeScript: $OUTPUT_BASE/typescript"
    echo "  - Python: $OUTPUT_BASE/python"
    echo "  - Go: $OUTPUT_BASE/go"
    echo "  - Java: $OUTPUT_BASE/java"
    echo "  - C#: $OUTPUT_BASE/csharp"
fi