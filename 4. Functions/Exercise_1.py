# Write a void (non-fruitful) function to draw a square. Use it in a program to draw the image shown below. Assume
# each side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last
# square when the program ends.)

import turtle


def square(t, sz):
    """ Make a turtle t draw a square of sz. """
    for i in range(4):
        t.forward(sz)
        t.left(90)
    """ Position of the square. """
    t.penup()
    t.forward(40)
    t.pendown()


wn = turtle.Screen()  # Set up the window and its attributes.
wn.bgcolor("lightgreen")
wn.title("Square")

alex = turtle.Turtle()  # Set up alex turtle.
alex.pensize(3)
alex.color("hot pink")

alex.penup()  # Starting position of the square.
alex.forward(-100)
alex.pendown()

square(alex, 20)  # Call function.
square(alex, 20)
square(alex, 20)
square(alex, 20)
square(alex, 20)

wn.mainloop()  # Wait for user to close window.
