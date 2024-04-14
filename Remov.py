def remove_repetidos(lista):
    lista.sort()
    n=int(len(lista))-1
    i=0
    while i<n:
        n=int(len(lista))-1
        c=i+1
        l=lista[i]
        while i<n and c<n:
            if lista[c]==l:
                del lista[c]
            c=c+1
        i=i+1 
    print(lista)
    return lista

lista=[1,2,1,3,4,7,10]
remove_repetidos(lista)
