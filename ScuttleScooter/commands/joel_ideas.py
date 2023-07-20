from tkinter import Menu
import discord
from discord.ui import view
from discord.ext import commands
from pclasses.sushi_picker import SushiPicker
from pclasses.menu_view import MenuView
from pclasses.sushi_cart import SushiCart

class JoelCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sushi_picker = SushiPicker()
        self.menu_view = MenuView(self.sushi_picker.sushi_info.menu)
        self.sushi_cart = SushiCart()

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

    @commands.command(name="adds")
    async def add_item_to_cart(self, ctx, *roll_name):
        try:
            self.sushi_cart.add_item_to_cart(self.sushi_picker.sushi_info.roll_container[' '.join(roll_name[:]).title()])
            await ctx.channel.send(f"Added {' '.join(roll_name[:]).title()} roll to cart.")
        except:
            await ctx.channel.send("Couldn't add roll to cart")
    
    @commands.command(name="rems")
    async def remove_item_from_cart(self, ctx, *roll_name):
        try:
            self.sushi_cart.remove_item_from_cart(self.sushi_picker.sushi_info.roll_container[' '.join(roll_name[:]).title()])
            await ctx.channel.send(f"Removed {' '.join(roll_name[:]).title()} roll from cart.")
        except:
            await ctx.channel.send("Couldn't remove roll from cart")

    @commands.command(name="carp")
    async def get_price(self, ctx):
        await ctx.channel.send(f"Cart total is ${self.sushi_cart.get_cart_total()}")

    @commands.command(name="clrc")
    async def clear_cart(self, ctx):
        self.sushi_cart.clear_cart()
        await ctx.channel.send("Your cart has been cleared.")

async def setup(bot):
    await bot.add_cog(JoelCommands(bot))

     