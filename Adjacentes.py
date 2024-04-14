adj=False
v=1
a=0
print("Informe os números e quando terminar digite 0 ")
while v!=0 and not adj :
    i=0
    v=input("Informe o número : ")
    t=len(v)
    n=int(v)
    a=((n//(10**(i+1)))*10)-(n//(10**i))
    while i<t:
        i+=1
        b=((n//(10**(i+1)))*10)-(n//(10**i))
        if b==a:
            adj=True 
        else:
            a=b            
    if n==0:
        adj=True
if adj:
    print("O número possui dois elemetons adjacentes")
else:
    print("Os números não possuem dois elemetons adjacentes")   
            
