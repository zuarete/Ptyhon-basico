n=int(input("Infomre o número : "))
primo=True
i=2

if n == 1:
    primo=False

while i<n and primo:
    if n % i == 0:
        primo = False
    i=i+1
    
if primo:
    print("primo")
else:
    print("não primo")