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
TOKEN = "NDc2NjMwNjAwODEyNDYyMDgw.DkwYkQ._EWfSmLXvVno1fOrfyrOKNR1XFo"

GENERAL_CHANNEL = discord.Object(id='471503386848788482')
SPAM_CHANNEL = discord.Object(id='471509338834337803')
DEV_CHANNEL = discord.Object(id='474468483749380096')

STATUS = ['!bothelp','!musicbot','<3']

PLAYERS = {}
QUEUES = {}
    
#------------------------------------ client event for startup -----------------------------------------------#
@client.event
async def change_status():
    await client.wait_until_ready()
    msgs = cycle(STATUS)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game = discord.Game(name = current_status))
        await asyncio.sleep(5)

@client.event # Used for boot of server
async def on_ready():
    print("Kouhai is on the server!")
    await client.send_message(DEV_CHANNEL, "Osuuu. Kouhai is online!")

#------------------------------------ client command for music player -----------------------------------------------#

def check_queues(id):
    if QUEUES[id] != []:
        PLAYERS[id] = player
        player = QUEUES[id].pop(0)
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
    player.start()
    PLAYERS[server.id] = player

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

    if server.id in QUEUES:
        QUEUES[server.id].append(player)
    else:
        QUEUES[server.id] = [player]
    await client.say('Video queued.')

    print(QUEUE)
    
    
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
    await client.say(output)

#-------------------------------- client run --------------------------------#
client.loop.create_task(change_status())
client.run(TOKEN)
 
