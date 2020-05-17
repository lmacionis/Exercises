# The two spirals in this picture differ only by the turn angle. Draw both.

import turtle


def spiral(t, sz):              # Function.
    for i in range(1):
        t.forward(sz)
        t.right(angle)
        t.forward(sz)
        tess.right(angle)


wn = turtle.Screen()            # Set up the window and its attributes.
wn.bgcolor("lightgreen")
wn.title("Spirals")

tess = turtle.Turtle()          # Create tess and set up tess turtle.
tess.color("hot pink")
tess.speed(6)

n = 40                          # Define variables.
sz = 5
angle = 90

tess.penup()                    # Turtles position
tess.forward(-200)
tess.pendown()

for i in range(n):
    spiral(tess, sz)            # Calling function.
    sz += 5

tess.stamp()                    # Turtles last position on the spiral, when finished.

tess.penup()                    # Turtles new position for the new spiral.
tess.goto(200, 0)
tess.pendown()

angle = 89                      # Redefine variables.
sz = 5

for i in range(n):
    spiral(tess, sz)            # Calling function.
    sz += 5

tess.stamp()                    # Turtles last position on the spiral, when finished.

wn.mainloop()                   # Wait for user to close window.
