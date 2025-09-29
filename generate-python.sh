#!/bin/bash

# Generate Python SDK for NFL API

set -e

echo "🐍 Generating Python SDK..."

openapi-generator-cli generate \
    -i openapi/nfl-com-api.yaml \
    -g python \
    -o sdks/python \
    --additional-properties="packageName=griddy_nfl_api,packageVersion=1.0.0,projectName=griddy-nfl-api" \
    --skip-validate-spec \
    --global-property models,apis,supportingFiles

echo "✅ Python SDK generated in sdks/python/"