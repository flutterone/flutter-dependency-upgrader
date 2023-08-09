# Flutter Local Packages Processor

This tool provides automation for processing dependencies in local Flutter packages, considering their interdependencies.

## Description

Flutter projects with multiple local packages can have interdependencies, making it crucial to process them in the right order to maintain compatibility. This script identifies the correct order to process these packages, using either `flutter pub get` or `flutter pub upgrade --major-versions`.

### Features

- Discovers all local Flutter packages in the current directory and subdirectories, excluding directories that start with a dot (like `.dart_tool`).
- Determines the interdependencies between the discovered local packages.
- Processes the packages in the correct order based on their interdependencies using either `flutter pub get` or `flutter pub upgrade --major-versions`.

## Requirements

- Python 3
- PyYAML: Install using `pip install pyyaml`
- Flutter SDK: Ensure the `flutter` command is accessible from the terminal.

## Usage

1. Navigate to the root directory containing your local Flutter packages.
2. Run the script with the desired command:
   - For upgrading: `python packages_processor.py --command upgrade`
   - For fetching dependencies: `packages_processor.py --command get`

## Warning

Before running the script, ensure the following:

- Backup all your `pubspec.yaml` files, as the script will modify them.
- Check the status of your version control (like git) to ensure you can roll back changes if necessary.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
