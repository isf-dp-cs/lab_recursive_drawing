from turtle import *

def draw_tree(length):
    if length < 20:
        return

    # 💻 TODO: Construct this recurisve function 




if __name__ == "__main__":
    speed(9)            # 1 is slowest, 0 is fastest
    left(90)
    penup()
    goto(0,-200)        # centers tree 
    pendown()
    pensize(5)          # changes pen size
    pencolor('green')   # changes pen color 

    draw_tree(100)              

    
    input()             # keeps window open
    