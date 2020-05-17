"""
Count how many words occur in a list up to and including the first occurrence of the word “sam”.
(Write your unit tests for this case too. What if “sam” does not occur?)
"""

import sys

def count_words(list, s = "sam"):
    count = 0
    for i in list:
        count = count + 1
        if i == s:
            break
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
    test(count_words(["as", "tu", "sam", "ji"]) == 3)
    test(count_words(["sam", "as"]) == 1)
    test(count_words(["as", "tu", "ji"]) == 3)
    test(count_words(["as", "tu", "ji", "sam"]) == 4)

test_suite()        # Here is the call to run the tests