print('='*30)
print('{:^30}'.format('BANCO PITTER'))
print('='*30)
valor = int(input('Qual o valor a ser sacado? R$'))
total = valor
print('='*30)
cedula1 = cedula10 = cedula20 = cedula50 = 0
while True:
    if valor >= 50:
        cedula50 = valor // 50
        valor = valor - 50*cedula50
    if valor >= 20:
        cedula20 = valor // 20
        valor = valor - 20*cedula20
    if valor >= 10:
        cedula10 = valor // 10
        valor = valor - 10*cedula10
    if valor >= 1:
        cedula1 = valor // 1
        valor = valor - 1*cedula1
    if valor == 0:
        break
if cedula50 > 0:
    print(f'Total de {cedula50} cédulas de R$50')
if cedula20 > 0:
    print(f'Total de {cedula20} cédulas de R$20')
if cedula10 > 0:
    print(f'Total de {cedula10} cédulas de R$10')
if cedula1 > 0:
    print(f'Total de {cedula1} cédulas de R$1')
print('='*30)
print('Volte sempre, Tenha um bom dia!')
