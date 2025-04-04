#!/bin/bash
# Script to convert MkDocs documentation to Word and PDF formats

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is required but not installed."
    exit 1
fi

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "Error: pandoc is required but not installed."
    echo "Please install pandoc:"
    echo "  - Ubuntu/Debian: sudo apt-get install pandoc"
    echo "  - macOS: brew install pandoc"
    echo "  - Windows: choco install pandoc"
    exit 1
fi

# Function to check if a package is installed
function is_package_installed() {
    pip3 list | grep -i "$1" &> /dev/null
    return $?
}

# Check if required Python packages are installed
echo "Checking required Python packages..."
MISSING_PACKAGES=()

if ! is_package_installed "pypandoc"; then
    MISSING_PACKAGES+=("pypandoc")
fi

# Install missing packages if any
if [ ${#MISSING_PACKAGES[@]} -gt 0 ]; then
    echo "Installing missing packages: ${MISSING_PACKAGES[*]}"
    pip3 install "${MISSING_PACKAGES[@]}"
fi

# Run the conversion script
echo "Starting conversion process..."
python3 $(dirname "$0")/convert_to_docs.py

# Check if conversion was successful
if [ $? -eq 0 ]; then
    echo -e "\nConversion completed successfully!"
    echo "Word documents are available in the 'exports/word' directory."
    echo "PDF documents are available in the 'exports/pdf' directory."
else
    echo -e "\nConversion failed. Please check the error messages above."
    exit 1
fi
