# Kai's Python Shit
# Managed by Dev Team from Tomodachi Oniichans
# Pew Pew Pew

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

client = discord.Client()
command = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(msg):

    general_server = discord.Object(id='471503386848788482')

    if msg.content.upper().startswith('!SAY'):
        _saymsg = msg.content.split(" ")
        await client.send_message(general_server," ".join(_saymsg[1:]))

    if msg.content.startswith('!ping'):
        userID = msg.author.id
        await client.send_message(general_server, "<@" + userID + "> Pong!")
        
    if msg.content.startswith('!ching'):
        userID = msg.author.id
        await client.send_message(general_server, "<@" + userID + "> Chong!")

    if msg.content.startswith('!tomato'):
        userID = msg.author.id
        await client.send_message(general_server, "<@" + userID + "> tomato!")
    
    if msg.content == "!marty":
        await client.send_message(general_server, "How's your garden today?")
    
    if msg.content == "!hlaing":
        await client.send_message(general_server, "Such a fuckin weeb")

    if msg.content == "!elijsha":
        await client.send_message(general_server, "Sup mah nigga")

    if msg.content == "!kaivan":
        await client.send_message(general_server, "Plz work on me later")
        
    if msg.content == "!joke":
        await client.send_message(general_server, "Marty is gay. Heh, get it.")
        
    if msg.content == "!github":
        await client.send_message(general_server, "https://github.com/speedykai/Tomodachi-Python-Bot")
        
    if msg.content == "!help":
        await client.send_message(general_server, "! is the prefix for every command. Available options: marty, hlaing, elijsha, kaivan, joke, github, ping, chong, tomato")

client.run("NDc0NDU4MTg3NDYzMDAwMDY0.DkQ3bA.f8mr9vy5Jh090JyW1hXsxqlg6B0")
 
