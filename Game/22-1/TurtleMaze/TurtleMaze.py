from queue import LifoQueue
from re import L
import turtle
import keyboard
from random import randint
import random
import sys
import time
from tkinter import *
turtle.title("Turtle Maze")
win=turtle.Screen()
win.setup(556,538)
win.bgpic("maze2.gif")

global life
life = 5
global w
w = 0
global mazelen

def writeGameOver():
    print("다시 시작")

#함정 좌표
x1=100
y1=-50
x2=-20
y2=100
x3=-120
y3=140
x4=-90
y4=210
x5=-61
y5=240
x6=11
y6=250


#미로게임 시작
def invisiblemaze():
  
  turtle.resetscreen()
  turtle.clearscreen()

  win.setup(850,850)

  global mazelen
  global cubesize
  global X
  global Y
  global maze
  


  #screen = T.Screen()


  maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
          [1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1],
          [1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],
          [1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1],
          [1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
          [1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1],
          [1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1],
          [1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1],
          [1,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1],
          [1,0,1,1,1,0,1,1,1,0,0,1,0,1,0,1],
          [1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1],
          [1,0,1,0,1,1,1,0,1,0,0,1,0,0,0,1],
          [1,0,1,0,0,0,1,0,1,1,0,1,1,1,1,1],
          [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

  tt=turtle.Turtle()
  t1=turtle.Turtle()
  t2=turtle.Turtle()
  t3=turtle.Turtle()
  t4=turtle.Turtle()

  turtle.shape('turtle')
  turtle.bgcolor("Black")

  t1.shape()
  t2.shape()
  t3.shape()
  t4.shape()

  t1.penup()
  t2.penup()
  t3.penup()
  t4.penup()

  t1.seth(90)
  t2.seth(180)
  t3.seth(270)
  t4.seth(0)

  '''
  t1.color("White")
  t2.color("White")
  t3.color("White")
  t4.color("White")

  '''

  def Hidearrow():

      t1.ht()
      t2.ht()
      t3.ht()
      t4.ht()

  Hidearrow()


  turtle.bgcolor("white")

  turtle.color("White")

  X=1

  Y=14

  cubesize=45

  mazelen = len(maze)

  turtle.hideturtle()

  def getx(x):

      global cubesize

      global mazelen

      return (x-mazelen/2)*cubesize

  def gety(y):

      global cubesize

      global mazelen

      return -(y-mazelen/2)*cubesize 


  def draw_wall(x,y):

      x=getx(x)

      y=gety(y)

      tt.penup()

      tt.goto(x,y)

      tt.color("white")

      tt.shape("square")

      tt.stamp() 


  def draw_maze(maze):

      tt.speed(50)

      tt.penup()

      tt.goto(getx(0),gety(0))

      tt.pendown()


      for y in range(len(maze)):

          for x in range(len(maze[y])):

              if(maze[y][x]==1):

                   draw_wall(x,y)

  def turn_left():

      global maze

      global X

      global Y

      if(X>0):

          if(maze[Y][X-1]==0):
              Hidearrow()

              X=X-1

              tt.seth(180)

              tt.goto(getx(X),gety(Y))

              scan(X,Y)

  def turn_right():

      global maze

      global X

      global Y

      if(X<16):

          if(maze[Y][X+1]==0):
              Hidearrow()

              X=X+1

              tt.seth(0)

              tt.goto(getx(X),gety(Y))

              scan(X,Y)

  def go_up():

      global maze

      global X

      global Y

      if(Y>0):

          if(maze[Y-1][X]==0):
              Hidearrow()

              Y=Y-1

              tt.seth(90)

              tt.goto(getx(X),gety(Y))

              scan(X,Y)

            

  def go_down():

      global maze

      global X

      global Y

      if(Y<15):

          if(maze[Y+1][X]==0):
              Hidearrow()

              Y=Y+1

              tt.seth(270)

              tt.goto(getx(X),gety(Y))

              scan(X,Y)

            

  def scan(x,y):

      global maze

      global X

      global Y


      if getx(X)==270 and gety(Y)==360 :
          turtle.bye()

          window = Tk()
          window.title("에필로그")
          window.geometry("400x350")
          window.resizable(width =FALSE, height = FALSE)
          
          photo = PhotoImage(file = "toki.gif")
          lable1 = Label(window, image = photo)
          lable2 = Label(window, text = "거북이와 토끼는 무사히 만나게 되어\n", font = ("바탕",12))
          lable3 = Label(window, text = "다시 예전처럼 행복하게 지냈답니다\n", font = ("바탕", 12))
          
          lable1.pack()
          lable2.pack()
          lable3.pack()

      if(maze[Y-1][X]==0):

          t1.goto(getx(X),gety(Y-1))

          t1.st()

      else:

          t1.ht()

      if(maze[Y][X-1]==0):

          t2.goto(getx(X-1),gety(Y))

          t2.st()

      else:

          t2.ht()

      if(maze[Y+1][X]==0):

          t3.goto(getx(X),gety(Y+1))

          t3.st()

      else:

          t3.ht()

      if(maze[Y][X+1]==0):

          t4.goto(getx(X+1),gety(Y))

          t4.st()

      else:

          t4.ht()
      time.sleep(1)

  draw_maze(maze)

     
  win.onkey(turn_left,"Left")

  win.onkey(turn_right,"Right")

  win.onkey(go_up,"Up")

  win.onkey(go_down,"Down")

  win.listen()


  tt.shape("turtle")

  tt.color("Black")

  tt.seth(90)

  tt.speed(4)

  tt.goto(getx(1),gety(14))

  turtle.showturtle()

  tt.pendown()

  tt.pensize(3)

  scan(X,Y)


  turtle.mainloop()


#묵찌빠
class MJPScreen:
    def __init__(self):
        self.Pturtle = turtle.Turtle()
        self.Cturtle = turtle.Turtle()
    
    def hide(self):
        self.Pturtle.hideturtle()
        self.Cturtle.hideturtle()
    
    def setting(self):
        self.win = turtle.Screen()
        self.Pturtle.penup()
        self.Pturtle.goto(-100,0)
        self.Pturtle.pendown()
        self.Cturtle.penup()
        self.Cturtle.goto(200,0)
        self.Cturtle.pendown()

        self.win.setup(1000,600)
        self.win.addshape('rock.gif')
        self.win.addshape('scissors.gif')
        self.win.addshape('paper.gif')

    def Cdrawing(self, computer):
        if computer == 1:
            self.Cturtle.shape('scissors.gif')
        elif computer == 2:
            self.Cturtle.shape('rock.gif')
        else:
            self.Cturtle.shape('paper.gif')
        
    def Pdrawing(self, player):
        if player == 1:
            self.Pturtle.shape('scissors.gif')
        elif player == 2:
            self.Pturtle.shape('rock.gif')
        else:
            self.Pturtle.shape('paper.gif')
    
class MJPjudgement():
    def __init__(self):
        self.s = MJPScreen()
        self.mjp = 1
        self.attack = 0
        self.win = ''
        
    def rspJudgement(self, player):
        self.s.setting()
        self.c = randint(1,3)
        if player == 1 and self.c == 3:
            self.attack = 0
            self.mjp = 0
            self.s.Cdrawing(self.c)
            self.s.Pdrawing(player)
        elif player == 2 and self.c == 1:
            self.attack = 0
            self.mjp = 0
            self.s.Cdrawing(self.c)
            self.s.Pdrawing(player)
        elif player == 3 and self.c == 2:
            self.attack = 0
            self.mjp = 0
            self.s.Cdrawing(self.c)
            self.s.Pdrawing(player)
        elif player == self.c:
            self.s.Cdrawing(self.c)
            self.s.Pdrawing(player)
        else:
            self.attack = 1
            self.mjp = 0
            self.s.Cdrawing(self.c)
            self.s.Pdrawing(player)

        if self.mjp == 0:
            self.mjpJudgement(player)

    def mjpJudgement(self, player):
        if player == self.c:
            if self.attack == 0:
                self.win = 'win'
                print(self.win)
            if self.attack == 1:
                self.win = 'lose'
                print(self.win)
            self.s.Cdrawing(self.c)
            self.s.Pdrawing(player)
        else:
            if player == 3 and self.c == 1:
                self.attack = 1
                self.s.Cdrawing(self.c)
                self.s.Pdrawing(player)
            elif player == 1 and self.c == 2:
                self.attack = 1
                self.s.Cdrawing(self.c)
            elif player == 2 and self.c == 3:
                self.attack = 1
                self.s.Cdrawing(self.c)
                self.s.Pdrawing(player)
            else:
                self.attack = 0
                self.s.Cdrawing(self.c)
                self.s.Pdrawing(player)

judgement = MJPjudgement()
screen = MJPScreen()

def mjp():
    while True:
        if keyboard.is_pressed('s') or keyboard.is_pressed('S'):
            judgement.rspJudgement(1)
        elif keyboard.is_pressed('r') or keyboard.is_pressed('R'):
            judgement.rspJudgement(2)
        elif keyboard.is_pressed('p') or keyboard.is_pressed('P'):
            judgement.rspJudgement(3)
        if judgement.win == 'win':
            judgement.__init__()
            screen.hide()
            '''turtle.bye
            Pturtle.clear()
            Cturtle.clear()
            win=turtle.Screen()'''
            win.setup(556,538)
            win.bgpic("maze2.gif")
            tp.reset()
            tp.penup()
            tp.setpos(-80,180)
            tp.setheading(0)
            break
        elif judgement.win == 'lose':
            judgement.__init__()
            screen.hide()
            '''turtle.bye
            Pturtle.clear()
            Cturtle.clear()
            win=turtle.Screen()'''
            win.setup(556,538)
            win.bgpic("maze2.gif")
            tp.reset()
            tp.penup()
            tp.setpos(-110,-250)
            tp.setheading(90)
            writeGameOver()
            break


#가위바위보
Pturtle=turtle.Turtle()
Cturtle=turtle.Turtle()

def exitP():
    turtle.bye()

def check(p,c):
    global life
    global w
    if(life == 0):
        Pturtle.hideturtle()
        Cturtle.hideturtle()
        win.setup(556,538)
        win.bgpic("maze2.gif")
        tp.reset()
        tp.penup()
        tp.setpos(-110,-250)
        tp.setheading(90)
        writeGameOver()
    elif(w == 5):
        Pturtle.hideturtle()
        Cturtle.hideturtle()
        win.setup(556,538)
        win.bgpic("maze2.gif")
        tp.reset()
        tp.penup()
        tp.setpos(-25,40)
        tp.setheading(180)
    else:
        if p==1:
            if c==1:
                print("비김")
            elif c==2:
                print("짐")
                life -= 1
            elif c==3:
                print("이김")
                w += 1
        if p==2:
            if c==1:
                print("이김")
                w += 1
            elif c==2:
                print("비김")
            elif c==3:
                print("짐")
                life -= 1
        if p==3:
            if c==1:
                print("짐")
                life -= 1
            elif c==2:
                print("이김")
                w += 1
            elif c==3:
                print("비김")
def game(player):
    if player==1:
        Pturtle.shape("scissors.gif")
    elif player==2:
        Pturtle.shape("rock.gif")
    elif player==3:
        Pturtle.shape("paper.gif")

def game2(computer):
    if computer==1:
        Cturtle.shape("scissors.gif")
    elif computer==2:
        Cturtle.shape("rock.gif")
    elif computer==3:
        Cturtle.shape("paper.gif")

def playgame(player):
    game(player)
    computer=random.randint(1,3)
    game2(computer)
    check(player, computer)

def scissors():
    playgame(1)
def rock():
    playgame(2)
def paper():
    playgame(3)

def rsp():
    global life
    global w
    life = 5
    w = 0
    win=turtle.Screen()
    Pturtle.penup()
    Pturtle.goto(-100,0)
    Pturtle.pendown()
    Cturtle.penup()
    Cturtle.goto(200,0)
    Cturtle.pendown()

    win.setup(1000,600)
    win.addshape("rock.gif")
    win.addshape("scissors.gif")
    win.addshape("paper.gif")

    win.onkey(scissors,"s")
    win.onkey(scissors,"S")
    win.onkey(rock,"r")
    win.onkey(rock,"R")
    win.onkey(paper,"p")
    win.onkey(paper,"P")
    win.listen()
    win.mainloop()

#가위바위보 함정
def getMinValue(v1, v2):
    if v1 < v2:
        return v1
    return v2

def getMaxValue(v1, v2):
    if v1 > v2:
        return v1
    return v2

def S1(x1,y1,x2,y2):
    tp.fillcolor('green')
    tp.begin_fill()
    tp.penup()
    tp.goto(x1,y1)
    tp.pendown()
    tp.goto(x2,y1)
    tp.goto(x2,y2)
    tp.goto(x1,y2)
    tp.goto(x1,y1)
    tp.end_fill()

def T1(x, y, x1, y1, x2, y2):#함정 사각형으로 표현하기
    minX = getMinValue(x1, x2)
    maxX = getMaxValue(x1, x2)
    minY = getMinValue(y1, y2)
    maxY = getMaxValue(y1, y2)
    if(minX<=x and x<=maxX)and(minY<=y and y<=maxY):#x,y가 사각형 안에 있는가
        return True
    else:
        return False

def C1(newx, newy):
    if T1(newx, newy, x1, y1, x2, y2):
        S1(x1, y1, x2, y2)
        rsp()

#묵찌빠 함정
def getMinValue(v1, v2):
    if v1 < v2:
        return v1
    return v2

def getMaxValue(v1, v2):
    if v1 > v2:
        return v1
    return v2

def S2(x3,y3,x4,y4):
    tp.fillcolor('green')
    tp.begin_fill()
    tp.penup()
    tp.goto(x3,y3)
    tp.pendown()
    tp.goto(x4,y3)
    tp.goto(x4,y4)
    tp.goto(x3,y4)
    tp.goto(x3,y3)
    tp.end_fill()

def T2(x, y, x3, y3, x4, y4):#함정 사각형으로 표현하기
    minX = getMinValue(x3, x4)
    maxX = getMaxValue(x3, x4)
    minY = getMinValue(y3, y4)
    maxY = getMaxValue(y3, y4)
    if(minX<=x and x<=maxX)and(minY<=y and y<=maxY):#x,y가 사각형 안에 있는가
        return True
    else:
        return False

def C2(newx, newy):
        
    if T2(newx, newy, x3, y3, x4, y4):
        S2(x3, y3, x4, y4)
        tp.setpos(-80,180)
        mjp()

#미로게임 시작조건
def S3(x5,y5,x6,y6):
    tp.fillcolor('black')
    tp.begin_fill()
    tp.penup()
    tp.goto(x5,y5)
    tp.pendown()
    tp.goto(x6,y5)
    tp.goto(x6,y6)
    tp.goto(x5,y6)
    tp.goto(x5,y5)
    tp.end_fill()

def T3(x, y, x5, y5, x6, y6):#함정 사각형으로 표현하기
    minX = getMinValue(x5, x6)
    maxX = getMaxValue(x5, x6)
    minY = getMinValue(y5, y6)
    maxY = getMaxValue(y5, y6)
    if(minX<=x and x<=maxX)and(minY<=y and y<=maxY):#x,y가 사각형 안에 있는가
        return True
    else:
        return False
def C3(newx, newy):
    if T3(newx, newy, x5, y5, x6, y6):
        S3(x5, y5, x6, y6)
        win.bgpic("\0")
        
        invisiblemaze()

#스토리 나오는 코드
window = Tk()
window.title("메이즈 터틀")
window.geometry("500x250")
window.resizable(width =FALSE, height = FALSE)
lable1 = Label(window, text = "우리가 알던 이야기 이전에 거북이와 토끼는 세상에 둘도 없는 절친이었습니다.\n", font = ("바탕",10))
lable2 = Label(window, text = "그러던 어느 날 토끼와 놀러 가기로 한 거북이는 토끼가 약속시간에 오지 않자\n", font = ("바탕", 10))
lable3 = Label(window, text = "이상한 낌새를 느낀 거북이는 토끼가 납치되었다는 소식을 듣게 되었습니다.\n", font = ("바탕", 10))
lable4 = Label(window, text = "거북이는 토끼를 구하기 위해 토끼가 납치된 섬으로 떠나게 되는데...\n\n", font = ("바탕", 10))
lable5 = Label(window, text = "거북이의 기본적인 움직임은 방향키로 움직일 수 있습니다\n", font = ("바탕", 10),fg = "blue")
lable6 = Label(window, text = "함정에 걸렸을때 'r'혹은's', 'p'를 누르면 게임을 시작할 수 있습니다\n", font = ("바탕", 10),fg = "blue")
lable7 = Label(window, text = "시야제한 미로게임은 로딩시간이 있으니 잠시 기다려주세요", font = ("바탕", 10),fg = "blue")
lable1.pack()
lable2.pack()
lable3.pack()
lable4.pack()
lable5.pack()
lable6.pack()
lable7.pack()

#이동
tp = turtle.Turtle()
tp.shape("turtle")
tp.speed(50)
distance=10
tp.penup()
tp.setpos(-110,-250)
tp.setheading(90)
    
def keyforward():
    tp.penup()
    tp.setheading(0)
    position = tp.pos()
    tp.goto(position[0] + distance, position[1])
    C1(position[0] + distance, position[1])
    C2(position[0] + distance, position[1])
    C3(position[0] + distance, position[1])


def keyforward1():
    tp.penup()
    tp.setheading(180)
    position = tp.pos()
    tp.goto(position[0] - distance, position[1])
    C1(position[0] - distance, position[1])
    C2(position[0] - distance, position[1])
    C3(position[0] - distance, position[1])

def keyforward2():
    tp.penup()
    tp.setheading(90)
    position = tp.pos()
    tp.goto(position[0], position[1] + distance)
    C1(position[0], position[1] + distance)
    C2(position[0], position[1] + distance)
    C3(position[0], position[1] + distance)

def keyforward3():
    tp.penup()
    tp.setheading(-90)
    position = tp.pos()
    tp.goto(position[0], position[1] - distance)
    C1(position[0], position[1] - distance)
    C2(position[0], position[1] - distance)
    C3(position[0], position[1] - distance)
    
def keyforward4():
    tp.penup()
    tp.fd(50)
    tp.pendown()
    
def keyforward5():
    tp.penup()
    tp.clear()
    tp.home()
    tp.pendown()
    
def keyforward6():
    tp.penup()
    tp.fd(100)
    tp.pendown()
    
def key():
    position=tp.pos()
    myPos="%s %s" % (position[0], position[1])
    tp.write(myPos)
  
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



