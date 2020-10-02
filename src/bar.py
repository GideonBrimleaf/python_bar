class Bar:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.list_of_drinks = []
    
    def add_drinks(self, drink):
        self.list_of_drinks.append(drink)