reqSono=True
reqIdade=True
reqPeso=True

idade = int(input("Informe sua idade:"))
peso  = int(input("informe seu peso:"))
sono = int(input("Informe quantas horas de sono você teve nas ultimas 24 horas:"))

if idade<16 or idade>69:
    reqIdade = False
if peso<50:
    reqPeso = False
if reqSono>=6 or reqSono>=24:
    reqSono = False

if reqIdade==False or reqSono==False or reqPeso==False:
    print("Você não esta apto para doação pelos seguintes motivos:")
    if reqSono==False:
        print("Horas de sono não batem com os requisitos")
    if reqIdade==False:
        print("Idade não bate com os requisitos")
    if reqPeso==False:
        print("Peso não bate com os requisitos")
else:
    print("Apto para Doação")