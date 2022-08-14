import turtle
import random
Pturtle=turtle.Turtle()
Cturtle=turtle.Turtle()

def exitP():
    turtle.bye()

def check(p,c):
    if p==1:
        if c==1:
            print("비김")
        elif c==2:
            print("짐")
        elif c==3:
            print("이김")
    if p==2:
        if c==1:
            print("이김")
        elif c==2:
            print("비김")
        elif c==3:
            print("짐")
    if p==3:
        if c==1:
            print("짐")
        elif c==2:
            print("이김")
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

rsp()
