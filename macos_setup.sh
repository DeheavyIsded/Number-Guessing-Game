#!/bin/bash

echo "=== NGG Project Setup for MacOS ==="

if command -v brew &>/dev/null; then
    echo "Installing 'tkinter'..."
    brew install python-tk
else
    echo "Homebrew not found, install tkinter manually."
fi

echo "Installing 'numpy'..."
pip3 install numpy

echo "=== Setup Complete ==="
read -p "You can close this window now"

rm -- "$0"
