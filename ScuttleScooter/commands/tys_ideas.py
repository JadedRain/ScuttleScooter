import discord
from pclasses.trivia_game import TriviaGame
from discord.ext import commands

class TyCommands(commands.Cog):

    trivia_game = TriviaGame()
    question_asked = False
    channel_of_asked_question = None
    user_that_asked_question = None

    def _init(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ty commands loaded")

    # Wait for a user to answer the question
    @commands.Cog.listener()
    async def on_message(self, msg):
        if self.question_asked and self.user_that_asked_question == msg.author:
            if self.trivia_game.check_answer(msg.content):
                self.question_asked = False
                await self.channel_of_asked_question.send("You got the correct answer!")

            elif self.trivia_game.lives == 0:
                self.question_asked = False
                self.trivia_game.reset_life()
                await self.channel_of_asked_question.send("You lost this attempt :(")

            else:
                self.trivia_game.remove_life()
                await self.channel_of_asked_question.send(f"That's not right! Guess again\nLives Left: {self.trivia_game.lives}")

    @commands.command(name="q")
    async def random_question(self, ctx):
        await ctx.send(f"Here is a random question: \nLives Left: {self.trivia_game.lives}\n{self.trivia_game.give_question()}")
        self.channel_of_asked_question = ctx.channel
        self.user_that_asked_question = ctx.message.author
        self.question_asked = True





async def setup(bot):
    await bot.add_cog(TyCommands(bot))
