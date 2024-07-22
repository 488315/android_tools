#!/bin/bash

# Usage function
usage() {
    echo ""
    echo " Usage: binarysearch <pattern> [files]"
    echo "        binaryeditor <pattern> [files] [replacement]"
    echo ""
    exit 1
}

# Check if Python script exists
if [ ! -f "/home/kjones/bin/binary_editor.py" ]; then
    echo "Error: binary_editor.py not found!"
    exit 1
fi

# Determine the command based on the invoked script name
COMMAND=$(basename "$0")

# Ensure at least one argument is provided
if [ "$#" -lt 1 ]; then
    usage
fi

PATTERN=$1
FILES=${2:-.}
REPLACEMENT=$3

# Run the Python script with the provided arguments
if [ "$COMMAND" == "binarysearch" ]; then
    python3 /home/kjones/bin/binary_editor.py binarysearch "$PATTERN" "$FILES"
elif [ "$COMMAND" == "binaryeditor" ]; then
    python3 /home/kjones/bin/binary_editor.py binaryeditor "$PATTERN" "$FILES" "$REPLACEMENT"
else
    usage
fi
