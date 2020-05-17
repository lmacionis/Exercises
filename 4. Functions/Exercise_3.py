# Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular polygon. When called with draw_poly(
# tess, 8, 50), it will draw a shape like this:

import turtle


def draw_poly(t, n, sz):
    angle = 360 / n  # Define variables.
    for i in range(n):
        t.forward(sz)
        t.left(angle)


wn = turtle.Screen()  # Set up the window and its attributes.
wn.bgcolor("lightgreen")
wn.title("Draw_poly")

tess = turtle.Turtle()  # Create tess and set up tess turtle.
tess.pensize(3)
tess.color("hot pink")
tess.speed(3)

draw_poly(tess, 8, 50)  # Calling function.

wn.exitonclick()
