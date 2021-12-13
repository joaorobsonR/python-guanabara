tup = (int(input('digite o primeiro valor: ')),
     int(input('digite segundo valor: ')),
     int(input('digite o terceiro valor: ')),
     int(input('digite o quarto valor: ')))

print('os valores digitados foram {}'.format(tup))
print(f'o numero nove foi digitado {tup.count(9)} vezes')
if 3 in tup:
    print(f'o primeiro valor três está na posição {tup.index(3)+1}')
print('os numeros pares digitados foram:', end=' ')
for c in tup:
    if c % 2 == 0:
        print(c, end=' ')
