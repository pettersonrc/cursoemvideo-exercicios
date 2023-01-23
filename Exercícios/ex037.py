num = int(input('Digite um número inteiro: '))
print('''Qual será a base de conversão? 
[1] BINÁRIO 
[2] OCTAL 
[3] HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('{}Opção INVÁLIDA{}!, Tente novamente.'.format('\033[1;31m', '\033[m'))
