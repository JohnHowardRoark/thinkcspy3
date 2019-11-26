""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 10: Exercise 01
"""

import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
tess = turtle.Turtle()               # Create our favorite turtle
PenSize = 1
tess.pensize(PenSize)
background_colors = ["lightgreen", "lightblue", "lightgray", "yellow"]
current_color = 0
wn.bgcolor(background_colors[current_color]) # Set the background color

# The next four functions are our "event handlers".
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()                        # Close down the turtle window

def h5():
    tess.color("red")

def h6():
    tess.color("green")

def h7():
    tess.color("blue")

def h8():
    global PenSize
    PenSize += 1
    if PenSize > 20:
        PenSize = 20
    tess.pensize(PenSize)

def h9():
    global PenSize
    PenSize -= 1
    if PenSize < 1:
        PenSize = 1
    tess.pensize(PenSize)


def h10():
    global background_colors
    global current_color
    current_color = (current_color + 1) % 4
    wn.bgcolor(background_colors[current_color])


# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "r")
wn.onkey(h6, "g")
wn.onkey(h7, "b")
""" using the "+" key generates an error. Also did not work if chr(43) was used instead. Had to select another key for the function to increase pen size. """
wn.onkey(h8, "0")
wn.onkey(h9, "-")
wn.onkey(h10, "space")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()