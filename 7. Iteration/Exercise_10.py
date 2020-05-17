"""
Write a function, is_prime, which takes a single integer argument and returns True
when the argument is a prime number and False otherwise. Add tests for cases like this:

test(is_prime(11))
test(not is_prime(35))
test(is_prime(19911121))

The last case could represent your birth date. Were you born on a prime day?
In a class of 100 students, how many do you think would have prime birth dates?
"""

import sys

# Based on the geeksforgeeks.org
# Rule: All the numbers which are ending with 5, cant be a prime number.
def is_prime(n):
    # Corner case
    if n <= 1:                  # becouse prime numbers can not be 1, 0, and all the minus numbers.
        return False
    # Check from 2 to n-1
    for i in range(2, n):       # i = from 2 till n, n is any number and just count a bit.
        if (n % i == 0):
            return False
    return True


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
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(not is_prime(19950225))


test_suite()        # Here is the call to run the tests

