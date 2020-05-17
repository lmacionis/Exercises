"""
Add some new key bindings to the first sample program:

Pressing keys R, G or B should change tess color to Red, Green or Blue.

# THIS PARTS EXP. FOUND IN A STACKOVERFLOW!
Pressing keys + or - should increase or decrease the width of tess pen.
Ensure that the pen size stays between 1 and 20 (inclusive).

Handle some other keys to change some attributes of tess, or attributes of the
window, or to give her new behaviour that can be controlled from the keyboard.
"""

import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle

# The next four functions are our "event handlers".
def h1():
   tess.forward(30)


def h2():
   tess.left(45)


def h3():
   tess.right(45)


def h4():
    tess.color("red")


def h5():
    tess.color("green")


def h6():
    tess.color("blue")


def h7():
    size = tess.pensize()
    if size < 20:
        tess.pensize(size + 1)


def h8():
    size = tess.pensize()
    if size > 1:
        tess.pensize(size - 1)


def h9():
    wn.bye()                        # Close down the turtle window


def bg_color():
    wn.bgcolor("black")


def pen_shape_cirkle():
    tess.shape("circle")


def stamp():
    tess.stamp()


# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "r")
wn.onkey(h5, "g")
wn.onkey(h6, "b")
wn.onkey(h7, "+")
wn.onkey(h8, "-")
wn.onkey(h9, "q")
wn.onkey(bg_color, 1)
wn.onkey(pen_shape_cirkle, 2)
wn.onkey(stamp, 3)

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()