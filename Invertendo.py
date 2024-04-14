r=1
lista=[]
while r!=0:
    r=int(input("Informe um número : "))
    if r!=0:
        lista.append(r)
lista.sort(reverse=True)

for elemento in lista:
    print(elemento)