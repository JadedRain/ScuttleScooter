import discord
from discord.ext import commands

class JoelCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Joel commands loaded")

    @commands.command(name="sr")
    async def select_roll(self, ctx, roll_name):
        await ctx.channel.send(f"You selected the {roll_name} roll")


async def setup(bot):
    await bot.add_cog(JoelCommands(bot))

