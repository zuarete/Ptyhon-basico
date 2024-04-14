def maior_primo(n):
    i=2
    k=0
    while i<=n:
        primo=True
        #teste
        c=2
        while c<i and primo:
            if i%c ==0:
               c+=1
               primo=False
            else:
                c+=1
        if primo:
            k=i
        i+=1
    return k

a=int(input("Informe o número : "))
print(maior_primo(a))


