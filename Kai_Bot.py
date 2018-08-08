# Kaivan Taylor
# Managed by Dev Team from Tomodachi Oniichans
# Pew Pew Pew Pew PEw PEw PEw PEwwwww pewdiepie

# --------------------------------------- module imports -------------------------------------------#

import discord
import asyncio
import time
import youtube_dl
from discord.ext import commands

#------------------------------------- channel variables ------------------------------------------------#

client = commands.Bot(command_prefix = "!") # All prefix starts with "!"

channel_mode = 0 # Change value to switch channel output for bot txt. 0 - gen, 1 - spam, 2 - dev
token = "NDc0NDU4MTg3NDYzMDAwMDY0.DkQ3bA.f8mr9vy5Jh090JyW1hXsxqlg6B0"

general_channel = discord.Object(id='471503386848788482')
spam_channel = discord.Object(id='471509338834337803')
dev_channel = discord.Object(id='474468483749380096')

players = {}
queues = {}

def check_queues(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()
    
#------------------------------------ client event for startup -----------------------------------------------#

@client.event # Used for boot of server
async def on_ready():
    print("Kai Bot is on the server!")
    await client.send_message(dev_channel, "Kaerimasu. Kai Bot is online!")

#------------------------------------ client command for music player -----------------------------------------------#

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
    players[server.id] = player
    player.start()

@client.command(pass_context = True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context = True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context = True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context = True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await client.say('Video queued.')
    
    
#-------------------------------- client command for replies --------------------------------#
@client.command()
async def help():
    await client.say('"!" is the prefix for all commands. Available Commands: ping, echo, musicbot')
    
@client.command()
async def musicbot():
    await client.say('Must be in a voice channel. Use !summon and !leave to move bot into channel. Available commands: play, stop, pause, resume, queue')

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

#-------------------------------- client run --------------------------------#
client.run(token)
 
