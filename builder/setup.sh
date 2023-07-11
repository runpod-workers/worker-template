#!/bin/bash

# Stop script on error
set -e

# Update System
apt-get update && apt-get upgrade -y

# Install System Dependencies
# - openssh-server: for ssh access and web terminal
apt-get install -y --no-install-recommends software-properties-common

# Install Python 3.10
add-apt-repository ppa:deadsnakes/ppa -y
apt-get update && apt-get install -y --no-install-recommends python3.10 python3.10-dev python3.10-distutils python3.10-pip
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

# Clean up
apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*
