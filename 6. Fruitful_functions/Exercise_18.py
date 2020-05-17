"""
Write the function f2c(t) designed to return the integer value of the nearest
degree Celsius for given temperature in Fahrenheit. (hint: you may want to make
use of the built-in function, round. Try printing round.__doc__ in a Python
shell or looking up help for the round function, and experimenting with it
until you are comfortable with how it works.)

test(f2c(212) == 100)     # Boiling point of water
test(f2c(32) == 0)        # Freezing point of water
test(f2c(-40) == -40)     # Wow, what an interesting case!
test(f2c(36) == 2)
test(f2c(37) == 3)
test(f2c(38) == 3)
test(f2c(39) == 4)
"""

import sys

                # My version of the function
def f2c(t):
    return round((t - 32) * 5 / 9)


"""             Founded verion of the function in google
def f2c(t):
    final = int(round(((t-32)*(5/9)), 0))
    return final
"""


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(f2c(212) == 100)     # Boiling point of water
    test(f2c(32) == 0)        # Freezing point of water
    test(f2c(-40) == -40)     # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)


test_suite()        # Here is the call to run the tests