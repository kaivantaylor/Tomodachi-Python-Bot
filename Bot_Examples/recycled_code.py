# Old code that has been recycled from other files.

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
        await client.send_message(channel, "Such a fuckin weeb.")

    if msg.content == "!elijsha": #Elijsha
        await client.send_message(channel, "Sup mah nigga.")

    if msg.content == "!kaivan": # Kaivan
        await client.send_message(channel, "Plz work on me later.")
        
    if msg.content == "!devon": # Devon
        await client.send_message(channel, "You play a lot of Mabinogi.")

    if msg.content == "!amanda": # Amanda
        await client.send_message(channel, "Is your name rose?")

    if msg.content == "!lettuce": # Lettuce
        await client.send_message(channel, "Why is a vegetable talking to me?")
        
    if msg.content == "!joke": # Joke
        await client.send_message(channel, "Marty is gay. Heh, get it.")
        
    if msg.content == "!help": # Help
        await client.send_message(channel, "! is the prefix for every command. Available commands: marty, hlaing, elijsha, kaivan, amanda, devon, lettuce, joke, ping, chong, tomato, dev")

    #-------------- Developers only have these permissions below ---------------------#
        
    if msg.content == "!dev": # Dev
        if '474507060940242955' in [role.id for role in msg.author.roles]:
            await client.send_message(channel, "! is the prefix for every command. Available commands: say, github, nukebot")
        else:
            await client.send_message(channel, "Command for developers only.")

    if msg.content == "!nukechat": # Dev
        if '474507060940242955' in [role.id for role in msg.author.roles]:
            await client.send_message(msg.channel, 'Clearing messages...')
            async for msg in client.logs_from(msg.channel):
                await client.delete_message(msg)
        else:
            await client.send_message(channel, "Command for developers only.")
            
    if msg.content == "!nukebot": # Dev
        if '474507060940242955' in [role.id for role in msg.author.roles]:
            await client.logout()
            
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

    #-------------------------------- Message filters ---------------------------------#
            
    contents = msg.content.split(" ") # Searches every word that is inputted
    for word in contents:
        if word.upper() in chat_filter:
            try:
                userID = msg.author.id  
                await client.delete_message(msg)
                await client.send_message(spam_channel, "<@" + userID + "> **Nani?! Yamete (Stop)** , that is a bad word!")
            except discord.errors.NotFound:
                return


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
