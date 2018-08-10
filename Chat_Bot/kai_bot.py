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

CHANNEL_MODE = 0 # Change value to switch channel output for bot txt. 0 - gen, 1 - spam, 2 - dev

GENERAL_CHANNEL = discord.Object(id='471503386848788482')
SPAM_CHANNEL = discord.Object(id='471509338834337803')
DEV_CHANNEL = discord.Object(id='474468483749380096')

PLAYERS = []
QUEUES = []
    
#--------------------------------------- startup --------------------------------------------------#

@client.event # Used for boot of server
async def on_ready():
    print("Kai Bot is on the server!")
    await client.send_message(DEV_CHANNEL, "Kaerimasu. Kai Bot is online!")
    await client.change_presence(game = discord.Game(name = '!help'))

@client.event
async def on_error(event, *args, **kwargs):
    message = args[0] #Gets the message object
    logging.warning(traceback.format_exc()) #logs the error
    
#---------------------------------------- music player --------------------------------------------------#

startup_extensions = ["music_bot"]

if __name__ == "__main__":
    for extension in startup_extensions:
        client.load_extension(extension)
    
#--------------------------------------------------- commands ---------------------------------------------------------#
        
@client.command()
async def logout():
    await client.logout()

@client.command(pass_context = True)
async def clear(ctx, amount = 10):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit = int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    
@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.send_message(GENERAL_CHANNEL, output)

#-------------------------------- client run --------------------------------#
client.run(oauth.TOKEN)
 
