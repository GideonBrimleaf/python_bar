import unittest
from src.bar import Bar
from src.drinks import Drink

class TestBar(unittest.TestCase):
    def setUp(self):
        self.my_amazing_bar = Bar("My Amazing Bar", "Edinburgh")
        self.my_awesome_drink = Drink("Screwdriver", 899, "Cocktail")
    
    def test_bar_has_name(self):
        self.assertEqual("My Amazing Bar", self.my_amazing_bar.name)
    
    def test_bar_has_location(self):
        self.assertEqual("Edinburgh", self.my_amazing_bar.location)
    

    def test_bar_starts_with_no_drinks(self):
        self.assertEqual(0, len(self.my_amazing_bar.list_of_drinks))
    
    def test_the_bar_can_add_a_drink(self):
        self.my_amazing_bar.add_drinks(self.my_awesome_drink)
        self.assertEqual(1, len(self.my_amazing_bar.list_of_drinks))
    
    def test_the_bar_drinks_have_prices(self):
        self.my_amazing_bar.add_drinks(self.my_awesome_drink)
        self.assertEqual(8.99, self.my_amazing_bar.list_of_drinks[0].price())