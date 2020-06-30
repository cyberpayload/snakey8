#! python3
# This is a classic game of snake written in Python3 utlizing the turtle module.
# By @cyberpayload

import turtle
import time
import random

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


# Snake food
food = turtle.Turtle()                      # creates the turle object
food.speed(0)                               # animation speed of the turtle
food.shape("square")                        # shape of the snake head
food.color("green")                         # color of the snake head
food.penup()                                # this allows the snake to NOT draw when moving (pen is up)
food.goto(0,100)                            # set the snake in the at 100 on y axis
food.direction = "up"                       # direction of snake head during start of game


# Keyboard functions
def keyUp():
    head.direction = "up"

def keyDown():
    head.direction = "down"

def keyRight():
    head.direction = "right"

def keyLeft():
    head.direction = "left"

# Keyboard Bindings
window.listen()                             # creates a listener so we can press keys to control the movement of the snake head
window.onkeypress(keyUp, "8")               # keypad press 8 goes up
window.onkeypress(keyDown, "5")             # keypad press 5 goes down
window.onkeypress(keyRight, "6")            # keypad press 6 goes right
window.onkeypress(keyLeft, "4")             # keypad press 4 goes left

# Main game loop
while True:
    window.update()
    
    if head.distance(food) < 20:            # stating a condotion if head makes a collision with the food
        x = random.randint(-780, 780)       # logical x axis boundary
        y = random.randint(-780, 780)       # logical y axis boundary
        food.goto(x.y)                      # food modes to a random x,y coordinate

    time.sleep(delay)                       # this variable delay is set to 1/10th of a second for any direction (the a human can play at an acceptable speed)

    move()                                  # move() calls the function to start moving the snake when you start the game


window.mainloop()                           # creates main window loop