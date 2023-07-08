import discord
from pclasses.trivia_game import TriviaGame
from discord.ext import commands

class TyCommands(commands.Cog):

    trivia_game = TriviaGame()
    question_asked = False

    def _init(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ty commands loaded")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if self.question_asked:
            self.question_asked = False
            await msg.channel.send("Cheese balls")

    @commands.command(name="q")
    async def random_question(self, ctx):
        await ctx.send(f"Here is a random question: \n{self.trivia_game.give_question()}")
        self.question_asked = True





async def setup(bot):
    await bot.add_cog(TyCommands(bot))
