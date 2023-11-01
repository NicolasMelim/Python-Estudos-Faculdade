import os
carros=[]
carro = input('Digite o nome de 5 carros: ')
while carro != "-1":
    carros.append(carro)
    carro=input('Digite o nome de 5 carros: ')
    
os.system('cls')
for x in carros:
    print(x)
print('\n Fim da nossa tabela (:')