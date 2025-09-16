import turtle
turtle.tracer(5, 0) # makes the drawing fast
turtle.hideturtle() # hides the arrow for aesthetics
turtle.penup() # pen is lifted until needed


def triangle(size, loc):
    """ Draws an equilateral triangle pointing north. 
    Parameters: 
        size (int):  side length 
        loc (turtle.Vec2D): location of the bottom left corner
    """
    turtle.goto(loc) # go to the starting location
    turtle.setheading(60) # point upward at a 60 degree angle

    turtle.pendown() # start drawing
    for i in range(3):
        turtle.forward(size) 
        turtle.right(120)
    turtle.penup() # stop drawing


def sierpinsky(size, loc):
    """ Draws a sierspinsky triangle. 
    Parameters: 
        size (int):  side length 
        loc (turtle.Vec2D): location of the bottom left corner
    """


    # your code goes here
    return



turtle.goto(-200,-200) # move for a centered triangle
start_loc = turtle.pos() # get my current position
sierpinsky(400, start_loc) # call recursive function

turtle.exitonclick() # drawing stays on screen