tupla = (int(input('Digite um número (1 a 10): ')),
         int(input('Digite outro número (1 a 10): ')),
         int(input('Digite mais número (1 a 10): ')),
         int(input('Digite o último número (1 a 10): ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeiro valor 3 aparece na posição {tupla.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
