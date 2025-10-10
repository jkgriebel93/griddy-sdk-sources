#!/bin/bash
set -e

echo "Current working directory: $(pwd)"
echo "GitHub workspace: ${GITHUB_WORKSPACE}"
echo "Python SDK Repo: ${PYTHON_SDK_REPO}"
echo "HOME: ${HOME}"
echo "Python Version: $(python --version)"


echo "Installing Speakeasy CLI..."
curl -fsSL https://raw.githubusercontent.com/speakeasy-api/speakeasy/main/install.sh | bash -s -- -b /usr/local/bin
speakeasy --version

cd $HOME
echo "Operating in $(pwd)"
echo "Using GitHub CLI to clone Python SDK Repo..."
gh repo clone $PYTHON_SDK_REPO