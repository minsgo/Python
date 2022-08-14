def base2(n):
    if n//2 == 0:
        return str(n%2)
    return base2(n//2) + str(n%2)

def base8(n):
    if n//8 == 0:
        return str(n%8)
    return base8(n//8) + str(n%8)

def base16(n):
    convertString="0123456789ABCDEF"
    if n <16 :
        return convertString[n]
    h = divmod(n,16)
    return base16(n//16) + convertString[h[1]]

num = int(input())

print(base2(num))
print(base8(num))
print(base16(num))
