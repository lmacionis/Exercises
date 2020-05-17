"""
Write three functions that are the “inverses” of to_secs:

hours_in returns the whole integer number of hours represented by a total number of seconds.
minutes_in returns the whole integer number of left over minutes in a total number of seconds, once the hours have been taken out.
seconds_in returns the left over seconds represented by a total number of seconds.
You may assume that the total number of seconds passed to these functions is an integer. Here are some test cases:

test(hours_in(9010) == 2)
test(minutes_in(9010) == 30)
test(seconds_in(9010) == 10)
"""

import sys

def hours_in(secs):
    hours = secs // 3600
    return int(hours)


def minutes_in(secs):
    minutes = (secs / 3600 - hours_in(secs)) * 60
    return int(minutes)


def seconds_in(secs):
    seconds = secs - minutes_in(secs) * 60 - hours_in(secs) * 3600
    return int(seconds)


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
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)


test_suite()        # Here is the call to run the tests