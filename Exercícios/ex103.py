def ficha(nome, gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 20)
n = str(input('Nome do jogador: '))
if n == '':
    n = '<desconhecido>'
g = str(input('Número de Gols: '))
if g == '':
    gol = '0'
ficha(n, g)
