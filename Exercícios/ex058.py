from random import randint
from time import sleep
tentativas = 0
acertou = False
n1 = randint(0, 10)
print('PENSANDO...')
sleep(2)
print('Acabei de pensar em um número entre 0 e 10')
while not acertou:
    n2 = int(input('Tente adivinhar o número que eu pensei: '))
    tentativas += 1
    if n2 == n1:
        acertou = True
    elif n2 > n1:
        print('Menos... Tente novamente.')
    else:
        print('Mais... Tente novamente.')
print('VOCÊ ACERTOU!!, e precisou de {} tentativas, Parabéns!'.format(tentativas))
