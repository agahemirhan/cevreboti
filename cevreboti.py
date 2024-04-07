import discord
from discord.ext import commands
import random
import os
import requests
print(os.listdir("videolar"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')



@bot.command()
async def örnekler1(ctx):
    video = random.choice(os.listdir('videolar'))
    with open(f'videolar/{video}', 'rb') as f:
        url = discord.File(f)
 
    await ctx.send(file = url)


@bot.command()
async def örnekler2(ctx):
    img_name = random.choice(os.listdir('resim'))
    with open(f'resim/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)



bot.run("TOKEN")
