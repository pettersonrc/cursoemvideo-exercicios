jogador = dict()
gols = list()
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f' - Quantos gold na partida {c+1}? ')))
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f' O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'   => Na partida {c+1}, fez {gols[c]} gols')
print(f'Foi um total de {jogador["Total"]} gols.')
