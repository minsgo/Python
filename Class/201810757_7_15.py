import turtle
import random

myTurtle, tx, ty, tColor, tSize = [None] * 5
playerTurtles = []
sizexy = []
swidth, sheight = 500, 500

turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)

for i in range(0, 5):
    myTurtle = turtle.Turtle()
    myTurtle.shape("turtle")
    myTurtle.penup()
    head = random.randint(0, 360)
    myTurtle.setheading(head)
    tx = random.randrange(-swidth / 2, swidth / 2)
    ty = random.randrange(-sheight / 2, sheight / 2)
    r = random.random(); g = random.random(); b = random.random()
    tsize = random.randrange(1, 100)/10
    playerTurtles.append([myTurtle, tx, ty, tsize, r, g, b])
    sizexy.append([tsize, tx, ty])

for tList in playerTurtles:
    myTurtle = tList[0]
    myTurtle.color(tList[4], tList[5], tList[6])
    myTurtle.turtlesize(tList[3])
    myTurtle.goto(tList[1], tList[2])

t1=turtle.Turtle()
t1.penup()
print("%s \n" %sizexy)
sizexy.sort()
print("%s \n" %sizexy)

for tList in sizexy:
    t1.goto(tList[1], tList[2])
    t1.pendown()
