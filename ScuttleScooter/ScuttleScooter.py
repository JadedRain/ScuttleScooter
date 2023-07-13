import asyncio
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv


# Sushi menu thing (choose a type of sushi ingredient and recommend sushi)- Joel 

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Set up intents for bot
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='~', intents=intents)

# Loads commands from other files
async def load():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')

# Gives how many servers the bot is in along with their name and ID
@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count+=1


        print("Bot is currently running in " + str(guild_count) + " guilds.")

async def main():
    await load()
    await bot.start(DISCORD_TOKEN)

asyncio.run(main())