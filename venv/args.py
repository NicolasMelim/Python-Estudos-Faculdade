#args É ARGUMENTOS NÃO NOMEADOS

def soma(*args):
  total = 0 
  for numero in args:
      total += numero 
      return total 
  
    
soma_1_2_3 = soma(1, 2,4 , 4)   
print(soma_1_2_3)

#args empacota oq eu enviar para função dentro de uma tupla
nome = 'Nicolas Melim'
argumentos = 0
while argumentos < len(nome):
      print(nome[argumentos])
      argumentos += 1