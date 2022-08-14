ss = input("문자열을 입력하세요 : ")
big = []
small = []
num = []
kor = []
ant = []
for i in range(0, len(ss)):
    if(65 <= ord(ss[i]) <= 90):
        big.append(ss[i])
    elif(97 <= ord(ss[i]) <= 122):
        small.append(ss[i])
    elif(48 <= ord(ss[i]) <= 57):
        num.append(ss[i])
    elif(44032 <= ord(ss[i]) <= 55203):
        kor.append(ss[i])
    else:
        ant.append(ss[i])

r = ''.join(str(s) for s in big)
r1 = ''.join(str(s) for s in small)
r2 = ''.join(str(s) for s in num)
r3 = ''.join(str(s) for s in kor)
r4 = ''.join(str(s) for s in ant)

print("대문자 : ", r)
print("소문자 : ", r1)
print("숫자 : ", r2)
print("한글 : ", r3)
print("기타 : ", r4)

