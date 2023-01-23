def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except Exception as erro:
            print(f'Erro desconhecido {erro.__class__}')
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mErro: por favor digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except Exception as erro:
            print(f'Erro desconhecido {erro.__class__}')
        else:
            return n


n1 = leiaint('Digite um inteiro: ')
n2 = leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2:.1f}')
