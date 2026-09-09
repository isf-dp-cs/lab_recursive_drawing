from turtle import *

def triangle(side_length):
    """Draws an equilaterial triangle"""
    
    for i in range(3):
        forward(side_length) 
        left(120)


def sierpinsky(n, side_length):
    """ Draws a sierspinsky triangle."""
    if n== 1:
        triangle(side_length)

    else:
        sierpinsky(n-1,side_length) # call recursive function
        forward(side_length)
        sierpinsky(n-1,side_length)


        left(120)
        forward(side_length)
        right(120)

        sierpinsky(n-1,side_length)

        left(60)
        back(side_length)
        right(60)
        

if __name__ == "__main__":

    # set up position and speed
    speed(9)    # 1 is slowest, 0 is fastest
    penup()
    goto(-200,200)
    pendown()

    # Draw tree
    sierpinsky(4,50)
         

    # Keep the window open until clicked
    input()