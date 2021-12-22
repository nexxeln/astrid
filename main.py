import discord
import os
from settings import TOKEN, PREFIX
from discord.ext import commands
from discord.commands import slash_command, Option

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

for file_name in os.listdir("./cogs"):
    if file_name.endswith(".py") and file_name != "__init__.py":
        bot.load_extension(f"cogs.{file_name[:-3]}")

bot.run(TOKEN)