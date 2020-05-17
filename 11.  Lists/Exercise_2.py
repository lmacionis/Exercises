"""
Consider this fragment of code:

import turtle

tess = turtle.Turtle()
alex = tess
alex.color("hotpink")
Does this fragment create one or two turtle instances? Does setting the color
of alex also change the color of tess? Explain in detail.
"""

# This program creates one turtle instance, so if you are changing the color
# of alex, color of tess also being changed.
# I think so, my proof is below.
import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
alex = tess
alex.color("hotpink")

alex.forward(20)
tess.forward(-20)

wn.mainloop()