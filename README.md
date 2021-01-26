Cafe Drink TDD Sample Project

This sample project demonstrates the power of Python 3.3 and `unittest` framework - namely:

* No need for `__init__.py` files to create package namespaces.  These are now done automatically
* The [`unittest` library ability to handle relative file imports in the test files](https://docs.python.org/3/library/unittest.html#test-discovery), removing the need for a top-level test runner file.

To run the tests (from the root directory):

```
python -m unittest discover tests "*_test.py"
cd tests
python -m unittest discover "*_test.py"
```