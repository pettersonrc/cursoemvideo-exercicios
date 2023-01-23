from random import randint
from time import sleep
n1 = randint(0, 5) # Faz o computador sortear um número
print('PENSANDO...')
sleep(2)
n2 = int(input('Tente advinhar em que número de 0 a 5 eu pensei: '))
print('PROCESSANDO...')
sleep(2)
if n1 == n2:
    print('VOCÊ VENCEU :), eu pensei no número {}!'.format(n1))
else:
    print('VOCÊ PERDEU :c, eu pensei no número {} e você digitou o número {}'.format(n1, n2))
