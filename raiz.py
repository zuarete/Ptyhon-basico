import math

a=int(input("Informe o coeficiente a : "))
b=int(input("Informe o coeficiente b : "))
c=int(input("Informe o coeficiente c : "))

delta = (b**2)-(4*a*c)

if delta > 0:
    print("\nExistem duas raizes reais !\n")
    x1=((-b)+(math.sqrt(delta)))/(2*a)
    x2=((-b)-(math.sqrt(delta)))/(2*a)
    if x1 < x2:
        print("as raízes da equação são",x1,"e",x2)
    else:
         print("as raízes da equação são",x2,"e",x1)
else:
    if delta == 0:
       print("\nExistem uma raizes reais !\n") 
       x=(-b)/(a*2)
       print("a raiz desta equação é",x)

    else:
        print("\nesta equação não possui raízes reais\n")
