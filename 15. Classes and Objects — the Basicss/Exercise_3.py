"""
Add a method slope_from_origin which returns the slope of the line joining the origin to the point. For example,
Point(4, 10).slope_from_origin()
2.5
What cases will cause this method to fail?
"""
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def slope_from_origin(self):
        return self.y / self.x


print(Point(4, 10).slope_from_origin())
# It will fail if there will be given to points and I will need to find a slope between them.
