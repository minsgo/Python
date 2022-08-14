import turtle
import keyboard
from random import randint

class MJPScreen:
    def __init__(self):
        self.Pturtle = turtle.Turtle()
        self.Cturtle = turtle.Turtle()
    
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

def game():
    while True:
        if keyboard.is_pressed('s') or keyboard.is_pressed('S'):
            judgement.rspJudgement(1)
        elif keyboard.is_pressed('r') or keyboard.is_pressed('R'):
            judgement.rspJudgement(2)
        elif keyboard.is_pressed('p') or keyboard.is_pressed('P'):
            judgement.rspJudgement(3)
        if judgement.win == 'win':
            turtle.bye()
            break
        elif judgement.win == 'lose':
            turtle.bye()
            break

game()