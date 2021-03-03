class Cafe:
    def __init__(self, name, location, list_of_drinks = []):
        self.name = name
        self.location = location
        self.list_of_drinks = list_of_drinks
    
    def add_drinks(self, drink):
        print("adding drink to list")
        self.list_of_drinks.append(drink)