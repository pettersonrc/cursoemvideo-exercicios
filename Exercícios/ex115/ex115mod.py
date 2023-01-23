def titulo(msg):
    print('~' * 40)
    print(f'{msg:^40}')
    print('~' * 40)


def mostrarlista(lista):
    for i, p in enumerate(lista):
        if i == 0 or i % 2 == 0:
            print(f'{p:<20}', end='')
        elif i % 2 == 1:
            print(f'{p:>15} anos')


def menu():
    print('\033[1;33m1 -\033[m \033[34mVer pessoas cadastradas\033[m')
    print('\033[1;33m2 -\033[m \033[34mCadastrar nova pessoa\033[m')
    print('\033[1;33m3 -\033[m \033[34mSair do Sistema\033[m')


def cadastro(lista):
    lista.append(str(input('Nome: ')))
    while True:
            try:
                lista.append(int(input('Idade: ')))
                break
            except (TypeError, ValueError):
                print()
                print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')

