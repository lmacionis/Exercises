# Draw this pretty pattern.

import turtle


def pretty_pattern(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()  # Set up the window and its atributes.
wn.bgcolor("lightgreen")
wn.title("Pretty pattern")

tess = turtle.Turtle()  # Create tess and set up tess turtle.
tess.pensize(3)
tess.color("hot pink")
tess.speed(3)

n = 20  # Define variables.
angle = 360 / n

for i in range(n):
    pretty_pattern(tess, 100)  # Calling function.
    tess.left(angle)

wn.mainloop()  # Wait for user to close window.
