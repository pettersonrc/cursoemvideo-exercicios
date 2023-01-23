from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('-='*20)
    print('''ESCOLHA UMA OPÇãO
    [1] SOMAR
    [2] MULTIPLICAR
    [3] QUAL É MAIOR?
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('OPÇÃO: '))
    print('-=' * 20)
    if opcao == 1:
        print('A soma entre {} + {} é {}!'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('O resultado entre {} x {} é {}!'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('entre {} e {} o maior é {}!'.format(n1, n2, n1))
        elif n2 > n1:
            print('entre {} e {} o maior é {}!'.format(n2, n1, n2))
        else:
            print('Os números são iguais.')
    elif opcao == 4:
        print('Digite novos números')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('NÚMERO INVÁLIDO, tente novamente')
sleep(1)
print('-='*20)
print('Fim do programa, Volte sempre!')
