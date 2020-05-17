"""
Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:

test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
Hint: use the split and join methods.
"""

import sys

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"

# modified by me
def replace(s, old, new):
    new_string = ""
    for word in s.split():
        s.split(old)
        new_string = new.join(s.split(old))
    return new_string


""""
# by the book, done by me.
def replace(s, old, new):
    new_string = ""
    for word in s.split():
        wds = s.split(old)
        glue = new
        new_string = glue.join(wds)
    return new_string
"""


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
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    test(replace(s, "om", "am") ==
         "I love spam! Spam is my favorite food. Spam, spam, yum!")
    test(replace(s, "o", "a") ==
         "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

test_suite()        # Here is the call to run the tests
