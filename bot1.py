import discord
from discord.ext import commands

TOKEN = "meu_token_aqui"
from discord.ext import commands

TOKEN = "meu_token_aqui"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("💜Audio School💜 está ONLINE!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("💜Audio School💜 está ONLINE!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)