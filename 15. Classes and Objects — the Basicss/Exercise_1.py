"""
Rewrite the distance function from the chapter titled Fruitful functions so that it takes two
Points as parameters instead of four numbers.
"""
# If I understood the condition correctly, then the answer should be good.
import math


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0


p = Point()
q = Point()
print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y


def distance(p, q):
    return math.sqrt((q.x-p.x)**2 + (q.y-p.y)**2)


p.x = 1
p.y = 2
q.x = 4
q.y = 6
print(distance(p, q))
