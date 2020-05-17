"""
The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + c”).
The coefficients a and b completely describe the line.
Write a method in the Point class so that if a point instance is given another point,
it will compute the equation of the straight line joining the two points.
It must return the two coefficients as a tuple of two values. For example,
print(Point(4, 11).get_line_to(Point(6, 15)))
(2, 3)
This tells us that the equation of the line joining the two points is “y = 2x + 3”. When will this method fail?
"""
# You can also use more methods here.
class Point:
   # ...
   def __init__(self, x=0, y=0):
       """ Create a new point at x, y """
       self.x = x
       self.y = y

   def get_line_to(self, target):
       a = (target.y*self.x - self.y*self.x) / (target.x - self.x) / self.x
       b = self.y - a * self.x
       return (a, b), "y = " + str(a) + "x + " + str(b)


print(Point(4, 11).get_line_to(Point(6, 15)))