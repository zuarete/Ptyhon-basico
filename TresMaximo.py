def maximo(a,b,c):
    r=0
    if a>b and a>c:
        r=a
    else:
        if b>c:
            r=b
        else:
            r=c
    return r
a=int(input(": "))
b=int(input(": "))
c=int(input(": "))
print(maximo(a,b,c))