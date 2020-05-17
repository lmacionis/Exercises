# Modify the turtle bar chart program so that the pen is up for the small gaps between each bar.

import turtle


def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)        # Draw up the left side
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)            # Width of bar, along the top
    t.right(90)
    t.forward(height)        # And down again!
    t.left(90)
    t.end_fill()             # Added this line
    t.penup()                # Raising the pen up
    t.forward(10)            # Put the turtle facing the way we found it.
    t.pendown()              # Putting the pen down


wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220]

for a in xs:                 # Assume xs and tess are ready
    draw_bar(tess, a)

wn.mainloop()
