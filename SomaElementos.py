n=input("Informe o número : ")
t=len(n)
i=0
soma=0
v=int(n)
while i<t:
    #a=v//(10**i)
    #b=(v//(10**(i+1)))*10
    soma=soma+(v//(10**i)-(v//(10**(i+1)))*10)
    i=i+1
print(soma)
