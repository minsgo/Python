a, b, s = 0, 0, 0
numStr, ch, starStr = "", "", ""

numStr = input("숫자를 여러 개 입력하세요 : ")
print("")
ch = numStr[a]
while True:
    s = int(ch) * 2

    starStr = ""
    for b in range(0, s):
        starStr += "\u2605"
        b += 1
    print(starStr)

    a += 1
    if(a > len(numStr) - 1):
        break
    ch = numStr[a]
