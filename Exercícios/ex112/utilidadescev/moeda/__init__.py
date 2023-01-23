def resumo(n, aum, red):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(n):>10}')
    print(f'{"Dobro do preço:":<20}{moeda(dobro(n)):>10}')
    print(f'{"Metade do preço:":<20}{moeda(metade(n)):>10}')
    print(f'{"80% de aumento:":<20}{moeda(aumentar(n, aum)):>10}')
    print(f'{"35% de redução:":<20}{moeda(diminuir(n, red)):>10}')
    print('-' * 30)


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