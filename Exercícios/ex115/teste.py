from time import sleep
from ex115 import ex115mod
pessoas = ['Ana Paula Vieira', 32, 'Cláudio Mendonça', 18, 'Gustavo Guanabara', 41,
           'Maria Clara Peixoto', 65, 'Maurício Souza', 19, 'Nilce Pedrosa', 43,
           'Pedro Gonçalves', 18, 'Rafael Albuquerque', 38, 'Renata Soares', 13]
while True:
    ex115mod.titulo('MENU PRINCIPAL')
    ex115mod.menu()
    print('-' * 40)
    try:
        opc = int(input('\033[1;33mSua Opção:\033[m '))
        if opc == 1:
            sleep(1)
            ex115mod.titulo('PESSOAS CADASTRADAS')
            ex115mod.mostrarlista(pessoas)
            sleep(1)
        elif opc == 2:
            sleep(1)
            ex115mod.titulo('NOVO CADASTRO')
            ex115mod.cadastro(pessoas)
            sleep(1)
        elif opc == 3:
            ex115mod.titulo('Saindo do sistema... Até logo!')
            break
        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
    except KeyboardInterrupt:
        print()
        print('\033[31mUsuário forçou a pausa.\033[m')
        break
