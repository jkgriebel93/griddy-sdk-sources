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
ls -lah
ls -lah work
echo "Operating in $(pwd)"
echo "Using GitHub CLI to clone Python SDK Repo..."
gh repo clone $PYTHON_SDK_REPO


cd $GITHUB_WORKSPACE
echo "Now operating in ${GITHUB_WORKSPACE}"
ls -lah

echo "Going to attempt to generate SDK now"
speakeasy generate sdk --lang python --schema openapi/nfl-com-api.yaml --out griddy-sdk-python

