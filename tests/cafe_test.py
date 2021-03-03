import unittest
import sys
import pdb; 
sys.path.append("..")

from src.cafe import Cafe
from src.drink import Drink

class TestCafe(unittest.TestCase):
    def setUp(self):
        print("running setup method")
        self.my_amazing_cafe = Cafe("My Amazing Cafe", "Edinburgh")
        self.my_awesome_drink = Drink("Mocha", 899, "Coffee")
        print(f"the drink list is ${self.my_amazing_cafe.list_of_drinks} for ${self.my_amazing_cafe}")
    
    def test_cafe_has_name(self):
        # pdb.set_trace()
        print("running cafe has name")
        self.assertEqual("My Amazing Cafe", self.my_amazing_cafe.name)
    
    def test_cafe_has_location(self):
        # pdb.set_trace()
        print("running cafe has location")
        self.assertEqual("Edinburgh", self.my_amazing_cafe.location)

    def test_cafe_starts_with_no_drinks(self):
        # pdb.set_trace()
        print("running cafe has no drinks")
        self.assertEqual(0, len(self.my_amazing_cafe.list_of_drinks))
    
    def test_cafe_can_add_a_drink(self):
        print("running can add drink")
        self.my_amazing_cafe.add_drinks(self.my_awesome_drink)
        self.assertEqual(1, len(self.my_amazing_cafe.list_of_drinks))
    
    # def test_cafe_drinks_have_prices(self):
    #     self.my_amazing_cafe.add_drinks(self.my_awesome_drink)
    #     self.assertEqual(8.99, self.my_amazing_cafe.list_of_drinks[0].price())

if __name__ == '__main__':
    unittest.main()