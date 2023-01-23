def leiadinheiro(msg):
    print('-' * 20)
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print(f'\033[0;31mERRO: "{n}" é um preço inválido!\033[m')
    return valor
