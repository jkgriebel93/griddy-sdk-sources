import yaml
import sys
from pathlib import Path


def add_servers_to_endpoints(openapi_file):
    """Add appropriate servers to each endpoint based on path pattern."""

    # Load the OpenAPI spec
    with open(openapi_file, 'r') as f:
        spec = yaml.safe_load(f)

    # Define server configurations
    pro_server = [{
        'url': 'https://pro.nfl.com',
        'description': 'Production NFL Pro API'
    }]

    regular_server = [{
        'url': 'https://api.nfl.com',
        'description': 'Production Regular NFL API'
    }]

    # Track changes
    pro_count = 0
    regular_count = 0

    # Iterate through all paths and operations
    for path, path_item in spec.get('paths', {}).items():
        # Determine which server based on path pattern
        if path.startswith('/api/'):
            server_config = pro_server
            pro_count += 1
        else:
            server_config = regular_server
            regular_count += 1

        # Add servers to each operation in this path
        for method in ['get', 'post', 'put', 'patch', 'delete', 'options', 'head', 'trace']:
            if method in path_item:
                path_item[method]['servers'] = server_config

    # Write back to file
    output_file = openapi_file.replace('.yaml', '.modified.yaml')
    with open(output_file, 'w') as f:
        yaml.dump(spec, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"✓ Modified OpenAPI spec written to: {output_file}")
    print(f"  - Pro API endpoints (/api/*): {pro_count}")
    print(f"  - Regular API endpoints (other): {regular_count}")
    print(f"\nTotal endpoints processed: {pro_count + regular_count}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_servers.py <openapi-file.yaml>")
        sys.exit(1)

    openapi_file = sys.argv[1]

    if not Path(openapi_file).exists():
        print(f"Error: File '{openapi_file}' not found")
        sys.exit(1)

    add_servers_to_endpoints(openapi_file)