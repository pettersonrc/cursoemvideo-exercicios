from random import randint
win = 0  # quantidade de vitórias
print('-='*13)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-='*13)
while True:
    opcao = 0
    print('--'*10)
    print('''PAR OU ÍMPAR?
[1] PAR
[2] ÍMPAR''')
    while opcao != 1 and opcao != 2:
        opcao = int(input('OPÇÃO: '))
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    total = computador + jogador
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print('--' * 10)
    print(f'''COMPUTADOR = {computador}
JOGADOR = {jogador}
TOTAL = {total}
RESULTADO = {resultado}''')
    if opcao == 1:
        if total % 2 == 0:
            print('VOCÊ VENCEU!!!')
            win += 1
        else:
            break
    else:
        if total % 2 == 1:
            print('VOCÊ VENCEU!!!')
            win += 1
        else:
            break
    print('Vamos jogar denovo!')
print('-='*10)
print('GAME OVER!')
print('--'*10)
print(f'Você venceu um total de {win} vezes')
