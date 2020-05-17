"""
Given four points that fall on the circumference of a circle, find the midpoint of the circle.
When will this function fail?
Hint: You must know how to solve the geometry problem before you think of going anywhere near programming.
You cannot program a solution to a problem if you don’t understand what you want the computer to do!
"""

# It should be good, because I found the formula in the
# https://en.wikipedia.org/wiki/Circumscribed_circle#Circumcenter_coordinates
# I could count the formula my self, but nowadays I would need a whole day for it, not 5min.:D
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, target, target2, target3):   # I don't use the third point because 3 points is more than enough to find the midpoint.
        d = 2 * (self.x * (target.y - target2.y) + target.x * (target2.y - self.y) + target2.x * (self.y - target.y))
        a = ((self.x**2 + self.y**2) * (target.y - target2.y) + (target.x**2 + target.y**2) *
             (target2.y - self.y) + (target2.x**2 + target2.y**2) * (self.y - target.y)) / d
        b = ((self.x**2 + self.y**2) * (target2.x - target.x) + (target.x**2 + target.y**2) *
             (self.x - target2.x) + (target2.x**2 + target2.y**2) * (target.x - self.x)) / d
        return a, b
