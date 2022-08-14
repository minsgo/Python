import random

a1, a2 = 0, 0
b1, b2 = 0, 0

def Adice():
    a3 = 0
    a1=random.randint(1,6)
    a2=random.randint(1,6)
    print("A의 주사위 숫자는 %d, %d 입니다." %(a1, a2))
    a3 = a1 + a2
    return a3

def Bdice():
    b3 = 0
    b1=random.randint(1,6)
    b2=random.randint(1,6)
    print("B의 주사위 숫자는 %d, %d 입니다." %(b1, b2))
    b3 = b1 + b2
    return b3

def check(a, b):
    if a > b:
        print("A가 이겼네요")
    elif a < b:
        print("B가 이겼네요")
    elif a == b:
        print("둘이 비겼네요")

def play():
    A=Adice()
    B=Bdice()
    check(A, B)

play()
