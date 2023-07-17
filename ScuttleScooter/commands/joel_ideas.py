import discord
from discord.ui import view
from discord.ext import commands
from pclasses.sushi_info import SushiInfo
from pclasses.menu_view import MenuView

class JoelCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sushi_info = SushiInfo()
        self.menu_view = MenuView(self.sushi_info.menu)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Joel commands loaded")

    @commands.command(name="sr")
    async def select_roll(self, ctx):
        await ctx.channel.send(embed=self.sushi_info.menu[0], view=self.menu_view)

    @commands.command(name="st")
    async def show_roll(self, ctx, *roll_name):
        await ctx.channel.send(self.sushi_info.show_roll(" ".join(roll_name[:]).title()))

async def setup(bot):
    await bot.add_cog(JoelCommands(bot))

