matriz = list()
numeros = list()
totpar = soma3 = mai2 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        numeros.append(int(input(f'Digite um valor para {linha, coluna}: ')))
        if numeros[0] % 2 == 0:
            totpar += numeros[0]
        if coluna == 2:
            soma3 += numeros[0]
        if linha == 1 and numeros[0] > mai2:
            mai2 = numeros[0]
        matriz.append(numeros[:])
        numeros.clear()
print('-=' * 30)
for n in range(0, 9):
    print(f'[ {matriz[n]} ]  ', end='')
    if n == 2 or n == 5:
        print()
print()
print('-=' * 30)
print(f'A soma dos números pares é {totpar}.')
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da segunda linha é {mai2}.')