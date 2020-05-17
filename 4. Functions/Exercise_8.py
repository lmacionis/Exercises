# Write a function area_of_circle(r) which returns the area of a circle of radius r.

import math  # importing math because of pi


def area_of_circle(r):
    """ Formula of the circle area"""
    s = math.pi * r ** 2
    return s  # Makes a function fruitful.


# now that we have the function above, let us call it.
r = int(input("Radiuis of a cicrle: "))
s = area_of_circle(r)
print(s)
