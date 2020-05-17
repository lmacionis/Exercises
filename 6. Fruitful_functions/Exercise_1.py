# The four compass points can be abbreviated by single-letter strings as “N”, “E”, “S”, and “W”.
# Write a function turn_clockwise that takes one of these four compass points as its parameter,
# and returns the next compass point in the clockwise direction. Here are some tests that should pass:

"""
test(turn_clockwise("N") == "E")
test(turn_clockwise("W") == "N")
"""
# You might ask “What if the argument to the function is some other value?” For all other cases, the function should return the value None:

"""
test(turn_clockwise(42) == None)
test(turn_clockwise("rubbish") == None)
"""

import sys



def turn_clockwise(n):
    if n == "N":
        return "S"
    elif n == "E":
        return "W"
    elif n == "W":
        return "E"
    elif n == "S":
        return "N"
    else:
        return



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
    test(turn_clockwise("N") == "S")
    test(turn_clockwise("W") == "E")
    test(turn_clockwise("E") == "W")
    test(turn_clockwise("S") == "N")


test_suite()        # Here is the call to run the tests