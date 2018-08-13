# Kaivan Taylor
# Managed by Dev Team from Tomodachi Oniichans
# Pew Pew Pew Pew PEw PEw PEw PEwwwww pewdiepie

# --------------------------------------- module imports -------------------------------------------#

import oauth
import discord
import asyncio
import youtube_dl
from discord.ext import commands
from itertools import cycle

#------------------------------------- channel variables ------------------------------------------------#

client = commands.Bot(command_prefix = "!") # All prefix starts with "!"

GENERAL_CHANNEL = discord.Object(id='477697821512826900')

PLAYERS = []
QUEUES = []

#------------------------------------- extensions ------------------------------------------------#


startup_extensions = ["music_bot","commands"]

if __name__ == "__main__":
    for extension in startup_extensions:
        client.load_extension(extension)
    
#--------------------------------------- startup --------------------------------------------------#

@client.event # Used for boot of server
async def on_ready():
    print("Kai Bot is on the server!")
    print("\n"+ "-" * 100)
    await client.send_message(GENERAL_CHANNEL, "Kaerimasu. Kai Bot is online!")
    await client.change_presence(game = discord.Game(name = '!help'))

@client.event
async def on_error(event, *args, **kwargs):
    message = args[0] #Gets the message object
    logging.warning(traceback.format_exc()) #logs the error

#-------------------------------- client run --------------------------------#
client.run(oauth.TOKEN)
 
