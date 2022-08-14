n = 100

for i in range(n + 1):
    result = True
    if(i < 3):
        result = False
    for j in range(3,i):
        if(i % j == 0):
            result = False
    if result:
        print(i, end = " ")
