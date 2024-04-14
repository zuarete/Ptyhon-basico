sT=int(input("Informe a quantidade de segundos : "))
dias=sT//86400
st=sT%86400
horas=st//3600
segundost= st %3600
minutos=segundost//60
segundos=segundost%60
print(dias,"dias,",horas,"horas,", minutos ," minutos e",segundos,"segundos.")