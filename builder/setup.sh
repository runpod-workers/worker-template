#!/bin/bash

apt-get update
apt-get upgrade -y

# Install System Dependencies
apt-get install -y software-properties-common python3

apt-get autoremove -y
apt-get clean -y
rm -rf /var/lib/apt/lists/*
