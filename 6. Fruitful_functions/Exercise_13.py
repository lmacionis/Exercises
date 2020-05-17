"""
Write a function slope(x1, y1, x2, y2) that returns the slope of the line
through the points (x1, y1) and (x2, y2). Be sure your implementation of slope
can pass the following tests:

test(slope(5, 3, 4, 2) == 1.0)
test(slope(1, 2, 3, 2) == 0.0)
test(slope(1, 2, 3, 3) == 0.5)
test(slope(2, 4, 1, 2) == 2.0)

Then use a call to slope in a new function named intercept(x1, y1, x2, y2)
that returns the y-intercept of the line through the points (x1, y1) and (x2, y2)

test(intercept(1, 6, 3, 12) == 3.0)
test(intercept(6, 1, 1, 6) == 7.0)
test(intercept(4, 6, 12, 8) == 5.0)
"""

import sys

def slope(x1, y1, x2, y2):
    slope = (y2 - y1) / float(x2 - x1)
    return slope


def intercept(x1, y1, x2, y2):
    y_intercept = y1 - x1 * slope(x1, y1, x2, y2)
    return y_intercept


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite1():
    """ Run the suite of tests for code in this module (this file).
    """
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)


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
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)


test_suite1()        # Here is the call to run the tests
test_suite()        # Here is the call to run the tests