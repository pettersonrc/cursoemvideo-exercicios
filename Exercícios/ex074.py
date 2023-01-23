from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10))
menor = tupla[0]
maior = 0
for n in tupla:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi: {maior}')
#  max(tupla)
print(f'O menor valor sorteado foi: {menor}')
#  min(tupla)
