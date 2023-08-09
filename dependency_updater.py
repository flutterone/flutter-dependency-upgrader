import os
import yaml

# Function to extract local dependencies from a pubspec.yaml file.
# Returns a dictionary mapping package names to their local paths.
def get_local_dependencies(pubspec_path):
    with open(pubspec_path, 'r') as file:
        data = yaml.safe_load(file)

    dependencies = data.get('dependencies', {})
    return {name: dep['path'] for name, dep in dependencies.items() if isinstance(dep, dict) and 'path' in dep}

# Function to order packages based on their dependencies.
# Returns an ordered list of package paths, where each package can be safely upgraded 
# after all its preceding packages in the list.
def order_by_dependencies(packages):
    ordered = []
    unprocessed = set(packages.keys())

    while unprocessed:
        for package, path in list(packages.items()):
            if package in unprocessed:
                deps = get_local_dependencies(path)
                if not set(deps.values()).intersection(unprocessed):
                    ordered.append((package, path))
                    unprocessed.remove(package)
    return ordered

# Main script logic

# First, find all local packages and their respective pubspec.yaml paths
packages = {}
for root, dirs, files in os.walk('.'):
    if 'pubspec.yaml' in files:
        full_path = os.path.join(root, 'pubspec.yaml')
        with open(full_path, 'r') as file:
            data = yaml.safe_load(file)
            if 'name' in data:
                packages[data['name']] = full_path

# Order the packages based on dependencies
ordered_packages = order_by_dependencies(packages)

# Perform the upgrade on each package in the correct order
for package, path in ordered_packages:
    dir_path = os.path.dirname(path)
    print(f"Updating {package} in {dir_path}")
    os.system(f"cd {dir_path} && flutter pub upgrade --major-versions")

print("All packages updated!")
