idade=int(input("informe a sua idade : "))
if idade >= 18 :
    print("Permitido a entrada !")
else :
        print("Entrada não permitida !")

print("\n")

ganho=int(input("Quanto você ganha por dia : "))
if ganho <= 2:
      print("Pobre")
elif ganho > 2 and ganho <=4:
      print("Médio")
elif ganho > 4 and ganho <=6:
      print("Rico")
else:
      print("Porco capitalista")