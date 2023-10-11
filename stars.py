from turtle import *
import random

### Functions
# Modify code in this section
speed(0)
penup()
left(90)
forward(100)
right(90)
pendown()
def star(radius):
    for _ in range(5):
        forward(radius)  # Move forward by 100 units
        right(144)    # Turn right by 144 degrees
    
    # Move the turtle to the starting position for the next star
    penup()
    forward(70)  # Move forward to create space between stars
    pendown()



### The main code that gets run
# Do not modify anything after this line

for i in range(13):
    size = random.randint(10,60)
    star(size)
    penup()
    right(360/13)
    forward(5)
    pendown()


done()
