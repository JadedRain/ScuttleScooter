from pclasses.sushi_info import SushiInfo

class SushiPicker():
    def __init__(self):
        self.sushi_info = SushiInfo()

    def select_roll(self, name):
           try:
               return f"You have selected the {self.sushi_info.roll_container[name].name} roll"
        
           except:
               return "Please enter a valid sushi roll"
