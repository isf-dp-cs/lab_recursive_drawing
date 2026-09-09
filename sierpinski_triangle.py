from turtle import *

def triangle(side_length):
    """Draws an equilaterial triangle"""
    
    for i in range(3):
        forward(side_length) 
        left(120)


def sierpinsky(n, side_length):
    """ Draws a sierspinsky triangle."""

    # 💻 TODO: Construct this recurisve function 






if __name__ == "__main__":
    speed(9)            # 1 is slowest, 0 is fastest
    penup()
    goto(-200,200)      # centers triangle
    pendown()

    sierpinsky(4,50)
         
    input()             # keeps window open