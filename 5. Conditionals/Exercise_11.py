# Write a function is_rightangled which, given the length of three sides of a triangle,
# will determine whether the triangle is right-angled. Assume that the third argument to
# the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

# Hint: Floating point arithmetic is not always exactly accurate, so it is not safe to
# test floating point numbers for equality. If a good programmer wants to know whether x
# is equal or close enough to y, they would probably code it up as:

# if  abs(x-y) < 0.000001:    # If x is approximately equal to y
#     ...


def is_right(x, y, z):
	hypot = ((x ** 2 + y **2) ** 0.5)

	if abs(z - hypot) < 0.001:
		return True
	else:
		return False


print(is_right(5, 5, 7.071))
