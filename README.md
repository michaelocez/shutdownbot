# shutdownbot
A simple Discord bot to remotely shut down your PC by sending a command in Discord.

# Files Included

shutdownbot.py: The main Python script for the bot.

script.vbs: A VBScript file to run the bot executable silently at startup.

# Requirements
Python 3.12 or later

discord.py library

A Discord bot token

Your Discord user ID

# Setup

1. Clone the repository
`git clone https://github.com/michaelocez/shutdownbot.git`

2. Install dependencies
`pip install discord.py`

3. Create discord bot via Discord dev portal
Make sure MESSAGE CONTENT INTENT is enabled.

4. Configure python file
Open `shutdownbot.py` and replace 'YOUR_BOT_TOKEN' with your Discord bot token and 'YOUR_USER_ID' with your Discord user ID.

# Convert python file into executable

1. Install PyInstaller
pip install pyinstaller

2. Create executable
Navigate to the directory containing `shutdownbot.py` and run:
`pyinstaller --onefile shutdownbot.py`

# Start up script

1. Edit `script.vbs` to where you store your executable (`shutdownbot.exe`).

2. Move VBScript to Startup Folder
Using WIN + R and type in `shell:startup`, put `script.vbs` into the StartUp folder.

# Start the bot

1. Invite your bot to a private discord server.
2. Restart your computer to ensure the bot starts automatically.
3. In Discord, send '!shutdown' from your account to the bot. The bot should respond with PC Shutting down and initiate the shutdown process.


# Notes

Ensure your bot token and user ID are kept secure.

The bot should only respond to commands from the specified user ID to prevent unauthorized shutdowns.

The VBScript ensures the bot starts silently in the background without opening a command prompt window.
