import asyncio
import discord
from discord.ext import commands

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')
    
def setup(client):
    client.add_cog(commands(client))
    print("Commands loaded")

def __init__(self, client):
        self.client = client
class commands:
    pass
