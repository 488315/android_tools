
# Android Tools

A collection of tools to assist Android development, including resource comparison and extraction utilities. This repository aims to simplify and streamline various aspects of Android development by providing scripts and tools that automate common tasks.

## Features

- Extract resources from APK files using apktool
- Compare AOSP resources with APK resources
- Generate formatted configuration XML files
- Supports handling of non-overlayable resources

## Requirements

- Python 3.6+
- [apktool](https://github.com/iBotPeaches/Apktool)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/android_tools.git
    cd android_tools
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure apktool is installed and accessible from your PATH:**
    ```bash
    # Example for installing apktool on Ubuntu
    sudo apt-get update
    sudo apt-get install apktool
    ```

## Usage

### Extracting APK Resources

The `extract_apk_resources` function extracts resources from an APK file using apktool.

**Example:**
```bash
/home/$USER/bin/extract_apk_resources /path/to/your.apk /path/to/output/directory
```
### Comparing Resources
The compare_resources function compares resources between AOSP and APK, returning differences that are not default values.
### Example:
```bash
/home/$USER/bin/compare_resources --apk_dir /romdumps/SAMFW.COM_SM-X710_XAR_X710XXS3BXE1_fac/system/system/framework/framework-res.apk --source_dir /home/$USER/android/lineageos/frameworks/base/core/res
```
### Generating Config XML
The inject_comments_and_fix_quotes function generates a config.xml file with the differences, injecting comments from the AOSP XML files and fixing quotes.
### Example:

```bash
/home/$USER/bin/inject_comments_and_fix_quotes /path/to/differences /path/to/config.xml /path/to/aosp/resources
```
### Command-Line Interface
You can use the provided command-line interface to perform these tasks directly from the terminal.
## Example:

```bash
/home/$USER/bin/compare_resources --apk_dir /path/to/your.apk --source_dir /path/to/aosp/resources
```
### Contributing
We welcome contributions to this repository. If you have an idea for a new feature or have found a bug, please open an issue or submit a pull request.

#### Steps to Contribute:
- Fork the repository
- Create a new branch
```bash
git checkout -b feature/your-feature-name
```
- Make your changes
- Commit your changes
``` bash
git commit -m "Add some feature"
```
- Push to the branch
```bash
git push origin feature/your-feature-name
```
- Open a pull request
### License
This project is licensed under the Apache License, Version 2.0. See the LICENSE file for details.
