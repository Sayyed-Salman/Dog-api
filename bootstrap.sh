#!/bin/bash

# Update package index
sudo apt-get update

# Install required dependencies
sudo apt-get install -y build-essential libssl-dev libffi-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev

# Download Python 3.9
wget https://www.python.org/ftp/python/3.9.9/Python-3.9.9.tgz

# Extract the archive
tar -xf Python-3.9.9.tgz

# Navigate to the Python directory
cd Python-3.9.9

# Configure the installation
./configure --enable-optimizations

# Build and install Python
make -j8
sudo make altinstall

# Clean up
cd ..
rm -rf Python-3.9.9*
