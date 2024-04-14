def maior_elemento(lista):
    m=lista[0]
    for elemento in lista:
        if m<elemento:
            m=elemento
    print(m)

lista=[]
maior_elemento(lista)