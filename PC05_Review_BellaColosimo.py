#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Bella Colosimo
Sep 10, 2020


Import random library
Hide the turtle
Increase pen size
While x is less than 1000, generate a random value for r,g,b
Use those random numbers are the color
Iterate through
'''
"""
REVIEWED CODE FOR PC05
OCTOBER 3, 2020
ALL NEW COMMENTS HAVE TRIPLE QUOTES
"""


from turtle import * 
import random

bgcolor("black")


# Create a panel to draw on. 
panel = Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
reset()
hideturtle()
speed(0)
pensize(5)

colormode(255)

penup()
goto(100,100)
pendown()

"""
Function added for DRYer code
"""
def randomColor(): 
    r = random.randrange(0, 125, 10) 
    g = random.randrange(0, 125, 10)
    b = random.randrange(0, 125, 10)
    color(r, g, b)

for x in range(500):
    """
    could this color setter be a function? Lets try...
    """
    #r = random.randrange(0, 125, 10) <-- old code
    #g = random.randrange(0, 125, 10) <-- old code
    #b = random.randrange(0, 125, 10) <-- old code
    #color(r, g, b) <-- old code
    randomColor()
    forward(x)
    right(70)
    x = x + 1

penup()
goto(-100,-100)
pendown() 

for c in range(500):
    #r = random.randrange(0, 257, 10) <-- old code
    #g = random.randrange(0, 257, 10) <-- old code
    #b = random.randrange(0, 257, 10) <-- old code
    #color(r, g, b) <-- old code
    randomColor()
    forward(c)
    left(70)
    c = c + 1

done()

"""
Code Summary:
    Although I wrote this code, there was a clear spot where I could make the code DRYer.
    I like the simplicity of the code as it is easy to understand and execute.
    That also might be the thing I don't like, there maybe needed to be more challenge?
    Adding in a color function reduced the amount of lines. 
    Is the dark color too dark? Could it be bright like the other shape?
"""
