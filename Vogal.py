def vogal(n):
    vogal=True
    if n=="a" or n=="e" or n=="i" or n=="o" or n=="u" :
        vogal=True
    else:
        vogal=False
    return vogal

a=input("Informe a letra : ")
print(vogal(a))