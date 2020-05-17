"""
Sum all the elements in a list up to but not including the first even number.
(Write your unit tests. What if there is no even number?)
"""
import sys

def sum_all_elements(list):
    sum_all = 0
    for i in list:
        if i % 2 == 1:
            sum_all = sum_all + i
        else:
            break
    return sum_all


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
    test(sum_all_elements([1,3,1,4,3,8]) == 5)
    test(sum_all_elements([1,3,5,7]) == 16)
    test(sum_all_elements([1, -7, 10, 23]) == -6)
    test(sum_all_elements(range(1,555,2)) == 76729)

test_suite()        # Here is the call to run the tests