"""
Revisit the drunk pirate problem from the exercises in chapter 3.
This time, the drunk pirate makes a turn, and then takes some steps forward,
and repeats this. Our social science student now records pairs of data: the
angle of each turn, and the number of steps taken after the turn.
Her experimental data is [(160, 20), (-43, 10), (270, 8), (-43, 12)].
Use a turtle to draw the path taken by our drunk friend.
"""

import turtle

wn = turtle.Screen()
wn.bgcolor("hotpink")
wn.title("Pirate")

pirate = turtle.Turtle()

# Good example off the loop for the list.
for angle, steps in [(160, 20), (-43, 10), (270, 8), (-43, 12)]:
    pirate.left(angle)
    pirate.forward(steps)


wn.mainloop()

