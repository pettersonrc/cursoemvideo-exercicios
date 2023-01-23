print('{:=^40}'.format('LOJAS PETTERSON'))
preco = float(input('Preço das compras: R$'))
print('''Qual a forma de pagamento?  
[1] À VISTA DINHEIRO/CHEQUE  
[2] À VISTA NO CARTÃO  
[3] EM ATÉ 2X NO CARTÃO  
[4] 3x OU MAIS NO CARTÃO ''')
pagamento = int(input('OPÇÃO: '))
if pagamento == 1:
    desconto = preco - preco*10/100
    print('Sua compra de R${:.2f}, passará a custar R${:.2f} no final.'.format(preco, desconto))
elif pagamento == 2:
    desconto = preco - preco*5/100
    print('Sua compra de R${:.2f}, passará a custar R${:.2f} no final.'.format(preco, desconto))
elif pagamento == 3:
    parcela = preco / 2
    print('Sua compra será parcelada em 2x e cada parcela custará R${:.2f} SEM JUROS.'.format(parcela))
elif pagamento == 4:
    numparcela = int(input('Quantas parcelas? '))
    parcela = (preco/numparcela) + (preco/numparcela)*30/100
    novopreco = parcela * numparcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(numparcela, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, novopreco))
else:
    print('{}NÚMERO INVÁLIDO{}'.format('\033[31m', '\033[m'))
