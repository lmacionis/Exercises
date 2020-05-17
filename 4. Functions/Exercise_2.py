# Write a program to draw this. Assume the innermost square is 20 units per side, and each successive square is 20
# units bigger, per side, than the one inside it.

import turtle


def square(t, sz):
    """ Make a turtle t draw a square of sz. """
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()  # Set up the window and its attributes.
wn.bgcolor("lightgreen")
wn.title("Square")

alex = turtle.Turtle()  # Create alex and set up alex turtle.
alex.pensize(3)
alex.color("hot pink")
alex.speed(3)

size = 20  # Define variables.
mv = -10

for i in range(10):
    square(alex, size)  # Calling function.
    size += 20  # Increasing size of the square.
    """ Position of the square."""
    alex.penup()
    alex.goto(mv, mv)
    alex.pendown()
    mv -= 10

wn.exitonclick()
