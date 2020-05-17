"""
Write a function that removes the first occurrence of a string from another string:

test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") == "bicycle")
"""

import sys

# DOTN HAVE A SLIGHTEST CLUE WHAT THE FUCK I AM DOING HERE
#COPIED FROM https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnx1c2ZjYWl4Y2FjZXJlc2NzMTEwfGd4OjM2M2NkYTVjZTg5OTNlNWE
def remove(str1, str2):
    index = 0
    while index < len(str2):
        if str1 == str2[index: index + len(str1)]:
            return str2[ : index] + str2[index+ len(str1): ]
        index += 1
    return str2


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
    test(remove("an", "banana") == "bana")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")

test_suite()        # Here is the call to run the tests