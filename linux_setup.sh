#!/bin/bash

if [ ! -x "$0" ]; then
    chmod +x "$0"
    exec "$0"
fi

echo "=== NGG Project Setup ==="

if command -v apt &>/dev/null; then
    echo "Installing 'tkinter'..."
    sudo apt update
    sudo apt install -y python3-tk
fi

echo "Installing 'numpy'..."
pip3 install numpy

echo "=== Setup Complete ==="
read -p "Press Enter to proceed, have a nice number-guessing!"

rm -- "$0"
