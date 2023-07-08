import discord
from discord.ext import commands

class BenCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ben commands loaded")
    
    # Command to say Hello to Ben
    @commands.command(name="hiben")
    async def hiben(self, ctx):
        ben = '<@398559344549036034>'
        await ctx.send(f"Hello {ben}! (You British Bitch)")


async def setup(bot):
    await bot.add_cog(BenCommands(bot))