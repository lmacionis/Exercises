"""
Add a method reflect_x to Point which returns a new Point,
one which is the reflection of the point about the x-axis.
For example, Point(3, 5).reflect_x() is (3, -5)
"""
class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def reflect_x(self):    # Adding a new method
        """Reflecting the point about x-axis."""
        return self.x, -self.y

# Other statements outside the class continue below here.
p = Point(3, 5)
print(p.x)
print(p.y)
print(p.reflect_x())