tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
         'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
         'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n < 0 or n > 20:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {tupla[n]}!')
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('PROGRAMA FINALIZADO!')
