import math

x1=int(input("Informe o primeiro x : "))
y1=int(input("Informe o primeiro y : "))
x2=int(input("Informe o segundo x : "))
y2=int(input("Informe o segundo y : "))
distancia=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
if distancia >=10:
    print("longe")
else:
    print("perto")