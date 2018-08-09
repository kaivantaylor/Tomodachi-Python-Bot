# Kaivan Taylor
# Managed by Dev Team from Tomodachi Oniichans
# Pew Pew Pew Pew PEw PEw PEw PEwwwww pewdiepie

# --------------------------------------- module imports -------------------------------------------#

import discord
import asyncio
import youtube_dl
from discord.ext import commands
from itertools import cycle

#------------------------------------- channel variables ------------------------------------------------#

client = commands.Bot(command_prefix = "!") # All prefix starts with "!"

CHANNEL_MODE = 0 # Change value to switch channel output for bot txt. 0 - gen, 1 - spam, 2 - dev
TOKEN = "NDc0NDU4MTg3NDYzMDAwMDY0.DkQ3bA.f8mr9vy5Jh090JyW1hXsxqlg6B0"

GENERAL_CHANNEL = discord.Object(id='471503386848788482')
SPAM_CHANNEL = discord.Object(id='471509338834337803')
DEV_CHANNEL = discord.Object(id='474468483749380096')

PLAYERS = {}
QUEUES = {}
    
#------------------------------------ client event for startup -----------------------------------------------#

@client.event # Used for boot of server
async def on_ready():
    print("Kai Bot is on the server!")
    await client.send_message(DEV_CHANNEL, "Kaerimasu. Kai Bot is online!")
    await client.change_presence(game = discord.Game(name = '!bothelp'))

#------------------------------------ client command for music player -----------------------------------------------#

def check_queue(id):
    if QUEUES != []:
        player = QUEUES[id].pop(0)
        PLAYERS[id] = player
        player.start()
        
@client.command(pass_context = True)
async def summon(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context = True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context = True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))

    if PLAYERS == {}:
        PLAYERS[server.id] = player
        player.start()
    else:
        QUEUES[server.id] = player

@client.command(pass_context = True)
async def stop(ctx):
    id = ctx.message.server.id
    PLAYERS[id].stop()

@client.command(pass_context = True)
async def pause(ctx):
    id = ctx.message.server.id
    PLAYERS[id].pause()

@client.command(pass_context = True)
async def resume(ctx):
    id = ctx.message.server.id
    PLAYERS[id].resume()
    
#-------------------------------- client command for replies --------------------------------#
@client.command()
async def bothelp():
    await client.say('"!" is the prefix for all commands. Available Commands: ping, echo, musicbot')
    
@client.command()
async def musicbot():
    await client.say('Must be in a voice channel. Use !summon and !leave to move bot into channel. Available commands: play, stop, pause, resume, queue')

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
    await client.send_messsage(GENERAL_CHAT, output)

#-------------------------------- client run --------------------------------#
client.run(TOKEN)
 
