class SushiRoll():
    def __init__(self, name, ingredients, toppings, price, vegitarian, spice_level):
        self.name = name
        self.ingredients = ingredients.split(',')
        self.toppings = toppings.split(',')
        self.price = float(price)
        self.vegitarian = vegitarian
        self.spice_level = spice_level




