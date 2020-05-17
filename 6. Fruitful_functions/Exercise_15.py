"""
Now write the function is_odd(n) that returns True when n is odd and False otherwise.
Include unit tests for this function too.

Finally, modify it so that it uses a call to is_even to determine if its
argument is an odd integer, and ensure that its test still pass.
"""

import sys
from Exercise_14 import is_even         # importing the function is_even from Exercise_14

# Modified verion off the function is_odd
def is_odd(n):
    if is_even(n) != 0:                 # != this means: not equal
        return False
    else:
        return True


"""             First part of the exercise
def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True
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
    test(is_odd(3) == True)
    test(is_odd(12) == False)
    test(is_odd(24) == False)
    test(is_odd(9) == True)


test_suite()        # Here is the call to run the tests