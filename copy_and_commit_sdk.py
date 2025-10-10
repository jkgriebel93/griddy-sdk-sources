#!/usr/bin/env python3

import os
import sys
import shutil
import subprocess
import argparse
from pathlib import Path
from typing import List, Tuple, Optional
import fnmatch

# ============================================================================
# DEFAULT IGNORE PATTERNS
# These patterns are used if no .codegenignore file is found
# Add file patterns here that should not be overwritten in the destination
# Supports wildcards: *.md, docs/*, etc.
# ============================================================================
DEFAULT_IGNORE_PATTERNS = [
    "*.md",
    "README.md",
    ".gitignore",
    ".git/*",
    "docs/*",
    "examples/*",
    # Add more patterns here as needed
]


# ANSI color codes
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color


class Logger:
    """Handles colored logging output"""

    @staticmethod
    def info(message: str):
        print(f"{Colors.GREEN}[INFO]{Colors.NC} {message}")

    @staticmethod
    def warn(message: str):
        print(f"{Colors.YELLOW}[WARN]{Colors.NC} {message}")

    @staticmethod
    def error(message: str):
        print(f"{Colors.RED}[ERROR]{Colors.NC} {message}")

    @staticmethod
    def pretend(message: str):
        print(f"{Colors.CYAN}[PRETEND]{Colors.NC} {message}")

    @staticmethod
    def action(message: str, pretend_mode: bool):
        if pretend_mode:
            print(f"{Colors.BLUE}[WOULD]{Colors.NC} {message}")
        else:
            Logger.info(message)


def find_codegen_ignore_file(explicit_path: Optional[Path] = None) -> Optional[Path]:
    """
    Find the codegen ignore file in the following priority order:
    1. Explicit path provided via --codegen-ignore-file
    2. .codegenignore in current directory
    3. Path specified in CODEGEN_IGNORE environment variable

    Args:
        explicit_path: Optional explicit path to ignore file

    Returns:
        Path to the ignore file if found, None otherwise
    """
    # Priority 1: Explicit parameter
    if explicit_path:
        if explicit_path.exists() and explicit_path.is_file():
            Logger.info(f"Using codegen ignore file: {explicit_path}")
            return explicit_path.resolve()
        else:
            Logger.warn(f"Specified codegen ignore file not found: {explicit_path}")

    # Priority 2: .codegenignore in current directory
    cwd_ignore = Path.cwd() / ".codegenignore"
    if cwd_ignore.exists() and cwd_ignore.is_file():
        Logger.info(f"Found codegen ignore file: {cwd_ignore}")
        return cwd_ignore.resolve()

    # Priority 3: CODEGEN_IGNORE environment variable
    env_path = os.environ.get('CODEGEN_IGNORE')
    if env_path:
        env_ignore = Path(env_path)
        if env_ignore.exists() and env_ignore.is_file():
            Logger.info(f"Using codegen ignore file from CODEGEN_IGNORE: {env_ignore}")
            return env_ignore.resolve()
        else:
            Logger.warn(f"CODEGEN_IGNORE points to non-existent file: {env_path}")

    # No ignore file found
    return None


def load_ignore_patterns(ignore_file: Optional[Path]) -> List[str]:
    """
    Load ignore patterns from file or return default patterns

    Args:
        ignore_file: Path to the ignore file, or None to use defaults

    Returns:
        List of ignore patterns
    """
    if ignore_file is None:
        Logger.warn("No codegen ignore file found - using default patterns")
        return DEFAULT_IGNORE_PATTERNS

    patterns = []
    try:
        with open(ignore_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Strip whitespace
                line = line.strip()

                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue

                patterns.append(line)

        Logger.info(f"Loaded {len(patterns)} pattern(s) from {ignore_file}")
        return patterns

    except IOError as e:
        Logger.error(f"Failed to read ignore file {ignore_file}: {e}")
        Logger.warn("Using default patterns instead")
        return DEFAULT_IGNORE_PATTERNS
    except Exception as e:
        Logger.error(f"Unexpected error reading ignore file: {e}")
        Logger.warn("Using default patterns instead")
        return DEFAULT_IGNORE_PATTERNS


def should_ignore_file(file_path: Path, dest_dir: Path, patterns: List[str]) -> bool:
    """
    Check if a file should be ignored based on patterns

    Args:
        file_path: The destination file path to check
        dest_dir: The destination directory root
        patterns: List of ignore patterns

    Returns:
        True if the file should be ignored, False otherwise
    """
    try:
        # Get relative path from destination directory
        rel_path = file_path.relative_to(dest_dir)
    except ValueError:
        # If file_path is not relative to dest_dir, don't ignore
        return False

    rel_path_str = str(rel_path)
    filename = file_path.name

    # Check against ignore patterns
    for pattern in patterns:
        if not pattern:
            continue

        # Check if the relative path matches the pattern
        if fnmatch.fnmatch(rel_path_str, pattern):
            return True

        # Also check just the filename for patterns like "*.md"
        if fnmatch.fnmatch(filename, pattern):
            return True

        # Handle directory patterns like "docs/*"
        if '/' in pattern:
            if fnmatch.fnmatch(rel_path_str, pattern):
                return True

    return False


def copy_files(src_dir: Path, dest_dir: Path, patterns: List[str], pretend_mode: bool) -> Tuple[int, int]:
    """
    Recursively copy files from source to destination

    Args:
        src_dir: Source directory
        dest_dir: Destination directory
        patterns: List of ignore patterns
        pretend_mode: If True, only show what would be done

    Returns:
        Tuple of (copied_count, skipped_count)
    """
    Logger.action(f"Copying files from {src_dir} to {dest_dir}", pretend_mode)

    copied_count = 0
    skipped_count = 0

    if pretend_mode:
        Logger.pretend(f"Would create destination directory if needed: {dest_dir}")
        print()
        Logger.pretend("Active ignore patterns:")
        for pattern in patterns:
            if pattern:
                Logger.pretend(f"  - {pattern}")
        print()
        Logger.pretend("Files that would be copied:")
        Logger.pretend("----------------------------")
    else:
        # Create destination directory if it doesn't exist
        dest_dir.mkdir(parents=True, exist_ok=True)

    # Walk through all files in source directory
    for src_file in src_dir.rglob('*'):
        if src_file.is_file():
            # Calculate relative path and destination file path
            rel_path = src_file.relative_to(src_dir)
            dest_file = dest_dir / rel_path

            # Check if file should be ignored
            if should_ignore_file(dest_file, dest_dir, patterns):
                if pretend_mode:
                    Logger.pretend(f"  [SKIP] {rel_path} (matches ignore pattern)")
                else:
                    Logger.warn(f"Skipping ignored file: {rel_path}")
                skipped_count += 1
                continue

            if pretend_mode:
                # Show if file exists and would be overwritten
                if dest_file.exists():
                    Logger.pretend(f"  [OVERWRITE] {rel_path}")
                else:
                    Logger.pretend(f"  [NEW] {rel_path}")
            else:
                # Create parent directory if needed
                dest_file.parent.mkdir(parents=True, exist_ok=True)

                # Copy the file
                shutil.copy2(src_file, dest_file)

            copied_count += 1

    if pretend_mode:
        print()
        Logger.pretend(f"Summary: Would copy {copied_count} file(s), skip {skipped_count} file(s)")
        print()
    else:
        Logger.info(f"Copied {copied_count} file(s), skipped {skipped_count} file(s)")

    return copied_count, skipped_count


def run_git_command(git_root: Path, command: List[str], check: bool = True) -> subprocess.CompletedProcess:
    """
    Run a git command in the specified directory

    Args:
        git_root: Git repository root directory
        command: Git command as list of strings
        check: If True, raise exception on non-zero exit code

    Returns:
        CompletedProcess instance
    """
    full_command = ['git', '-C', str(git_root)] + command
    return subprocess.run(
        full_command,
        capture_output=True,
        text=True,
        check=check
    )


def check_git_repo(dest_dir: Path, pretend_mode: bool):
    """
    Verify that destination directory is in a git repository

    Args:
        dest_dir: Destination directory to check
        pretend_mode: If True, only show what would be checked

    Raises:
        SystemExit if not in a git repository
    """
    try:
        result = run_git_command(dest_dir, ['rev-parse', '--git-dir'], check=False)
        if result.returncode != 0:
            Logger.error(f"Destination directory is not in a git repository: {dest_dir}")
            sys.exit(1)

        if pretend_mode:
            Logger.pretend("Verified destination is in a git repository")
    except FileNotFoundError:
        Logger.error("Git is not installed or not in PATH")
        sys.exit(1)


def get_git_root(dest_dir: Path) -> Path:
    """Get the root directory of the git repository"""
    result = run_git_command(dest_dir, ['rev-parse', '--show-toplevel'])
    return Path(result.stdout.strip())


def get_current_branch(git_root: Path) -> str:
    """Get the current git branch name"""
    result = run_git_command(git_root, ['branch', '--show-current'], check=False)
    return result.stdout.strip() if result.returncode == 0 else "detached"


def branch_exists_locally(git_root: Path, branch_name: str) -> bool:
    """Check if a branch exists locally"""
    result = run_git_command(
        git_root,
        ['show-ref', '--verify', '--quiet', f'refs/heads/{branch_name}'],
        check=False
    )
    return result.returncode == 0


def branch_exists_remotely(git_root: Path, branch_name: str) -> bool:
    """Check if a branch exists on remote"""
    result = run_git_command(
        git_root,
        ['ls-remote', '--heads', 'origin', branch_name],
        check=False
    )
    return branch_name in result.stdout


def setup_git_branch(dest_dir: Path, branch_name: str, pretend_mode: bool):
    """
    Create or checkout the specified git branch

    Args:
        dest_dir: Destination directory (must be in git repo)
        branch_name: Name of the branch to create/checkout
        pretend_mode: If True, only show what would be done
    """
    Logger.action(f"Setting up git branch: {branch_name}", pretend_mode)

    git_root = get_git_root(dest_dir)
    current_branch = get_current_branch(git_root)

    if branch_exists_locally(git_root, branch_name):
        if pretend_mode:
            Logger.pretend(f"Would checkout existing local branch: {branch_name} (currently on: {current_branch})")
        else:
            Logger.info(f"Checking out existing branch: {branch_name}")
            run_git_command(git_root, ['checkout', branch_name])

    elif branch_exists_remotely(git_root, branch_name):
        if pretend_mode:
            Logger.pretend(f"Would checkout remote branch: origin/{branch_name} (currently on: {current_branch})")
        else:
            Logger.info(f"Checking out remote branch: {branch_name}")
            run_git_command(git_root, ['checkout', '-b', branch_name, f'origin/{branch_name}'])

    else:
        if pretend_mode:
            Logger.pretend(f"Would create new branch: {branch_name} (currently on: {current_branch})")
        else:
            Logger.info(f"Creating new branch: {branch_name}")
            run_git_command(git_root, ['checkout', '-b', branch_name])

    if pretend_mode:
        print()


def has_changes(git_root: Path) -> bool:
    """Check if there are any uncommitted changes"""
    # Check both staged and unstaged changes
    result_diff = run_git_command(git_root, ['diff', '--quiet'], check=False)
    result_cached = run_git_command(git_root, ['diff', '--cached', '--quiet'], check=False)

    return result_diff.returncode != 0 or result_cached.returncode != 0


def get_status_porcelain(git_root: Path, path: Path) -> str:
    """Get git status in porcelain format for a specific path"""
    result = run_git_command(
        git_root,
        ['status', '--porcelain', str(path)],
        check=False
    )
    return result.stdout


def output_git_status(dest_dir: Path):
    """
    Output git status to the console

    Args:
        dest_dir: Destination directory (must be in git repo)
    """
    Logger.info("Git status:")
    print()
    git_root = get_git_root(dest_dir)
    result = run_git_command(git_root, ['status'], check=False)
    print(result.stdout)


def commit_and_push(dest_dir: Path, branch_name: str, pretend_mode: bool):
    """
    Commit and push changes to the remote repository

    Args:
        dest_dir: Destination directory
        branch_name: Branch to push to
        pretend_mode: If True, only show what would be done
    """
    git_root = get_git_root(dest_dir)
    rel_dest_dir = dest_dir.relative_to(git_root)

    if pretend_mode:
        Logger.pretend("Git operations that would be performed:")
        Logger.pretend("----------------------------------------")
        Logger.pretend(f"Would stage changes in: {rel_dest_dir}")

        # Try to show what changes exist (if any)
        changes = get_status_porcelain(git_root, rel_dest_dir)

        if not changes:
            Logger.pretend("No changes detected - would skip commit and push")
            print()
            return

        print()
        Logger.pretend("Changed files that would be committed:")
        for line in changes.strip().split('\n'):
            if line:
                Logger.pretend(f"  {line}")

        print()
        commit_msg = f"Update SDK with changes resulting from speakeasy sdk generate"
        Logger.pretend(f'Would commit with message: "{commit_msg}"')
        Logger.pretend(f"Would push to: origin/{branch_name}")
        print()

    else:
        # Check if there are any changes
        if not has_changes(git_root):
            Logger.info("No changes to commit")
            return

        # Stage all changes in destination directory
        Logger.info(f"Staging changes in {rel_dest_dir}")
        run_git_command(git_root, ['add', str(rel_dest_dir)])

        # Commit changes
        commit_msg = f"Update SDK files in {rel_dest_dir}"
        Logger.info(f"Committing changes: {commit_msg}")
        run_git_command(git_root, ['commit', '-m', commit_msg])

        # Push to remote
        Logger.info(f"Pushing branch {branch_name} to remote")
        run_git_command(git_root, ['push', 'origin', branch_name])

        Logger.info(f"Successfully pushed changes to remote branch: {branch_name}")


def print_banner(pretend_mode: bool):
    """Print the pretend mode banner"""
    if pretend_mode:
        print()
        print("═" * 59)
        print(f"{Colors.CYAN}                    PRETEND MODE ACTIVE{Colors.NC}")
        print("          No files or git state will be modified")
        print("═" * 59)
        print()


def print_footer(pretend_mode: bool):
    """Print the pretend mode footer"""
    if pretend_mode:
        print("═" * 59)
        print(f"{Colors.CYAN}           PRETEND MODE - No changes were made{Colors.NC}")
        print("═" * 59)
        print()
        Logger.info("To execute these changes, run without --pretend flag")
    else:
        Logger.info("Script completed successfully!")


def main():
    """Main script execution"""
    parser = argparse.ArgumentParser(
        description='Recursively copy files, commit to git, and push to remote',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
The script looks for a codegen ignore file in the following order:
1. --codegen-ignore-file parameter
2. .codegenignore in current directory
3. Path specified in CODEGEN_IGNORE environment variable
4. If none found, uses default ignore patterns

When --pretend is specified, the script will:
- Show all files that would be copied
- Show files that would be skipped (ignored)
- Show git operations that would be performed
- Not modify any files or git state

By default, the script will NOT commit and push changes. Use --commit to enable.

The --output-status flag will print the git status output to the console after
copying files, which is useful for reviewing changes before committing.
        """
    )

    parser.add_argument(
        '--source-dir',
        required=True,
        type=Path,
        help='Directory to copy files from'
    )

    parser.add_argument(
        '--destination-dir',
        required=True,
        type=Path,
        help='Directory to copy files to'
    )

    parser.add_argument(
        '--branch',
        default='sdk-updates',
        help='Git branch name (default: sdk-updates)'
    )

    parser.add_argument(
        '--codegen-ignore-file',
        type=Path,
        help='Path to codegen ignore file'
    )

    parser.add_argument(
        '--pretend',
        action='store_true',
        help='Dry-run mode - show what would be done without doing it'
    )

    parser.add_argument(
        '--commit',
        action='store_true',
        help='Commit and push changes to remote (default: False)'
    )

    parser.add_argument(
        '--output-status',
        action='store_true',
        help='Print git status output to console'
    )

    args = parser.parse_args()

    # Show pretend mode banner
    print_banner(args.pretend)

    # Validate source directory exists
    if not args.source_dir.exists():
        Logger.error(f"Source directory does not exist: {args.source_dir}")
        sys.exit(1)

    if not args.source_dir.is_dir():
        Logger.error(f"Source path is not a directory: {args.source_dir}")
        sys.exit(1)

    # Convert to absolute paths
    source_dir = args.source_dir.resolve()
    destination_dir = args.destination_dir.resolve()

    # Find and load ignore patterns
    ignore_file = find_codegen_ignore_file(args.codegen_ignore_file)
    ignore_patterns = load_ignore_patterns(ignore_file)

    if args.pretend:
        Logger.pretend("Configuration:")
        Logger.pretend(f"  Source directory: {source_dir}")
        Logger.pretend(f"  Destination directory: {destination_dir}")
        Logger.pretend(f"  Branch name: {args.branch}")
        Logger.pretend(f"  Ignore patterns: {len(ignore_patterns)} pattern(s) configured")
        if ignore_file:
            Logger.pretend(f"  Ignore file: {ignore_file}")
        print()

    # Check if destination is in a git repository
    check_git_repo(destination_dir, args.pretend)

    # Setup git branch
    setup_git_branch(destination_dir, args.branch, args.pretend)

    # Copy files
    copy_files(source_dir, destination_dir, ignore_patterns, args.pretend)

    # Output git status if requested
    if args.output_status:
        output_git_status(destination_dir)

    # Commit and push changes (only if --commit flag is passed)
    if args.commit:
        commit_and_push(destination_dir, args.branch, args.pretend)
    else:
        if not args.pretend:
            Logger.info("Skipping commit and push (use --commit to enable)")

    # Print footer
    print_footer(args.pretend)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        Logger.error("Script interrupted by user")
        sys.exit(1)
    except Exception as e:
        Logger.error(f"Unexpected error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)