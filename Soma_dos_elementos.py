def soma_elementos(lista):
    soma=0
    for elemento in lista:
        soma=soma+int(elemento)
        print(soma)
    return soma

lista=[]
soma_elementos(lista)
