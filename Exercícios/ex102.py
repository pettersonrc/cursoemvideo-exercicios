def fatorial(n=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    print('-' * 40)
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c != 1:
                print(end=' x ')
            elif c == 1:
                print(end=' = ')
        f *= c
    return f


# Programa Principal
print(fatorial(5, True))
