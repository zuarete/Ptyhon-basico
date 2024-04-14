def calc (a, b):
    c=b
    d=b
    if a <=2:
        while a>0:
            while b>0:
                print("#",end="")
                b=b-1
            b=c
            a=a-1
            print()
    else: 
        while b>0:
            print("#",end="")
            b=b-1
        print()
        b=d
        a=a-2
        while a>0:
            b=c
            while b>0:
                if b==1 or b==c:
                  print("#",end="")
                else:
                    print(" ",end="")
                b=b-1
            print()
            a=a-1
        b=c
        while b>0:
            print("#",end="")
            b=b-1   
            
b=int(input("Informe a base do retangulo : "))
a=int(input("Informe a altura do retangulo : "))

calc(a,b)