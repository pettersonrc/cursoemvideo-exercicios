cores = {'limpa':'\033[m',
         'roxo':'\033[35m',
         'vermelho':'\033[31m'}
N = int(input('Digite um número: '))
An = N-1
Sn = N+1
print('O antecessor do número {}{}{} é {}{}{} e o sucessor é {}{}{}!'.format(cores['roxo'], N, cores['limpa'], cores['vermelho'], An, cores['limpa'], cores['roxo'], Sn, cores['limpa']))
