from turtle import *

def draw_tree(length):
    # BASE CASE: Stop when the branches get too short

    if length < 20:
        return

    forward(length)

    left(20)
    draw_tree(length-20)

    right(40)
    draw_tree(length-20)

    left(20)
    back(length)


if __name__ == "__main__":

    # set up position and speed
    speed(9)    # 1 is slowest, 0 is fastest
    left(90)
    penup()
    goto(0,-200)
    pendown()
    pensize(5)
    pencolor('green')

    # Draw tree
    draw_tree(100)              

    # Keep the window open
    input()
    