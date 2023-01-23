from time import sleep
while True:
    print('\033[1;30;42m''~' * 25)
    print(' SISTEMA DE AJUDA PyHELP ')
    print('~' * 25)
    print('\033[m')
    ajuda = str(input('Função ou Biblioteca > ')).lower().strip()
    if ajuda == 'fim':
        break
    print('\033[1;30;44m''~' * 38)
    print(f' Acessando o manual do comando {ajuda} ')
    print('~' * 38)
    print('\033[m')
    sleep(1)
    print('\033[1;37;40m')
    help(ajuda)
    print('\033[m')
    sleep(1)
print('\033[1;30;41m''~' * 11)
print(' ATÉ LOGO!')
print('~' * 11)
print('\033[m')
