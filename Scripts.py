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
    if msg.content == "!marty":
        await client.send_message(msg.channel, "How's your garden today?")
    
    if msg.content == "!hlaing":
        await client.send_message(msg.channel, "Such a fuckin weeb")

    if msg.content == "!elijsha":
        await client.send_message(msg.channel, "Sup mah nigga")

    if msg.content == "!kaivan":
        await client.send_message(msg.channel, "Plz work on me later")
        
    if msg.content == "!github":
        await client.send_message(msg.channel, "https://github.com/speedykai/Tomodachi-Python-Bot")
        
    if msg.content == "!help":
        await client.send_message(msg.channel, "! is the prefix for every command. Available options: marty, hlaing, elijsha, kaivan, github")

client.run("NDc0NDU4MTg3NDYzMDAwMDY0.DkQ3bA.f8mr9vy5Jh090JyW1hXsxqlg6B0")
