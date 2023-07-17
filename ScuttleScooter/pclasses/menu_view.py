import discord
import discord.ui

class MenuView(discord.ui.View):
    def __init__(self, menu):
        super().__init__(timeout=60)
        self.current_page = 0
        self.menu = menu
    
    @discord.ui.button(label="Prev Page")
    async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page -=1
        if self.current_page < 0: self.current_page = len(self.menu) - 1
        await interaction.message.edit(embed=self.menu[self.current_page])
        await interaction.response.defer()

    @discord.ui.button(label="Next Page")
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page+=1
        if self.current_page >= len(self.menu): self.current_page = 0
        await interaction.message.edit(embed=self.menu[self.current_page])
        await interaction.response.defer()




