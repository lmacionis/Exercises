class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0


p = Point()         # Instantiate an object of type Point
q = Point()         # Make a second point

print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y


p.x = 3
p.y = 4

print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y

print(p.y)
x = p.x
print(x)

print("(x={0}, y={1})".format(p.x, p.y))
distance_squared_from_origin = p.x * p.x + p.y * p.y
print(distance_squared_from_origin)

p = Point()
p.x = 7
p.y = 6


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

# Other statements outside the class continue below here.
q = Point()

p = Point(4, 2)
q = Point(6, 3)
r = Point()       # r represents the origin (0, 0)
print(p.x, q.y, r.x)


class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


p = Point(3, 4)
print(p.x)
print(p.y)
print(p.distance_from_origin())
q = Point(5, 12)
print(q.x)
print(q.y)
print(q.distance_from_origin())
r = Point()
print(r.x)
print(r.y)
print(r.distance_from_origin())


def print_point(pt):
    print("({0}, {1})".format(pt.x, pt.y))


print_point(p)


class Point:
    # ...

    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)


    p = Point(3, 4)
print(p.to_string())


class Point:
    # ...

    def __str__(self):  # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)


str(p)     # Python now uses the __str__ method that we wrote.
print(p)


def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)


class Point:
   # ...

   def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)


p = Point(3, 4)
