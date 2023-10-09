from turtle import *

### Functions
# Modify code in this section
speed(0)

def star():
    for _ in range(5):
    # Loop to draw a single star
        for _ in range(1):
            forward(30)  # Move forward by 100 units
            right(144)    # Turn right by 144 degrees
    
    # Move the turtle to the starting position for the next star
    penup()
    forward(70)  # Move forward to create space between stars
    pendown()



### The main code that gets run
# Do not modify anything after this line

for i in range(13):
    star()
    penup()
    right(360/13)
    forward(5)
    pendown()


done()
