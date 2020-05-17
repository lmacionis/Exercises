"""
What will be the output of the following program?

this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))
Provide a detailed explanation of the results.
"""

# Mine explanation
this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
# Ats.: Test 1: False
# a and b have the same value but do not refer to the same object.
that = this         # This makes list refer to the same object.
print("Test 2: {0}".format(this is that))
# Ats.: Test 2: True
# This tells us that both a and b refer to the same object,

# Found in a google
"""
Initially, this and that are initialized to the same value. 
he first condition tests if the objects "this " and "that" are the same, 
and the result is False because "this" and "that" are different objects even 
though they have the same values. The second condition is True because after the 
first test, the variables that = this, and so the condition: this is that, is True afterall.
"""
