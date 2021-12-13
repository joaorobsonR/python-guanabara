palavra = ('aprender', 'programar', 'python', 'caderno', 'faculdade',
           'futuro', 'nasa', 'escola', 'isis', 'trabalhar')

for p in palavra:
    print(f'\nNa palavra {p.upper()} temos as vogais ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
