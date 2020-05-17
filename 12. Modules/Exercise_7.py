"""
Give the Python interpreter’s response to each of the following from a continuous interpreter session:

>>> s = "If we took the bones out, it wouldn't be crunchy, would it?"

>>> s.split()
 ['If', 'we', 'took', 'the', 'bones', 'out,', 'it', "wouldn't", 'be', 'crunchy,', 'would', 'it?']
>>> type(s.split())
 <class 'list'>
>>> s.split("o")
 ['If we t', '', 'k the b', 'nes ', 'ut, it w', "uldn't be crunchy, w", 'uld it?']
>>> s.split("i")
 ['If we took the bones out, ', "t wouldn't be crunchy, would ", 't?']
>>> "0".join(s.split("o"))
 "If we t00k the b0nes 0ut, it w0uldn't be crunchy, w0uld it?"

Be sure you understand why you get each result. Then apply what you have learned to fill in the body
of the function below using the split and join methods of str objects:

def myreplace(old, new, s):
    # Replace all occurrences of old with new in s.
    ...


test(myreplace(",", ";", "this, that, and some other thing") ==
                         "this; that; and some other thing")
test(myreplace(" ", "**",
                 "Words will now      be  separated by stars.") ==
                 "Words**will**now**be**separated**by**stars.")

If the last test would look like this:
test(myreplace(" ", "**",
                 "Words will now be separated by stars.") ==
                 "Words**will**now**be**separated**by**stars.")
the test would pass, thou I dont know how to pass the test with the given test.

Your solution should pass the tests.
"""

import sys

# my answer, doesnt work with the second test.
def myreplace(old, new, s):
    # Replace all occurrences of old with new in s...
    new_s = ""
    for i in s.split():
        s.split(old)
        new_s = new.join(s.split(old))
    return new_s

# Answer from stackoverflow
def myreplace(old, new, s):
    # Replace all occurrences of old with new in s...
    if old == ' ':
        return new.join(s.split())
    else:
        return new.join(s.split(old))


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
    test(myreplace(",", ";", "this, that, and some other thing") ==
         "this; that; and some other thing")
    test(myreplace(" ", "**",
                   "Words will now      be  separated by stars.") ==
         "Words**will**now**be**separated**by**stars.")
test_suite()        # Here is the call to run the tests