"""
Extra challenge for the mathematically inclined: Write a function cross_product(u, v)
that takes two lists of numbers of length 3 and returns their cross product. You should write your own tests.
"""

import sys

def cross_product(u, v):
    s = []
    for i in range(len(u)):
        if i == 0:
            j,k = 1,2       # numbers / arguments position in a list
            s.append(u[j]*v[k] - u[k]*v[j])
        elif i == 1:
            j,k = 2,0       # numbers / arguments position in a list
            s.append(u[j]*v[k] - u[k]*v[j])
        else:
            j,k = 0,1       # numbers / arguments position in a list
            s.append(u[j]*v[k] - u[k]*v[j])
    return s


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
    test(cross_product([1, 1, 1], [1, 1, 1]) == [0, 0, 0])
    test(cross_product([1, 2, 3], [4, 5, 6]) == [-3, 6, -3])
    test(cross_product([1, 2, 1], [1, 4, 3]) == [2, -2, 2])

test_suite()        # Here is the call to run the tests
