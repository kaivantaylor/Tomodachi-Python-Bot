# Kaivan Taylor
# Managed by Dev Team from Tomodachi Oniichans
# Pew Pew Pew Pew PEw PEw PEw PEwwwww pewdiepie

# --------------------------------------- module imports -------------------------------------------#

import discord
import asyncio
import time
import youtube_dl
from discord.ext import commands

client = commands.Bot(command_prefix = "!") # All prefix starts with "!"

#------------------------------------- channel variables ------------------------------------------------#

channel_mode = 9 # Change value to switch channel output for bot txt. 0 - gen, 1 - spam, 2 - dev
token = "NDc0NDU4MTg3NDYzMDAwMDY0.DkQ3bA.f8mr9vy5Jh090JyW1hXsxqlg6B0"

general_channel = discord.Object(id='471503386848788482')
spam_channel = discord.Object(id='471509338834337803')
dev_channel = discord.Object(id='474468483749380096')

players = {}

#------------------------------------ client events -----------------------------------------------#

if channel_mode == 0:
    channel = general_channel
elif channel_mode == 1:
    channel = spam_channel
else:
    channel = dev_channel

@client.event # Used for boot of server
async def on_ready():
    print("Kai Bot is on the server!")
    await client.send_message(dev_channel, "Kaerimasu. Kai Bot is online!")

@client.command(pass_context = True)
async def join(ctx):
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
    player = await voice_client.create_ytdl_player(url)
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
    
#-------------------------------- Client Run --------------------------------#

client.run(token)
 
