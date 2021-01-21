# Import relative from anywhere in your project in Python

It's no secret - importing in Python is A Hard Thing.  I've suffered and done the hard work so you don't have to.
The following is compatible with Python 3.3 onwards since there's no need for empty `__init__.py` files anymore to litter up your code.

## Simple Start

Let's say you want to start with a simple Python class and want to write some tests for it.  You may have a folder structure similar to the following:

```
project
├── src
│   └── drinks.py
└── tests
    └── drinks_test.py
```

As mentioned - Python 3.3 onwards can [happily create namespaces for packages without an `__init__.py` file](https://stackoverflow.com/a/37140173/13898069) so we might think we're all good to go.  Let's try and run our tests:

```
python tests/drinks_test.py
```