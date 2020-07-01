#! python3
# This is a classic game of snake written in Python3 utlizing the turtle module.
# By @cyberpayload

import turtle
import time
import random

delay = 0.05

# Score
score = 0
high_score = 0


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
head.direction = "stop"                       # direction of snake head during start of game

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
food.shape("circle")                        # shape of the snake head
food.color("red")                           # color of the snake head
food.penup()                                # this allows the snake to NOT draw when moving (pen is up)
food.goto(0,100)                            # set the snake in the at 100 on y axis
food.direction = "up"                       # direction of snake head during start of game

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Keyboard functions
def keyUp():
    if head.direction != "down":
        head.direction = "up"

def keyDown():
    if head.direction != "up":
        head.direction = "down"

def keyRight():
    if head.direction != "left":
        head.direction = "right"

def keyLeft():
    if head.direction != "right":
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

# Check for collision with border
    if head.xcor()>380 or head.xcor()<-380 or head.ycor()>380 or head.ycor()<-380:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the existing segments
        segments.clear()

        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
        # Reset delay
        delay = 0.05
        
#check for collision
    if head.distance(food) < 20:            # stating a condition if head makes a collision with the food
        x = random.randint(-380, 380)       # logical x axis boundary
        y = random.randint(-380, 380)       # logical y axis boundary
        food.goto(x,y)                      # food moves to a random x,y coordinate

        # Add a segment    
        new_segment = turtle.Turtle()
        new_segment.speed(0)                               # animation speed of the turtle
        new_segment.shape("square")                        # shape of the snake head
        new_segment.color("blue")                         # color of the snake head
        new_segment.penup()                                # this allows the snake to NOT draw when moving (pen is up)
        segments.append(new_segment)

        # Increase score by 10
        score += 10

        # Increase snake speed by shortening the delay
        delay -= 0.001
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    # Move the end segments first in reverse
    for index in range(len(segments)-1, 0, -1):     # specify -1 as start, 0 or forward at the max (creating a distance) and a "reverse step" (for snake tail motion)
        x = segments[index-1].xcor()                # moving the snake body backwards horizontally from the snake head 
        y = segments[index-1].ycor()                # moving the snake head backwards vertically from the snake head
        segments[index].goto(x, y)

    # Move segment zero to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)                  # moves the first segment og index x to where the snake head is

    move()                                      # move() calls the function to start moving the snake when you start the game
    
    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the existing segments
            segments.clear()

        
            # Reset the score
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            # Reset delay
            delay = 0.05

    time.sleep(delay)                           # this variable delay is set to 1/10th of a second for any direction (the a human can play at an acceptable speed)

window.mainloop()                               # creates main window loop