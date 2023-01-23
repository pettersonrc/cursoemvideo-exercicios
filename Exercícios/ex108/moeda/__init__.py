def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumentar(n=0, por=0):
    n = n + (n/100*por)
    return n


def diminuir(n=0, por=0):
    n = n - (n/100*por)
    return n


def moeda(n):
    n = str(f'R${n:.2f}').replace('.', ',')
    return n
