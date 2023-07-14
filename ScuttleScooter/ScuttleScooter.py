import asyncio
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from pclasses.guild_info import GuildInfo


# Sushi menu thing (choose a type of sushi ingredient and recommend sushi)- Joel 

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='~', intents=intents)

async def load():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')

@bot.event
async def on_ready():
    guild_info = GuildInfo(bot.guilds)
    guild_info.list_guild_info()

async def main():
    await load()
    await bot.start(DISCORD_TOKEN)

asyncio.run(main())