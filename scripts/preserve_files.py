#!/usr/bin/env python3
"""
Smart file preservation script for SDK regeneration.

This script preserves specified files during SDK regeneration by copying them
from the original SDK repository to the newly generated SDK directory.

Usage:
    python preserve_files.py <source_dir> <target_dir> <preserve_file>

Example:
    python preserve_files.py sdk-repo griddy-sdk-python sdk-repo/.speakeasy-preserve
"""
import sys
import shutil
from pathlib import Path
from typing import List, Tuple


def read_preserve_patterns(preserve_file: Path) -> List[str]:
    """
    Read and parse the preservation patterns file.

    Args:
        preserve_file: Path to the .speakeasy-preserve file

    Returns:
        List of file patterns to preserve (comments and empty lines removed)
    """
    patterns = []

    with open(preserve_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Strip whitespace
            line = line.strip()

            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue

            patterns.append(line)

    return patterns


def preserve_files(
        source_dir: Path,
        target_dir: Path,
        preserve_file: Path
) -> Tuple[int, int]:
    """
    Copy files from source to target based on preserve file specifications.

    Args:
        source_dir: Directory containing original files to preserve
        target_dir: Directory where preserved files should be copied
        preserve_file: File containing list of paths to preserve

    Returns:
        Tuple of (preserved_count, missing_count)
    """
    if not preserve_file.exists():
        print(f"No preservation file found at {preserve_file}")
        return 0, 0

    print(f"📋 Reading preservation rules from {preserve_file.name}")
    print(f"   Source: {source_dir}")
    print(f"   Target: {target_dir}")
    print()

    patterns = read_preserve_patterns(preserve_file)

    if not patterns:
        print("No files specified for preservation")
        return 0, 0

    preserved_count = 0
    missing_count = 0

    for pattern in patterns:
        source_path = source_dir / pattern
        target_path = target_dir / pattern

        if source_path.exists():
            # Create parent directories if needed
            target_path.parent.mkdir(parents=True, exist_ok=True)

            # Copy file or directory, preserving metadata
            if source_path.is_file():
                shutil.copy2(source_path, target_path)
                print(f"Preserved file: {pattern}")
            elif source_path.is_dir():
                shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                print(f"Preserved directory: {pattern}")

            preserved_count += 1
        else:
            print(f"Not found: {pattern}")
            missing_count += 1

    return preserved_count, missing_count


def validate_directories(source_dir: Path, target_dir: Path) -> None:
    """
    Validate that source and target directories exist.

    Args:
        source_dir: Source directory path
        target_dir: Target directory path

    Raises:
        FileNotFoundError: If either directory doesn't exist
    """
    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")

    if not source_dir.is_dir():
        raise NotADirectoryError(f"Source path is not a directory: {source_dir}")

    if not target_dir.exists():
        raise FileNotFoundError(f"Target directory does not exist: {target_dir}")

    if not target_dir.is_dir():
        raise NotADirectoryError(f"Target path is not a directory: {target_dir}")


def print_summary(preserved_count: int, missing_count: int) -> None:
    """
    Print a summary of the preservation operation.

    Args:
        preserved_count: Number of files successfully preserved
        missing_count: Number of files that were not found
    """
    print()
    print("=" * 50)
    print("Preservation Summary")
    print("=" * 50)
    print(f"Files preserved: {preserved_count}")

    if missing_count > 0:
        print(f"Files missing: {missing_count}")
        print()
        print("Note: Missing files may have been removed or renamed.")
        print("Update .speakeasy-preserve to reflect the current structure.")

    print("=" * 50)


def main():
    """Main entry point for the script."""
    if len(sys.argv) != 4:
        print("Error: Incorrect number of arguments")
        print()
        print("Usage: preserve_files.py <source_dir> <target_dir> <preserve_file>")
        print()
        print("Arguments:")
        print("  source_dir    - Directory containing files to preserve")
        print("  target_dir    - Directory where files should be copied")
        print("  preserve_file - File listing paths to preserve")
        print()
        print("Example:")
        print("  python preserve_files.py sdk-repo generated-sdk sdk-repo/.speakeasy-preserve")
        sys.exit(1)

    # Parse arguments
    source_dir = Path(sys.argv[1]).resolve()
    target_dir = Path(sys.argv[2]).resolve()
    preserve_file = Path(sys.argv[3]).resolve()

    try:
        # Validate inputs
        validate_directories(source_dir, target_dir)

        # Perform preservation
        preserved_count, missing_count = preserve_files(
            source_dir,
            target_dir,
            preserve_file
        )

        # Print summary
        print_summary(preserved_count, missing_count)

        # Exit with success
        print("\nFile preservation complete!")
        sys.exit(0)

    except FileNotFoundError as e:
        print(f"\nError: {e}")
        sys.exit(1)
    except NotADirectoryError as e:
        print(f"\nError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error during preservation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()