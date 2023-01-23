num = list()
pares = list()
impares = list()
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}o. valor: '))
    if n % 2 == 0:
        pares.append(n)
    if n % 2 == 1:
        impares.append(n)
pares.sort()
impares.sort()
num.append(pares[:])
num.append(impares[:])
print('-=' * 30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
