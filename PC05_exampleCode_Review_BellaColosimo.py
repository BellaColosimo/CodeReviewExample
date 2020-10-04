#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:00:12 2020

@author: Dr. Z

A generative art piece that uses 5 turtles to make random walk patterns in 
different colors. One turtle draws a wiggly spiral in the middle of the 
screen. 

EDITED AND REVIEWED BY: BELLA COLOSIMO FOR PC05
"""
from turtle import *
import math 
import random

# create palette
COLORS = ['aquamarine','pink','white','orange','yellow']

# create screen, and set size
panel = Screen()
w = 500
h = 500
panel.setup(width=w,height=h)
tracer(0) # turn off the animation or it will take forEVER

# set background color
panel.bgcolor('purple')

# define variables for turtle movement
step = 2  # amount of straightness in paths


# create turtles
turtle1 = Turtle(visible=False)
turtle2 = Turtle(visible=False)
turtle3 = Turtle(visible=False)
turtle4 = Turtle(visible=False)
spiral = Turtle(visible=False)

# assign colors
#turtle1.color(COLORS[0])
#turtle2.color(COLORS[1])
#turtle3.color(COLORS[2])
#turtle4.color(COLORS[3])
#spiral.color(COLORS[4])#random.choice(COLORS))

turtle1.color(random.choice(COLORS))
turtle2.color(random.choice(COLORS))
turtle3.color(random.choice(COLORS))
turtle4.color(random.choice(COLORS))
spiral.color(random.choice(COLORS))


#thicc = 20  # pen width

turtle1.penup()
turtle1.width(20)

turtle2.penup()
turtle2.width(20)

turtle3.penup()
turtle3.width(20)

turtle4.penup()
turtle4.width(20)

spiral.penup()
spiral.width(20)


rot = 90  # amount of bend in paths


# place randomly around edge screen
X = random.randint(w/2-100,w/2)
Y = random.randint(w/2-100,w/2)
turtle1.goto(X,Y)
turtle1.seth(turtle1.towards(0,0))


# place randomly around edge screen
X = random.randint(-w/2,-w/2+100)
Y = random.randint(-w/2,-w/2+100)
turtle2.goto(X,Y)
turtle2.seth(turtle1.towards(spiral))


# place randomly around edge screen
X = random.randint(w/2-100,w/2)
Y = random.randint(w/2-100,w/2)
turtle3.goto(X,Y)
turtle3.seth(turtle1.towards(0,0))


# place randomly around edge screen
X = random.randint(-w/2,-w/2+100)
Y = random.randint(-w/2,-w/2+100)
turtle4.goto(X,Y)
turtle4.seth(turtle1.towards(0,0))

# set down pens
turtle1.pendown()
turtle2.pendown()
turtle3.pendown()
turtle4.pendown()
spiral.pendown()

# walk forward (iterate 10000 times or use a while loop) with random turns
for i in range(10000):
    #spiral = Turtle()
    forward(step) # move each turtle forward
    turtle1.left(random.randint(-rot,rot))
    turtle2.forward(step)
    turtle2.left(random.randint(-rot,rot))
    turtle3.forward(step)
    turtle3.left(random.randint(-rot,rot))
    turtle4.forward(step)
    turtle4.left(random.randint(-rot,rot))
    spiral.left(random.randint(-rot,rot))
    # TODO: spin in circles??
    spiral.forward(random.randint(-step*2,step*2))
    spiral.left(rot)


done()

"""
Code Summary:
    Fixed on line 93 and line 94 unexpected indents
    When first running code, it doesn't do anything...we will go back later
    Added spacing to make it more readable
    Moved "import random" to its own line because I get confused :)
    Changed the range from 2 to 1000 so that it iterates 10000 times
    Commented out line 105 because we already defined this turtle
    On line 45, you had a possible random color choice. I implemented this.
    Commented out line 54 because of redundancy

Overall I think the code now works as it was intended to. 
I really like the color choices and the sense of randomness.
Could we maybe find a way to have it spread across the screen more? Maybe iterate more times?

"""