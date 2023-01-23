valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    print('Valor adicionado com sucesso.')
    resp = ' '
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Lista: {valores}')
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Valores ordenados de forma descrescente: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
