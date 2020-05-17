# Write a void function draw_equitriangle(t, sz) which calls draw_poly from the previous question to have its turtle
# draw a equilateral triangle.

import turtle


def draw_poly(t, n, sz):
    """Will draw 'n'-sided polygon having sides of 'sz' in length."""
    for i in range(n):
        t.forward(sz)
        t.left(360 / n)


def draw_equitriangle(t, sz):
    """Will draw an equilateral triangle having sides of 'sz' in length."""
    draw_poly(t, 3, sz)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

draw_equitriangle(tess, 100)

wn.mainloop()
