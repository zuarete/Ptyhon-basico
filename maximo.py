def maximo(a,b):
    r=0
    if a>b:
        r=a
    else:
        r=b
    return r


a=int(input("Informe o primeiro número : "))
b=int(input("Informe o segundo número : "))
print(maximo(a, b))
