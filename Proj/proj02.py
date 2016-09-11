#Computer Project #02
#section 730.
#May 31,2016
    #input how many squares you want to draw and the length of the side
    #draw squares and fill in with different colors

import turtle
import random
import time
#a brief descriptive message of what the program does
print('This program draws squares of many colors')
# prompt before starting to draw
#decide how many squares you want to draw
while True:
    ipt_number=input('\nPlease enter the number of squares you want to draw:')
    if ipt_number.isdigit():
        num_int=int (ipt_number)    #conver input into interger
        if num_int==0:     #make sure drawing at least 1 square
            print ('\nPlease enter the number of squares at least 1\n','Please try again')
            continue
        break
    else:
        print ('\nPlease enter a numerical input')
#decide how long you want the side to be
while True:
    ipt_number_side=input('\nPlease Enter the length of the side you want to the square to be:')
    if ipt_number_side.isdigit():
        num_side_int=int (ipt_number_side)  #conver input into interger
        if num_side_int<50 or num_side_int>200:   #make sure the length of the side is in range
            print ('\nPlease enter the length of side in the range from 50 to 200\n','Please try again')
            continue
        break
    else:
        print ('\nPlease enter a numerical input')
#decide waht angle the next square will turn after done with the last one
angle=360/num_int
for i in range(num_int):
    #random color of the pen
    turtle.color(random.random(),random.random(),random.random())
    #start to fill in with random color
    turtle.begin_fill()
    for j in range(4):
        turtle.forward(num_side_int)
        turtle.right(90)
    #end of fill in color
    turtle.end_fill()
    turtle.left(angle)
#hide the pen
turtle.hideturtle()
#hold turtle window for 10 second
time.sleep(10)
#close the turtle window
turtle.bye()
