#!/bin/bash
set -e

echo "Current working directory: $(pwd)"
echo "GitHub workspace: ${GITHUB_WORKSPACE}"
echo "Python SDK Repo: ${PYTHON_SDK_REPO}"
echo "Python Version: $(python --version)"
ls -lah

echo "Installing Speakeasy CLI..."
curl -fsSL https://raw.githubusercontent.com/speakeasy-api/speakeasy/main/install.sh | bash -s -- -b /usr/local/bin
speakeasy --version

