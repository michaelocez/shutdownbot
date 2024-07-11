import discord
import os

TOKEN = 'YOUR_BOT_TOKEN' # Replace 'YOUR_BOT_TOKEN' with your bot's token
USER_ID = 'YOUR_USER_ID'  # Replace 'YOUR_USER_ID' with your user ID

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.wait_until_ready()
    print(f'Bot is ready. Logged in as {client.user}')

@client.event
async def on_message(message):

    if message.author.id != USER_ID:
        return

    command = message.content.strip()
    print(f"Received command: '{command}'") 
    if command == '!shutdown':
        await message.channel.send('PC Shutting down')
        os.system('shutdown /s /t 1')

client.run(TOKEN)
