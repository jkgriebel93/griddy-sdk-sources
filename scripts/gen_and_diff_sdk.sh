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

cd "${HOME}"
export FULL_SDK_REPO_PATH="${HOME}/griddy-sdk-python"
ls -lah
ls -lah work
echo "Operating in $(pwd)"
echo "Using GitHub CLI to clone Python SDK Repo..."
gh repo clone "${PYTHON_SDK_REPO}"


cd "${GITHUB_WORKSPACE}"
echo "Now operating in ${GITHUB_WORKSPACE}"
ls -lah

echo "Going to attempt to generate SDK now"
speakeasy generate sdk --lang python --schema openapi/nfl-com-api.yaml --out griddy-sdk-python
echo "Attempting preserve files command"
python scripts/preserve_files.py "${FULL_SDK_REPO_PATH}" griddy-sdk-python "${FULL_SDK_REPO_PATH}/.speakeasy-preserve"

echo "Preservation complete. Running rsync now."
rsync -av --delete --exclude='.git' griddy-sdk-python "${FULL_SDK_REPO_PATH}"

cd "${FULL_SDK_REPO_PATH}"
echo "Operating in $(pwd)"

if git diff --quiet; then
  echo "has_changes=false" >> "${GITHUB_OUTPUT}"
  echo "No changes detected"
else
  echo "has_changes=true" >> "${GITHUB_OUTPUT}"
  echo "Changes detected"
  git diff --stat
fi

git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"
git add .
git commit -s -m "Update SDK with Speakeasy generated changes"
git checkout -b "auto-update-sdk-${COMMIT_SHA}"
git push origin "auto-update-sdk-${COMMIT_SHA}"
gh auth login --with-token "${PAT_TOKEN}"
gh pr create --title "Update Griddy Python SDK" --body "Auto-generated update" --base master --head "auto-update-sdk-${COMMIT_SHA}"