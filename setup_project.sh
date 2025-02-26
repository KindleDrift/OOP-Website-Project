#!/bin/bash

echo "Setting up the Python project using virtualenv..."

# Install virtualenv if not installed
if ! command -v virtualenv &> /dev/null; then
    echo "virtualenv not found, installing..."
    pip install --user virtualenv
fi

# Create virtual environment using virtualenv
virtualenv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "Setup complete! Run 'source venv/bin/activate' to activate the environment."