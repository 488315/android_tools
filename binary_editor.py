#!/usr/bin/env python3

"""
Android Tools - Binary Files Parser and Editor

A collection of utilities for parsing and editing binary files, including searching and replacing patterns. This script is inspired by AdrianDC's advanced_development_shell_tools.

Credits: https://github.com/AdrianDC/advanced_development_shell_tools/blob/master/sources/host/binary.rc
"""

import os
import re
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

def stringsgetall(file_path):
    """
    Run the 'strings' command based on host variants.
    """
    try:
        result = subprocess.run(['strings', '-accepteula'], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        if 'sysinternals' in result.stderr:
            return subprocess.run(['strings', '-a', '-accepteula', '-nobanner', file_path], capture_output=True, text=True).stdout
    except Exception:
        pass
    return subprocess.run(['strings', '-a', file_path], capture_output=True, text=True).stdout

def process_file(file_path, pattern, replacement=None):
    """
    Process a single file for searching or replacing the pattern.
    """
    try:
        strings_output = stringsgetall(file_path)
        matches = re.findall(pattern, strings_output)
        unique_matches = sorted(set(matches), reverse=True)

        if replacement:
            if unique_matches:
                print(f"   {file_path} : {unique_matches} ", end='')
                for old_string in unique_matches:
                    new_string = re.sub(pattern, replacement, old_string)

                    old_string_hex = old_string.encode().hex().upper() + '00'
                    new_string_hex = new_string.encode().hex().upper() + '00'

                    if len(new_string_hex) <= len(old_string_hex):
                        new_string_hex += '00' * (len(old_string_hex) - len(new_string_hex))

                        user_input = input(' [y/N] ')
                        if user_input.lower() == 'y':
                            with open(file_path, 'rb') as f:
                                file_content = f.read().hex().upper()
                            file_content = file_content.replace(old_string_hex, new_string_hex)
                            with open(f"{file_path}.tmp", 'wb') as f:
                                f.write(bytes.fromhex(file_content))
                            os.chmod(f"{file_path}.tmp", os.stat(file_path).st_mode)
                            os.replace(f"{file_path}.tmp", file_path)
                            print(" Done!")
                        else:
                            print(" Ignored.")
                    else:
                        print(" [N] String too long...")
            else:
                if replacement in strings_output:
                    print(f"   {file_path}: {replacement} Found.")
        else:
            if unique_matches:
                yellow = "\033[93m"
                reset = "\033[0m"
                matches_str = f"{yellow}{', '.join(unique_matches)}{reset}"
                print(f"   {file_path}: {matches_str}")

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def binaryeditor(pattern, files='.', replacement=None):
    """
    Binary files parser and editor.
    Usage: binaryeditor(pattern, [files], [replacement])
    """
    if not pattern:
        print("\n Usage: binaryeditor(pattern, [files], [replacement])\n")
        return

    pattern = pattern.replace('*', '.*').replace('.', '.')

    if replacement:
        print(f"\n === Replacing '{pattern}' with '{replacement}' in {files} ===\n")
    else:
        print(f"\n === Searching '{pattern}' in {files} ===\n")

    with ThreadPoolExecutor() as executor:
        for root, _, filenames in os.walk(files):
            if ".git" in root or ".repo" in root:
                continue

            for filename in filenames:
                file_path = Path(root) / filename
                if not file_path.is_file():
                    continue

                executor.submit(process_file, file_path, pattern, replacement)

def binarysearch(pattern, files='.'):
    """
    Binary files parser and searcher.
    Usage: binarysearch(pattern, [files])
    """
    if not pattern:
        print("\n Usage: binarysearch(pattern, [files])\n")
        return

    binaryeditor(pattern, files)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("\n Usage: binarysearch <pattern> [files] (Binary files parser and searcher)")
        print("        binaryeditor <pattern> [files] [replacement] (Binary files parser and editor)\n")
    elif sys.argv[1] == "binarysearch":
        binarysearch(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '.')
    elif sys.argv[1] == "binaryeditor":
        binaryeditor(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '.', sys.argv[4] if len(sys.argv) > 4 else None)
    else:
        print("\n Invalid command. Usage:")
        print("        binarysearch <pattern> [files] (Binary files parser and searcher)")
        print("        binaryeditor <pattern> [files] [replacement] (Binary files parser and editor)\n")
