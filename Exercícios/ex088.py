from random import randint
from time import sleep
palpites = list()
jogos = list()
print('-' * 30)
print('       JOGA NA MEGA SENA        ')
print('-' * 30)
qjogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {qjogos} JOGOS -=-=-=')
sleep(1)
for c in range(0, qjogos):
    for n in range(0, 6):
        jogos.append(randint(1, 60))
        if jogos[n] in palpites:
            jogos.pop()
    jogos.sort()
    palpites.append(jogos[:])
    jogos.clear()
    print(f'Jogo {c+1}: {palpites[c]}')
    sleep(1)
print('-=-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=-=-=-')
