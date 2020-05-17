"""
Can your day_add function already work with negative deltas?
For example, -1 would be yesterday, or -7 would be a week ago:

test(day_add("Sunday", -1) == "Saturday")
test(day_add("Sunday", -7) == "Sunday")
test(day_add("Tuesday", -100) == "Sunday")
If your function already works, explain why. If it does not work, make it work.

Hint: Play with some cases of using the modulus function %
(introduced at the beginning of the previous chapter).
Specifically, explore what happens to x % 7 when x is negative.
"""

import sys

def day_add(num, delta_arg):
        return day_name((day_num(num) + delta_arg) % 7)


weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def day_num(num):
    if num in weekdays:
        return weekdays.index(num)
    return None


def day_name(day):
    if day in range(7):
        return weekdays[day]
    return None


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
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")


test_suite()        # Here is the call to run the tests

"""
Function works with the negative delta_arg becouse of the float or modulus devision

Modulo with Negative Numbers:
Python modulo operator always return the remainder having the same sign as the divisor. This can lead to some confusion with the output.

>>> -5 % 3
1
>>> 5 % -3
-1
>>> -10 % 3
2
>>>
-5 % 3 = (1 -2*3) % 3 = 1
5 % -3 = (-1 * -2*-3) % 3 = -1
-10 % 3 = (2 -4*3) % 3 = 2
"""