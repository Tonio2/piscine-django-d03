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
if [ $? -eq 0 ]; then
    echo "path.py installed successfully."

    LOCAL_LIB_PATH=$(pwd)/local_lib
    # Check if LOCAL_LIB_PATH is already in PYTHONPATH
    if [[ ":$PYTHONPATH:" != *":$LOCAL_LIB_PATH:"* ]]; then
        export PYTHONPATH="$PYTHONPATH:$LOCAL_LIB_PATH"
    fi
    python3 program.py
else
    echo "Installation failed. Check install.log for details."
fi
