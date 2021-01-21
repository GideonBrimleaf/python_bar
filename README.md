# Import relative from anywhere in your project in Python

It's no secret - importing in Python is A Hard Thing.  I've suffered and done the hard work so you don't have to.
The following is compatible with Python 3.3 onwards as there's no need for empty `__init__.py` files anymore to litter up your code.

If you want to know why this is The Way then [here's a good starting point to understanding it](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time). Good Luck!

## Simple Start

Let's say you want to start with a simple Python class and want to write some tests for it.  You may have a folder structure similar to the following:

```
project
├── src
│   └── drinks.py
└── tests
    └── drinks_test.py
```

As mentioned - Python 3.3 onwards can [happily create namespaces for packages without an `__init__.py` file](https://stackoverflow.com/a/37140173/13898069) so we might think we're all good to go. 

Our `drinks` class could look like the following:

`drinks.py`
```
class Drink:
    
    def __init__(self, name, price_in_pence, type):
        self.name = name
        self.price_in_pence = price_in_pence
        self.type = type


    def price(self):
        return self.price_in_pence / 100
```

And our test are set up using `unittest` like so, importing in the class using the relative `..` notation:

`drinks_test.py`
```
import unittest
from ..src.drinks import Drink

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.my_awesome_drink = Drink("Mojito", 450, "Cocktail")
    
    def test_drink_has_name(self):
        self.assertEqual("Mojito", self.my_awesome_drink.name)
    
    def test_drink_has_price(self):
        self.assertEqual(4.50, self.my_awesome_drink.price())
    
    def test_drink_has_type(self):
        self.assertEqual("Cocktail", self.my_awesome_drink.type)

# We need the following so it will execute the tests when we run the file in python
if __name__ == '__main__':
    unittest.main()
```

## The Problem

Let's try and run our tests - for now let's say we're executing this whilst in the `project` directory (that's going to matter real quick)

```
#terminal
python tests/drinks_test.py

ImportError: attempted relative import with no known parent package
```

Ok so it's recognised that we're using a relative path... but it doesn't understand where that relative path goes.  Great.

Why is this a problem.  Let's just say it's complicated - if you want to know why this is The Way then [here's a good starting point to understanding it](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time). Good Luck! 

In short, imports in python aren't relative to the file where they are defined.  They are relative to where python gets executed. Additionally - if we tried to execute the test file without the `-m` flag, it loses all concept of where it is. For now we can solve this with the following:

1. Remove the relative path to the `drinks` class file:

`drinks_test.py`
```
import unittest
from src.drinks import Drink # altered!

class TestDrinks(unittest.TestCase):
#########################################
```

2. Run the test file with the `-m` flag - again from the top-level `project` directory. Note the omission of the `.py` extension AND the use of dot notation rather than `/` to traverse directories.

```
#terminal
python -m tests.drinks_test
```

Your tests should run just fine now.  However this feels really weird - `drinks_test.py` now imports from `src` by pointing a location totally wrong from where it sits. Additionally the `-m` flag seems to remove the need for the extension.

It's also a bit flaky - if we move into the test file and try to apply the same logic we get another error:

```
#terminal
python -m drinks_test

ModuleNotFoundError: No module named 'src'
```

## A Neat Solution

1. Need to append the relative parent directory to the sys_path - this is where Python looks for files when it's executing:

```
import sys
sys.path.append("..")
```

2. If you're executing at the project level run `python -m tests.drinks_test` WITHOUT the file extension.  This runs it in module mode (running `python tests/drinks_test.py` won't work some [big fuss over the name being "main" otherwise](https://stackoverflow.com/a/14132912/13898069))

3. If you're executing inside the test file - you can either `python drinks_test.py` or `python -m drinks_test`