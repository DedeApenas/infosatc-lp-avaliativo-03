idadeF = 0
nFemin = 0
idadeM = 0 
nMascu = 0

for X in range(0,10):

    sexo=(input("Qual o seu sexo ?(M/F)"))
    if sexo == "M":
        nMascu = nMascu + 1
        idadeM = idadeM + (int(input("Qual a sua idade?")))
    elif sexo == "F":
      nFemin = nFemin + 1
      idadeF = idadeF + (int(input("Qual a sua idade?")))  
      break
    else:
      print("Informação Invalida, Digite Novamente!")

g  =  (idadeF + idadeM)
g2 =  (nMascu + nFemin)
g3 =  (g/g2)
mediaM = (idadeM/nMascu)
mediaF = (idadeF/nFemin)
print("Média de idade do grupo: ",g3)
print("Média de idade do sexo Feminino:",mediaF)
print("Média de idade do sexo Masculino: ",mediaM)