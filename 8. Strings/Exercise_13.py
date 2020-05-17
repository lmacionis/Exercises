"""
Write a function that removes all occurrences of a string from another string:

test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")
"""

import sys

# STILL DONT UNDERSTAND A FUCK. https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnx1c2ZjYWl4Y2FjZXJlc2NzMTEwfGd4OjM2M2NkYTVjZTg5OTNlNWE
# THIS FUNCTION ONLY REPEATS FUNCTION REMOVE UNTIL IT REMOVES ALL THE STR1 FROM STR2
def remove_all(str1, str2):
    while str1 in str2:
        str2 = remove(str1, str2)
    return str2


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
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")

test_suite()        # Here is the call to run the tests