##@client.event # Used for specific message instances in server
##async def on_message(msg):
##
##    #-------- All users have these permissions below -------------#
##    
##    if msg.content.startswith('!ping'): # Ping
##        userID = msg.author.id
##        await client.send_message(channel, "<@" + userID + "> Pong!")
##        
##    if msg.content.startswith('!ching'): # Ching
##        userID = msg.author.id
##        await client.send_message(channel, "<@" + userID + "> Chong!")
##
##    if msg.content.startswith('!tomato'): # Tomato
##        userID = msg.author.id
##        await client.send_message(channel, "<@" + userID + "> tomato!")
##    
##    if msg.content == "!marty": # Marty
##        await client.send_message(channel, "How's your garden today?")
##    
##    if msg.content == "!hlaing": # Hlaing
##        await client.send_message(channel, "Such a fuckin weeb.")
##
##    if msg.content == "!elijsha": #Elijsha
##        await client.send_message(channel, "Sup mah nigga.")
##
##    if msg.content == "!kaivan": # Kaivan
##        await client.send_message(channel, "Plz work on me later.")
##        
##    if msg.content == "!devon": # Devon
##        await client.send_message(channel, "You play a lot of Mabinogi.")
##
##    if msg.content == "!amanda": # Amanda
##        await client.send_message(channel, "Is your name rose?")
##
##    if msg.content == "!lettuce": # Lettuce
##        await client.send_message(channel, "Why is a vegetable talking to me?")
##        
##    if msg.content == "!joke": # Joke
##        await client.send_message(channel, "Marty is gay. Heh, get it.")
##        
##    if msg.content == "!help": # Help
##        await client.send_message(channel, "! is the prefix for every command. Available commands: marty, hlaing, elijsha, kaivan, amanda, devon, lettuce, joke, ping, chong, tomato, dev")
##
##    #-------------- Developers only have these permissions below ---------------------#
##        
##    if msg.content == "!dev": # Dev
##        if '474507060940242955' in [role.id for role in msg.author.roles]:
##            await client.send_message(channel, "! is the prefix for every command. Available commands: say, github, nukebot")
##        else:
##            await client.send_message(channel, "Command for developers only.")
##
##    if msg.content == "!nukechat": # Dev
##        if '474507060940242955' in [role.id for role in msg.author.roles]:
##            await client.send_message(msg.channel, 'Clearing messages...')
##            async for msg in client.logs_from(msg.channel):
##                await client.delete_message(msg)
##        else:
##            await client.send_message(channel, "Command for developers only.")
##            
##    if msg.content == "!nukebot": # Dev
##        if '474507060940242955' in [role.id for role in msg.author.roles]:
##            await client.logout()
##            
##    if msg.content == "!github": # Github
##        if '474507060940242955' in [role.id for role in msg.author.roles]:
##            await client.send_message(channel, "https://github.com/speedykai/Tomodachi-Python-Bot")
##        else:
##            await client.send_message(channel, "Command for developers only.")
##
##    if msg.content.upper().startswith('!SAY'): # Say
##        if '474507060940242955' in [role.id for role in msg.author.roles]:
##            _saymsg = msg.content.split(" ")
##            await client.send_message(channel," ".join(_saymsg[1:]))
##        else:
##            await client.send_message(channel, "Command for developers only.")
##
##    #-------------------------------- Message filters ---------------------------------#
##            
##    contents = msg.content.split(" ") # Searches every word that is inputted
##    for word in contents:
##        if word.upper() in chat_filter:
##            try:
##                userID = msg.author.id  
##                await client.delete_message(msg)
##                await client.send_message(spam_channel, "<@" + userID + "> **Nani?! Yamete (Stop)** , that is a bad word!")
##            except discord.errors.NotFound:
##                return