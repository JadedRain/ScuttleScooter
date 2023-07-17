import discord
import discord.ui
import math
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
        self.menu = self.create_menu()

    def load_data_to_dict(self):
        for i, roll in enumerate(self.sushi_file_data.iloc):
            self.roll_container[roll[0]] = SushiRoll(*roll)   

    def create_menu(self):
        menu_pages = []
        embed = discord.Embed(title="Sushi Menu", description="A list of sushi with their ingredients", color=0xffb19a)
        for i, roll in enumerate(self.roll_container):
            if i % 10 == 0 and i != 0:
                embed.set_footer(text=f"Page {math.ceil(i/10)}")
                menu_pages.append(embed)
                embed =  discord.Embed(title="Sushi Menu", description="A list of sushi with their ingredients", color=0xffb19a)
            embed.add_field(name=f"{self.roll_container[roll].name} ${self.roll_container[roll].price}", value=f"{', '.join(self.roll_container[roll].ingredients)} topped w/ {', '.join(self.roll_container[roll].toppings)}", inline=False)

        embed.set_footer(text=f"Page {math.ceil(i/10)}")
        menu_pages.append(embed)
        return menu_pages