"""
In games, we often put a rectangular “bounding box” around our sprites.
(A sprite is an object that can move about in the game, as we will see shortly.)
We can then do collision detection between, say, bombs and spaceships,
by comparing whether their rectangles overlap anywhere.

Write a function to determine whether two rectangles collide.
Hint: this might be quite a tough exercise! Think carefully about all the cases before you code.
"""
# It should be good, but I'm not sure how to check it. That means tests can be bad.
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Rect:
    def __init__(self, p1, p2):
        self.left = min(p1.x, p2.x)
        self.right = max(p1.x, p2.x)
        self.bottom = min(p1.y, p2.y)
        self.top = max(p1.y, p2.y)

    def __str__(self):
        return "({0}, {1}, {2}, {3})".format(self.left, self.right, self.bottom, self.top)

    def collide(r1, r2):
        if (r1.left <= r2.right) and (r1.right >= r2.left):
            return True

        if (r1.bottom <= r2.top) and (r1.top >= r2.bottom):
            return True

        return False


p1 = Point(1, 1)
p2 = Point(3, 3)
r1 = Rect(p1, p2)
p3 = Point(2, 2)
p4 = Point(4, 4)
r2 = Rect(p3, p4)
print(r1.collide(Rect(p1, p2)))
print(r2.collide(Rect(p2, p1)))
