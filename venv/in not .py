# in = a 'entre'
# not in = 'não está entre' EX: ABAIXO 
nome = 'Nicolas'
print('Ni' in nome)
print('colas' in nome)
print(10 * '-')
print('Ni' not in nome)
print('colas' not in nome)



nome = input('Digite o seu nome: ')
encontrar = input('Digite o que vc quer encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está entre {nome}')
else:
    print(f'{encontrar} não está entre `{nome}')