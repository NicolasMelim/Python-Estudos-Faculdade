 #Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável. 
def multiplicar(*args):
    total = 1 
    for numeros in args:
         total *= numeros  #precisa salvar em uma variavel antes  <-
    return total


multiplicação = multiplicar(10, 2, 3, 4, 5)
print(multiplicação)
    


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def npar_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par!'
    return f'{numero} é ímpar'