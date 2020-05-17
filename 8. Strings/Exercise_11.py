"""
Write a function that counts how many times a substring occurs in a string:

test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 4)
"""

import sys


# COPIED FROM https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnx1c2ZjYWl4Y2FjZXJlc2NzMTEwfGd4OjM2M2NkYTVjZTg5OTNlNWE
# TRIED EVERYTHING, BUT COULD NOT SOLVED IT.
def count(sub, s):
	count = 0
	v = len(sub)
	index = 0
	while index < len(s):
		sub_strng = s[index: index + v]
		if sub_strng == sub:
			count += 1
		index += 1
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
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)

test_suite()        # Here is the call to run the tests
