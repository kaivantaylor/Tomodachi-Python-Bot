# Kai's Python Shit
# Managed by Dev Team from Tomodachi Oniichans
# Pew Pew Pew

import discord
import asyncio
import time
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
command = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Kai Bot is on the server!")

@client.event
async def on_message(msg):

    general_channel = discord.Object(id='471503386848788482')
    dev_channel = discord.Object(id='474468483749380096')

    if msg.content.upper().startswith('!SAY'):
        _saymsg = msg.content.split(" ")
        await client.send_message(general_channel," ".join(_saymsg[1:]))

    if msg.content.startswith('!ping'):
        userID = msg.author.id
        await client.send_message(general_channel, "<@" + userID + "> Pong!")
        
    if msg.content.startswith('!ching'):
        userID = msg.author.id
        await client.send_message(general_channel, "<@" + userID + "> Chong!")

    if msg.content.startswith('!tomato'):
        userID = msg.author.id
        await client.send_message(general_channel, "<@" + userID + "> tomato!")
    
    if msg.content == "!marty":
        await client.send_message(general_channel, "How's your garden today?")
    
    if msg.content == "!hlaing":
        await client.send_message(general_channel, "Such a fuckin weeb")

    if msg.content == "!elijsha":
        await client.send_message(general_channel, "Sup mah nigga")

    if msg.content == "!kaivan":
        await client.send_message(general_channel, "Plz work on me later")
        
    if msg.content == "!joke":
        await client.send_message(general_channel, "Marty is gay. Heh, get it.")
        
    if msg.content == "!github":
        await client.send_message(general_channel, "https://github.com/speedykai/Tomodachi-Python-Bot")
        
    if msg.content == "!dev":
        await client.send_message(general_channel, "! is the prefix for every command. Available commands: say, github")
        
    if msg.content == "!help":
        await client.send_message(general_channel, "! is the prefix for every command. Available commands: marty, hlaing, elijsha, kaivan, joke, ping, chong, tomato")

client.run("NDc0NDU4MTg3NDYzMDAwMDY0.DkQ3bA.f8mr9vy5Jh090JyW1hXsxqlg6B0")
 
