menor = maior = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        menor = maior = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Lista: {valores}')
print(f'Maior número: {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'Menor número: {menor} na posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()
