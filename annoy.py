import os
import discord
import time
import random
import string
from discord.utils import get

def randomletters(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

TOKEN = ("")# token here 
Muted_role = "<@&123456789>" # muted role id within <@& here >
client=discord.Client()

@client.event
async def on_ready():
    print('connected to Discord!')

@client.event
async def on_message(message):
    response = Muted_role, ' REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'
    x=100
    while int(x)==100:
        print("message sent "+random.choice(string.ascii_letters))
        await message.channel.send(response)

client.run(TOKEN)
