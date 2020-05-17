"""
Add the following statement to mymodule1.py, mymodule2.py, and namespace_test.py from the previous exercise:

print("My name is", __name__)
Run namespace_test.py. What happens? Why? Now add the following to the bottom of mymodule1.py:
The output.: It prints out module names and then changes to the attribute. Not sure, but I think that what happens.
Modules contain functions as well as attributes, and the dot operator is used to access them in the same way.
My name is mymodule1
My name is mymodule2
My name is __main__


if __name__ == "__main__":
    print("This won't run if I'm  imported.")
Run mymodule1.py and namespace_test.py again. In which case do you see the new print statement?
Into mymodule1fpy
"""