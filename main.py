import discord
from discord.ext import commands


TOKEN = "NDQ5MDMwNzg1MzQ5OTc2MDgx.DyLe8Q.1JRskKgix9NbtElqc9FY417LHWk" # Bot Token
client = commands.Bot(command_prefix='.')
key_holder = "Bryngle"
holder_id = ""
people_in_room = []


@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="Making a bot"))

@client.command(pass_context = True)
async def key(msg):
    global key_holder
    global holder_id

    if(msg.message.content == ".key get"):
        usr = msg.message.author.mention
        key_holder = usr
        holder_id = msg.message.author.id
        await client.say('%s now holds the key.' % usr)

    elif(msg.message.content == ".key bryngle " or msg.message.content == ".key Bryngle "):
        key_holder= "Bryngle"
        await client.say("Bryngle was given the key")

    elif (msg.message.content ==".key current"):
        await client.say('The current holder is %s' % key_holder)

    elif (msg.message.content ==".key request"): # Need to add input validation
        if (holder_id == ""):
            await client.send_message(msg.message.channel, 'No one has the key, probably with Bryngle')
        else:
            await client.send_message(msg.message.channel, 'Hey, <@%s> can I get the key?' % holder_id)


@client.command(pass_context = True)
async def room(msg):
    global people_in_room

    if (msg.message.content == ".room add"): # Adds a person using their discord name
        people_in_room.append(msg.message.author.mention)
        await client.say('%s is in the esport \'s room' %msg.message.author.mention)

    elif (msg.message.content ==".room ?"): # Find out who is currently in the room
        await client.say("**Currently in room :**")
        for p in list(set(people_in_room)):
            uniq_list = list(set(people_in_room))
            people_in_room = list(set(people_in_room)) #Gets rid of duplicate names in the list
            await client.say("%s \n" % p)

    elif(msg.message.content ==".room remove"): # Remove's yourself out of room
        people_in_room.remove(msg.message.author.mention)
        await client.say("Removed from room")

@client.command()
async def helpme():
    await client.say("""\n \n
                        **__.key__ commands**
*get* Call this when you obtain the key
*current* Find out who currently has the key                                
*request* Request the key from the current holder
*Bryngle* Call this when you give the key back to Bryngle                              
                                                        
**__.room__ commands**                                   
*add* Add yourself to the list of people who are currently in the esport's room                               
*?*   See who is currently in the room
*remove* Remove yourself from the room                              
                                                      """)

@client.command()
async def ping():
    await client.say('pong')


client.run(TOKEN)