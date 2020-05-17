# Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units,
# turn right by 144, put the pen down, and draw the next star. You’ll get something like this:

import turtle


def star(t, sz):  # Function for a star.
    for i in range(5):
        t.forward(sz)
        t.right(144)


def five_star(t, n):  # Function for putting a turtle in a different position.
    for i in range(1):
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()


wn = turtle.Screen()  # Setting up a turtle window.
wn.bgcolor("lightgreen")
wn.title("Stars")

tess = turtle.Turtle()  # Setting up a turtle.
tess.pensize(3)
tess.color("hot pink")

star(tess, 100)  # Calling functions.
five_star(tess, 1)
star(tess, 100)
five_star(tess, 1)
star(tess, 100)
five_star(tess, 1)
star(tess, 100)
five_star(tess, 1)
star(tess, 100)
five_star(tess, 1)

wn.mainloop()  # Wait for user to close a window.
