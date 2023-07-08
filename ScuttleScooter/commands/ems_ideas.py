import discord
from discord.ext import commands

class EmCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Em commands loaded")

    @commands.command(name='join_vc')
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect(self_deaf = True)
    
    @commands.command(name='leave_vc')
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

async def setup(bot):
    await bot.add_cog(EmCommands(bot))