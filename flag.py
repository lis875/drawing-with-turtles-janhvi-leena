from turtle import *

### Functions for drawing
# Modify the code in this function
speed(0)
def bar(bar_color):
    begin_fill()  # Begin filling the shape
    fillcolor(bar_color)  # Set the fill color
    for _ in range(2):
        forward(300)
        right(90)
        forward(50)
        right(90)
    end_fill()  # End filling the shape

def star(size):
    begin_fill()
    fillcolor("black")
    for i in range(5):
        forward(size)
        right(144)
    end_fill()    
    penup()
    forward(100)
    pendown()
    

### Main code that gets run, to draw the German flag
# Do not modify code below this line for Exercise 7. It is OK to add code below this for Exercise 8
penup()
back(100)
pendown()
bar("black")
right(90)
forward(50)
left(90)
bar("red")
right(90)
forward(50)
left(90)
bar("yellow")
right(90)

back(30); left(90); 
penup()
forward(125)
pendown()
star(52)






done()
