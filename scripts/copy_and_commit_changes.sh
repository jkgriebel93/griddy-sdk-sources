#!/bin/bash

set -e  # Exit on error
set -o pipefail  # Exit on pipe failure

# ============================================================================
# HARDCODED IGNORE PATTERNS
# Add file patterns here that should not be overwritten in the destination
# Supports wildcards: *.md, docs/*, etc.
# ============================================================================
IGNORE_PATTERNS=(
    ".claude/*"
    ".github/*"
    ".speakeasy/*"
    ".git/*"
    ".vscode/*"
    "pyproject.toml"
    "uv.lock"
    "README.md"
    "USAGE.md"
    "src/griddy/nfl/__init__.py"
    "src/griddy/nfl/_version.py"
    "src/griddy/nfl/sdk.py"
    # Add more patterns here as needed
)

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Global variable for pretend mode
PRETEND_MODE=false

# Function to print colored messages
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_pretend() {
    echo -e "${CYAN}[PRETEND]${NC} $1"
}

log_action() {
    if [[ "$PRETEND_MODE" == true ]]; then
        echo -e "${BLUE}[WOULD]${NC} $1"
    else
        log_info "$1"
    fi
}

# Function to display usage
usage() {
    cat << EOF
Usage: $0 --source-dir <source> --destination-dir <destination> [OPTIONS]

Required arguments:
    --source-dir <path>         Directory to copy files from
    --destination-dir <path>    Directory to copy files to

Optional arguments:
    --branch <name>             Git branch name (default: sdk-updates)
    --pretend                   Dry-run mode - show what would be done without doing it
    -h, --help                  Display this help message

Ignore patterns are hardcoded in the script in the IGNORE_PATTERNS array.
Edit the script to modify which files are ignored.

When --pretend is specified, the script will:
- Show all files that would be copied
- Show files that would be skipped (ignored)
- Show git operations that would be performed
- Not modify any files or git state
EOF
    exit 1
}

# Function to check if a file should be ignored based on hardcoded patterns
should_ignore_file() {
    local file_path="$1"
    local dest_dir="$2"

    # Get relative path from destination directory
    local rel_path="${file_path#$dest_dir/}"

    # Check against hardcoded ignore patterns
    for pattern in "${IGNORE_PATTERNS[@]}"; do
        # Skip empty patterns
        [[ -z "$pattern" ]] && continue

        # Convert glob pattern to regex for matching
        # Replace * with .* for regex matching
        local regex_pattern="${pattern//\*/.*}"

        # Check if the relative path matches the pattern
        if [[ "$rel_path" == $pattern ]] || [[ "$rel_path" =~ ^${regex_pattern}$ ]]; then
            return 0  # Should ignore
        fi

        # Also check just the filename for patterns like "*.md"
        local filename=$(basename "$file_path")
        if [[ "$filename" == $pattern ]] || [[ "$filename" =~ ^${regex_pattern}$ ]]; then
            return 0  # Should ignore
        fi
    done

    return 1  # Don't ignore
}

# Function to copy files recursively
copy_files() {
    local src="$1"
    local dest="$2"
    local copied_count=0
    local skipped_count=0

    log_action "Copying files from $src to $dest"

    if [[ "$PRETEND_MODE" == true ]]; then
        log_pretend "Would create destination directory if needed: $dest"
        echo ""
        log_pretend "Active ignore patterns:"
        for pattern in "${IGNORE_PATTERNS[@]}"; do
            [[ -n "$pattern" ]] && log_pretend "  - $pattern"
        done
        echo ""
        log_pretend "Files that would be copied:"
        log_pretend "----------------------------"
    else
        # Create destination directory if it doesn't exist
        mkdir -p "$dest"
    fi

    # Find all files in source directory
    while IFS= read -r -d '' file; do
        # Get relative path
        local rel_path="${file#$src/}"
        local dest_file="$dest/$rel_path"

        # Check if file should be ignored
        if should_ignore_file "$dest_file" "$dest"; then
            if [[ "$PRETEND_MODE" == true ]]; then
                log_pretend "  [SKIP] $rel_path (matches ignore pattern)"
            else
                log_warn "Skipping ignored file: $rel_path"
            fi
            ((skipped_count++))
            continue
        fi

        if [[ "$PRETEND_MODE" == true ]]; then
            # Show if file exists and would be overwritten
            if [[ -f "$dest_file" ]]; then
                log_pretend "  [OVERWRITE] $rel_path"
            else
                log_pretend "  [NEW] $rel_path"
            fi
        else
            # Create parent directory if needed
            local dest_dir=$(dirname "$dest_file")
            mkdir -p "$dest_dir"

            # Copy the file
            cp "$file" "$dest_file"
        fi
        ((copied_count++))
    done < <(find "$src" -type f -print0)

    if [[ "$PRETEND_MODE" == true ]]; then
        echo ""
        log_pretend "Summary: Would copy $copied_count file(s), skip $skipped_count file(s)"
        echo ""
    else
        log_info "Copied $copied_count file(s), skipped $skipped_count file(s)"
    fi
}

# Function to check if we're in a git repository
check_git_repo() {
    local dir="$1"

    if ! git -C "$dir" rev-parse --git-dir > /dev/null 2>&1; then
        log_error "Destination directory is not in a git repository: $dir"
        exit 1
    fi

    if [[ "$PRETEND_MODE" == true ]]; then
        log_pretend "Verified destination is in a git repository"
    fi
}

# Function to create or checkout branch
setup_git_branch() {
    local dest_dir="$1"
    local branch_name="$2"

    log_action "Setting up git branch: $branch_name"

    # Navigate to git repository root
    local git_root=$(git -C "$dest_dir" rev-parse --show-toplevel)

    if [[ "$PRETEND_MODE" == false ]]; then
        cd "$git_root"
    fi

    # Check current branch (for pretend mode context)
    local current_branch=$(git -C "$git_root" branch --show-current 2>/dev/null || echo "detached")

    # Check if branch exists locally
    if git -C "$git_root" show-ref --verify --quiet "refs/heads/$branch_name"; then
        if [[ "$PRETEND_MODE" == true ]]; then
            log_pretend "Would checkout existing local branch: $branch_name (currently on: $current_branch)"
        else
            log_info "Checking out existing branch: $branch_name"
            git checkout "$branch_name"
        fi
    # Check if branch exists remotely
    elif git -C "$git_root" ls-remote --heads origin "$branch_name" 2>/dev/null | grep -q "$branch_name"; then
        if [[ "$PRETEND_MODE" == true ]]; then
            log_pretend "Would checkout remote branch: origin/$branch_name (currently on: $current_branch)"
        else
            log_info "Checking out remote branch: $branch_name"
            git checkout -b "$branch_name" "origin/$branch_name"
        fi
    else
        if [[ "$PRETEND_MODE" == true ]]; then
            log_pretend "Would create new branch: $branch_name (currently on: $current_branch)"
        else
            log_info "Creating new branch: $branch_name"
            git checkout -b "$branch_name"
        fi
    fi

    if [[ "$PRETEND_MODE" == true ]]; then
        echo ""
    fi
}

# Function to commit and push changes
commit_and_push() {
    local dest_dir="$1"
    local branch_name="$2"

    # Navigate to git repository root
    local git_root=$(git -C "$dest_dir" rev-parse --show-toplevel)

    if [[ "$PRETEND_MODE" == false ]]; then
        cd "$git_root"
    fi

    # Get relative path of destination directory from git root
    local rel_dest_dir=$(realpath --relative-to="$git_root" "$dest_dir")

    if [[ "$PRETEND_MODE" == true ]]; then
        log_pretend "Git operations that would be performed:"
        log_pretend "----------------------------------------"

        # Show what files would be staged
        log_pretend "Would stage changes in: $rel_dest_dir"

        # Try to show what changes exist (if any)
        local changes=$(git -C "$git_root" status --porcelain "$rel_dest_dir" 2>/dev/null || echo "")

        if [[ -z "$changes" ]]; then
            log_pretend "No changes detected - would skip commit and push"
            echo ""
            return 0
        fi

        echo ""
        log_pretend "Changed files that would be committed:"
        while IFS= read -r line; do
            if [[ -n "$line" ]]; then
                log_pretend "  $line"
            fi
        done <<< "$changes"

        echo ""
        local commit_msg="Update SDK files in $rel_dest_dir"
        log_pretend "Would commit with message: \"$commit_msg\""
        log_pretend "Would push to: origin/$branch_name"
        echo ""

    else
        # Check if there are any changes
        if git diff --quiet && git diff --cached --quiet; then
            log_info "No changes to commit"
            return 0
        fi

        # Stage all changes in destination directory
        log_info "Staging changes in $rel_dest_dir"
        git add "$rel_dest_dir"

        # Commit changes
        local commit_msg="Update SDK files in $rel_dest_dir"
        log_info "Committing changes: $commit_msg"
        git commit -m "$commit_msg"

        # Push to remote
        log_info "Pushing branch $branch_name to remote"
        git push origin "$branch_name"

        log_info "Successfully pushed changes to remote branch: $branch_name"
    fi
}

# Main script execution
main() {
    local source_dir=""
    local destination_dir=""
    local branch_name="sdk-updates"

    # Parse command line arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --source-dir)
                source_dir="$2"
                shift 2
                ;;
            --destination-dir)
                destination_dir="$2"
                shift 2
                ;;
            --branch)
                branch_name="$2"
                shift 2
                ;;
            --pretend)
                PRETEND_MODE=true
                shift
                ;;
            -h|--help)
                usage
                ;;
            *)
                log_error "Unknown argument: $1"
                usage
                ;;
        esac
    done

    # Show pretend mode banner
    if [[ "$PRETEND_MODE" == true ]]; then
        echo ""
        echo "═══════════════════════════════════════════════════════════"
        echo -e "${CYAN}                    PRETEND MODE ACTIVE${NC}"
        echo "          No files or git state will be modified"
        echo "═══════════════════════════════════════════════════════════"
        echo ""
    fi

    # Validate required arguments
    if [[ -z "$source_dir" ]] || [[ -z "$destination_dir" ]]; then
        log_error "Missing required arguments"
        usage
    fi

    # Validate source directory exists
    if [[ ! -d "$source_dir" ]]; then
        log_error "Source directory does not exist: $source_dir"
        exit 1
    fi

    # Convert to absolute paths
    source_dir=$(realpath "$source_dir")
    destination_dir=$(realpath "$destination_dir")

    if [[ "$PRETEND_MODE" == true ]]; then
        log_pretend "Configuration:"
        log_pretend "  Source directory: $source_dir"
        log_pretend "  Destination directory: $destination_dir"
        log_pretend "  Branch name: $branch_name"
        log_pretend "  Ignore patterns: ${#IGNORE_PATTERNS[@]} pattern(s) configured"
        echo ""
    fi

    # Check if destination is in a git repository
    check_git_repo "$destination_dir"

    # Setup git branch
    setup_git_branch "$destination_dir" "$branch_name"

    # Copy files
    copy_files "$source_dir" "$destination_dir"

    # Commit and push changes
    commit_and_push "$destination_dir" "$branch_name"

    if [[ "$PRETEND_MODE" == true ]]; then
        echo "═══════════════════════════════════════════════════════════"
        echo -e "${CYAN}           PRETEND MODE - No changes were made${NC}"
        echo "═══════════════════════════════════════════════════════════"
        echo ""
        log_info "To execute these changes, run without --pretend flag"
    else
        log_info "Script completed successfully!"
    fi
}

# Run main function
main "$@"