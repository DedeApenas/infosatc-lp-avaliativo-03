mes = { 
    1:"Janeiro",
    2:"Fevereiro",
    3:"Março",
    4:"Abril",
    5:"Maio",
    6:"Junho",
    7:"Julho",
    8:"Agosto",
    9:"Setembro",
    10:"Outubro",
    11:"Novembro",
    12:"Dezembro",
}
while(True):
    numero = (int(input("Digite um número correspondente a um mês(1 a 12): ")))
    if numero in mes:
        print("O mês selecionado foi:", mes[numero])
        break
    else:
        print("Numero Invalido")