# Write a function find_hypot which, given the length of two sides of a right-angled triangle,
# returns the length of the hypotenuse. (Hint: x ** 0.5 will return the square root.)


def find_hypot(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c


a = int(input("Length of one side: "))
b = int(input("Length of second side: "))

print(find_hypot(a, b))