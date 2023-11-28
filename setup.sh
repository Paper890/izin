#!/bin/bash

# Step 1: Install Python
sudo apt-get update
sudo apt-get install -y python3

# Step 2: Clone GitHub Repository
git clone https://github.com/Paper890/izin.git

# Step 3: Navigate to Repository Directory
cd izin

# Step 4: Install Python Dependencies
pip install -r requirements.txt

# Step 5: Set Environment Variables
export GITHUB_TOKEN=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

# Step 6: Run Python Script
python bot.py
