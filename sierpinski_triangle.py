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
    """ Draws an equilateral triangle pointing north. 
    Parameters: 
        size (int):  side length 
        loc (turtle.Vec2D): location of the bottom left corner
    """
    
    turtle.goto(loc)
    turtle.setheading(60)

    if size <= 20: # base case
        triangle(size, loc) # draw a triangle
    else:
        loc1 = turtle.pos() # get loc for first triangle
        
        turtle.goto(loc) # return to bottom left
        turtle.forward(size/2) # find midpoint of bottom
        loc2 = turtle.pos() # get loc for second triangle

        turtle.goto(loc) # return to bottom left
        turtle.right(60) 
        turtle.forward(size/2) # find midpoint of left side
        loc3 = turtle.pos() # get loc for third triangle


        sierpinsky(size/2, loc1,) # recursive call
        sierpinsky(size/2, loc2) # recursive call
        sierpinsky(size/2, loc3) # recursive call




turtle.goto(-200,-200) # move for a centered triangle
start_loc = turtle.pos() # get my current position
sierpinsky(400, start_loc) # call recursive function

turtle.exitonclick() # drawing stays on screen