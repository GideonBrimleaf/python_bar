Cafe Drink TDD

This sample project demonstrates the power of Python 3.3 and `unittest framework` - namely:

* No need for `__init__.py` files to create package namespaces.  These are now done automatically
* The `unittest` ability to handle relative file imports in the test files.

To run the tests:

```
python -m unittest discover tests "*_test.py"
```