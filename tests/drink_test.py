import unittest
import sys
sys.path.append("..")

from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.my_awesome_drink = Drink("Mojito", 450, "Cocktail")
    
    def test_drink_has_name(self):
        self.assertEqual("Mojito", self.my_awesome_drink.name)
    
    def test_drink_has_price(self):
        self.assertEqual(4.50, self.my_awesome_drink.price())
    
    def test_drink_has_type(self):
        self.assertEqual("Cocktail", self.my_awesome_drink.type)

if __name__ == '__main__':
    unittest.main()