from audioop import add
import discord
import discord.ui
import pandas as pd
from pclasses.sushi_roll import SushiRoll

class SushiInfo():

    count = 0
    roll_container = {}
    sushi_file_data = None
    menu = None

    def __init__(self):
        self.sushi_file_data = pd.read_csv('./sushi_list.csv')
        self.load_data_to_dict()
        self.create_menu()

    def load_data_to_dict(self):
        for i, roll in enumerate(self.sushi_file_data.iloc):
            self.roll_container[roll[0]] = SushiRoll(*roll)   

    def create_menu(self, filter=None):
        menu_pages = []
        embed = discord.Embed()

        def add_page():
            embed.title = "Sushi Menu"
            embed.description = "A list of sushi rolls with their ingredients"
            embed.color = 0xffb19a
            embed.set_footer(text=f"Page {len(menu_pages) + 1}")
            menu_pages.append(embed)

        for i, roll in enumerate(self.roll_container):
            if filter:
                if filter in self.roll_container[roll].ingredients:
                    embed.add_field(name=f"{self.roll_container[roll].name} ${self.roll_container[roll].price}", value=f"{', '.join(self.roll_container[roll].ingredients)} topped w/ {', '.join(self.roll_container[roll].toppings)}", inline=False)
            else:
                embed.add_field(name=f"{self.roll_container[roll].name} ${self.roll_container[roll].price}", value=f"{', '.join(self.roll_container[roll].ingredients)} topped w/ {', '.join(self.roll_container[roll].toppings)}", inline=False)
            
            if len(embed.fields) == 10:
                add_page()
                embed = discord.Embed()
        
        if len(embed.fields):
            add_page()
        self.menu = menu_pages

  