import asyncio
import discord
import random
from discord.ext import commands

GENERAL_CHANNEL = discord.Object(id='477697821512826900')

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
    
    @commands.command(pass_context = True)
    async def poyo(self, ctx):
        """Kirby is here to give some Poyos
        """
        channel = ctx.message.channel
        rand_num = random.randint(1,5)

        if rand_num == 1:
            image = './images/badkirbdab.png'
        elif rand_num == 2:
            image = './images/Minekirb.jpg'
        elif rand_num == 3:
            image = './images/thick.gif'
        elif rand_num == 4:
            image = './images/korb.gif'
        elif rand_num == 5:
            image = './images/KirbyStahps.PNG'
        elif rand_num == 6:
            image = './images/ImSorryKirbyPls.PNG'
        elif rand_num == 7:
            image = './images/HAAAAAa.PNG'
        else:
			print("Pika")
            image = './images/Pika.gif'
        
        await self.client.send_message(channel)
        await self.client.send_file(channel, image)
		
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
