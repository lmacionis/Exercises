# In the turtle bar chart program, what do you expect to happen if one or more of the data values in the list is
# negative? Try it out. Change the program so that when it prints the text value for the negative bars, it puts the
# text below the bottom of the bar.

import turtle


def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    if height < 0:           # Writes the height, before drawing a bar.
        t.write("  " + str(height))
    t.left(90)
    t.forward(height)        # Draw up the left side
    if height >= 0:          # Writes the height, after you get one line of your bar.
        t.write("  " + str(height))
    t.right(90)
    t.forward(40)            # Width of bar, along the top
    t.right(90)
    t.forward(height)        # And down again!s
    t.left(90)
    t.end_fill()             # Added this line
    t.penup()                # Raising the pen up
    t.forward(10)            # Put the turtle facing the way we found it.
    t.pendown()              # Putting the pen down


wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
# tess.color("blue", "red")
tess.pensize(3)

xs = [48, -117, 200, 240, 160, 260, 220]

""" Seting up the color and calling a function draw_bar(t, height) """


def fill_color(t, height):
    if height >= 200:
        t.color("red")
    elif height >= 100 and height < 200:
        t.color("yellow")
    else:
        t.color("green")

    draw_bar(t, height)


for a in xs:                 # Assume xs and tess are ready
    fill_color(tess, a)

wn.mainloop()
