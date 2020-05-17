# Write a void function to draw a star, where the length of each side is 100 units.
# (Hint: You should turn the turtle by 144 degrees at each point.)

import turtle


def star(t, sz):
    for i in range(5):
        t.forward(sz)
        t.right(144)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Star")

tess = turtle.Turtle()
tess.pensize(3)
tess.color("hot pink")

star(tess, 100)
wn.mainloop()
