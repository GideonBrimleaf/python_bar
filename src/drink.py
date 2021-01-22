class Drink:
    
    def __init__(self, name, price_in_pence, type):
        self.name = name
        self.price_in_pence = price_in_pence
        self.type = type


    def price(self):
        return self.price_in_pence / 100
    
