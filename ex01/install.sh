#!/bin/bash

# Print pip version
echo "Current pip version:"
pip --version

# Create the local_lib directory if it doesn't exist
mkdir -p local_lib

# Install/Update path.py from GitHub to local_lib
echo "Installing path.py..."
pip install --upgrade --target=./local_lib --log install.log git+https://github.com/jaraco/path.py.git

# Check if path.py is installed correctly
if [ -d "./local_lib/path" ]; then
    echo "path.py installed successfully."
    # Execute the Python program
    python3 program.py
else
    echo "Installation failed. Check install.log for details."
fi
