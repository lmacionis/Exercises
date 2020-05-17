"""
Write a function that reverses its string argument, and satisfies these tests:

test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")
"""

# MORE ABOUT THIS IN: https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
import sys

# Using extended slice syntax
def reverse(word):
    word = word[::-1]
    return word


# Using recursion
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


# Using a loop
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str


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
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")

test_suite()        # Here is the call to run the tests
