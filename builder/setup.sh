#!/bin/bash

# Update System
apt-get update && apt-get upgrade -y


# Install System Dependencies
# - openssh-server: for ssh access and web terminal
apt-get install -y software-properties-common openssh-server

# Install Python 3.10
add-apt-repository ppa:deadsnakes/ppa -y
apt-get update && apt-get install -y python3.10 python3.10-dev python3.10-distutils python3.10-pip


# Clean up
apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*
