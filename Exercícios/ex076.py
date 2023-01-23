listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90, 'Lápis', 1.75,
            'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00)
print('-='*15)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-='*15)
for cont in range(0, len(listagem)):
    if cont % 2 == 0:
        print(f'{listagem[cont]:.<23}', end='')
    else:
        print(f'R${listagem[cont]:>5.2f}')
print('-='*15)
