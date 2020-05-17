"""
Add a method area to the Rectangle class that returns the area of any instance:
r = Rectangle(Point(0, 0), 10, 5)
test(r.area() == 50)
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


box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)    # In my video game
print("box: ", box)
print("bomb: ", bomb)
r = Rectangle(Point(0, 0), 10, 5)
test(r.area() == 50)
