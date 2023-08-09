# Flutter Local Packages Upgrader

This tool automates the process of upgrading the major versions of local Flutter packages, considering their interdependencies.

## Description

When dealing with multiple local Flutter packages that depend on each other, it's essential to upgrade them in a specific order to maintain compatibility. This script identifies the right order to upgrade these packages and then performs the upgrade using the `flutter pub upgrade --major-versions` command.

### Features

- Discovers all local Flutter packages in the current directory and subdirectories.
- Determines the interdependencies between the discovered local packages.
- Upgrades the packages in the correct order, based on their interdependencies.

## Requirements

- Python 3
- PyYAML: Install using `pip install pyyaml`
- Flutter SDK: Ensure that `flutter` command is accessible from the terminal.

## Usage

1. Navigate to the root directory containing your local Flutter packages.
2. Run the script: `python path_to_script.py`

## Warning

Before running the script, make sure to:

- Backup all your `pubspec.yaml` files, as the script will modify them.
- Check the status of your version control (like git) to ensure you can roll back changes if necessary.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
