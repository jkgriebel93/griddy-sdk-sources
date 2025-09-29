#!/bin/bash

# Generate TypeScript SDK for NFL API

set -e

echo "🚀 Generating TypeScript SDK..."

openapi-generator-cli generate \
    -i openapi/nfl-com-api.yaml \
    -g typescript-axios \
    -o sdks/typescript \
    --additional-properties="npmName=@griddy/nfl-api,npmVersion=1.0.0,withInterfaces=true,withoutRuntimeChecks=false" \
    --skip-validate-spec \
    --global-property models,apis,supportingFiles

echo "✅ TypeScript SDK generated in sdks/typescript/"