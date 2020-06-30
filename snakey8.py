#! python3
# This is a classic game of snake written in Python3 utlizing the turtle module.
# By @cyberpayload

import turtle

# Setting up screenplay

window = turtle.Screen()                    # creates application object
window.title("Snakey8")                     # sets application title name
window.bgcolor("yellow")                    # sets play area background color
window.setup(width=800, height=800)         # sets size of play area
window.tracer(0)                            # turns off screen updates

# Snakehead
head = turtle.Turtle()                      # creates the turle object
head.speed(0)                               # animation speed of the turtle
head.shape("square")                        # shape of the snake head
head.color("black")                         # color of the snake head
head.penup()                                # this allows the snake to NOT draw when moving (pen is up)
head.goto(0,0)                              # set the snake in the center
head.direction = "up"                       # direction of snake head during start of game

# Functions
def move():                                 # defining the function called "move" for the behavior of the snake
    if head.direction == "up":              # creating if statement for positive vertical movement
        y = head.ycor()                     # creating variable y and setting it to y coordinate with no arguement
        head.sety(y + 20)                   # calling the set method and giving it a positive vertial coordinate from its current location

# Main game loop
while True:
    window.update()


move()
window.mainloop()                           # creates main window loop