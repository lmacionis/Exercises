"""
In an earlier chapter we saw two turtle methods, hideturtle and showturtle that
can hide or show a turtle. This suggests that we could take a different approach
to the traffic lights program. Add to your program above as follows: draw a
second housing for another set of traffic lights. Create three separate turtles
to represent each of the green, orange and red lights, and position them
appropriately within your new housing. As your state changes occur, just make
one of the three turtles visible at any time. Once you’ve made the changes,
sit back and ponder some deep thoughts: you’ve now got two different ways to
use turtles to simulate the traffic lights, and both seem to work. Is one
approach somehow preferable to the other? Which one more closely resembles
reality — i.e. the traffic lights in your town?
"""

import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
green_light = turtle.Turtle()
red_light = turtle.Turtle()
orange_light = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


def second_housing():
    for i in range(1):
        tess.penup()
        tess.right(180)
        tess.forward(90)
        tess.right(180)
        tess.pendown()


def green_light_position():
    green_light.penup()
# Position of a green light
    green_light.forward(40)
    green_light.left(90)
    green_light.forward(50)
# Turning a green light into a big circle
    green_light.shape("circle")
    green_light.shapesize(3)
    green_light.fillcolor("green")


def orange_light_position():
    orange_light.penup()
# Position of an orange light
    orange_light.forward(40)
    orange_light.left(90)
    orange_light.forward(120)
# Turning an orange light into a big circle
    orange_light.shape("circle")
    orange_light.shapesize(3)
    orange_light.fillcolor("orange")


def red_light_position():
    red_light.penup()
# Position of a red light
    red_light.forward(40)
    red_light.left(90)
    red_light.forward(190)
# Turning a red light into a big circle
    red_light.shape("circle")
    red_light.shapesize(3)
    red_light.fillcolor("red")


def tess_position():
    tess.penup()
# Position tess onto the place where the green light should be
    tess.forward(40)
    tess.left(90)
    tess.forward(50)
# Turn tess into a big green circle
    tess.shape("circle")
    tess.shapesize(3)
    tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine


state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine, "200")  # SETING A TIMER IT IS COUNTING TIME IN A MILISECONDS
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
        wn.ontimer(advance_state_machine, "700")  # SETING A TIMER IT IS COUNTING TIME IN A MILISECONDS
    else:                    # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
        wn.ontimer(advance_state_machine, "1000")  # SETING A TIMER IT IS COUNTING TIME IN A MILISECONDS


# This variable holds the current state of the machine
state_num1 = 0


def new_state_machine():
    global state_num1
    if state_num1 == 0:        # Transition from state 0 to state 1
        green_light.hideturtle()            # Hiding green turtle
        red_light.hideturtle()              # Hiding red turtle
        orange_light.fillcolor("orange")
        wn.ontimer(new_state_machine, 200)  # SETING A TIMER IT IS COUNTING TIIME IN A MILISECONDS
        orange_light.showturtle()
        state_num1 = 1
    elif state_num1 == 1:      # Transition from state 1 to state 2
        orange_light.hideturtle()           # Hiding orange turtle
        green_light.hideturtle()            # Hiding green turtle
        red_light.fillcolor("red")
        wn.ontimer(new_state_machine, 700)  # SETING A TIMER IT IS COUNTING TIIME IN A MILISECONDS
        red_light.showturtle()
        state_num1 = 2
    else:                 # Transition from state 2 to state 0
        red_light.hideturtle()              # Hiding red turtle
        orange_light.hideturtle()           # Hiding orange turtle
        green_light.fillcolor("green")
        wn.ontimer(new_state_machine, 1000)
        green_light.showturtle()
        state_num1 = 0


# CALLING FUNCTIONS
draw_housing()
green_light_position()
red_light_position()
orange_light_position()
second_housing()
draw_housing()
tess_position()
# NEED TO CALL A FUNCTION, BECOUSE WHEN ONE SETS A TIMER IT ONLY GOES ONCE
advance_state_machine()
new_state_machine()

wn.listen()                      # Listen for events
wn.mainloop()