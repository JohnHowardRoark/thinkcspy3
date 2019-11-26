""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 10: Exercise 03
"""
import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.hideturtle()
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
    tess.penup()


def h1():
    global state_num
    wn.bye()


def advance_state_machine():
    global state_num
    tess_green.hideturtle()
    tess_orange.hideturtle()
    tess_red.hideturtle()
    
    if state_num == 0:       # Transition from state 0 to state 1
        tess_green.showturtle()
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        tess_orange.showturtle()
        state_num = 2
    else:                    # Transition from state 2 to state 0
        tess_red.showturtle()
        state_num = 0

    wn.onkey(h1, "space")
    wn.ontimer(advance_state_machine, 500)


""" Make all three turtles for the lights"""
tess_green = turtle.Turtle()
tess_green.hideturtle()
tess_green.penup()
tess_green.goto(40, 50)
tess_green.shape("circle")
tess_green.shapesize(3)
tess_green.fillcolor("green")

tess_orange = turtle.Turtle()
tess_orange.hideturtle()
tess_orange.penup()
tess_orange.goto(40, 120)
tess_orange.shape("circle")
tess_orange.shapesize(3)
tess_orange.fillcolor("orange")

tess_red = turtle.Turtle()
tess_red.hideturtle()
tess_red.penup()
tess_red.goto(40, 190)
tess_red.shape("circle")
tess_red.shapesize(3)
tess_red.fillcolor("Red")

wn.listen()

state_num = 0
draw_housing()
advance_state_machine()

wn.mainloop()