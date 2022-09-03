import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.environ["BOT_TOKEN"]


intents = discord.Intents.default()
# intents.message_content = True



# client = discord.Client(intents=intents)
client = commands.Bot(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))
    




@client.event
async def on_message(message):
    
    username = str(message.author).split('#')[0] # split Itspran_#9999 to ['Itspran',9999] and get 0th index
    user_message = str(message.content) ## split out message id and format extra space by skipping first char
    if isinstance(message.channel, discord.DMChannel):
        print(f'FROM DM: {user_message} FROM: {username}')
        
        
        
        
        return
    else:
        channel = str(message.channel.name)
    if channel == 'stuff':
        return
    print(f'{username}: {user_message} ({channel})')
    
    
    if message.author == client.user: #bot should not respond to itself
        return
    
    if user_message.lower() == 'hello':
        # await message.channel.send(f'Hello {username}')
        embed=discord.Embed(title="Response", description=f'Hello, {username}', color=0xff0000)
        # embed.add_field(name="Fiel1", value="hi", inline=False)
        
        await message.channel.send(embed=embed)

        return
    
    if user_message.lower() == 'rutger':
        await message.author.send("??")
    await client.process_commands(message)




@client.slash_command(name="slash", guild_ids=[1014304623714111488]) 
async def slash(ctx): 
    await ctx.respond("You executed the slash command!")
    


    
@client.slash_command(name="dm", guild_ids=[1014304623714111488])
async def dm(ctx, member: discord.Member):
    await ctx.respond("what do you want to say")
    def check(m):
        return m.author.id == ctx.author.id
    message = await client.wait_for("message", check=check)
    
    await ctx.respond(f"sent message to <@{member.id}>")
    await member.respond(f"{ctx.author.mention} has sent you a message:\n{message.content}")
# client.add_command(dm)

@client.slash_command(name="getbook", guild_ids=[1014304623714111488], description="Find a book from top databases")
async def getbook(ctx):
    await ctx.defer() # wait a bit longer to avoid "Did not respond" error
    
    # must respond after defer to avoid infinite "Thinking..." message
    
    
    await ctx.respond("Check DMs")
    await ctx.author.send("What Book?")
    def check(m):
        return (m.author.id == ctx.author.id) and (isinstance(m.channel, discord.channel.DMChannel))
    book = await client.wait_for("message", check=check)
    

    
    
    
    
    
    
    await ctx.author.send(f"Grabbing top 3 results of {book.content}...")
    
    
    #make the query friendly for the URL to parse
    query = book.content.replace(" ","%20")
    query.replace("'","%27")
    query.replace("!","%21")
    query.replace("$","%24")
    query.replace("(","%28")
    query.replace(")","%29")
    query.replace("+","%2B")
    query.replace("=","%3D")
    query.replace(":","%3A")
    
    mainurl = 'http://b-ok.cc'
    
    
    url = 'http://b-ok.cc/s/'+query
    
    
    print(f"URL: {url}")
    r = requests.get(url)
    await ctx.author.send(f"Status Code:  {r.status_code}")
    
    
    soup = BeautifulSoup(r.content, 'html.parser')
    
    h3 = soup.find_all('h3', attrs={"itemprop":True})
    
    # print(h3)
    
    i =3
    
    for link in h3:
        if i==0:
            break
        h3link = link.find_all('a')[0].text.strip()
        booklink = "LINK: "+mainurl+link.find_all('a')[0]['href']
        await ctx.author.send(f"Book: {h3link}\n{booklink}")
        i-=1
    
    
    
    
    await ctx.respond("Search Complete")

    
    

client.run(TOKEN)