# Kaivan Taylor
# Managed by Dev Team from Tomodachi Oniichans
# Pew Pew Pew

# --------------------------------------- module imports -------------------------------------------#

import discord
import asyncio
import time
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
command = commands.Bot(command_prefix = "!") # All prefix starts with "!"

#------------------------------------- channel variables ------------------------------------------------#

channel_mode = 3 # Change value to switch channel output for bot txt. 0 - gen, 1 - spam, 2 - dev

general_channel = discord.Object(id='471503386848788482')
spam_channel = discord.Object(id='471509338834337803')
dev_channel = discord.Object(id='474468483749380096')

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

@client.event # Used for specific message instances in server
async def on_message(msg):

    #-------- All users have these permissions below -------------#
    
    if msg.content.startswith('!ping'): # Ping
        userID = msg.author.id
        await client.send_message(channel, "<@" + userID + "> Pong!")
        
    if msg.content.startswith('!ching'): # Ching
        userID = msg.author.id
        await client.send_message(channel, "<@" + userID + "> Chong!")

    if msg.content.startswith('!tomato'): # Tomato
        userID = msg.author.id
        await client.send_message(channel, "<@" + userID + "> tomato!")
    
    if msg.content == "!marty": # Marty
        await client.send_message(channel, "How's your garden today?")
    
    if msg.content == "!hlaing": # Hlaing
        await client.send_message(channel, "Such a fuckin weeb")

    if msg.content == "!elijsha": #Elijsha
        await client.send_message(channel, "Sup mah nigga")

    if msg.content == "!kaivan": # Kaivan
        await client.send_message(channel, "Plz work on me later")

    if msg.content == "!lettuce": # Kaivan
        await client.send_message(channel, "Why is a vegetable talking to me?")
        
    if msg.content == "!joke": # Joke
        await client.send_message(channel, "Marty is gay. Heh, get it.")
        
    if msg.content == "!help": # Help
        await client.send_message(channel, "! is the prefix for every command. Available commands: marty, hlaing, elijsha, kaivan, lettuce, joke, ping, chong, tomato, dev")

    #-------------- Developers only have these permissions below ---------------------#
        
    if msg.content == "!dev": # Dev
        if '474507060940242955' in [role.id for role in msg.author.roles]:
            await client.send_message(channel, "! is the prefix for every command. Available commands: say, github")
        else:
            await client.send_message(channel, "Command for developers only.")
        
    if msg.content == "!github": # Github
        if '474507060940242955' in [role.id for role in msg.author.roles]:
            await client.send_message(channel, "https://github.com/speedykai/Tomodachi-Python-Bot")
        else:
            await client.send_message(channel, "Command for developers only.")

    if msg.content.upper().startswith('!SAY'): # Say
        if '474507060940242955' in [role.id for role in msg.author.roles]:
            _saymsg = msg.content.split(" ")
            await client.send_message(channel," ".join(_saymsg[1:]))
        else:
            await client.send_message(channel, "Command for developers only.")
            
#-------------------------------- Client Run --------------------------------#

client.run("NDc0NDU4MTg3NDYzMDAwMDY0.DkQ3bA.f8mr9vy5Jh090JyW1hXsxqlg6B0")
 
