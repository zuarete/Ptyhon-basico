def primo(n):
    primo=True
    i=2
    while i<n and primo:
        if n % i == 0:
            primo = False
        i=i+1

    if primo:
        return 1
    else:
        return 0
    
def n_primos(n):
    if n==2:
        print("1")
    else:
        cont=1
        while n>2:
            c=primo(n)
            cont=cont+c
            n=n-1
        return cont

n=int(input("Informe um número : "))
print(n_primos(n))