#! python3
# This is a classic game of snake written in Python3 utlizing the turtle module.
# By @cyberpayload

import turtle
import time

delay = 0.1

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

    if head.direction == "down":            # creating if statement for negative vertical movement
        y = head.ycor()                     # creating variable y and setting it to y coordinate with no arguement
        head.sety(y - 20)                   # calling the set method and giving it a negative vertial coordinate from its current location
    
    if head.direction == "right":           # creating if statement for positive horizontal movement
        x = head.xcor()                     # creating variable x and setting it to x coordinate with no arguement
        head.setx(x + 20)                   # calling the set method and giving it a positive horizontal coordinate from its current location

    if head.direction == "left":            # creating if statement for negative horiztonal movement
        x = head.xcor()                     # creating variable x and setting it to x coordinate with no arguement
        head.setx(x - 20)                   # calling the set method and giving it a negative horiztonal coordinate from its current location
    
# Keyboard functions
def keyUp():
    head.direction = "up"

def keyDown():
    head.direction = "down"

def keyRight():
    head.direction = "right"

def keyLeft():
    head.direction = "left"

# Main game loop
while True:
    window.update()
    
    time.sleep(delay)

    move()


window.mainloop()                           # creates main window loop