class SushiCart():
    cart_total = 0
    items_in_cart = []

    def add_item_to_cart(self, item):
        self.cart_total+=item.price
        self.items_in_cart.append(item)

    def remove_item_from_cart(self, item):
        self.items_in_cart.remove(item)
        self.cart_total-=item.price
    
    def clear_cart(self):
        self.items_in_cart = []
        self.cart_total = 0

    def get_cart_total(self):
        return self.cart_total