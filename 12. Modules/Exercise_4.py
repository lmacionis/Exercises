"""
Create a module named mymodule1.py. Add attributes myage set to your current age, and year set to the current year.
Create another module named mymodule2.py. Add attributes myage set to 0, and year set to the year you were born.
Now create a file named namespace_test.py. Import both of the modules above and write the following statement:

print( (mymodule2.myage - mymodule1.myage) ==
       (mymodule2.year - mymodule1.year)  )
When you will run namespace_test.py you will see either True or False as output depending on whether
or not you’ve already had your birthday this year.

What this example illustrates is that out different modules can both have attributes named myage and year.
Because they’re in different namespaces, they don’t clash with one another. When we write namespace_test.py,
we fully qualify exactly which variable year or myage we are referring to.
"""

import mymodule1
import mymodule2

print("My name is", __name__)


print( (mymodule2.myage - mymodule1.myage) ==
       (mymodule2.year - mymodule1.year)  )


