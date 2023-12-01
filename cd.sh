#!/bin/bash
# Do not forget to make script executable

# Change directory to YOUR venv
echo "Executing a bash command"
cd /home/mike/venv

# Check
pwd
echo $$

# run script
python alert.py
