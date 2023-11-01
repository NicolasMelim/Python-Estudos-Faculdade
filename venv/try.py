## try = tenta executar o codigo
## except = ocorreu um erro ao executar o codigo

numero_str = input('Digite um número que eu irei dobrar ele: ')


try:
    numero_float = float(numero_str)
    print('Flutuante', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número!')