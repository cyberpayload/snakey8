#! python3
# This is a classic game of snake written in Python3 utlizing the turtle module.
# By @cyberpayload

import turtle

# Setting up screenplay

window = turtle.Screen()                    #creates application object
window.title("Snakey8")                     #sets application title name
window.bgcolor("yellow")                    #sets play area background color
window.setup(width=800, height=800)         #sets size of play area
window.tracer(0)                            # turns off screen updates

# Snakehead
head = turtle.Turtle()                      #creates the turle object
head.speed(0)                               #animation speed of the turtle
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)


# Main game loop
while True:
    window.update()

window.mainloop()                           #creates main window loop