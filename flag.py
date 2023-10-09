from turtle import *

### Functions for drawing
# Modify the code in this function

def bar(bar_color):
    begin_fill()  # Begin filling the shape
    fillcolor(bar_color)  # Set the fill color
    for _ in range(2):
        forward(300)
        right(90)
        forward(50)
        right(90)
    end_fill()  # End filling the shape

### Main code that gets run, to draw the German flag
# Do not modify code below this line for Exercise 7. It is OK to add code below this for Exercise 8

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
forward(50)
left(90)
forward(300)
left(90)

# Add line in between
left(90)
forward(50)
left(90)




done()
