import unittest
import sys
sys.path.append("..")

from src.cafe import Cafe
from src.drink import Drink

class TestCafe(unittest.TestCase):
    def setUp(self):
        self.my_amazing_cafe = Cafe("My Amazing Cafe", "Edinburgh")
        self.my_awesome_drink = Drink("Mocha", 899, "Coffee")
    
    def test_cafe_has_name(self):
        self.assertEqual("My Amazing Cafe", self.my_amazing_cafe.name)
    
    def test_cafe_has_location(self):
        self.assertEqual("Edinburgh", self.my_amazing_cafe.location)

    def test_cafe_starts_with_no_drinks(self):
        self.assertEqual(0, len(self.my_amazing_cafe.list_of_drinks))
    
    def test_cafe_can_add_a_drink(self):
        self.my_amazing_cafe.add_drinks(self.my_awesome_drink)
        self.assertEqual(1, len(self.my_amazing_cafe.list_of_drinks))
    
    def test_cafe_drinks_have_prices(self):
        self.my_amazing_cafe.add_drinks(self.my_awesome_drink)
        self.assertEqual(8.99, self.my_amazing_cafe.list_of_drinks[0].price())

if __name__ == '__main__':
    unittest.main()