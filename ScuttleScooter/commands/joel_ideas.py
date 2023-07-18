from tkinter import Menu
import discord
from discord.ui import view
from discord.ext import commands
from pclasses.sushi_picker import SushiPicker
from pclasses.menu_view import MenuView

class JoelCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sushi_picker = SushiPicker()
        self.menu_view = MenuView(self.sushi_picker.sushi_info.menu)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Joel commands loaded")

    @commands.command(name="shos")
    async def show_rolls(self, ctx):
        await ctx.channel.send(embed=self.sushi_picker.sushi_info.menu[0], view=self.menu_view)

    @commands.command(name="sels")
    async def select_roll(self, ctx, *roll_name):
        await ctx.channel.send(self.sushi_picker.select_roll(' '.join(roll_name[:]).title()))

    @commands.command(name="fils")
    async def filter_roll(self, ctx, *ingredient):
        ing = ' '.join(ingredient).lower()
        await ctx.channel.send(f"Now filtering by {ing}")
        self.sushi_picker.sushi_info.create_menu(ing)
        self.menu_view = MenuView(self.sushi_picker.sushi_info.menu)
        await self.show_rolls(ctx)
    
    @commands.command(name="clrf")
    async def clear_filters(self, ctx):
        self.sushi_picker.sushi_info.create_menu()
        self.menu_view = MenuView(self.sushi_picker.sushi_info.menu)
        await ctx.channel.send("Filters cleared")
async def setup(bot):
    await bot.add_cog(JoelCommands(bot))

     