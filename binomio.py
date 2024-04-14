
def fatorial(v):
    if v !=0:
        a=v
        i=1
        while i<v:
         a=a*i
         i+=1
    else:
        a=1
    return a
        
def binomio(k, n):
    r=fatorial(n)/(fatorial(k)*fatorial(n-k))
    return r

b=int(input("Informe o valor de k : "))
c=int(input("Informe o valor de n : "))
print(binomio(b,c))