import discord
from discord.ext import commands
from emt import uinput
from emt import wrt
import time as t

token = "" #PLANT2
client = discord.Client(intents = discord.Intents.all())
channel = 723585037131579401 #ibston general
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.command(name = "w")
async def test(ctx, *args):
    utext = "" #formatted 
    for i in args:
        utext = utext + i + " "

    
    await ctx.channel.send(wrt(uinput(utext)))

bot.run(token)
