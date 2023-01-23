tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
          'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
          'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás',
          'Bragantino', 'Curitiba', 'Cuiabá', 'Ceará', 'Atlético-GO',
          'Avaí', 'Juventude')
print('LISTA DE TIMES DO BRASILEIRÃO')
#  print(tabela)
print('-='*15)
for t in tabela:
    print(t)
print('-=' * 15)
print('PRIMEIROS CINCO COLOCADOS DA TABELA')
#  print(tabela[0:5])
for c in range(0, 5):
    print(tabela[c])
print('-='*15)
print('ÚLTIMOS QUATRO COLOCADOS DA TABELA')
#  print(tabela[-4:])
for c in range(16, len(tabela)):
    print(tabela[c])
print('-='*15)
print('TIMES EM ORDEM ALFABÉTICA')
print(sorted(tabela))
print('-='*15)
print('O botafogo está na posição {}'.format(tabela.index('Botafogo') + 1))
