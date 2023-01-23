valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    if valores[-1] in valores[0:len(valores) - 1]:
        valores.pop()
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
    resp = ''
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
valores.sort()
print('-='*30)
print(f'Você digitou os valores: {valores}')
