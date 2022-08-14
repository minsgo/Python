import turtle
win = turtle.Screen()
t1 = turtle.Turtle()
t1.shape("turtle")
t1.speed(50)
distance=10
x1 = 90
y1 = -138
x2 = 108
y2 = -198
def getMinValue(v1, v2):
    if v1 < v2:
        return v1
    return v2

def getMaxValue(v1, v2):
    if v1 > v2:
        return v1
    return v2

def C(newx, newy):
    if T(newx, newy, x1, y1, x2, y2):
        S(x1, y1, x2, y2)
    
def S(x1,y1,x2,y2):
    t1.fillcolor('green')
    t1.begin_fill()
    t1.penup()
    t1.goto(x1,y1)
    t1.pendown()
    t1.goto(x2,y1)
    t1.goto(x2,y2)
    t1.goto(x1,y2)
    t1.goto(x1,y1)
    t1.end_fill()

def T(x, y, x1, y1, x2, y2):#함정 사각형으로 표현하기
    minX = getMinValue(x1, x2)
    maxX = getMaxValue(x1, x2)
    minY = getMinValue(y1, y2)
    maxY = getMaxValue(y1, y2)
    if(minX<=x and x<=maxX)and(minY<=y and y<=maxY):#x,y가 사각형 안에 있는가
        return True
    else:
        return False

def keyforward():
    t1.setheading(0)
    position = t1.pos()
    t1.goto(position[0] + distance, position[1])
    C(position[0] + distance, position[1])


def keyforward1():
    t1.setheading(180)
    position = t1.pos()
    t1.goto(position[0] - distance, position[1])
    C(position[0] - distance, position[1])

def keyforward2():
    t1.setheading(90)
    position = t1.pos()
    t1.goto(position[0], position[1] + distance)
    C(position[0], position[1] + distance)

def keyforward3():
    t1.setheading(-90)
    position = t1.pos()
    t1.goto(position[0], position[1] - distance)
    C(position[0], position[1] - distance)
    
def keyforward4():
    t1.penup()
    t1.fd(50)
    t1.pendown()
    
def keyforward5():
    t1.penup()
    t1.clear()
    t1.home()
    t1.pendown()
    
def keyforward6():
    t1.penup()
    t1.fd(100)
    t1.pendown()
    
def key():
    position=t1.pos()
    myPos="%s %s" % (position[0], position[1])
    t1.write(myPos)
  
win.onkey(keyforward, "Right")
win.onkey(keyforward1, "Left")
win.onkey(keyforward2, "Up")
win.onkey(keyforward3, "Down")
win.onkey(keyforward4, "space")# 50만큼 점프
win.onkey(keyforward5, "Escape")# 초기화
win.onkey(keyforward6, "Tab")# 100만큼 점프
win.onkey(key, "p")# 좌표출력
win.listen()
turtle.mainloop()

