galera = list()
dados = list()
maispesado = menospesado = cont = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    if cont == 0:
        maispesado = menospesado = galera[0][1]
    else:
        if galera[cont][1] > maispesado:
            maispesado = galera[cont][1]
        if galera[cont][1] < menospesado:
            menospesado = galera[cont][1]
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo, foram cadastradas {len(galera)} pessoas.')
print(f'O maior peso foi de {maispesado}Kg. Peso de', end=' ')
for n in range(0, len(galera)):
    if galera[n][1] == maispesado:
        print(f'[{galera[n][0]}]', end=' ')
print()
print(f'O menor peso foi de {menospesado}Kg. Peso de', end=' ')
for n in range(0, len(galera)):
    if galera[n][1] == menospesado:
        print(f'[{galera[n][0]}]', end=' ')
