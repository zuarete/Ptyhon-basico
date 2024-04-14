def calc (a, b):
    c=b
    while a>0:
        while b>0:
            print("#",end="")
            b=b-1
        b=c
        a=a-1
        print()

b=int(input("Informe a base do retangulo : "))
a=int(input("Informe a altura do retangulo : "))

calc(a,b)
    