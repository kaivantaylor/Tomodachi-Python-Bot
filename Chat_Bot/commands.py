import asyncio
import discord
from discord.ext import commands

def setup(client):
    client.add_cog(Commands(client))
    print("Commands loaded!")

def __init__(self, client):
    self.client = client
    
class Commands:
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def logout(self):
        """Forces Kai Bot to logout of the server."""
        await self.client.logout()

    @commands.command(pass_context = True)
    async def clear(self, ctx, amount = 10):
        """Clears out messages.
        Use !clear [number of messages to delete].
        """
        channel = ctx.message.channel
        messages = []
        async for message in self.client.logs_from(channel, limit = int(amount)):
                messages.append(message)
        await self.client.delete_messages(messages)

    @commands.command()
    async def ping(self):
        """Give a "Pong!" back to the user."""
        await self.client.say('Pong!')

    @commands.command()
    async def echo(self, *args):
        """Repeats a message to the user.
        Use !echo [message].
        """
        output = ''
        for word in args:
                output += word
                output += ' '
        await self.client.send_message(GENERAL_CHANNEL, output)


