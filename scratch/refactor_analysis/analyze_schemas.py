#!/usr/bin/env python3
"""
Analyze OpenAPI spec to determine which schemas are used by Pro API vs Regular API paths
"""

import yaml
import re
from collections import defaultdict
from pathlib import Path

def extract_schema_refs(obj, refs=None):
    """Recursively extract all $ref schema references from an object"""
    if refs is None:
        refs = set()

    if isinstance(obj, dict):
        if '$ref' in obj:
            ref = obj['$ref']
            # Extract schema name from reference like '#/components/schemas/SchemaName'
            match = re.search(r'#/components/schemas/(\w+)', ref)
            if match:
                refs.add(match.group(1))

        for value in obj.values():
            extract_schema_refs(value, refs)

    elif isinstance(obj, list):
        for item in obj:
            extract_schema_refs(item, refs)

    return refs

def get_all_referenced_schemas(schema_name, all_schemas, visited=None):
    """Recursively get all schemas referenced by a given schema"""
    if visited is None:
        visited = set()

    if schema_name in visited or schema_name not in all_schemas:
        return visited

    visited.add(schema_name)

    # Get direct references from this schema
    direct_refs = extract_schema_refs(all_schemas[schema_name])

    # Recursively get references from referenced schemas
    for ref in direct_refs:
        get_all_referenced_schemas(ref, all_schemas, visited)

    return visited

def main():
    spec_path = Path('/home/jkgriebel/Repos/griddy-sdk-sources/openapi/nfl-com-api.yaml')

    print("Loading OpenAPI spec...")
    with open(spec_path, 'r') as f:
        spec = yaml.safe_load(f)

    paths = spec.get('paths', {})
    all_schemas = spec.get('components', {}).get('schemas', {})

    # Categorize paths
    pro_api_paths = []
    regular_api_paths = []

    for path in paths.keys():
        if path.startswith('/api/'):
            pro_api_paths.append(path)
        else:
            regular_api_paths.append(path)

    print(f"\n{'='*80}")
    print(f"PATH ANALYSIS")
    print(f"{'='*80}")
    print(f"\nTotal Pro API paths (/api/*): {len(pro_api_paths)}")
    print(f"Total Regular API paths: {len(regular_api_paths)}")

    # Track direct schema references per path
    pro_direct_schemas = set()
    regular_direct_schemas = set()

    print("\n\nAnalyzing Pro API paths...")
    for path in pro_api_paths:
        path_obj = paths[path]
        refs = extract_schema_refs(path_obj)
        pro_direct_schemas.update(refs)

    print(f"Direct schema references in Pro API: {len(pro_direct_schemas)}")

    print("\nAnalyzing Regular API paths...")
    for path in regular_api_paths:
        path_obj = paths[path]
        refs = extract_schema_refs(path_obj)
        regular_direct_schemas.update(refs)

    print(f"Direct schema references in Regular API: {len(regular_direct_schemas)}")

    # Now resolve all transitive dependencies
    print("\n\nResolving transitive schema dependencies...")

    pro_all_schemas = set()
    for schema in pro_direct_schemas:
        pro_all_schemas.update(get_all_referenced_schemas(schema, all_schemas))

    regular_all_schemas = set()
    for schema in regular_direct_schemas:
        regular_all_schemas.update(get_all_referenced_schemas(schema, all_schemas))

    # Calculate shared vs exclusive schemas
    shared_schemas = pro_all_schemas & regular_all_schemas
    pro_exclusive_schemas = pro_all_schemas - regular_all_schemas
    regular_exclusive_schemas = regular_all_schemas - pro_all_schemas

    print(f"\n{'='*80}")
    print(f"SCHEMA ANALYSIS (including transitive dependencies)")
    print(f"{'='*80}")
    print(f"\nTotal schemas used by Pro API: {len(pro_all_schemas)}")
    print(f"Total schemas used by Regular API: {len(regular_all_schemas)}")
    print(f"Shared schemas (used by both): {len(shared_schemas)}")
    print(f"Pro API exclusive schemas: {len(pro_exclusive_schemas)}")
    print(f"Regular API exclusive schemas: {len(regular_exclusive_schemas)}")

    # Write detailed results to files
    output_dir = Path('/home/jkgriebel/Repos/griddy-sdk-sources')

    # Pro API paths
    with open(output_dir / 'pro_api_paths.txt', 'w') as f:
        f.write(f"Pro API Paths ({len(pro_api_paths)} total)\n")
        f.write("=" * 80 + "\n\n")
        for path in sorted(pro_api_paths):
            f.write(f"{path}\n")

    # Regular API paths
    with open(output_dir / 'regular_api_paths.txt', 'w') as f:
        f.write(f"Regular API Paths ({len(regular_api_paths)} total)\n")
        f.write("=" * 80 + "\n\n")
        for path in sorted(regular_api_paths):
            f.write(f"{path}\n")

    # Shared schemas
    with open(output_dir / 'shared_schemas.txt', 'w') as f:
        f.write(f"Shared Schemas ({len(shared_schemas)} total)\n")
        f.write("=" * 80 + "\n")
        f.write("These schemas are used by BOTH Pro API and Regular API\n")
        f.write("and should go in the shared spec\n")
        f.write("=" * 80 + "\n\n")
        for schema in sorted(shared_schemas):
            f.write(f"{schema}\n")

    # Pro exclusive schemas
    with open(output_dir / 'pro_exclusive_schemas.txt', 'w') as f:
        f.write(f"Pro API Exclusive Schemas ({len(pro_exclusive_schemas)} total)\n")
        f.write("=" * 80 + "\n")
        f.write("These schemas are ONLY used by Pro API paths\n")
        f.write("=" * 80 + "\n\n")
        for schema in sorted(pro_exclusive_schemas):
            f.write(f"{schema}\n")

    # Regular exclusive schemas
    with open(output_dir / 'regular_exclusive_schemas.txt', 'w') as f:
        f.write(f"Regular API Exclusive Schemas ({len(regular_exclusive_schemas)} total)\n")
        f.write("=" * 80 + "\n")
        f.write("These schemas are ONLY used by Regular API paths\n")
        f.write("=" * 80 + "\n\n")
        for schema in sorted(regular_exclusive_schemas):
            f.write(f"{schema}\n")

    # Summary report
    with open(output_dir / 'schema_analysis_summary.txt', 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("NFL API SCHEMA ANALYSIS SUMMARY\n")
        f.write("=" * 80 + "\n\n")

        f.write("PATH COUNTS:\n")
        f.write("-" * 80 + "\n")
        f.write(f"Pro API paths (/api/*):     {len(pro_api_paths):>4}\n")
        f.write(f"Regular API paths:          {len(regular_api_paths):>4}\n")
        f.write(f"Total paths:                {len(pro_api_paths) + len(regular_api_paths):>4}\n\n")

        f.write("SCHEMA COUNTS (including transitive dependencies):\n")
        f.write("-" * 80 + "\n")
        f.write(f"Pro API schemas:            {len(pro_all_schemas):>4}\n")
        f.write(f"Regular API schemas:        {len(regular_all_schemas):>4}\n")
        f.write(f"Shared schemas (both):      {len(shared_schemas):>4}\n")
        f.write(f"Pro API exclusive:          {len(pro_exclusive_schemas):>4}\n")
        f.write(f"Regular API exclusive:      {len(regular_exclusive_schemas):>4}\n")
        f.write(f"Total unique schemas:       {len(all_schemas):>4}\n\n")

        f.write("SPLIT STRATEGY:\n")
        f.write("-" * 80 + "\n")
        f.write("1. Create shared spec with {shared_schemas} schemas\n".format(shared_schemas=len(shared_schemas)))
        f.write("2. Pro API spec references shared + {pro_exclusive} exclusive schemas\n".format(pro_exclusive=len(pro_exclusive_schemas)))
        f.write("3. Regular API spec references shared + {regular_exclusive} exclusive schemas\n".format(regular_exclusive=len(regular_exclusive_schemas)))
        f.write("\nFiles generated:\n")
        f.write("  - pro_api_paths.txt (list of Pro API paths)\n")
        f.write("  - regular_api_paths.txt (list of Regular API paths)\n")
        f.write("  - shared_schemas.txt (schemas for shared spec)\n")
        f.write("  - pro_exclusive_schemas.txt (schemas only in Pro API)\n")
        f.write("  - regular_exclusive_schemas.txt (schemas only in Regular API)\n")

    print("\n\nDetailed results written to:")
    print(f"  - {output_dir}/pro_api_paths.txt")
    print(f"  - {output_dir}/regular_api_paths.txt")
    print(f"  - {output_dir}/shared_schemas.txt")
    print(f"  - {output_dir}/pro_exclusive_schemas.txt")
    print(f"  - {output_dir}/regular_exclusive_schemas.txt")
    print(f"  - {output_dir}/schema_analysis_summary.txt")

    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"\nPro API:     {len(pro_api_paths):>3} paths, {len(pro_all_schemas):>3} schemas ({len(pro_exclusive_schemas)} exclusive)")
    print(f"Regular API: {len(regular_api_paths):>3} paths, {len(regular_all_schemas):>3} schemas ({len(regular_exclusive_schemas)} exclusive)")
    print(f"Shared:      {len(shared_schemas):>3} schemas (used by both APIs)")

if __name__ == '__main__':
    main()
