from time import sleep


def maior(*num):
    print('Analisando os valores passados...')
    for c in num:
        sleep(0.3)
        print(c, end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    maiornum = 0
    for n in num:
        if n > maiornum:
            maiornum = n
    print(f'O maior valor informado foi {maiornum}')
    print('-=' * 30)


maior(1, 4, 6, 3, 2, 8)
maior(4, 7, 0)
maior(2, 1)
maior()
