"""
What will num_digits(0) return? Modify it to return 1 for this case.
Why does a call to num_digits(-24) result in an infinite loop?
(hint: -1//10 evaluates to -1)
Modify num_digits so that it works correctly with any integer value.

Add these tests:

test(num_digits(0) == 1)
test(num_digits(-12345) == 5)
"""

# A call to num_digits(-24) results in an infinite loop because it's a negative number and should be the absolute value.
# If you run not modified function off the num_digits with the negative numbers, it will turn into the infinitive loop.

import sys

def num_digits(n):
    count = 0
    if n == 0:
        count += 1              # here you can also write return 1.
    while n > 0 or n < 0:
        if n < 0:               # you need this loop, becouse off the negative numbers, they has to be turn into absolute values.
            n = -1 * n
        count = count + 1
        n = n // 10
    return count

print(num_digits(0))

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
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)

test_suite()        # Here is the call to run the tests