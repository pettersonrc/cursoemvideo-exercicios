total = cont1000 = nomebarato = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        cont1000 += 1
    if cont == 1 or preco < barato:
        barato = preco
        nomebarato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total gasto na compra foi de R${total:.2f}')
print(f'Temos {cont1000} produtos custando mais de R$1000.00')
print(f'O prduto mais barato foi {nomebarato} que custa R${barato:.2f}.')
