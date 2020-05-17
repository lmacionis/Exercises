"""
Draw a state snapshot for a and b before and after the third line of the following Python code is executed:

a = [1, 2, 3]
b = a[:]
b[0] = 5
"""

a = [1, 2, 3]
b = a[:]
print(a == b)  # True

a = [1, 2, 3]
b = a[:]
b[0] = 5

print(a == b)  # False
print(a is b)  # False, because its the same as above
