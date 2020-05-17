"""
Many interesting shapes can be drawn by the turtle by giving a list of pairs like we did above,
where the first item of the pair is the angle to turn, and the second item is the distance to move forward.
Set up a list of pairs so that the turtle draws a house with a cross through the centre, as shown here.
This should be done without going over any of the lines / edges more than once, and without lifting your pen.

_images/tess_house.png
"""

import turtle

wn = turtle.Screen()
wn.bgcolor("hotpink")
wn.title("House")

pirate = turtle.Turtle()

# Good example off the loop for the list.
for angle, steps in [(0, 100), (135, 140), (135, 100), (135, 140),
                    (135, 100), (-135, 70), (270, 70), (315, 100)]:

    pirate.left(angle)
    pirate.forward(steps)


wn.mainloop()