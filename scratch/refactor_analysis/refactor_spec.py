#!/usr/bin/env python3
"""
Refactor nfl-com-api.yaml into three separate files:
1. nfl-shared.yaml - Shared schemas only
2. nfl-pro-api.yaml - Pro API paths and schemas
3. nfl-regular-api.yaml - Regular API paths and schemas
"""

import yaml
import os
from pathlib import Path

# Load the analysis files
def load_list_file(filepath):
    """Load a list of items from a text file, skipping headers and empty lines"""
    with open(filepath, 'r') as f:
        lines = f.readlines()

    items = []
    for line in lines:
        line = line.strip()
        # Skip empty lines, header lines, and separator lines
        if not line or '=' in line or 'total' in line or 'should go in' in line or 'ONLY used' in line:
            continue
        items.append(line)

    return items

# Load the analysis files
base_dir = '/home/jkgriebel/Repos/griddy-sdk-sources'
shared_schemas = set(load_list_file(f'{base_dir}/shared_schemas.txt'))
pro_schemas = set(load_list_file(f'{base_dir}/pro_exclusive_schemas.txt'))
regular_schemas = set(load_list_file(f'{base_dir}/regular_exclusive_schemas.txt'))
pro_paths = set(load_list_file(f'{base_dir}/pro_api_paths.txt'))
regular_paths = set(load_list_file(f'{base_dir}/regular_api_paths.txt'))

print(f"Loaded {len(shared_schemas)} shared schemas")
print(f"Loaded {len(pro_schemas)} pro exclusive schemas")
print(f"Loaded {len(regular_schemas)} regular exclusive schemas")
print(f"Loaded {len(pro_paths)} pro paths")
print(f"Loaded {len(regular_paths)} regular paths")

# Load the original OpenAPI spec
print("\nLoading original OpenAPI spec...")
with open(f'{base_dir}/openapi/nfl-com-api.yaml', 'r') as f:
    original_spec = yaml.safe_load(f)

print(f"Original spec has {len(original_spec.get('paths', {}))} paths")
print(f"Original spec has {len(original_spec.get('components', {}).get('schemas', {}))} schemas")

# Create output directory
output_dir = f'{base_dir}/openapi/refactored'
os.makedirs(output_dir, exist_ok=True)

# ============================================================================
# 1. Create nfl-shared.yaml - Only shared schemas
# ============================================================================
shared_spec = {
    'openapi': '3.0.3',
    'info': {
        'title': 'NFL Shared Schemas',
        'version': '1.0.0',
        'description': 'Shared schema definitions used by both NFL Regular API and NFL Pro API'
    },
    'components': {
        'schemas': {}
    }
}

# Extract shared schemas
all_schemas = original_spec.get('components', {}).get('schemas', {})
for schema_name in shared_schemas:
    if schema_name in all_schemas:
        shared_spec['components']['schemas'][schema_name] = all_schemas[schema_name]
    else:
        print(f"WARNING: Shared schema '{schema_name}' not found in original spec")

print(f"\nShared spec created with {len(shared_spec['components']['schemas'])} schemas")

# ============================================================================
# 2. Create nfl-pro-api.yaml - Pro API paths and schemas
# ============================================================================
pro_spec = {
    'openapi': '3.0.3',
    'info': {
        'title': 'NFL Pro API',
        'version': '1.0.0',
        'contact': {
            'name': 'NFL',
            'url': 'https://www.nfl.com'
        },
        'description': "NFL's Pro API for accessing advanced statistics, film room content, player data, and fantasy information. This API provides comprehensive access to NFL Pro features including Next Gen Stats, Film Room analysis, player projections, and game insights."
    },
    'servers': [
        {
            'url': 'https://pro.nfl.com',
            'description': 'Production NFL Pro API'
        }
    ],
    'security': original_spec.get('security', []),
    'tags': [],
    'paths': {},
    'components': {
        'schemas': {},
        'securitySchemes': original_spec.get('components', {}).get('securitySchemes', {})
    }
}

# Add Pro-specific tags
pro_tag_names = {
    'Betting', 'Content', 'Content Insights', 'Defensive Pass Rush Statistics',
    'Defensive Player Overview', 'Defensive Statistics', 'Fantasy Statistics',
    'Filmroom', 'Player Passing Statistics', 'Player Receiving Statistics',
    'Player Rushing Statistics', 'Players', 'Plays', 'Schedules',
    'Schedules Extended', 'Scores', 'Season Schedule', 'Secured Videos',
    'Stats', 'Team Defense Pass Statistics', 'Team Defense Rush Statistics',
    'Team Defense Statistics', 'Team Offense Overview Statistics',
    'Team Offense Pass Statistics', 'Teams', 'Win Probability'
}

for tag in original_spec.get('tags', []):
    if tag.get('name') in pro_tag_names:
        pro_spec['tags'].append(tag)

# Extract Pro API paths
all_paths = original_spec.get('paths', {})
for path in pro_paths:
    if path in all_paths:
        pro_spec['paths'][path] = all_paths[path]
    else:
        print(f"WARNING: Pro path '{path}' not found in original spec")

# Extract Pro-exclusive schemas and convert shared schema references
for schema_name in pro_schemas:
    if schema_name in all_schemas:
        pro_spec['components']['schemas'][schema_name] = all_schemas[schema_name]
    else:
        print(f"WARNING: Pro schema '{schema_name}' not found in original spec")

print(f"\nPro API spec created with {len(pro_spec['paths'])} paths and {len(pro_spec['components']['schemas'])} exclusive schemas")

# ============================================================================
# 3. Create nfl-regular-api.yaml - Regular API paths and schemas
# ============================================================================
regular_spec = {
    'openapi': '3.0.3',
    'info': {
        'title': 'NFL Regular API',
        'version': '1.0.0',
        'contact': {
            'name': 'NFL',
            'url': 'https://www.nfl.com'
        },
        'description': "NFL's public API for accessing game schedules, team information, standings, statistics, and venue data. This API provides comprehensive access to NFL data including real-time game information, team rosters, seasonal statistics, and historical data."
    },
    'servers': [
        {
            'url': 'https://api.nfl.com',
            'description': 'Production Regular NFL API'
        }
    ],
    'security': original_spec.get('security', []),
    'tags': [],
    'paths': {},
    'components': {
        'schemas': {},
        'securitySchemes': original_spec.get('components', {}).get('securitySchemes', {})
    }
}

# Add Regular-specific tags
regular_tag_names = {
    'Authentication', 'Experience', 'Football'
}

for tag in original_spec.get('tags', []):
    if tag.get('name') in regular_tag_names:
        regular_spec['tags'].append(tag)

# Extract Regular API paths
for path in regular_paths:
    if path in all_paths:
        regular_spec['paths'][path] = all_paths[path]
    else:
        print(f"WARNING: Regular path '{path}' not found in original spec")

# Extract Regular-exclusive schemas
for schema_name in regular_schemas:
    if schema_name in all_schemas:
        regular_spec['components']['schemas'][schema_name] = all_schemas[schema_name]
    else:
        print(f"WARNING: Regular schema '{schema_name}' not found in original spec")

print(f"\nRegular API spec created with {len(regular_spec['paths'])} paths and {len(regular_spec['components']['schemas'])} exclusive schemas")

# ============================================================================
# 4. Update schema references to use external shared file
# ============================================================================
def update_refs(obj, shared_schemas_set):
    """Recursively update $ref to point to external shared file where appropriate"""
    if isinstance(obj, dict):
        if '$ref' in obj:
            ref = obj['$ref']
            # Check if this is a schema reference
            if ref.startswith('#/components/schemas/'):
                schema_name = ref.split('/')[-1]
                # If it's a shared schema, update to external reference
                if schema_name in shared_schemas_set:
                    obj['$ref'] = f'./nfl-shared.yaml#/components/schemas/{schema_name}'
        else:
            for value in obj.values():
                update_refs(value, shared_schemas_set)
    elif isinstance(obj, list):
        for item in obj:
            update_refs(item, shared_schemas_set)

print("\nUpdating references to shared schemas...")
update_refs(pro_spec, shared_schemas)
update_refs(regular_spec, shared_schemas)

# ============================================================================
# 5. Write the three files
# ============================================================================
print("\nWriting output files...")

# Custom YAML dumper to preserve formatting
class CustomDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(CustomDumper, self).increase_indent(flow, False)

def write_yaml(filepath, data):
    with open(filepath, 'w') as f:
        yaml.dump(data, f, Dumper=CustomDumper, default_flow_style=False,
                  sort_keys=False, allow_unicode=True, width=1000)

write_yaml(f'{output_dir}/nfl-shared.yaml', shared_spec)
write_yaml(f'{output_dir}/nfl-pro-api.yaml', pro_spec)
write_yaml(f'{output_dir}/nfl-regular-api.yaml', regular_spec)

print(f"\nFiles written to {output_dir}/")

# ============================================================================
# 6. Generate summary
# ============================================================================
import os

def get_file_size(filepath):
    size_bytes = os.path.getsize(filepath)
    if size_bytes < 1024:
        return f"{size_bytes} bytes"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"

print("\n" + "="*80)
print("REFACTORING SUMMARY")
print("="*80)
print(f"\n1. nfl-shared.yaml")
print(f"   Location: {output_dir}/nfl-shared.yaml")
print(f"   Size: {get_file_size(f'{output_dir}/nfl-shared.yaml')}")
print(f"   Schemas: {len(shared_spec['components']['schemas'])}")
print(f"   Paths: 0 (schemas only)")

print(f"\n2. nfl-pro-api.yaml")
print(f"   Location: {output_dir}/nfl-pro-api.yaml")
print(f"   Size: {get_file_size(f'{output_dir}/nfl-pro-api.yaml')}")
print(f"   Paths: {len(pro_spec['paths'])}")
print(f"   Exclusive Schemas: {len(pro_spec['components']['schemas'])}")
print(f"   Tags: {len(pro_spec['tags'])}")
print(f"   Server: https://pro.nfl.com")

print(f"\n3. nfl-regular-api.yaml")
print(f"   Location: {output_dir}/nfl-regular-api.yaml")
print(f"   Size: {get_file_size(f'{output_dir}/nfl-regular-api.yaml')}")
print(f"   Paths: {len(regular_spec['paths'])}")
print(f"   Exclusive Schemas: {len(regular_spec['components']['schemas'])}")
print(f"   Tags: {len(regular_spec['tags'])}")
print(f"   Server: https://api.nfl.com")

print(f"\nTotal paths: {len(pro_spec['paths']) + len(regular_spec['paths'])}")
print(f"Total schemas: {len(shared_spec['components']['schemas'])} shared + "
      f"{len(pro_spec['components']['schemas'])} pro + "
      f"{len(regular_spec['components']['schemas'])} regular = "
      f"{len(shared_spec['components']['schemas']) + len(pro_spec['components']['schemas']) + len(regular_spec['components']['schemas'])}")

print("\n" + "="*80)
print("REFACTORING COMPLETE!")
print("="*80)
