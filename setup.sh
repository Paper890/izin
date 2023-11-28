#!/bin/bash

# Update package lists
sudo apt update

# Install Python and pip
sudo apt install -y python3 python3-pip

# Install required Python libraries
pip3 install python-telegram-bot PyGithub

# Clone repository
git clone https://github.com/Paper890/san.git

# Move to repository directory
cd your_repository

# Install any additional dependencies (if needed)
# ...

# Run the bot in the background
nohup python3 bot.py > bot.log 2>&1 &
 
chmod +x install_and_run.sh

./install_and_run.sh