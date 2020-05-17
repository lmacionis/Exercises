"""
Write a new method in the Rectangle class to test if a Point falls within the rectangle.
For this exercise, assume that a rectangle at (0,0) with width 10 and height 5 has open
upper bounds on the width and height, i.e. it stretches in the x direction from [0 to 10),
where 0 is included but 10 is excluded, and from [0 to 5) in the y direction.
So it does not contain the point (10, 2). These tests should pass:
r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))
"""
import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):  # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return ("({0}, {1}, {2})"
                  .format(self.corner, self.width, self.height))

    def area(self):
        s = self.width * self.height
        return s

    def perimeter(self):
        p = (self.width + self.height) * 2
        return p

    def flip(self):
        y = self.width
        self.width = self.height
        self.height = y

    def contains(self, item):
        # I think that you can do this without 0, but I couldn't figure it out.
        return (0 <= item.x < self.width) and (0 <= item.y < self.height)


box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)    # In my video game
print("box: ", box)
print("bomb: ", bomb)
r = Rectangle(Point(0, 0), 10, 5)
test(r.area() == 50)
r = Rectangle(Point(0, 0), 10, 5)
test(r.perimeter() == 30)
r = Rectangle(Point(100, 50), 10, 5)
test(r.width == 10 and r.height == 5)
r.flip()
test(r.width == 5 and r.height == 10)
r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))

