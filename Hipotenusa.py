def é_hipotenusa(n):
    s=0
    soma=0
    while n>0:
        
        c=True
        a=1
        while a<n and c:
            b=0
            while b<n and c:
                b=b+1
                if n**2==(a**2)+(b**2):
                    s=s+1
                    soma=soma+n
                    c=False
            a=a+1
        c=True
        n=n-1
    return soma

def soma_hipotenusas(n):
    return é_hipotenusa(n)
    

n=int(input(" : "))
soma_hipotenusas(n)