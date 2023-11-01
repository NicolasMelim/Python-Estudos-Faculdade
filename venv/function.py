def soma(x, y , z=None):
 if z is not None:
     print(f'{x=} {y=} {z=}', x + y + z)
 else:
    print(f'{x=} {y=}', x + y)
    
soma(1, 5, 6)
soma(2, 5)       
# SE Z NÃO FOR SEM VALOR (IF Z IS NOT NONE)