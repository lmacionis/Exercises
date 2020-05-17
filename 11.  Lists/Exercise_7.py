"""
Write a function dot_product(u, v) that takes two lists of numbers of the same length, and returns
the sum of the products of the corresponding elements of each (the dot_product).

test(dot_product([1, 1], [1, 1]) ==  2)
test(dot_product([1, 2], [1, 4]) ==  9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
"""

import sys

def dot_product(u, v):
    sum = 0
    result = 0
    if len(u) != len(v):
        return 0
    else:
        for i in range(len(u)):
            sum = (u[i] * v[i])
            result += sum
        return result


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
    test(dot_product([1, 1], [1, 1]) == 2)
    test(dot_product([1, 2], [1, 4]) == 9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

test_suite()        # Here is the call to run the tests
