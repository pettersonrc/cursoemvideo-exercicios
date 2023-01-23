from time import sleep
lista = list()
aluno = list()
notas = list()
cont = 0
while True:
    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media = (notas[0] + notas[1])/2
    notas.append(media)
    aluno.append(notas[:])
    lista.append(aluno[:])
    aluno.clear()
    notas.clear()
    cont += 1
    resp = ' '
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 45)
for c in range(0, cont):
    print(f'{c:<4}{lista[c][0]:<10}{lista[c][1][2]:>8}')
while True:
    opcao = int(input('Mostras notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    print(f'Notas de {lista[opcao][0]} são: {lista[opcao][1][0]} e {lista[opcao][1][1]}')
print(f'FINALIZANDO...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')
