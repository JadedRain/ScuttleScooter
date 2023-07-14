import pandas as pd

class TriviaGame:
    
    correct_answer = ""
    trivia_file_data = None
    player_lives = 3

    def __init__(self):
        self.trivia_file_data = pd.read_csv("./trivia_sheet.csv")

    def give_question(self):
        question = self.trivia_file_data.sample()
        self.correct_answer = question.iloc[0][2]
        return question.iloc[0][1]

    def check_answer(self, answer):
        return answer.lower() == self.correct_answer

    def remove_life(self):
        self.player_lives-=1

    def reset_life(self):
        self.player_lives = 3

