import discord
from discord.ext import commands

class LoganCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Logan commands loaded")


async def setup(bot):
    await bot.add_cog(LoganCommands(bot))

