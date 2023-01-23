def resumo(n=0, aum=10, red=5):
    print('-=' * 15)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-=' * 15)
    print(f'{"Preço analisado:":<20}\t{moeda(n)}')
    print(f'{"Dobro do preço:":<20}\t{moeda(dobro(n))}')
    print(f'{"Metade do preço:":<20}\t{moeda(metade(n))}')
    print(f'{f"{aum}% de aumento:":<20}\t{moeda(aumentar(n, aum))}')
    print(f'{f"{red}% de redução:":<20}\t{moeda(diminuir(n, red))}')
    print('-=' * 15)


def metade(n):
    n = n / 2
    return n


def dobro(n):
    n = n * 2
    return n


def aumentar(n, por):
    n = n + (n/100*por)
    return n


def diminuir(n, por):
    n = n - (n/100*por)
    return n


def moeda(n):
    n = str(f'R${n:.2f}')
    return n
