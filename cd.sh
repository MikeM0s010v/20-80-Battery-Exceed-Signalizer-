#!/bin/bash
# Do not forget to make this script executable with chmod 755 cd.sh

# Change directory to YOUR venv
echo "Executing a bash command"
cd /path/to/venv

# Check
pwd
echo $$

# Running py-file
python alert.py
