from turtle import *

def line(depth, length):

    if depth == 0:
        forward(length)

    line(depth-1,length//3)
    left(60)
    line(depth-1,length//3)
    right(120)
    line(depth-1,length//3)
    left(60)
    line(depth-1,length//3)




if __name__ == "__main__":

    # set up position and speed
    speed(9)    # 1 is slowest, 0 is fastest


    # Draw tree
    line(2,200)              

    # Keep the window open until clicked
    exitonclick()
    