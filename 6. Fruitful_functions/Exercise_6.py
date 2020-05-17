"""
Write a function days_in_month which takes the name of a month,
and returns the number of days in the month. Ignore leap years:

test(days_in_month("February") == 28)
test(days_in_month("December") == 31)
If the function is given invalid arguments, it should return None.
"""

import sys

def days_in_month(month_name):
    if month_name in months:
        return 31
    elif month_name in months2:
        return 30
    elif month_name in months3:
        return 28
    else:
        return None


months = ["January", "March" "May", "July", "August", "October", "December"]
months2 = ["April", "June", "September", "November"]
months3 = ["February"]


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
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)

test_suite()        # Here is the call to run the tests

print(days_in_month("February"))