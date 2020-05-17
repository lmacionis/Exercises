"""
Write a function called is_even(n) that takes an integer as an argument
and returns True if the argument is an even number and False if it is odd.

Add your own tests to the test suite.
"""

import sys

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


"""
Short version of the function:
def is_even(n):
    return n % 2 == 0
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
    test(is_even(3) == False)
    test(is_even(12) == True)
    test(is_even(24) == True)
    test(is_even(9) == False)


test_suite()        # Here is the call to run the tests