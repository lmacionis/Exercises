"""
Write a function num_even_digits(n) that counts the number of even digits in n. These tests should pass:

test(num_even_digits(123456) == 3)
test(num_even_digits(2468) == 4)
test(num_even_digits(1357) == 0)
test(num_even_digits(0) == 1)
"""

import sys

# This function doesnt work with the negative numbers, i could not make it work, and didint found a normal answer in the google.
def num_even_digits(n):
    count = 0
    if n == 0:
        count += 1
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            count = count + 1
        n = n // 10
    return count


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
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)

test_suite()        # Here is the call to run the tests