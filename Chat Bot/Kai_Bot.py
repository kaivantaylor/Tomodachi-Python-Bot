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
TOKEN = "NDc0NDU4MTg3NDYzMDAwMDY0.Dk4ftw.y60mWF0DZ5X4i2otX5onAEAc5GU"

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
    await client.change_presence(game = discord.Game(name = '!bothelp'))

@client.event
async def on_error(event, *args, **kwargs):
    message = args[0] #Gets the message object
    logging.warning(traceback.format_exc()) #logs the error
    
#---------------------------------------- music player --------------------------------------------------#

def check_queue(id):
    player = QUEUES.pop(0)
    PLAYERS = player
    player.start()
    PLAYERS.pop(0)
        
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
async def volume(ctx, volume):
    if PLAYERS != []:
        volume = int(volume)
        player = PLAYERS[0]
        player.volume = volume / 100
        await client.say('Set the volume to {}%'.format(volume))
    
@client.command(pass_context = True)
async def play(ctx, url):
    opts =  {
            'default_search': 'auto',
            'quiet': True,
            }
    try:
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, ytdl_options=opts, after = lambda:check_queue(server.id))

        if PLAYERS == []:
            PLAYERS.append(player)
            player.start()
        else:
            QUEUES.append(player)
            
    except Exception as e:
        print("Not a valid link.")

@client.command(pass_context = True)
async def stop(ctx):
    if PLAYERS != []:
        player = PLAYERS[0]
        player.stop()
    else:
        pass
@client.command(pass_context = True)
async def pause(ctx):
    if PLAYERS != []:
        player = PLAYERS[0]
        player.pause()
@client.command(pass_context = True)
async def resume(ctx):
    if PLAYERS != []:
        player = PLAYERS[0]
        player.resume()

@client.command(pass_context = True)
async def skip(ctx):
    channel = ctx.message.channel
    try:
        player = PLAYERS[0]
        player.stop()
        PLAYERS.pop(0)
        
        new_player = QUEUES.pop(0)
        PLAYERS.append(new_player)

        player = PLAYERS[0]
        player.start()
    except Exception as e:
        print("No song in queue.")
        await client.send_message(channel, "No song in queue.")
    
#--------------------------------------------------- commands ---------------------------------------------------------#

@client.command()
async def bothelp():
    await client.say('"!" is the prefix for all commands. Available Commands: ping, echo, musicbot, logout.')
    
@client.command()
async def musicbot():
    await client.say(
'''Must be in a voice channel. Use !summon and !leave to move bot into channel.
Available commands: play, stop, pause, resume, queue, skip, volume.
''')

@client.command(pass_context = True)
async def logout(ctx):
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
    await client.send_messsage(GENERAL_CHAT, output)

#-------------------------------- client run --------------------------------#
client.run(TOKEN)
 
