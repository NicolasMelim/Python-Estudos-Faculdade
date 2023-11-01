#Higher Order Functions - Funções que podem receber e/ou retornar outras funções
#First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

def funcao1(nome, idade):
    return f'{nome}, {idade}'


def FunctionName( funcao2 , *args):
    return funcao2(*args)

print(FunctionName(funcao1, 'Nicolas Melim', '19 anos de idade'))
    