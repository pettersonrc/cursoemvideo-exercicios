palavras = ('pinto', 'pau', 'penis', 'pauzao',
         'curso', 'mercado', 'programador', 'futuro',
         'trabalhar', 'linguagem', 'aprender')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
