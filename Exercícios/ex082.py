lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um número: ')))
    print('Valor adicionado com sucesso...')
    resp = ' '
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 1:
        impares.append(v)
    elif v % 2 == 0:
        pares.append(v)
print('-='*15)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
