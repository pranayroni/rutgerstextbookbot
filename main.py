import discord
import random
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.environ["BOT_TOKEN"]


intents = discord.Intents.default()
intents.message_content = True



client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))




@client.event
async def on_message(message):
    username = str(message.author).split('#')[0] # split Itspran_#9999 to ['Itspran',9999] and get 0th index
    user_message = str(message.content) ## split out message id and format extra space by skipping first char
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    
    
    if message.author == client.user: #bot should not respond to itself
        return
    
    if user_message.lower() == 'hello':
        # await message.channel.send(f'Hello {username}')
        embed=discord.Embed(title="Response", description=f'Hello, {username}', color=0xff0000)
        # embed.add_field(name="Fiel1", value="hi", inline=False)
        
        await message.channel.send(embed=embed)

        return



client.run(TOKEN)