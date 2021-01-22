# Import relative from anywhere in your project in Python

It's no secret - importing in Python is A Hard Thing.  I've suffered and done the hard work so you don't have to.
The following is compatible with Python 3.3 onwards as there's no need for empty `__init__.py` files anymore to litter up your code.

## Simple Start

Let's say you want to start with a simple Python class and want to write some tests for it.  You may have a folder structure similar to the following:

```
project
├── src
│   └── drinks.py
└── tests
    └── drinks_test.py
```

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

As mentioned - Python 3.3 onwards can [happily create namespaces for packages without an `__init__.py` file](https://stackoverflow.com/a/37140173/13898069) so we might think we're all good to go. 

## The Problem

Let's try and run our tests - for now let's say we're executing this whilst in the `project` directory (that's going to matter real quick):

```
#terminal
python tests/drinks_test.py

ImportError: attempted relative import with no known parent package
```

Ok so it's recognised that we're using a relative path... but it doesn't understand where that relative path goes.  Great.

Why is this a problem?  Let's just say it's complicated - if you want to know why then [here's a good starting point to understanding it](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time). Good Luck! For now we can solve this with the following:

## The Initial Fix

1. Remove the relative path to the `drinks` class file:

`drinks_test.py`
```
import unittest
from src.drinks import Drink # altered!

class TestDrinks(unittest.TestCase):

```

2. Run the test file with the `-m` flag - again from the top-level `project` directory. Note the omission of the `.py` extension AND the use of dot notation rather than `/` to traverse directories.

```
#terminal
➜ project python -m tests.drinks_test
```

Your tests should run just fine now.  However this feels really weird - `drinks_test.py` now imports from `src` by pointing to a location totally wrong from where it sits. Additionally the `-m` flag seems to remove the need for the extension.

It's also a bit flaky - if we move into the test file and try to apply the same logic we get another error:

```
#terminal
➜ project/test python -m drinks_test

ModuleNotFoundError: No module named 'src'
```

So why do we need to make these changes?  And why is the fix not consistent? In short, imports in python aren't relative to the file where they are defined.  They are relative to where python gets executed. Additionally - if we tried to execute the test file without the `-m` flag, [it loses all concept of where it is](https://stackoverflow.com/a/14132912/13898069). It's quite tricky to get your head around but the `-m` flag runs it in a kind of "module mode" preserving the context of where the file is relative to other files it refers to.

## A Neat Solution

To get the test file running regardless of where we are running Python from we need to append the relative parent directory to Python's in-built `sys.path` variable. This is [the list of directories Python looks through when it's executing](https://www.geeksforgeeks.org/sys-path-in-python/#:~:text=path-,sys.,among%20its%20built%2Din%20modules.):

`test_drinks.py`
```
import unittest
import sys # added!
sys.path.append("..") # added!

from ..src.drinks import Drink 

class TestDrinks(unittest.TestCase):
```

This allows us to execute this file from within the file's directory like so:

```
➜ project/test python -m drinks_test
```

While still also allowing us to execute it from the parent project directory like we did before.

And we can also call this without the `-m` flag with the same results:

```
➜ project/test python drinks_test.py
```

However to maintain consistency, I'd recommend sticking with the `-m` flag.

## Running Multiple files

So now we have a way to execute the test files from both the top level directory as well as the individual directory.  This is scaleable with multiple class and test files:

```
project
├── src
│   ├── bar.py
│   └── drinks.py
└── tests
    ├── bar_test.py
    └── drinks_test.py
```

Our `bar` class expects to be able to add `drinks` to it's stock:

```
class Bar:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.list_of_drinks = []
    
    def add_drinks(self, drink):
        self.list_of_drinks.append(drink)
```

And we can test that like so - import drinks into the bar test:

```
import unittest
import sys
sys.path.append("..")

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

if __name__ == '__main__':
    unittest.main()
```

We can call the bar test using the same principle from the root and test directory:

```
➜ project python -m test.bar_test
```

```
➜ project/test python -m bar_test
➜ project/test python bar_test.py
```

What if we wanted to run both all our test files in one go?