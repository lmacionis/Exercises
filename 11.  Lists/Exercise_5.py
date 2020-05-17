"""
Lists can be used to represent mathematical vectors. In this exercise and several that follow
you will write functions to perform standard operations on vectors. Create a script named
vectors.py and write Python code to pass the tests in each case.

Write a function add_vectors(u, v) that takes two lists of numbers of the same length,
and returns a new list containing the sums of the corresponding elements of each:

test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
"""

import sys

# Found in a stackoverflow and modified by my conditions.
def add_vectors(v1, v2):
    newVector = []
    for index in range(len(v1)):
        newVector.append(v1[index] + v2[index])     # append is a list method which adds the argument passed to it to the end of the list.
    return newVector


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
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])


test_suite()        # Here is the call to run the tests